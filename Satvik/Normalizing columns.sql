update Plan_Attributes set MOOP = 
(TEHBInnTier1IndividualMOOP - (select min(TEHBInnTier1IndividualMOOP) from Plan_Attributes))/((select max(TEHBInnTier1IndividualMOOP)
from Plan_Attributes) - (select min(TEHBInnTier1IndividualMOOP) from Plan_Attributes));
update Plan_Attributes set DedInn = 
(TEHBDedInnTier1Individual - (select min(TEHBDedInnTier1Individual) from Plan_Attributes))/((select max(TEHBDedInnTier1Individual)
from Plan_Attributes) - (select min(TEHBDedInnTier1Individual) from Plan_Attributes));
update Plan_Attributes set CountryCoverage = 
case when OutOfCountryCoverage = 'Yes' then 1 else 0 end;
update cost set rate_norm = 
(indiv_rate - (select min(indiv_rate) from cost))/((select max(indiv_rate)
from cost) - (select min(indiv_rate) from cost));
update cost set smoker_norm = 
(smoker_rate - (select min(smoker_rate) from cost))/((select max(smoker_rate)
from cost) - (select min(smoker_rate) from cost));
update benefits set copayin_norm = 
(copay_in - (select min(copay_in) from benefits))/((select max(copay_in)
from benefits) - (select min(copay_in) from benefits));
update benefits set coinsin_norm = 
(coinsurance_in - (select min(coinsurance_in) from benefits))/((select max(coinsurance_in)
from benefits) - (select min(coinsurance_in) from benefits));
update visits set visits_norm = 
(visits - (select min(visits) from visits))/((select max(visits)
from visits) - (select min(visits) from visits));
