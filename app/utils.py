from rest_framework.filters import BaseFilterBackend


class CustomGenericFilter(BaseFilterBackend):

    def queryset_filter(self, queryset, query_params):
        fields = {f.name for f in queryset.model._meta.fields}
        for field in [f for f in fields if f in query_params]:
            string = query_params.get(field)
            try:
                filter = int(string)
                queryset = queryset.filter(**{field:filter})
            except Exception:
                pass
        return queryset
    
    def queryset_order(self, queryset, query_params):
        string = query_params.get('order')
        if string:
            order = string.split(',')
            fields_pos = {f'{f.name}' for f in queryset.model._meta.fields}
            fields_neg = {f'-{f.name}' for f in queryset.model._meta.fields}
            fields = fields_pos.union(fields_neg)
            order_valid = [o for o in order if o in fields]
            queryset = queryset.order_by(*order_valid)
        return queryset
    
    def filter_queryset(self, request, queryset, view):
        queryset = self.queryset_filter(queryset, request.query_params)
        queryset = self.queryset_order(queryset, request.query_params)
        return queryset
