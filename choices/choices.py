TYPE_SOFIA = 'Sofia'
TYPE_PLOVDIV = 'Plovdiv'
TYPE_VARNA = 'Varna'
TYPE_BURGAS = 'Burgas'
TYPE_RUSE = 'Ruse'
TYPE_STARAZAGORA = 'Stara Zagora'
TYPE_PLEVEN = 'Pleven'
TYPE_UNKNOWN = ''

CITY_CHOICES = (
    (TYPE_SOFIA, 'Sofia'),
    (TYPE_PLOVDIV, 'Plovdiv'),
    (TYPE_VARNA, 'Varna'),
    (TYPE_BURGAS, 'Burgas'),
    (TYPE_RUSE, 'Ruse'),
    (TYPE_STARAZAGORA, 'Stara Zagora'),
    (TYPE_PLEVEN, 'Pleven'),
    (TYPE_UNKNOWN, ''),
)

TYPE_HR = 'Human Resources'
TYPE_IT = 'Information Technology'
TYPE_CUSTEMERSERVICE = 'Customer Service'
TYPE_MARKETING = 'Marketing'
TYPE_SALES = 'SALES'
TYPE_MANUFACTURING = 'Manufacturing'
TYPE_TOURISM = 'Tourism'

FIELD_CHOICES = (
    (TYPE_HR, 'Human Resources'),
    (TYPE_IT, 'Information Technology'),
    (TYPE_CUSTEMERSERVICE, 'Customer Service'),
    (TYPE_MARKETING, 'Marketing'),
    (TYPE_SALES, 'Sales'),
    (TYPE_MANUFACTURING, 'Manufacturing'),
    (TYPE_TOURISM, 'Tourism'),
    (TYPE_UNKNOWN, ''),
)

TYPE_ONE_MONTH = '1 month'
TYPE_TWO_MONTHS = '2 months'
TYPE_TREE_MONTHS = '3 months'
TYPE_FOUR_MONTHS = '4 months'
TYPE_FIVE_MONTHS = '5 months'
TYPE_SIX_MONTHS = '6 months'
TYPE_SEVEN_MONTHS = '7 months'
TYPE_EIGHT_MONTHS = '8 months'
TYPE_NINE_MONTHS = '9 months'
TYPE_TEN_MONTHS = '10 months'
TYPE_ELEVEN_MONTHS = '11 months'
TYPE_ONE_YEAR = '1 year'

DURATION_CHOICES = (
    (TYPE_ONE_MONTH, '1 month'),
    (TYPE_TWO_MONTHS, '2 months'),
    (TYPE_TREE_MONTHS, '3 months'),
    (TYPE_FOUR_MONTHS, '4 months'),
    (TYPE_FIVE_MONTHS, '5 months'),
    (TYPE_SIX_MONTHS, '6 months'),
    (TYPE_SEVEN_MONTHS, '7 months'),
    (TYPE_EIGHT_MONTHS, '8 months'),
    (TYPE_NINE_MONTHS, '9 months'),
    (TYPE_TEN_MONTHS, '10 months'),
    (TYPE_ELEVEN_MONTHS, '11 months'),
    (TYPE_ONE_YEAR, '1 year'),
    (TYPE_UNKNOWN, ''),
)

TYPE_COMPANY = 'Company'
TYPE_CANDIDATE = 'Candidate'

PROFILE = (
    (TYPE_COMPANY, 'Company'),
    (TYPE_CANDIDATE, 'Candidate')
)

TYPE_FULL_TYME = 'Full-Time'
TYPE_PART_TYME = 'Part-Time'

EMPLOYMENT_TYPE = (
    (TYPE_FULL_TYME, 'Full-Time'),
    (TYPE_PART_TYME, 'Part-Time'),
    (TYPE_UNKNOWN, ''),
)
