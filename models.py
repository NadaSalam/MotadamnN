from django.db import models


class Admin(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Beneficiary(models.Model):
    id = models.BigAutoField(primary_key=True)
    national_id = models.BigIntegerField(unique=True)
    gender = models.IntegerField()
    martial_status = models.CharField(max_length=8)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    birthdate = models.DateField()
    photo = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    charity = models.ForeignKey('Charity', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'beneficiary'


class Cases(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField()
    needed_amount = models.IntegerField()
    approved = models.IntegerField()
    subcat = models.ForeignKey('Subcategory', models.DO_NOTHING)
    ben = models.ForeignKey(Beneficiary, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'cases'


class CasesFeatures(models.Model):
    id = models.BigAutoField(primary_key=True)
    cases = models.ForeignKey(Cases, models.DO_NOTHING)
    features = models.ForeignKey('Features', models.DO_NOTHING)
    answer = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'cases_features'


class Charity(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    phone = models.TextField()
    address = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    description = models.TextField()
    password = models.CharField(max_length=255)
    is_banned = models.IntegerField()
    created_at = models.DateTimeField()
    city = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'charity'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'


class Donation(models.Model):
    id = models.BigAutoField(primary_key=True)
    donation_ref = models.CharField(unique=True, max_length=255)
    payment_amount = models.IntegerField()
    payment_method = models.CharField(max_length=7)
    created_at = models.DateTimeField()
    donor = models.ForeignKey('Donor', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'donation'


class DonationCases(models.Model):
    id = models.BigAutoField(primary_key=True)
    donation = models.ForeignKey(Donation, models.DO_NOTHING)
    cases = models.ForeignKey(Cases, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'donation_cases'


class Donor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.TextField()
    address = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    gender = models.IntegerField()
    birthdate = models.DateField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_banned = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'donor'


class Features(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'features'


class Fundraising(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    photo = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    sub = models.ForeignKey('Subcategory', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'fundraising'


class Subcategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    super = models.ForeignKey('Supercategory', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'subcategory'


class SubcategoryFeatures(models.Model):
    id = models.BigAutoField(primary_key=True)
    subcat = models.ForeignKey(Subcategory, models.DO_NOTHING)
    feature = models.ForeignKey(Features, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'subcategory_features'


class Supercategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'supercategory'
