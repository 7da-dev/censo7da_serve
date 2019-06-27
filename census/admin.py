from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from census.models import Inst, Camp, Unit
# Register your models here.
#@admin.register(Lote)
class InstAdmin(ImportExportModelAdmin):
    list_display = ('year', 'inst_id', 'inst_e_id',
                    'inst_type', 'inst_title', 'inst_name_l',
                    'inst_name_s', 'is_active', 'fiscal_id',
                    'inst_e2_id')
admin.site.register(Inst, InstAdmin)

class CampAdmin(ImportExportModelAdmin):
    list_display = ('year', 'camp_id', 'inst_id',
                    'camp_type', 'camp_title', 'camp_name_l',
                    'camp_name_s', 'is_active', 'resp_id',
                    'account')
admin.site.register(Camp, CampAdmin)

class UnitAdmin(ImportExportModelAdmin):
    list_display = ('year', 'unit_id', 'camp_id',
                    'unit_type', 'unit_title', 'unit_name_l',
                    'unit_name_s', 'is_active', 'resp_id',
                    'account')
admin.site.register(Unit, UnitAdmin)