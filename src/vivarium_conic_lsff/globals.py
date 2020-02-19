import itertools

from typing import NamedTuple

####################
# Project metadata #
####################

PROJECT_NAME = 'vivarium_conic_lsff'
CLUSTER_PROJECT = 'proj_cost_effect'

CLUSTER_QUEUE = 'all.q'
MAKE_ARTIFACT_MEM = '3G'
MAKE_ARTIFACT_CPU = '1'
MAKE_ARTIFACT_RUNTIME = '3:00:00'
MAKE_ARTIFACT_SLEEP = 10

LOCATIONS = [
    'India',
    'Nigeria',
    'Ethiopia',
]


#############
# Data Keys #
#############

METADATA_LOCATIONS = 'metadata.locations'

POPULATION_STRUCTURE = 'population.structure'
POPULATION_AGE_BINS = 'population.age_bins'
POPULATION_DEMOGRAPHY = 'population.demographic_dimensions'
POPULATION_TMRLE = 'population.theoretical_minimum_risk_life_expectancy'

ALL_CAUSE_CSMR = 'cause.all_causes.cause_specific_mortality_rate'

COVARIATE_LIVE_BIRTHS_BY_SEX = 'covariate.live_births_by_sex.estimate'

DIARRHEA_CAUSE_SPECIFIC_MORTALITY_RATE = 'cause.diarrheal_diseases.cause_specific_mortality_rate'
DIARRHEA_PREVALENCE = 'cause.diarrheal_diseases.prevalence'
DIARRHEA_INCIDENCE_RATE = 'cause.diarrheal_diseases.incidence_rate'
DIARRHEA_REMISSION_RATE = 'cause.diarrheal_diseases.remission_rate'
DIARRHEA_EXCESS_MORTALITY_RATE = 'cause.diarrheal_diseases.excess_mortality_rate'
DIARRHEA_DISABILITY_WEIGHT = 'cause.diarrheal_diseases.disability_weight'
DIARRHEA_RESTRICTIONS = 'cause.diarrheal_diseases.restrictions'

MEASLES_CAUSE_SPECIFIC_MORTALITY_RATE = 'cause.measles.cause_specific_mortality_rate'
MEASLES_PREVALENCE = 'cause.measles.prevalence'
MEASLES_INCIDENCE_RATE = 'cause.measles.incidence_rate'
MEASLES_EXCESS_MORTALITY_RATE = 'cause.measles.excess_mortality_rate'
MEASLES_DISABILITY_WEIGHT = 'cause.measles.disability_weight'
MEASLES_RESTRICTIONS = 'cause.measles.restrictions'

LRI_CAUSE_SPECIFIC_MORTALITY_RATE = 'cause.lower_respiratory_infections.cause_specific_mortality_rate'
LRI_PREVALENCE = 'cause.lower_respiratory_infections.prevalence'
LRI_INCIDENCE_RATE = 'cause.lower_respiratory_infections.incidence_rate'
LRI_REMISSION_RATE = 'cause.lower_respiratory_infections.remission_rate'
LRI_EXCESS_MORTALITY_RATE = 'cause.lower_respiratory_infections.excess_mortality_rate'
LRI_DISABILITY_WEIGHT = 'cause.lower_respiratory_infections.disability_weight'
LRI_RESTRICTIONS = 'cause.lower_respiratory_infections.restrictions'

NEURAL_TUBE_DEFECTS_CAUSE_SPECIFIC_MORTALITY_RATE = 'cause.neural_tube_defects.cause_specific_mortality_rate'
NEURAL_TUBE_DEFECTS_PREVALENCE = 'cause.neural_tube_defects.prevalence'
NEURAL_TUBE_DEFECTS_BIRTH_PREVALENCE = 'cause.neural_tube_defects.birth_prevalence'
NEURAL_TUBE_DEFECTS_EXCESS_MORTALITY_RATE = 'cause.neural_tube_defects.excess_mortality_rate'
NEURAL_TUBE_DEFECTS_DISABILITY_WEIGHT = 'cause.neural_tube_defects.disability_weight'
NEURAL_TUBE_DEFECTS_RESTRICTIONS = 'cause.neural_tube_defects.restrictions'


###########################
# Disease Model variables #
###########################

# TODO - sample states and transitions
DIARRHEA_MODEL_NAME = 'diarrheal_diseases'
DIARRHEA_SUSCEPTIBLE_STATE_NAME = f'susceptible_to_{DIARRHEA_MODEL_NAME}'
DIARRHEA_WITH_CONDITION_STATE_NAME = DIARRHEA_MODEL_NAME
DIARRHEA_MODEL_STATES = (DIARRHEA_SUSCEPTIBLE_STATE_NAME, DIARRHEA_WITH_CONDITION_STATE_NAME)
DIARRHEA_MODEL_TRANSITIONS = (
    f'{DIARRHEA_SUSCEPTIBLE_STATE_NAME}_TO_{DIARRHEA_WITH_CONDITION_STATE_NAME}',
    f'{DIARRHEA_WITH_CONDITION_STATE_NAME}_TO_{DIARRHEA_SUSCEPTIBLE_STATE_NAME}',
)

# TODO - add all diseases to DISEASE_MODELS tuple and the DISEASE_MODEL_MAP dictionary
DISEASE_MODELS = (DIARRHEA_MODEL_NAME)
DISEASE_MODEL_MAP = {
    DIARRHEA_MODEL_NAME: {
        'states': DIARRHEA_MODEL_STATES,
        'transitions': DIARRHEA_MODEL_TRANSITIONS,
    },
}


########################
# Risk Model Constants #
########################
# TODO - remove if you don't need lbwsg
LBWSG_MODEL_NAME = 'low_birth_weight_and_short_gestation'


class __LBWSG_MISSING_CATEGORY(NamedTuple):
    CAT: str = 'cat212'
    NAME: str = 'Birth prevalence - [37, 38) wks, [1000, 1500) g'
    EXPOSURE: float = 0.


LBWSG_MISSING_CATEGORY = __LBWSG_MISSING_CATEGORY()


#################################
# Results columns and variables #
#################################

TOTAL_POPULATION_COLUMN = 'total_population'
TOTAL_YLDS_COLUMN = 'years_lived_with_disability'
TOTAL_YLLS_COLUMN = 'years_of_life_lost'

STANDARD_COLUMNS = {
    'total_population': TOTAL_POPULATION_COLUMN,
    'total_ylls': TOTAL_YLLS_COLUMN,
    'total_ylds': TOTAL_YLDS_COLUMN,
}

TOTAL_POPULATION_COLUMN_TEMPLATE = 'total_population_{POP_STATE}'
PERSON_TIME_COLUMN_TEMPLATE = 'person_time_in_{YEAR}_among_{SEX}_in_age_group_{AGE_GROUP}'
DEATH_COLUMN_TEMPLATE = 'death_due_to_{CAUSE_OF_DEATH}_in_{YEAR}_among_{SEX}_in_age_group_{AGE_GROUP}'
YLLS_COLUMN_TEMPLATE = 'ylls_due_to_{CAUSE_OF_DEATH}_in_{YEAR}_among_{SEX}_in_age_group_{AGE_GROUP}'
YLDS_COLUMN_TEMPLATE = 'ylds_due_to_{CAUSE_OF_DISABILITY}_in_{YEAR}_among_{SEX}_in_age_group_{AGE_GROUP}'
STATE_PERSON_TIME_COLUMN_TEMPLATE = '{STATE}_person_time_in_{YEAR}_among_{SEX}_in_age_group_{AGE_GROUP}'
TRANSITION_COUNT_COLUMN_TEMPLATE = '{TRANSITION}_event_count_in_{YEAR}_among_{SEX}_in_age_group_{AGE_GROUP}'

COLUMN_TEMPLATES = {
    'population': TOTAL_POPULATION_COLUMN_TEMPLATE,
    'person_time': PERSON_TIME_COLUMN_TEMPLATE,
    'deaths': DEATH_COLUMN_TEMPLATE,
    'ylls': YLLS_COLUMN_TEMPLATE,
    'ylds': YLDS_COLUMN_TEMPLATE,
    'state_person_time': STATE_PERSON_TIME_COLUMN_TEMPLATE,
    'transition_count': TRANSITION_COUNT_COLUMN_TEMPLATE,
}

POP_STATES = ('living', 'dead', 'tracked', 'untracked')
SEXES = ('male', 'female')
# TODO - add literals for years in the model
YEARS = ()
# TODO - add literals for ages in the model
AGE_GROUPS = ()
# TODO - add causes of death
CAUSES_OF_DEATH = (
    'other_causes',
    DIARRHEA_WITH_CONDITION_STATE_NAME,
)
# TODO - add causes of disability
CAUSES_OF_DISABILITY = (
    DIARRHEA_WITH_CONDITION_STATE_NAME,
)
STATES = (state for model in DISEASE_MODELS for state in DISEASE_MODEL_MAP[model]['states'])
TRANSITIONS = (transition for model in DISEASE_MODELS for transition in DISEASE_MODEL_MAP[model]['transitions'])

TEMPLATE_FIELD_MAP = {
    'POP_STATE': POP_STATES,
    'YEAR': YEARS,
    'SEX': SEXES,
    'AGE_GROUP': AGE_GROUPS,
    'CAUSE_OF_DEATH': CAUSES_OF_DEATH,
    'CAUSE_OF_DISABILITY': CAUSES_OF_DISABILITY,
    'STATE': STATES,
    'TRANSITION': TRANSITIONS,
}


def RESULT_COLUMNS(kind='all'):
    if kind not in COLUMN_TEMPLATES and kind != 'all':
        raise ValueError(f'Unknown result column type {kind}')
    columns = []
    if kind == 'all':
        for k in COLUMN_TEMPLATES:
            columns += RESULT_COLUMNS(k)
        columns = list(STANDARD_COLUMNS.values()) + columns
    else:
        template = COLUMN_TEMPLATES[kind]
        filtered_field_map = {field: values
                              for field, values in TEMPLATE_FIELD_MAP.items() if f'{{{field}}}' in template}
        fields, value_groups = filtered_field_map.keys(), itertools.product(*filtered_field_map.values())
        for value_group in value_groups:
            columns.append(template.format(**{field: value for field, value in zip(fields, value_group)}))
    return columns
