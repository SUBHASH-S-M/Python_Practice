select Prim.co,Prim.date from
((select CC.Hospitalised as co,CC.DateAnnounced as date,dense_rank() over(partition by 
CC.StateCode,CC.DateAnnounced order by Hospitalised desc)rnk  from CovidCases CC
left join States St 
on CC.StateCode=St.StateCode)Prim)
where rnk=1


select St.StateName as State,
EXTRACT(MONTH FROM CC.DateAnnounced)  as "Month",
avg(CC.Hospitalised) as AverageHospitalised,
max(CC.Hospitalised) as MaximumHospitalised,
avg(CC.Deceased) as AverageDeceased,
max(CC.Deceased) as MaximumDeceased
from CovidCases as CC
left join States St 
on CC.StateCode=St.StateCode
where CC.StateName LIKE '%Pradesh' and  EXTRACT(MONTH FROM CC.DateAnnounced) ='May'
group by St.StateName



