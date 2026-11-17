# Investigation of HZE particle fluxes as a space radiation hazard for future Mars missions

**Journal:** *Heliyon* 5 (2019) e02972 (CellPress / ScienceDirect)  
**DOI:** `https://doi.org/10.1016/j.heliyon.2019.e02972`  
**Received:** 7 August 2019 | **Received in revised form:** 30 October 2019 | **Accepted:** 28 November 2019  

**Authors:**  
Nagaraja Kamsali\*, S.C. Chakravarty, Praveen Kumar Basuvaraj  

**Affiliation:**  
Department of Physics, Bangalore University, Bengaluru, India  

\* **Corresponding author:** `kamsalinagaraj@bub.ernet.in` (N. Kamsali)

**Keywords:** Astrophysics; Planetary sciences; Particle physics; GCR; HZE particle flux; Space radiation; Mars exploration; Sunspot cycles; SNR cycle 25

---

## Abstract

Manned Mars missions planned in the near future of very low solar activity period and hence higher than acceptable radiation doses due mainly to the Galactic Cosmic Rays (GCR), would require special techniques and technological development for maintaining the good health of the astronauts. The present study is an attempt to make an assessment and characterise the coming years in terms of solar activity and space radiation environment especially due to the abundance of highly energetic heavy ions (known as HZE charged particles). These HZE particle fluxes constitute a major hazard to the astronauts and also to the critical electronic components of the spacecraft. Recent data on the HZE species (from $\text{B}$ to $\text{Ni}$) obtained from ACE spacecraft shows a clear enhancement of the particle fluxes between the solar cycle 23 and solar cycle 24 ($\sim$between SSN peaks 2002 and 2014) due to the persisting low sunspot numbers of the latter cycle. The peak values of these cosmic ray fluxes occur with a time lag of about a year of the corresponding minimum value of the sunspots of a particular 11-year cycle which is pseudo-periodic in nature. This is demonstrated by the Fourier and Wavelet transform analyses of the long duration (1700–2018) yearly mean sunspot number data. The same time series data is also used to train a Hybrid Regression Neural Network (HRNN) model to generate the predicted yearly mean sunspot numbers for the solar cycle 25 ($\sim$2019–2031). The wavelet analysis of this new series of annual sunspot numbers including the predictions up to the end of 2031 shows a clear trend of continuation of the low solar activity and hence continuation of very high HZE fluxes prevailing in Solar cycle 24 into the solar cycle 25 and perhaps beyond.

---

## 1. Introduction

Astronauts undertaking future space voyages to Mars would need to spend long periods of at least 1–2 years to gather information about its surface features, geological, environmental and atmospheric phenomena, including efforts for a confirmatory evidence of possible existence of any form of present or past life. Extending this goal to gear up for a human settlement in Mars, plans are afoot to realise manned Mars missions within the next decade (NASA, 2013). In addition to general safety considerations, mission to Mars involving such long duration stays would need to be carefully designed to minimise the doses of potentially damaging solar and cosmic radiations which could constrain the planetary work schedule to the extent of jeopardising the mission objectives. While in transit through Earth's magnetosphere the spacecraft shielding brings down the radiation effects considerably, the situation in Martian space would be harsher with only relatively marginal natural shielding of the atmosphere and the non-existent magnetosphere (ICRP, 2013).

The radiation exposure measured by the absorbed dose, $D$, is the mean energy deposited per unit mass and given below as Eq. (1):

$$D = \frac{d\overline{E}}{dm} \quad (1)$$

where $\overline{E}$ is the mean energy and $m$ the mass of the absorbing matter, $D$ is given in units of Gray ($\text{Gy}$) and $1\text{ Gy}$ is equal to $1\text{ J/kg}$ which is equal to $100\text{ rads}$, one rad being equivalent to the absorption of $100\text{ ergs}$ per gram.

For biological tissues, each type of radiation has an ionisation potential, determining the equivalent dose $H_T$ given below in Eq. (2):

$$H_T = \sum_R W_R \times D_{T,R} \quad (2)$$

where $D_{T,R}$ is the absorbed dose for radiation type $R$; $T$ stands for a particular tissue and $W_R$ varying with the type of radiation, is the quality or weighting factor.

The equivalent dose is measured in Sieverts ($\text{Sv}$), which is $1\text{ J/kg}$, equal to $100$ Roentgen equivalent man ($\text{rem}$) (ICRP, 2007). To illustrate the potential risks involved, the Apollo astronauts received average radiation doses of $1.6\text{ mGy}$ ($1\text{ mGy} = 0.001\text{ Gy}$) to $14\text{ mGy}$ over two weeks. Assuming a quality factor of around $4$, the missions resulted in an equivalent dose of $6.4\text{ mSv}\text{--}56\text{ mSv}$ during the return moon trips, which is greater than the allowable radiation workers' yearly dose limit of $50\text{ mSv}$ ($5\text{ rem}$) and maximum public allowable exposure limit of $1\text{ mSv}$ ($0.1\text{ rem}$) per annum.

The major components of space radiation consist of high energy ionising charged particles such as heavy ions (from $\text{Be}$ to $\text{Ni}$), protons and beta particles. Through nuclear interactions of these charged particles with materials of spacecraft, planetary surface, atmosphere, base structures, and the space suits of astronauts, secondary radiation of energetic albedo neutrons and protons can be produced further enhancing the overall radiation exposure. For a long duration manned Mars mission, the high energy (primarily in the hundreds of $\text{MeV}$ to many $\text{GeV}$ range peaking around $1\text{ GeV}$) protons and high ($H$) energy ($E$) and high atomic number ($Z$) ions called HZE particles of the Galactic Cosmic Rays (GCR) are the major contributors to space radiation doses (Simpson, 1983; O'Neill, 2006). Due to their high energies and high Linear Energy Transfer ($\text{LET}: dE/dx$) values, it is difficult to shield HZE radiations and make a realistic estimate of experimentally verified biologically effective doses. High energy (in $\text{keV}\text{--}\text{MeV}$ range) solar charged particle radiations with a component of moderate energy and high $Z$ ions are also important to consider. However the exposure to these radiations could be controlled by nominal shielding and avoiding open space ventures during intense eruptive processes of sun (lasting for a few hours to few days) called Solar Particle Events (SPE) as these can be predicted to a degree of reliability (Bertsch et al., 1969; Kim et al., 2011).

The intensity of the GCR flux varies over the 11 year solar cycle due to the changes in the interplanetary plasma emanating from the expanding solar corona resulting in maximum doses during the solar minimum year (Babcock, 1961; Badhwar and O'Neill, 1992). The equivalent annual radiation dose from GCR in interplanetary free space has been estimated to be about $0.73\text{ Sv/year}$ and $0.28\text{ Sv/year}$ during solar minimum and solar maximum years respectively (Borggräfe et al., 2009). While the dose rates (estimated using OLTARIS website (Singleterry et al., 2010)) vary between $0.33$ and $0.08\text{ Sv/year}$ on the surface of Mars due to planet self-shielding and some attenuation through the thin Martian $\text{CO}_2$ atmosphere of about $16\text{ g/cm}^2$ using further aluminium shielding of even $20\text{ g/cm}^2$ does not reduce the dose rates appreciably ($0.26$ & $0.07$ as against $0.33$ & $0.08\text{ Sv/year}$). Hence the prevention against the GCR radiation doses is the main challenge to undertake manned Mars missions particularly during the solar minimum period.

The main purpose of the present research is to examine the details of the variations of solar activity during solar cycles 23, 24 and 25 covering the period up to $\sim$2031 for an assessment of risks involved in manned Mars missions. Suitably shielded robotic Mars missions may prove to be a better alternative during the low solar activity conditions.

---

## 2. Data and method of analysis

As mentioned above, future Mars missions would need to guard from the deleterious space radiation primarily due to the continuous influx of GCR charged particles which are difficult to filter out by reasonable shielding techniques on Martian surface. As already seen the temporal variation of this radiation is anti-correlated with the changes in solar activity revealed mainly by the sunspot numbers. However in the present context it is necessary to have a better understanding of the variation of the long term changes in solar activity with its inherent periodicities and possible predictions up to the year 2031 or till the end of the $25^{\text{th}}$ solar cycle. The results of this analysis along with the recent data on GCR fluxes from spacecraft measurements are examined for projecting the levels of this radiation in the years to come.

The internationally revised daily and annual mean sunspot number (SSN) data used here are obtained from the World Data Centre (WDC) for the production, preservation and dissemination of the international sunspot number in Brussels (`http://www.sidc.be/silso/`). The GCR data has been downloaded from Advanced Composition Explorer (ACE) Science Centre covering the period 1997–2019.

Hybrid Regression Neural Network (HRNN) technique is used along with a programme code generated by Daniel Okoh and available to users (published in MathWorks website, 2018: `https://in.mathworks.com/matlabcentral/fileexchange/65686`) to predict the smoothed yearly mean SSN for the solar activity cycle 25. The SSN time series with and without these predictions are subjected to Fast Fourier Transform (FFT) and Wavelet Transform analyses to determine the relative amplitudes of the main periodicities and their combined effect on variation of SSN in the coming decades, as this is one of the key parameters to predict GCR radiation environment in space and on Mars.

---

## 3. Results and discussion

The charged particle fluxes of GCR are measured by the Cosmic Ray Isotope Spectrometer (CRIS) instrumental payload on board ACE spacecraft that was launched around L1 point on August 25, 1997 (Stone et al., 1998). It is designed to measure the elemental and isotopic composition of GCR over 7 energy bands spanning $\sim 50\text{--}500\text{ MeV/nucleon}$. The energy bands are different for each element. The energy bands are provided along with the fluxes (counts) of the ionic species by the ACE Science Centre (`http://www.srl.caltech.edu/ACE/ASC/index.html`).

Figure 1 shows a sample plot (facilitated by the data centre) for daily average Boron ion counts in 7 energy bands ($51.4\text{--}160.2\text{ MeV}$) during the period 1 Jan 2000 to 2 Mar 2018 covering two solar minimum (2009, 2018/19) and two solar maximum (2002, 2014) activity years. While the inherent inaccuracy in the measurements is not a limiting factor to discern relative temporal variabilities between different energy bands, detailed information regarding the calculation of the CRIS intensities and related errors are given in the references (George et al., 2009; Lave, 2012a, 2012b). The energy-band associated colour-coded particle counts show decreasing trend with increasing energy of Boron ion and its anti-correlation with solar activity for all energy bands; counts peaking near the minimum solar activity years. Similar characteristic variations are observed in other 23 plots (not shown here) pertaining to the elements from Carbon ($\text{C}$) to Nickel ($\text{Ni}$).

> **Figure 1.** ACE/CRIS Level-2 Data plot of Boron ion counts during 1 Jan 2000–2 Mar 2018 for 7 different energy range between $51.4$ and $160.2\text{ MeV/nucleon}$.

The level 2 CRIS data is organised into 27-day time periods (Bartels Rotations — roughly one solar rotation period). For each Bartels rotation time average particle flux values are provided for 24 elements ($\text{C}$ to $\text{Ni}$), in units of $\text{particles}/(\text{cm}^2 \cdot \text{sr} \cdot \text{sec} \cdot \text{MeV/nucleon})$, in 7 energy bands mentioned above. Figure 2 shows sample time series plots of selected ion particle fluxes of $\text{B}$, $\text{F}$, $\text{Sc}$ and $\text{Fe}$ (atomic numbers $5$, $9$, $21$ and $26$) which are representative of the general pattern of long term variation with solar activity. The monthly average sunspot numbers for the solar cycles 23 and 24 are also plotted as secondary y-axis.

> **Figure 2.** ACE/CRIS Level-2 Data plots of Bartels Rotation (27 day) average cosmic ray element fluxes of Boron ($\text{B}$), Fluorine ($\text{F}$), Scandium ($\text{Sc}$) and Iron ($\text{Fe}$) ions during 1997–2018 for roughly similar energy bands. The monthly mean SSN are also shown for comparison.

The anti-correlation between the GCR flux and SSN can be seen for all the 4 GCR elements. Flux values of GCR elements $\text{B}$ and $\text{Fe}$ are higher by more than one order of magnitude compared to those of $\text{F}$ and $\text{Sc}$ throughout the observation period. While the GCR flux values are considerably lower at SSN peak years (2002 and 2014), the overall level of fluxes is considerably higher during the period of solar cycle 24 as compared to cycle 23 since the sun is going through a very low 11-year activity phase under cycle 24. This result is further expanded in Figure 3 showing contours of particle fluxes ($\text{Si}$ and $\text{Fe}$) using the same data set but retaining the information of the full energy coverage of all the 7 bands. The plots indicate the following characteristics related mainly to solar cycles 23 and 24: (a) the flux intensities peak around $200\text{--}300\text{ MeV}$ of particle energies, (b) lower SSN values in cycle 24 has given a prolonged period of higher GCR fluxes between 2007–2018 when the 11 year SSN values were very low compared to the previous 11 years, (c) there is a lag of at least one year between the SSN minimum and flux maximum evidenced from the concurrent plot of monthly mean SSN values. The figure also provides an unconfirmed clue that the low solar activity related GCR fluxes would continue to be higher by a factor of 2 in the coming years if the trend of low solar activity persists for the next cycle 25. The trends also suggest that the starting of cycle 25 may be delayed or may be slow to pick up in solar activity resulting in continuation of enhanced GCR fluxes.

> **Figure 3.** ACE/CRIS Level-2 Data plots of Bartels Rotation (27 day) average cosmic ray element fluxes of Silicon ($\text{Si}$) and Iron ($\text{Fe}$) ions during 1997–2018 covering observations in all the energy bands. The monthly mean SSN values are also shown for reference.

Results presented so far and further studies in this direction require a better appreciation of different periodicities of solar activity leading to variations in the radiation environment. In view of this and taking advantage of the availability of a very long series of SSN data since 1700, a detailed analysis has been carried out using FFT, Wavelet and Neural Network techniques. The results provide insights into the likely future changes in solar activity during the solar cycle 25. Figure 4 shows the FFT frequency spectrum of the yearly mean sunspot numbers for the time interval 1700–2018. The discrete frequencies are equivalent to solar activity cycles of 11, 22, 53 and 107 years. It is seen that 11 year periodicity has maximum power followed by that of 107 (about 20% power compared to the 11 year cycle), 53 and 22 year periodicities.

> **Figure 4.** Power spectrum of yearly mean SSN data series (1700–2018) showing discrete frequencies (periods) of prominent solar activity cycles of approximately 11, 22, 53 and 107 years.

It is known that the SSN peak year values vary from solar cycle to cycle. The 11 year cycle is actually pseudo-periodic, and the past SSN data over centuries show that its amplitude of maxima varies by a factor of 2–3. The signal strength of the Gleissberg cycle (Frick et al., 1997) of $\sim$100 years duration is strong enough to modulate the main cycle of 11 years as can be seen from Figure 4. This modulation can be studied in more detail by subjecting the yearly mean SSN data to wavelet analysis.

The FFT spectrum provides major frequency components with different sinusoidal wave periods but does not provide details of the relative magnitude of different prominent waves as a function of time. This is done by continuous wavelet analysis. The continuous wavelet transform is the sum over all time of the signal multiplied by scaled, shifted versions of the wavelet. This process produces wavelet coefficients that are a function of scale and position (Torresani, 1995). From the FFT analysis the main periods for the sunspot cycles are obtained as 11, 22, 53 and 107 years. The corresponding wavelet scales lie within 1–128 in a continuous 1-D wavelet spectrum.

Figure 5 shows this continuous wavelet spectrum of the yearly mean values of SSN time series during 1700–2018. It is clear from the figure that the maximum and minimum values of SSN related to different 11-year solar cycles go through a regular modulation of about 100 years. The wavelet spectrum shows very low values of coefficients for the entire range of scales (frequencies) during three groups of solar cycles around 1800, 1900 and 2000 when the SSN peak values of corresponding solar cycles were about less than half of the normal peak SSN values. The effect of this coincidence for the first and second groups lasted for 2–3 solar cycles (approximately 30 years). From the pattern of variations of these coefficients it is seen that the solar cycles 24 is going through this epoch of low solar activity. It is indicated that this third epoch may continue to the future solar cycles establishing the pattern of low solar activity trend of 2–3 solar cycles every 100 years. However this cannot be verified fully as existing predictive models at best project yearly mean sunspot numbers only for the next solar cycle 25 (Bhowmik and Nandy, 2018; Hathaway and Upton, 2016). An attempt has been made in our study to forecast sunspot numbers of solar cycle 25 running the publicly available HRNN model developed by Daniel Okoh and the results given in Okoh et al. (2018) mentioned earlier and generate a new set of continuous wavelet spectrum by extending the time series of annual mean SSN data to the year 2031 or to the end of solar cycle 25.

> **Figure 5.** Top panel: Yearly mean SSN (y-axis) time sequence during 1700–2018 period corresponding to 319 points (x-axis); Bottom panel: contours of continuous (1D) wavelet coefficients colour coded from minimum to maximum values for scales 1–128 (covering major FFT frequencies: see Figure 4) for the same time period of 319 years.

In HRNN model, regression analysis is combined with neural network learning for forecasting the SSN. The programme package consists of 2 executable files and one text file for inputs/outputs. Downloading this package from MathWorks website (`https://in.mathworks.com/matlabcentral/fileexchange/65686`), it is run to obtain the smoothed yearly mean SSN values for the period 2019–2031 covering the solar cycle 25. The resultant predictions are added to the observed SSN series data till 2018 and the wavelet analysis is repeated for the entire range 1700–2031 (332 years). The result of such analysis is shown in Figure 6. It can be seen that the basic pattern of variation with the very low spell of solar activity is repeating roughly every 100 years. But the overall coincidence of low values of wavelet coefficients along the entire range of scales (vertical columns in Figure 5) continuing during the third group of low solar activity starting from solar cycle 24 indicates a higher probability of a situation like the first group of low solar activity. Hence from visual pattern recognition it is clear that the very low solar activity period is likely to continue not only up to 2031 but perhaps beyond during at least up to solar cycle 26 ($\sim$2031–2042), i.e., a spell of 3 solar cycles like the first group. While this is only a model prediction, it however implies that GCR radiation flux is likely to be near its peak at least during the solar cycle 25 and with little less certainty during the cycle 26 also. From the results of a predictive radiation model developed by Badhwar and O'Neill (1992), it is estimated that the HZE particle fluxes inside a typical spacecraft in interplanetary space could be enhanced by a factor of 3 for the low SSN cycles like 24. Hence continuous and very high doses of deleterious cosmic radiation are expected at least up to 2032 taking into account the lag factor of 1 year shown earlier. It is known that while fluxes of HZE particles are only a fraction of the GCR small ions ($\text{H}$ and $\text{He}$), their LET (a function of $z^2$, $z$ being the ion charge or the atomic number) is very high (Chen et al., 1994) and coupled with their $\text{MeV}\text{--}\text{GeV}$ energy range are very difficult to shield. Hence the current projections during solar cycle 25 would lead to higher cosmic radiation exposures in future as demonstrated in a statistical model of correlation between solar activity and GCR deceleration potential (Kim et al., 2006).

> **Figure 6.** Top panel: Yearly mean SSN (y-axis) time sequence during 1700–2031 period corresponding to 331 points (x-axis); Bottom panel: contours of continuous (1D) wavelet coefficients colour coded from minimum to maximum values for scales 1–128 (including corresponding major FFT frequencies) for the period 1700–2031, including the HRNN model generated annual mean SSN values between 2019–2031.

From the above results it is clear that planning of any human Mars mission in near future should consider the long term cumulative effects of the high levels of GCR/HZE fluxes to minimise the exposure to maintain the acceptable career dose levels. Considerable research and technology development may be required to realise special shielding and other safeguarding strategies from these lethal radiations. As a follow up to this research work we intend to model the scenario of various shielding and other associated measures to carry out future exploration of Mars.

---

## 4. Conclusion

In this study an effort is made to characterise the space radiation environment mainly pertaining to the cosmic rays HZE particle fluxes that would be encountered by future human and robotic missions to Mars due to the likely continuation of a very low sunspot activity period. While the biological effectiveness to cause cell damage of these high LET radiations require a better understanding, it is clear that its long term exposure would constitute a major hazard. In our work the state of solar activity in the ensuing solar cycle 25 is predicted using a HRNN model. The yearly mean SSN data for 331 years (1700–2031) are subjected to Fourier and continuous 1-D wavelet analysis. It is shown that apart from the main 11 year solar Schwabe cycle, the SSN also has a strong Gleissberg cycle of $\sim$100 years. Also it has revealed that the years affected by continuously existing weak wavelet coefficients over the entire range of scales/frequencies lead to a predictable spell of overall lower than normal activity of sun as evidenced from the situation of the $24^{\text{th}}$ and $25^{\text{th}}$ SSN cycles. Further research is being pursued to model spacecraft shielding, spacesuit and related safeguards for the astronauts should they venture a trip to Mars.

---

## Declarations

### Author contribution statement
Nagaraja Kamsali, S.C. Chakravarty, Praveen Kumar Basuvaraj: Conceived and designed the experiments; Performed the experiments; Analyzed and interpreted the data; Contributed reagents, materials, analysis tools or data; Wrote the paper.

### Funding statement
This work was supported by Bangalore University, India; Indian Space Research Organisation, India.

### Competing interest statement
The authors declare no conflict of interest.

### Additional information
No additional information is available for this paper.

### Acknowledgements
Authors acknowledge the use of data from WDC for internationally revised monthly and annual mean sunspot numbers (v2.0) from SILSO data/image, Royal Observatory of Belgium, Brussels and the cosmic ray high energy particle flux data from ACE-Science centre.

---

## References

* Babcock, H.W., 1961. The topology of the Sun's magnetic field and the 22-year cycle, 1961. *Astrophys. J.* 133 (2), 572–587.
* Badhwar, G.D., O'Neill, P.M., 1992. An improved model of galactic cosmic radiation for space exploration missions. *Int. J. Radiat. Appl. Instrum. D Nucl. Tracks Radiat. Meas.* 20 (3), 403–410.
* Bertsch, D.L., Fichtel, C.E., Reames, D.V., 1969. Relateve abundance of iron-group nuclei in solar cosmic rays. *Astrophys. J.* 157, L53–L56.
* Bhowmik, P., Nandy, D., 2018. Prediction of the strength and timing of sunspot cycle 25 reveal decadal-scale space environmental conditions. *Nat. Commun.*
* Borggräfe, A., Quatmann, Michael, Daniel, Nölke, 2009. Radiation protective structures on the base of a case study for a manned Mars mission. *Acta Astronaut.* 65, 1292–1305.
* Chen, J., Chenette, D., Clark, R., Garcia-Munoz, M., Guzik, T.G., Pyle, K.R., Sang, Y., Wefel, J.P., 1994. A Model of galactic cosmic rays for use in calculating linear energy transfer spectra. *Adv. Space Res.* 14 (10), 765–769.
* Frick, P., Galyagin, D., Foyt, D.V., E Nesme-Ribes, K.H., Schatten, D Sokoloff, Zakharov, V., 1997. Wavelet analysis of solar activity recorded by sunspot groups. *Astron. Astrophys.* 328, 670–681.
* George, J.S., Lave, K.A., Wiedenbeck, M.E., Binns, W.R., Cummings, A.C., Davis, A.J., de Nolfo, G.A., Hink, P.L., Israel, M.H., Mewaldt, R.A.R.A., Scott, L.M., Stone, E.C., von Rosenvinge, T.T., Yanasak, N.E., 2009. Elemental composition and energy spectra of Galactic Cosmic Rays during cycle 23. *Astrophys. J.* 698 (2), 1666–1681.
* Hathaway, D.H., Upton, Lisa A., 2016. Predicting the amplitude and hemispheric asymmetry of solar cycle 25 with surface flux transport. *J. Geophys. Res. Space Phy.* 121 (10), 744–10,753.
* ICRP, 2007. The Recommendations of the International Commission on Radiological Protection, 0146-6453.
* ICRP, 2013. Assessment of radiation exposure of astronauts in space ICRP Publication 123. *Ann. ICRP* 42 (4), 42(4):1–339.
* Kim, M.Y., Wilson, J.W., Cucinotta, F.A., 2006. A Solar cycle statistical model for the projection of space radiation environment. *Adv. Space Res.* 37 (9), 1741–1748.
* Kim, M.Y., De Angelis, Giovanni, Cucinotta, Francis A., 2011. Acta Probabilistic assessment of radiation risk for astronauts in space missions. *Astronautica* 68, 747–759.
* Lave, K.A., 2012a. *The Interstellar Transport of Galactic Cosmic Rays*. Ph. D. Thesis. Washington University, St. Louis. `http://openscholarship.wustl.edu/etd/707`.
* Lave, K.A., 2012b. Thesis Erratum. `www.srl.caltech.edu/ACE/ASC/DATA/level3/cris/Erratum_11-20-122.pdf`.
* Okoh, D.I., Seemala, G.K., Rabiu, A.B., Uwamahoro, J., Habarulema, J.B., Aggarwal, M., 2018. A Hybrid regression-neural network (HR-NN) method for forecasting the solar activity. *Space Weather* 16 (9).
* O'Neill, P.M., 2006. Badhwar-O'Neill galactic cosmic ray model update based on advanced composition explorer (ACE) energy spectra from 1997 to present. *Adv. Space Res.* 37 (9), 1727–1733.
* Simpson, J.A., 1983. Elemental and isotopic composition of the galactic cosmic rays. *Annu. Rev. Nucl. Part Sci.* 33, 323–381.
* Singleterry, R.C., Blattnig, S.R., Clowdsley, M.S., Qualls, G.D., Sandridge, C.A., Simonsen, L.C., Norbury, J.W., Slaba, T.C., Walker, S.A., Badavi, F.F., Spangler, J.L., Aumann, A.R., Zapp, E.N., Rutledge, R.D., Lee, K.T., Norman, R.B., 2010. OLTARIS: On-Line Tool for the Assessment of Radiation in Space. NASA/TP-2010-216722.
* NASA, 2013. Radiation Shielding Optimisation on Mars, Tony C. Slaba, Christopher J. Mertens, and Steve R. Blatting. Langley Research Center, Hampton, Virginia. NASA/TP-2013-217985.
* Stone, E.C., Frandsen, A.M., Mewaldt, R.A., Christian, E.R., Margolies, D., Ormes, J.F., Snow, F., 1998. The advanced composition explorer. *Space Sci. Rev.* 86, 1–22.
* Torresani, B., 1995. *Analyse continue par ondelettes*, Inter-editions. Savior Actuels.