# Identification of health events in astronaut missions using longitudinal molecular signature detection

**Authors:** G. I. Mias$^{1,2,3}$, C. Piermarocchi$^{3}$, J. M. Charvat$^{4}$, B. E. Crucian$^{5}$, S. M. Smith$^{5}$, S. R. Zwart$^{6}$, M. Zheng$^{1}$, and S. Xue$^{1,3}$

**Affiliations:**
1. Institute for Quantitative Health Science and Engineering, Michigan State University, East Lansing, MI 48824, USA
2. Department of Biochemistry and Molecular Biology, Michigan State University, East Lansing, MI 48824, USA
3. Department of Physics and Astronomy, Michigan State University, East Lansing, MI 48824, USA
4. KBR, Houston, TX 77058, USA
5. NASA Johnson Space Center, Houston, TX 77058, USA
6. University of Texas Medical Branch, Galveston, TX 77555, USA

**Correspondence:** `gmias@msu.edu`

## Background

Individualized health monitoring can now incorporate a precision medicine approach, profiling multiple molecular and physiological measures of health (generalized omics) longitudinally to enable the timely diagnosis and treatment of disease. Such measurements can include blood chemistries, gene expression data, metabolite measurements, and digital device data. We will present our work on extending such an approach to monitoring individual astronaut health for deep space missions. We have developed and implemented novel algorithms to monitor and detect physiological state departures from individualized healthy astronaut baselines, utilizing and biologically annotating generalized omics. Our new methods can detect baseline deviations across omics corresponding to potentially adverse medical events. Events pointing to changes in individual health are then compared across individuals to identify common responses and detect changes affecting multiple crewmembers. We show the utility of our methods in detecting temporal health changes across subjects using retrospective Earth and astronaut mission data (metabolite and immune marker data across multiple missions), in order for this technique to be applicable for future missions.

## Methods and Results

We will summarize results from:

1. An Earth-based study using individual omics monitoring (RNA, proteomics, and microbiome data) from prediabetics and diabetics subjected to immune and stress responses; and
2. Retrospective astronaut data ($n=27$) from a cohort spanning long-duration missions on the ISS, using data from Immune Monitoring and Nutritional Status Assessment studies where we detected individual changes in astronaut generalized omics, common trends, and groups/communities of astronauts with similar temporal responses.

Our omics time series pattern detection and characterization methods focused first on identifying changes in individual subjects in each study by detecting changes from their own baseline:

* We used spectral methods and periodograms/autocorrelations (comparisons of a signal to a delayed version of itself) to detect patterns within each omics, and group collective omics behavior showing deviations from each individual's baseline.
* We used the correspondence of time series to graph/network representations (visibility graphs) to identify aggregate changepoints that could correspond to potentially adverse medical events.

Our methods accounted for practical aspects of astronaut time series analyses, including underlying noise, uneven sampling rates, missing data (without imputation), and sampling over different time-scales for different data modalities. All code and methods are available through our open source Python package **PyIOmica** (<https://github.com/gmiaslab/pyiomica>), which includes a broad range of utilities for processing and annotating time series.

After identifying individual trends and classifying them into temporal categories, we then compared across subjects using a network approach. In such a network, subjects were connected with edges based on the temporal similarity of their generalized omics/measurement spectra. Using the network structural characteristics, we identified communities of subjects with similar temporal behavior, both in the Earth-based and astronaut studies. The community memberships corresponded to different macroscopic/phenotypic characteristics of the constituent community members.

## Outlook

We have implemented our spectral-based time series approach to both monitoring individualized changes, as well as comparing such changes across subjects to identify communities of subjects displaying similar physiological responses in time, both using Earth- and space-collected omics data. Such personalized, longitudinal monitoring of generalized omics signals has high utility for monitoring astronauts, especially if coupled to non-invasive approaches (e.g., digital devices, saliva omics profiling). Our approach is an extensible prototype that can improve NASA's ability to detect medical events and deviations from a healthy baseline during flight, and design timely interventions with countermeasures, to maintain individualized wellness for personnel in both short and long-duration space missions.

## Acknowledgments

*Research reported was supported by the Translational Research Institute for Space Health, through NASA NNX16A069A (Project Number T0412).*