from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField, IntegerField, ForeignKey, BooleanField,\
    ManyToManyField


##### SR27 Starts Here #####
class FdGroup(models.Model):
    # 4-digit code identifying a food group. Only the first 2 digits are
    # currently assigned. In the future, the last 2 digits may be used. Codes
    # may not be consecutive.
    fdgrp_cd = models.CharField(db_column='fdGrp_Cd', primary_key=True,
                                max_length=4)
    # Name of food group.
    fdgrp_desc = models.CharField(db_column='fdGrp_Desc', max_length=60)

    class Meta:
        managed = False
        db_table = 'fd_group'


class FoodDes(models.Model):
    # 5-digit Nutrient Databank number that uniquely identifies a food item. If
    # this field is defined as numeric, the leading zero will be lost.
    ndb_no = models.CharField(db_column='nDB_No', primary_key=True,
                              max_length=5)
    # 4-digit code indicating food group to which a food item belongs.
    fdgrp_cd = models.ForeignKey(FdGroup, db_column='fdGrp_Cd', blank=True,
                                 null=True)
    # 200-character description of food item.
    long_desc = models.CharField(db_column='long_Desc', max_length=200)
    # 60-character abbreviated description of food item. Generated from the
    # 200-character description using abbreviations in Appendix A. If short
    # description is longer than 60 characters, additional abbreviations are
    # made.
    shrt_desc = models.CharField(db_column='shrt_Desc', max_length=60,
                                 null=False)
    # Other names commonly used to describe a food, including local or regional
    # names for various foods, for example, soda or pop for carbonated
    # beverages.
    comname = models.CharField(db_column='comName', max_length=100, blank=True,
                               null=True)
    # Indicates the company that manufactured the product, when appropriate.
    manufacname = models.CharField(db_column='manufacName', max_length=65,
                                   blank=True, null=True)
    # Indicates if the food item is used in the USDA Food and Nutrient Database
    # for Dietary Studies (FNDDS) and thus has a complete nutrient profile for
    # the 65 FNDDS nutrients.
    survey = models.NullBooleanField()
    # Description of inedible parts of a food item (refuse), such as seeds or
    # bone.
    ref_desc = models.CharField(max_length=135, blank=True, null=True)
    # Percentage of refuse.
    refuse = models.IntegerField(blank=True, null=True)
    # Scientific name of the food item. Given for the least processed form of
    # the food (usually raw), if applicable.
    sciname = models.CharField(db_column='sciName', max_length=65, blank=True,
                               null=True)
    # Factor for converting nitrogen to protein (see p. 11).
    n_factor = models.DecimalField(db_column='n_Factor', max_digits=4,
                                   decimal_places=2, blank=True, null=True)
    # Factor for calculating calories from protein (see p. 12).
    pro_factor = models.DecimalField(db_column='pro_Factor', max_digits=4,
                                     decimal_places=2, blank=True, null=True)
    # Factor for calculating calories from fat (see p. 12).
    fat_factor = models.DecimalField(db_column='fat_Factor', max_digits=4,
                                     decimal_places=2, blank=True, null=True)
    # Factor for calculating calories from carbohydrate (see p. 12).
    cho_factor = models.DecimalField(db_column='cHO_Factor', max_digits=4,
                                     decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_des'


class LanguaLFactorsDescription(models.Model):
    # The LanguaL factor from the Thesaurus. Only those codes used to factor
    # the foods contained in the LanguaL Factor file are included in this file
    factor_code = models.CharField(db_column='factor_Code', primary_key=True,
                                   max_length=5)
    description = models.CharField(max_length=140)

    class Meta:
        managed = False
        db_table = 'langdesc'


class Langual(models.Model):
    ndb_no = models.ForeignKey(FoodDes, db_column='nDB_No', blank=True,
                               null=True)
    factor_code = models.ForeignKey(LanguaLFactorsDescription,
                                    db_column='factor_Code', blank=True,
                                    null=True)

    class Meta:
        managed = False
        db_table = 'langual'


class DerivCd(models.Model):
    # Derivation Code.
    deriv_cd = models.CharField(db_column='deriv_Cd', primary_key=True,
                                max_length=4)
    # Description of derivation code giving specific information on how the
    # value was determined.
    deriv_desc = models.CharField(db_column='deriv_Desc', max_length=120)

    class Meta:
        managed = False
        db_table = 'deriv_cd'


class DataSrc(models.Model):
    # Unique number identifying the reference/source.
    datasrc_id = models.CharField(db_column='dataSrc_ID', primary_key=True,
                                  max_length=6)
    # List of authors for a journal article or name of sponsoring organization
    # for other documents.
    authors = models.CharField(max_length=255, blank=True, null=True)
    # Title of article or name of document, such as a report from a company or
    # trade association.
    title = models.CharField(max_length=255, blank=True, null=True)
    # Year article or document was published.
    year = models.CharField(max_length=4, blank=True, null=True)
    # Name of the journal in which the article was published.
    journal = models.CharField(max_length=135, blank=True, null=True)
    # Volume number for journal articles, books, or reports; city where
    # sponsoring organization is located.
    vol_city = models.CharField(db_column='vol_City', max_length=16,
                                blank=True, null=True)
    # Issue number for journal article; State where the sponsoring organization
    # is located.
    issue_state = models.CharField(db_column='issue_State', max_length=5,
                                   blank=True, null=True)
    # Starting page number of article/document.
    start_page = models.CharField(db_column='start_Page', max_length=5,
                                  blank=True, null=True)
    # Ending page number of article/document.
    end_page = models.CharField(db_column='end_Page', max_length=5, blank=True,
                                null=True)

    class Meta:
        managed = False
        db_table = 'data_src'


class NutData(models.Model):
    nutr_id = models.AutoField(db_column='nutr_ID', primary_key=True)
    # 5-digit Nutrient Databank number.
    ndb_no = models.ForeignKey(FoodDes, db_column='nDB_No', blank=True,
                               null=True, related_name='nutrients')
    # Unique 3-digit identifier code for a nutrient
    nutr_no = models.ForeignKey('NutrDef', db_column='nutr_No', blank=True,
                                null=True)
    # Amount in 100 grams, edible portion
    nutr_val = models.DecimalField(db_column='nutr_Val', max_digits=10,
                                   decimal_places=3)
    # Number of data points (previously called Sample_Ct) is the number of
    # analyses used to calculate the nutrient value. If the number of data
    # points is 0, the value was calculated or imputed.
    num_data_pts = models.DecimalField(db_column='num_Data_Pts', max_digits=5,
                                       decimal_places=0)
    # Standard error of the mean. Null if cannot be calculated. The standard
    # error is also not given if the number of data points is less than three.
    std_error = models.DecimalField(db_column='std_Error', max_digits=8,
                                    decimal_places=3, blank=True, null=True)
    # Code indicating type of data.
    src_cd = models.ForeignKey('SrcCd', db_column='src_Cd', blank=True,
                               null=True)
    # Data Derivation Code giving specific information on how the value is
    # determined
    deriv_cd = models.ForeignKey(DerivCd, db_column='deriv_Cd', blank=True,
                                 null=True)
    # NDB number of the item used to impute a missing value. Populated only for
    # items added or updated starting with SR14.
    ref_ndb_no = models.CharField(db_column='ref_NDB_No', max_length=5,
                                  blank=True, null=True)
    # Indicates a vitamin or mineral added for fortification or enrichment.
    # This field is populated for ready-to-eat breakfast cereals and many
    # brand-name hot cereals in food group 8.
    add_nutr_mark = models.NullBooleanField(db_column='add_Nutr_Mark')
    # Number of studies
    num_studies = models.IntegerField(db_column='num_Studies', blank=True,
                                      null=True)
    # Minimum values
    minval = models.DecimalField(db_column='minVal', max_digits=10,
                                 decimal_places=3, blank=True, null=True)
    # Maximum value
    maxval = models.DecimalField(db_column='maxVal', max_digits=10,
                                 decimal_places=3, blank=True, null=True)
    # Degrees of freedom
    df = models.IntegerField(db_column='dF', blank=True, null=True)
    # Lower 95% error bound
    low_eb = models.DecimalField(db_column='low_EB', max_digits=10,
                                 decimal_places=3, blank=True, null=True)
    # Upper 95% error bound
    up_eb = models.DecimalField(db_column='up_EB', max_digits=10,
                                decimal_places=3, blank=True, null=True)
    # Statistical comments
    stat_cmt = models.CharField(max_length=10, blank=True, null=True)
    # Indicates when a value was either added to the database or last modified.
    addmod_date = models.CharField(db_column='addMod_Date', max_length=10,
                                   blank=True, null=True)
    # Confidence Code indicating data quality, based on evaluation of sample
    # plan, sample handling, analytical method, analytical quality control, and
    # number of samples analyzed. Not included in this release, but is planned
    # for future releases.
    cc = models.CharField(db_column='cC', max_length=1, blank=True, null=True)
    datasrc = models.ForeignKey(DataSrc, db_column='dataSrc_ID', blank=True,
                                null=True)

    class Meta:
        managed = False
        db_table = 'nut_data'


class NutrDef(models.Model):
    # Unique 3-digit identifier code for a nutrient.
    nutr_no = models.CharField(db_column='nutr_No', primary_key=True,
                               max_length=3)
    # Units of measure (mg, g, g, and so on).
    units = models.CharField(max_length=7)
    # International Network of Food Data Systems (INFOODS) Tagnames. A unique
    # abbreviation for a nutrient/food component developed by INFOODS to aid in
    # the interchange of data.
    tagname = models.CharField(max_length=20, blank=True, null=True)
    # Name of nutrient/food component.
    nutrdesc = models.CharField(db_column='nutrDesc', max_length=60)
    # Number of decimal places to which a nutrient value is rounded.
    num_dec = models.CharField(db_column='num_Dec', max_length=1)
    # Used to sort nutrient records in the same order as various reports
    # produced from SR.
    sr_order = models.IntegerField(db_column='sR_Order')

    class Meta:
        managed = False
        db_table = 'nutr_def'


class SrcCd(models.Model):
    # 2-digit code
    src_cd = models.CharField(db_column='src_Cd', primary_key=True,
                              max_length=2)
    # Description of source code that identifies the type of nutrient data.
    srccd_desc = models.CharField(db_column='srcCd_Desc', max_length=60)

    class Meta:
        managed = False
        db_table = 'src_cd'


class Weight(models.Model):
    weight_id = models.AutoField(db_column='weight_ID', primary_key=True)
    # 5-digit Nutrient Databank number.
    ndb_no = models.ForeignKey(FoodDes, db_column='nDB_No', blank=True,
                               null=True)
    # Sequence number
    seq = models.CharField(max_length=2, blank=True, null=True)
    # Unit modifier (for example, 1 in "1 cup").
    amount = models.DecimalField(max_digits=5, decimal_places=3)
    # Description (for example, cup, diced, and 1-inch pieces).
    msre_desc = models.CharField(db_column='msre_Desc', max_length=84)
    # Gram weight
    gm_wgt = models.DecimalField(db_column='gm_Wgt', max_digits=7,
                                 decimal_places=1)
    # Number of data points
    num_data_pts = models.IntegerField(db_column='num_Data_Pts', blank=True,
                                       null=True)
    # Standard deviation
    std_dev = models.DecimalField(db_column='std_Dev', max_digits=7,
                                  decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weight'


class Footnote(models.Model):
    footnote_id = models.AutoField(primary_key=True)
    # 5-digit Nutrient Databank number.
    ndb_no = models.ForeignKey(FoodDes, db_column='nDB_No', blank=True,
                               null=True)
    # Sequence number. If a given footnote applies to more than one nutrient
    # number, the same footnote number is used. As a result, this file cannot
    # be indexed.
    footnt_no = models.CharField(db_column='footnt_No', max_length=4)
    # Type of footnote (see pdf, p.35)
    footnt_typ = models.CharField(db_column='footnt_Typ', max_length=1)
    # Unique 3-digit identifier code for a nutrient to which footnote applies.
    nutr_no = models.CharField(db_column='nutr_No', max_length=3, blank=True,
                               null=True)
    # Footnote text
    footnt_txt = models.CharField(db_column='footnt_Txt', max_length=200)

    class Meta:
        managed = False
        db_table = 'footnote'


class FoodPrice(models.Model):
    price_id = models.AutoField(primary_key=True)
    ndb_no = models.ForeignKey(FoodDes, db_column='nDB_No', blank=True,
                               null=True, related_name="prices")
    # region_id = Column(Integer, ForeignKey('region.region_id')
    cents = models.IntegerField(blank=True, null=True)
    unit_name = models.CharField(max_length=10, blank=True, null=True)
    units = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_price'

##### SR27 ENDS HERE #####
##### BEGIN APP MODEL #####
class Profile(models.Model):
    '''Each profile can belong to several users, but only if it is published.
    Once a profile is published, it cannot be edited.  If a user wishes to
    build a variation of a profile, a new profile is created with a copy of the
    published profile data.

    Each profile has one to many LimitRequirements and RatioRequirements.
    '''
    users = ManyToManyField(User)
    name = CharField(max_length=32)
    description = CharField(max_length=128)
    # limit_requirements
    # ratio_requirements


class LimitRequirement(models.Model):
    '''Each limit requirement has a boolean operator that determines if the
    requirement is a minimum or maximum value.  Each limit requirement also has
    a nutrient that it is tied to.  The unit for the limit requirement will be
    determined by the unit that is used for the nutrient.'''
    profile = ForeignKey(Profile)
    nutr = ForeignKey(NutData, db_column='nutr_ID', blank=True, null=True)
    maximum = BooleanField()
    limit = IntegerField()  # Will always be in usda's unit for nutrient


class RatioRequirement(models.Model):
    '''A ratio requirement will have two nutrients, a numerator, and a
    denominator.  The nutrients will be nutrients in the USDA database'''
    pass
    profile = ForeignKey(Profile)
    nutrients = ManyToManyField(NutData, db_column='nutr_ID',
                                blank=True, null=True)
    maximum = BooleanField()


class Recipe(models.Model):
    '''
    A recipe will have a list of food ids from the usda database, and
    quantities for each food.
    '''
    users = ManyToManyField(User)
    name = CharField(max_length=32)
    description = CharField(max_length=128)
    # Ingredients


class Ingredient(models.Model):
    recipe = ForeignKey(Recipe)
    ndb_no = models.ForeignKey(FoodDes, db_column='nDB_No', blank=True,
                               null=True)
    minimum = IntegerField(blank=True, null=True)
    maximum = IntegerField(blank=True, null=True)
    # quantity will always be in grams
    quantity = IntegerField(blank=True, null=True)


