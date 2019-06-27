from django.db import models
from uuid import uuid4
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Inst(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    year = models.CharField(_('year'), max_length=4, blank=True)
    inst_id = models.CharField(_('inst id'), max_length=20, blank=True)
    inst_e_id = models.CharField(_('inst e id'), max_length=20, null=True, blank=True)
    inst_type = models.CharField(_('type'), max_length=20, blank=True)
    inst_title = models.CharField(_('title'), max_length=20, blank=True)
    inst_name_l = models.CharField(_('name l'), max_length=120, blank=True)
    inst_name_s = models.CharField(_('name s'), max_length=20, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    fiscal_id = models.CharField(_('fiscal id'), max_length=20, blank=True)
    inst_e2_id = models.CharField(_('inst e2 id'), max_length=20, null=True, blank=True)

    birth_date = models.DateField(_('birth date'), null=True, blank=True)
    photo = models.ImageField(
        _('photo'), upload_to='inst', default='inst/default.png',
        null=True, blank=True)

    created = models.DateTimeField(_('created'), auto_now_add=True, blank=True)
    modified = models.DateTimeField(_('modified'), auto_now=True, blank=True)

    class Meta:
        verbose_name = _('inst')
        verbose_name_plural = _('insts')
        unique_together = (
            ('year','fiscal_id', 'inst_name_s'),
        )

    def __str__(self):
        return '%s %s' % (self.fiscal_id, self.inst_name_s, )

class Camp(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    year = models.CharField(_('year'), max_length=4, blank=True)
    camp_id = models.CharField(_('camp id'), max_length=20, blank=True)
    inst_id = models.CharField(_('inst id'), max_length=20, null=True, blank=True)
    camp_type = models.CharField(_('type'), max_length=20, blank=True)
    camp_title = models.CharField(_('title'), max_length=20, blank=True)
    camp_name_l = models.CharField(_('name l'), max_length=120, blank=True)
    camp_name_s = models.CharField(_('name s'), max_length=20, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    resp_id = models.CharField(_('resp id'), max_length=20, null=True, blank=True)
    account = models.CharField(_('account'), max_length=20, null=True, blank=True)

    birth_date = models.DateField(_('birth date'), null=True, blank=True)
    photo = models.ImageField(
        _('photo'), upload_to='camp', default='camp/default.png',
        null=True, blank=True)

    created = models.DateTimeField(_('created'), auto_now_add=True, blank=True)
    modified = models.DateTimeField(_('modified'), auto_now=True, blank=True)

    class Meta:
        verbose_name = _('camp')
        verbose_name_plural = _('camps')
        unique_together = (
            ( 'year','camp_name_s'),
        )

    def __str__(self):
        return '%s %s' % (self.camp_name_l, self.camp_name_s, )

class Unit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    year = models.CharField(_('year'), max_length=4, blank=True)
    unit_id = models.CharField(_('unit id'), max_length=20, blank=True)
    camp_id = models.CharField(_('camp id'), max_length=20, null=True, blank=True)
    unit_type = models.CharField(_('type'), max_length=20, blank=True)
    unit_title = models.CharField(_('title'), max_length=20, blank=True)
    unit_name_l = models.CharField(_('name l'), max_length=120, blank=True)
    unit_name_s = models.CharField(_('name s'), max_length=20, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    resp_id = models.CharField(_('resp id'), max_length=20, null=True, blank=True)
    account = models.CharField(_('account'), max_length=20, null=True, blank=True)

    created = models.DateTimeField(_('created'), auto_now_add=True, blank=True)
    modified = models.DateTimeField(_('modified'), auto_now=True, blank=True)

    class Meta:
        verbose_name = _('unit')
        verbose_name_plural = _('units')


    def __str__(self):
        return '%s %s' % (self.unit_name_l, self.unit_name_s, )