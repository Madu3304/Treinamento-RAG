**arXiv:2509.09051v1 \[physics.comp-ph\] 10 Sep 2025**

# An Improved Rapid Performance Analysis Model for Solenoidal Magnetic Radiation Shields

**Joseph L. Hesse-Withbroe\*, Katya S. Arquilla**

*Smead Department of Aerospace Engineering Sciences, University of Colorado, Boulder, 3775 Discovery Dr, Boulder, 80303, CO, USA*

*Preprint submitted to Elsevier*

**Highlights:**
* Crewed spaceflight
* Space technology
* Space radiation
* Magnetic shields
* GCR

**Keywords:** Crewed spaceflight; Space technology; Space radiation; Magnetic shields; GCR

$^*$ *Corresponding author:* joseph.hesse-withbroe@colorado.edu (J.L. Hesse-Withbroe); katya.arquilla@colorado.edu (K.S. Arquilla)
*ORCID(s):* [0000-0001-6812-5369](https://orcid.org/0000-0001-6812-5369) (J.L. Hesse-Withbroe)

> **ABSTRACT**
>
> Astronauts participating in deep-space exploration missions will be exposed to significantly greater amounts of radiation than is typically encountered on Earth or in low Earth orbit (LEO), which poses significant risks to crew health and mission safety. Active magnetic radiation shields based on the Lorentz deflection of charged particles have the potential to reduce astronaut doses with lower mass costs than passive shielding techniques. Typically, active shielding performance is evaluated using high-fidelity Monte Carlo simulations, which are too computationally expensive to evaluate an entire trade space of shield designs. A rapid, semi-analytical model based on the High Charge and Energy Transport code (HZETRN) developed in 2014 provided an alternative method by which to evaluate the performance of solenoidal shields. However, various simplifying assumptions made in the original model have limited its accuracy, and therefore require evaluation and correction. In this work, a number of aspects of the original semi-analytical model are updated and validated by Monte Carlo simulation, then used to recharacterize the design trade space of solenoidal magnetic shields. The updated model predicts improved performance for weaker shields as compared to the original model, but greatly diminished performance for strong shields with bending powers greater than $20\text{ T}\cdot\text{m}$. Overall, the results indicate that magnetic shields enable significant mass savings over passive shields for mission scenarios where the requisite dose reduction is greater than about $60\%$ relative to free space, which includes most exploration missions longer than one year with significant time spent outside LEO.

---

## 1. Introduction

The deep space radiation environment, consisting of both solar energetic particles (SEPs) and galactic cosmic rays (GCRs), represents a major obstacle currently impeding our ability to conduct long-duration crewed exploration missions beyond LEO. Exposure to this space radiation causes myriad physiological effects that impact both crew and mission safety and are comprehensively reviewed in Willey et al. (2021). Chief among the health detriments are acceleration of bone degradation (Macias et al., 2016), cataractogenesis (Ainsbury et al., 2009), cognitive decrements (Davis et al., 2014; Hadley et al., 2016; Jewell et al., 2018), degenerative cardiovascular and renal diseases (Patel et al., 2015; Siew et al., 2024), and carcinogenesis (Gilbert, 2009; Ozasa et al., 2018).

The multitude of detrimental physiological effects of radiation exposure necessitate mitigation to limit their impact on crew health and mission safety. NASA's established career permissible exposure limit (PEL) for spaceflight-associated radiation dose is $600\text{ mSv}$ for all astronauts (Francisco, 2023). This limit was designed to limit the risk of exposure-induced death associated with fatal carcinogenesis to $3\%$ for all crewmember demographics, evaluated at the upper $95\%$ confidence bound (Cucinotta, 2010). The total dose for an 860-day conjunction-class crewed Mars mission during solar maximum (e.g. Mars Design Reference Architecture 5.0 (Simon et al., 2017)) for a lightly shielded habitat has been estimated to be $1.01\text{ Sv}$, far in excess of the NASA career PEL (Hassler et al., 2014). Passive shields have been shown to be incapable of reducing doses to acceptable levels for long-duration exploration missions without excessive mass costs on the order of hundreds of tons (Norman et al., 2017; Case, 2021).

Alternative, mass-efficient radiation mitigation approaches are necessary to bring anticipated dose rates in line with permissible limits. Shields based on the Lorentz deflection of charged particles using superconducting electromagnets have been studied since the beginning of the space program (Ferrone et al., 2023). The dose reduction capability of these shields is typically estimated using high-fidelity Monte Carlo simulations of particle interaction with matter and magnetic fields (e.g., Battiston et al. (2011); Westover et al. (2014); Vuolo et al. (2016); Calvelli et al. (2017); Chesny et al. (2020); Ferrone et al. (2021); Al Zaman and Monira (2023)). While these approaches enable a highly accurate quantification of shielding performance, they require significant computational resources and are prohibitively expensive for use in a trade study wherein the influence of key design parameters on shield performance must be quantified in order to identify optimal designs. Previous efforts have also often neglected to include comprehensive system mass estimates, which prevents their benchmarking against existing solutions and limits the utility of their results.

In this article, a brief overview of the operating principles of a magnetic radiation shield is provided. Then, improvements to a semi-analytical shield mass and dose estimation model (Washburn et al., 2014, 2015) based on the deterministic radiation transport code HZETRN (Slaba et al., 2020) are discussed. First, a correction factor is added to rectify a performance bias introduced by the original model's assumption of field uniformity. Second, a refined analytical description of GCR flux into the protected habitat is derived and is shown via Monte Carlo simulation to more accurately predict the magnetically-attenuated GCR spectrum inside the shield. Finally, the updated attenuation model also enables the estimation of dose throughout the entire volume of the protected habitat, whereas the original model was limited only to dose estimates at points along the central axis of the habitat. These updates to the model yield more accurate performance estimation of solenoidal radiation shields while maintaining the computational efficiency of the original model.

## 2. Theory

The fundamental physics that describes the operating principles of a solenoidal magnetic radiation shield are described in the following subsections.

### 2.1. Magnetic Deflection of Charged Particles

The motion of a charged particle in a pure magnetic field is described by the Lorentz equation, given by

$$
\mathbf{F}_{L} = q\mathbf{V} \times \mathbf{B} \tag{1}
$$

where $q$ is the particle's charge, $\mathbf{V}$ is its velocity, and $\mathbf{B}$ is the magnetic flux density at the location of the particle. From this expression, it can be shown that particle motion in a magnetic field of uniform flux density is circular. This gyromotion has a characteristic gyroradius given by

$$
r_{g} = \gamma \frac{R}{B} = \gamma \frac{m_{0}V_{\perp}}{qB} \tag{2}
$$

where $\gamma$ is the relativistic Lorentz factor, $R$ is the particle's magnetic rigidity, $m_{0}$ is the particle's rest mass, and $V_{\perp}$ is the component of the particle's velocity perpendicular to the magnetic field (Griffiths, 2013). Eq. (2) can be rearranged to express the particle's kinetic energy as a function of its gyroradius:

$$
K(r_{g}) = \sqrt{\left(\frac{r_{g}qBc}{\sin\theta}\right)^{2} + (m_{0}c^{2})^{2}} - m_{0}c^{2} \tag{3}
$$

where $\theta$ is the angle between the particle's velocity and the direction of the uniform magnetic field.

### 2.2. Generation of Magnetic Fields

A shield's strength is best described in terms of its bending power (the path-integrated magnetic flux density, expressed in $\text{T}\cdot\text{m}$). The requisite bending powers for a shield capable of deflecting meaningful amounts of GCR radiation necessitate the generation of extremely strong magnetic fields on the order of $\sim 1\text{ T}$. Superconducting electromagnets have previously been shown to be the most viable means of producing sufficient fields without excessive mass penalties (Washburn, 2013). A current loop $C$ produces a magnetic field at a point $\mathbf{r}$ according to the Biot-Savart Law

$$
\mathbf{B}(\mathbf{r}) = \frac{\mu_{0}}{4\pi} \int_{C} \frac{I d\mathbf{l} \times \mathbf{r}'}{\vert{}\mathbf{r}'\vert{}^{3}} \tag{4}
$$

where $\mu_{0}$ is the permeability constant, $I d\mathbf{l}$ is an infinitesimal current element along loop $C$, and $\mathbf{r}'$ is the displacement vector from the current element to $\mathbf{r}$. Analytical solutions to Eq. (4) exist for a few ideal geometries. For example, the magnetic field at the center of an ideal, long, thin-walled solenoid aligned with the $Z$ axis is given by

$$
\mathbf{B} = \frac{\mu_{0}NI}{\sqrt{(D^{2} + h_{s}^{2})}}\hat{z} \tag{5}
$$

where $N$ is the number of coil windings, $I$ is the coil current, $D$ is the coil diameter, and $h_{s}$ is the coil length (Iwasa and Marken, 1995). The spatial variation of the field within the bore of the solenoid is generally assumed to be negligible.

> **Figure 1:** Geometry of a solenoidal shield surrounding a representative habitat (grey) with relevant features and dimensions labeled.
> * **Left (3D view):** The shield is modeled as an annular cylinder (blue, height $h_s$, inner radius $r_i$, outer radius $r_o$) surrounding the shielded habitat (grey, height $h_h$, radius $r_h$) with uniform magnetic flux density $\mathbf{B}$ throughout. A GCR proton (red) approaching with polar incidence angle $\theta$ strikes the shield and is deflected into a small spherical water phantom located at $(r=r_p, \phi=0, z=h_p)$. Only one of the six solenoids in this design is shown.
> * **Right (Top-down $X$-$Y$ cross-section):** Shows the annular shield ($r_i$ to $r_o$), solenoid diameter $D$, magnetic field $\mathbf{B}$ directed into the page, incoming particle striking at horizontal incidence angle $\alpha$, deflecting along an arc of gyroradius $r_g$, and exiting the inner wall along an azimuth $\phi$ toward the phantom at $r_p$.

### 2.3. Overview of the Original Analysis Model

The rapid analysis model discussed in later sections is an improved version of one first proposed by Washburn (2013) (see also, Washburn et al. (2014, 2015)). The model produces estimates of both the total mass of the shield and the shielding performance (i.e., dose reduction) with a runtime of approximately $20\text{ s}$ per design. This quick runtime enables the rapid evaluation of an entire trade space of solenoidal shield designs on the order of minutes to hours, depending on the number and resolution of the traded variables. To provide context for the improvements to the model, a general discussion of the modeling approach is included here. Interested readers are referred to the appendices of this article and to the original works for a more comprehensive description of the model. Key shield design and particle approach variables referenced throughout the following subsections are described and visualized to aid in clarity (Figure 1).

#### 2.3.1. Mass Estimation

There are four primary subsystems that contribute significantly to the total mass of the shield. The superconductor subsystem is responsible for the production of the magnetic field, and is mainly composed of the superconducting cabling. The structure subsystem is responsible for maintaining the shape of the solenoids as they are powered on and their positioning with respect to the habitat and the other coils. The structural components must support tensile loads in the radial direction, compressive loads in the axial direction, and complex forces and torques resulting from the interaction of the magnetic fields of adjacent coils. The power subsystem supplies and transmits electrical power to operate the fluxpumps that charge the coils and the cryocoolers that maintain their operating temperature below the superconducting critical current. The thermal subsystem rejects the heat loads incident on the coils, including solar and albedo heat loads, IR emissions from the habitat, and resistive heat loads from splices between adjacent superconducting cables. For each subsystem, basic physical principles and heuristic relationships are used to derive an estimate of that subsystem's mass. A representative example of such a derivation is provided in the appendix, while detailed derivations for all subsystems are available in Washburn (2013) and Washburn et al. (2015).

#### 2.3.2. Dose Estimation

To estimate the dose at a point inside the shield, the model must determine the influence on the GCR spectrum of both the magnetic attenuation afforded by the magnetic field and the passive shielding afforded by the protected habitat's pressure vessel and the physical shield materials (e.g., structural mass, superconducting cable mass). First, magnetic attenuation of the GCR spectrum is calculated as a function of particle energy for a point along the central axis of the habitat by

$$
\Phi_{i}^{*}(K) = 2\pi\Phi_{i}(K)\int_{0}^{\pi} H\left(K - K_{i,co}(\theta, r_{g}(\theta))\right)\sin\theta\, d\theta \tag{6}
$$

where $\Phi_{i}(K)$ is the unattenuated isotropic GCR flux of particle species $i$ at energy $K$ predicted by the Badhwar-O'Neill model, $H$ is the Heaviside step function, and $K_{i,co}(\theta, r_{g})$ is particle $i$'s cutoff kinetic energy (described by Eq. (3)) as a function of that particle's polar approach angle $\theta$ (defined with respect to the $+Z$ axis) and its gyroradius. The form of the expression for the particle's gyroradius $r_{g}$ depends on the surface of the shield upon which the particle is incident (see Figure 2), which in turn depends on the polar approach angle $\theta$. Particles approaching near the poles of the shield (i.e., $\theta \approx 0$ or $\theta \approx \pi$) do not encounter the magnetic field prior to reaching the habitat, and so do not experience magnetic attenuation (i.e., $r_{g} = 0$). Particles with relatively flat approaches centered around $\theta = \pi/2$ strike the shield along its vertical surface (the "barrel" surface). The gyroradius for these particles is given by

$$
r_{g} = \frac{r_{o}^{2} - r_{i}^{2}}{2r_{o}} \tag{7}
$$

where $r_{o}$ is the outer radius of the shield annulus and $r_{i}$ is the inner radius of the shield annulus. Approaching particles with intermediate polar angles between $0$ and $\pi/2$ ($\pi/2$ and $\pi$) strike the shield along its upper (lower) horizontal surface (the "outer transition" surface). The gyroradius for these particles is given by

$$
r_{g}(\theta) = \frac{((h_{s} \pm 2h_{p})\tan(\theta))^{2} - 4r_{i}^{2}}{4(h_{s} \pm 2h_{p})\tan(\theta)} \tag{8}
$$

where $h_{p}$ is the height along the central axis of the habitat at which the point dose is to be estimated. The $+$ case corresponds to particles entering through the bottom surface, while $-$ corresponds to the top surface. Eq. (6) is piecewise numerically integrated over the polar angle $\theta$ to produce a modified GCR flux spectrum representing the effect of the shield's magnetic attenuation on incoming radiation. The modified GCR spectrum is subsequently passed to the deterministic radiation transport code HZETRN (Slaba et al., 2010, 2020). HZETRN is used to transport the magnetically-attenuated GCR spectrum through the mass of the shield materials located near the habitat and the mass of the habitat itself. Barrel and transition region particles are transported through $12\text{ g/cm}^{2}$ of habitat aluminum, while endcap particles are transported through $25\text{ g/cm}^{2}$. The transport procedure returns an estimate of the point dose equivalent in water produced by the actively- and passively-attenuated GCR spectrum, which is assumed to adequately represent the dose equivalent in tissue. In the original articles, HZETRN2010 was used to perform all transport calculations. With the release of HZETRN2020, the legacy 2010 codes were removed from NASA software repositories. Accordingly, all dose estimates presented in this article, for both the original and new models, were computed using HZETRN2020.

A number of assumptions underly the original model's derivation of magnetic GCR attenuation discussed above. First, an analytical expression for the kinetic energy cutoff $K_{i,co}$ is only achievable by assuming that the field magnitude is uniform throughout an annular cylindrical region, even though gaps between adjacent coils will have significantly reduced flux density. This results in an underprediction of total GCR flux inside the shield. Second, Eqs. (7) and (8) are only valid under the assumption that all particles approach along the most penetrating horizontal incidence angle (i.e. $\alpha = 0$). This is a conservative assumption that overpredicts the amount of GCR flux inside the shield and positively biases the total estimated dose. Third, integrating over the approach angle $\theta$ prevents the inclusion of those particles whose initial velocities were not directed in such a way as to intersect the phantom, but, as a result of their interactions with the shield, are ultimately redirected into the phantom. As will be shown in the following section, these particles can contribute significantly to the total dose. Finally, the derived equations are only valid for points located along the central axis of the habitat (i.e., $r_{p} = 0$). As a conservative estimate, the original model computed the dose equivalent at the end of the habitat along the axial centerline (where dose is expected to be highest). While that convention is also used throughout the next section, a generalized formulation capable of computing the dose at any location within the habitat is also presented.

## 3. Analysis Model Modernization

In this section, the updates to Washburn's original performance evaluation model are discussed. Critical assumptions in the original model are reevaluated and generalized. The default parameters used to produce the data in this and subsequent sections are provided (Table 1). These default values are used unless otherwise specified.

### 3.1. Annular Cylinder Assumption

A solenoidal radiation shield is formed by surrounding a space habitat with a number of solenoid coils (Figure 1). To simplify analysis, the original model modeled the shield as an annular cylinder with a uniform flux density given by Eq. (5), including in the gap regions between adjacent coils. While the assumption of field uniformity in the annular volume is necessary to enable the derivation of an analytical expression for GCR flux attenuation, in its original form this assumption positively biases the performance of the shields. In reality, the gaps between shield coils will have a substantially lower field flux density than that predicted by Eq. (5), and the average bending power of the shield will be lower than predicted by the model. To rectify the biases introduced by the averaging process while maintaining the field uniformity property, the field flux density within the coils is scaled by a geometrical factor describing the ratio of the volume of the annular cylinder to the volume contained within the coils

$$
\epsilon = \frac{h_{s}\pi(r_{o}^{2} - r_{i}^{2})}{N_{\text{coils}}h_{s}\pi\left(\frac{D}{2}\right)^{2}} = \frac{r_{o}^{2} - r_{i}^{2}}{N_{\text{coils}}\left(\frac{D}{2}\right)^{2}} \tag{9}
$$

where $N_{\text{coils}}$ is the number of solenoid coils that form the shield, and $r_{o}$ and $r_{i}$ are the outermost and innermost radii of the shield, respectively. To enable the comprehensive evaluation of the design trade space, the original model allowed $N_{\text{coils}}$ to vary continuously according to the interpolation function

$$
N_{\text{coils}} = \frac{2\pi\left(r_{i} + \frac{D}{2}\right)}{D} \tag{10}
$$

Substituting Eq. (10) into equation (9) and simplifying yields $\epsilon = 4/\pi$. Accordingly, solenoids producing within their bores a field of $4B/\pi$ will produce an averaged field of $B$ across the entire annular cylinder. The correction scale factor is applied only to the mass estimation component of the analysis model, whereas the dose estimation components remain unscaled. Applying this scaling to the mass estimation model is intended to yield a more accurate representation of the additional mass of shield components that would be required to produce a field that is approximable by an annular cylinder with uniform flux density $B$.

**Table 1:** Default simulation and habitat parameters.

| Parameter | Value | Note |
| :--- | :--- | :--- |
| Solar Modulation Parameter ($\Phi$) | $481\text{ MV}$ | 1977 Solar Min (worst-case GCR conditions) |
| Heavy Ion Fragmentation Model | RAADFRG | Werneth et al. (2021) |
| HZETRN Target Material | Water | Assumed to be representative of tissue dose |
| Phantom Radial Location ($r_{p}$) | $0$ | GCR flux integrals simpler along central axis |
| Phantom Axial Location ($h_{p}$) | $4.95\text{ m}$ | End of habitat, worst-case position |
| Habitat Height ($h_{h}$) | $10\text{ m}$ | Representative Mars transit habitat dimensions |
| Habitat Radius ($r_{h}$) | $3\text{ m}$ | |
| Habitat Sidewall Thickness | $12\text{ g/cm}^{2}\text{ Al}$ | Same as original model |
| Habitat Endcap Thickness | $25\text{ g/cm}^{2}\text{ Al}$ | Same as original model |
| Shield Inner Radius ($r_{i}$) | $4\text{ m}$ | $1\text{ m}$ gap between habitat and shield |

### 3.2. Magnetic GCR Spectrum Attenuation

Charged particles entering the shield region will be deflected via the Lorentz force (Eq. (1)). The deflections caused by the magnetic field will naturally cause some particles that would have otherwise intersected the phantom to deflect away from the habitat, but will also cause other particles that would have originally missed the habitat to be "focused" into the habitat and intersect the phantom. An accurate description of the GCR environment within the protected habitat requires treatment of both cases. Whether a particle ultimately penetrates the shield depends on the size of the shield and its flux density, the particle's rigidity, the particle's direction of incidence (defined by the polar angle $\theta$ and azimuthal angle $\alpha$), and the shield surface upon which the particle is incident. Here, a brief overview of key improvements to the magnetic attenuation model and their effects is provided, while the full derivation of the expressions describing GCR flux attenuation is left to the appendix.

There are four surfaces through which GCR particles can enter the shield: barrel, endcap, inner, and transition (Figure 2). Barrel particles initially strike the shield along its outermost wall $r = r_{o}$ and experience a high-pass filtering effect, where only particles with sufficiently high rigidities will penetrate through to the inside of the shield. Endcap particles enter through the very top or bottom of the shield with $r < r_{i}$ and do not ever encounter the magnetic field, and so maintain the same spectral characteristics as the unattenuated GCR spectrum. Similarly to endcap particles, inner particles enter through the ends of the shield, but instead intersect the inner wall of the shield ($r = r_{i}$) prior to reaching the habitat and can rebound off the shield back into the habitat. These particles experience a low-pass filtering effect: particles of sufficiently high rigidity will penetrate through to the outside wall of the shield, while low energy particles will be deflected back into the inside of the shield. Transition particles strike the shield along its top or bottom surface with $r_{i} < r < r_{o}$. Like the barrel surface, the transition surface acts as a high-pass filter, but only for particles whose velocities are directed towards the center of the shield at the moment of intersection (i.e., $\dot{r} < 0$, hereafter referred to as "outer transition" particles). In the other case ("inner transition" particles), where particle velocity is directed outward at the moment of intersection ($\dot{r} > 0$), the transition surface instead acts as a band-pass filter: if particle energy is sufficiently high, it will penetrate through to the outside of the shield (much like the inner case), while particles with sufficiently low energy will penetrate neither the inner nor outer wall, and instead will remain within the field surface and move helically until they pass out of the top or bottom of the shield.

In the original model, the derivation of magnetic attenuation of incident GCR flux was greatly simplified by the conservative assumption that all particles approach along the most penetrating incidence angle $\alpha$. Furthermore, by integrating over the polar approach angle $\theta$ instead of the area elements of the shield, the original model only considered those particles approaching from directions that would have intersected the phantom had the shield not been present; it does not account for those particles whose initial approaches would not have originally reached the phantom, but whose motion within the shield causes their deflection into the phantom. In other words, the original model only considered particle flux through the barrel, outer transition, and endcap surfaces, neglecting those particles passing through the inner transition surface and inner surface.

In the updated model, the magnetic attenuation component is fully generalized. For each surface, an analytical expression for the GCR flux from an arbitrary infinitesimal area element on that surface onto a small spherical water phantom located within the habitat was derived. Surface integrals of these cutoff expressions over each surface are then numerically computed and used to construct the total attenuated GCR flux reaching the phantom through that surface. Detailed derivations of the surface flux integrals are available in the appendix.

> **Figure 2:** GCR proton flux through each of the shield surfaces calculated by the original analytical model, updated analytical model, and a Monte Carlo (MC) simulation for a $10\text{ T} \times 10\text{ m}$ shield design, normalized by unattenuated flux at that energy ($10^{-2}$ to $10^{6}\text{ MeV}$):
> * **Barrel:** High-pass step at $\sim 2 \times 10^{4}\text{ MeV}$ rising to $\sim 0.58$; New model shows a smooth shoulder matching MC closely.
> * **Outer Transition:** High-pass step at $\sim 10^{4}\text{ MeV}$ rising to $\sim 0.34$; New model tracks the MC curve accurately.
> * **Endcap:** Constant unattenuated normalized flux near $0.07$ across all energies; Analytical and MC agree completely.
> * **Inner:** Low-pass behavior at $\sim 0.15$ below $10^{4}\text{ MeV}$ (with an MC focusing peak near $3 \times 10^{3}\text{ MeV}$), dropping to $0$ at high energies; omitted in the original model.
> * **Inner Transition:** Band-pass peak around $10^{4}\text{ MeV}$ reaching $\sim 0.25$; captured by the New model and MC, omitted in the original model.
> * **Net:** Total normalized proton flux is $\sim 0.22$ at low energies ($< 10^{2}\text{ MeV}$) in both the New model and MC, whereas the Original model underpredicts net low-energy flux at $\sim 0.07$ due to omitting the inner and inner transition regions.

#### 3.2.1. Magnetic Model Validation

The new magnetic attenuation formulation was validated using Monte Carlo simulation. A simulation environment was constructed wherein GCR protons are transported through an annular cylindrical magnetic field of specifiable size and magnetic flux density. Protons ranging in energy from $10^{-2}$ to $10^{6}\text{ MeV}$ are generated uniformly on the surface of a sphere of radius $r_{\text{inf}} = 100\text{ m}$ surrounding the shield. The protons' velocities are initially directed inward towards the shield (i.e., antiparallel to the spherical $\hat{r}$ direction), then randomly rotated slightly away from the $\hat{r}$ to approximate an isotropic distribution. Particles are propagated using the Boris algorithm for pure magnetic fields (Boris, 1971) until they leave the vicinity of the shield or strike a small spherical phantom located at the origin. Additional details on the simulation construction are available in the appendix. A total of $250\text{ million}$ particles ($2\text{ million}$ at each energy level) were simulated; phantom hits were tallied and normalized by the probability of a phantom hit for an uncharged particle under the same simulation conditions (Figure 2). Generally, the Monte Carlo results show better agreement with the new model across the range of energies simulated, particularly at lower energies. The new model still somewhat underpredicts phantom strikes at intermediate energies, but outperforms the original model in predicting the effect of magnetic attenuation on the incident GCR spectrum.

### 3.3. Spatial Dose Variation

The modified radiation environment within a shield varies as a function of position within the protected volume (Washburn, 2013). The original model only considered the dose along the axial centerline of the shield. Here, the rederived expressions for the GCR environment inside the habitat are fully generalized and capable of providing the approximate GCR spectrum at any point within the shielded habitat. This capability could be used in conjunction with a higher-fidelity human phantom to produce an estimate of tissue-specific doses and whole-body effective doses.

It is noted that for points along the axial centerline, the $\phi$ dependence in the double integrals that describe the magnetically-attenuated GCR flux (Eqs. (B.8–B.36)) is eliminated. This reduces them to single integrals over the radial or axial coordinate, reducing their computational cost by more than two orders of magnitude. Accordingly, the full spatial dose distribution should only be sparingly calculated. As a demonstration, the spatial distribution is calculated for a $20\text{ m}$ tall, $3\text{ T} \times 5\text{ m}$ shield, which is later shown to be the minimal-mass shield capable of reducing doses below $250\text{ mSv/yr}$.

## 4. Results

### 4.1. Field Uniformity Correction

Increasing the magnitude of the field produced by the coils ensures that the field averaging process does not artificially inflate the performance of the shield. The scaled flux density results in additional system mass penalties. In turn, the extra mass serves as added passive shielding. This extra mass lowers the radiation dose until the effective thickness of the passive mass of the shield reaches a critical threshold of about $40\text{ g/cm}^{2}$, above which doses tend to increase with additional passive shielding (Figure 3) due to neutron production within the material (Norman et al., 2017).

> **Figure 3:** Effect of the field uniformity scaling factor on system mass (solid contours, in $5\%$ intervals from $20\%$ to $60\%$) and dose equivalent (line contours, $5\text{ mSv/yr}$ intervals from $-5$ to $+15\text{ mSv/yr}$) across coil diameter $D$ ($1\text{–}10\text{ m}$) and magnetic flux density $B$ ($1\text{–}10\text{ T}$).

### 4.2. Magnetic Attenuation Improvements

The effects of the improvements to the magnetic attenuation computations are visualized for a range of shield designs (Figure 4). The elimination of the original model's conservative assumption that all particles approach along the most penetrating incidence angle (i.e., $\alpha = 0$) reduces estimated doses across the range of designs considered. However, the inclusion of particle flux through the inner and inner transition surfaces offsets this dose reduction. Increasing the size and flux density of the shield increases the size of the inner and inner transition surfaces and the cutoff energy below which particles are able to penetrate through these surfaces. Accordingly, the contribution to the total dose of inner and inner transition particles becomes increasingly relevant and ultimately outweighs the dose reduction associated with generalizing the incidence angle $\alpha$. For a $20\text{ m}$ tall, $3\text{ T} \times 5\text{ m}$ shield, the inner and inner transition surfaces respectively contribute $44.6$ and $20.6\text{ mSv/yr}$ to the total dose of $246\text{ mSv/yr}$.

> **Figure 4:** Change in predicted dose equivalent ($\Delta\text{Dose}$ in $\text{mSv/yr}$, from $-60$ to $+60\text{ mSv/yr}$) using the updated magnetic model for $h_s = 10\text{ m}$ (left) and $h_s = 20\text{ m}$ tall (right) shields with $5\text{ mSv/yr}$ contours across $D$ ($1\text{–}10\text{ m}$) and $B$ ($1\text{–}10\text{ T}$).

### 4.3. Spatial Dose Variation

The spatial variation of dose within the habitat protected by a $20\text{ m}$ tall, $3\text{ T} \times 5\text{ m}$ solenoidal shield is visualized (Figure 5). Annual dose equivalent at the standard test point within the shield (along the axial centerline at the end of the habitat) is $246\text{ mSv/yr}$ while the volume-averaged dose equivalent throughout the habitat is $240\text{ mSv/yr}$, a difference of approximately $3\%$. While these differences are minor, other designs are likely to have more extreme spatial variations in dose equivalent, particularly for larger habitats and smaller shields. Future efforts to characterize spatial dose variations across a broader range of shield and habitat designs will be important to ensure that the standard axial test point used in this article remains an appropriate, representative choice for characterizing shield performance.

> **Figure 5:** Spatial variation in solar minimum annual dose equivalent ($\text{mSv/yr}$) within a habitat ($r \in [-3, 3]\text{ m}$, $z \in [-5, 5]\text{ m}$) protected by a $20\text{ m}$ tall, $3\text{ T} \times 5\text{ m}$ solenoidal magnetic shield. The volume-averaged dose equivalent within the habitat is $240\text{ mSv/yr}$, ranging from $\sim 230\text{ mSv/yr}$ at the radial edges near $z=0$ to $\sim 250\text{ mSv/yr}$ near the endcaps ($z = \pm 5\text{ m}$), varying by roughly $10\%$ within the volume of the habitat.

### 4.4. Net Results

Estimated system masses and annual dose equivalents under the updated model with all aforementioned changes (Figure 6, left) and its difference compared to the original model (right) are visualized for $20\text{ m}$ tall shields. The combined effects of the updates to the model result in reductions in estimated dose equivalents for shields with bending powers below about $9\text{ T}\cdot\text{m}$, while stronger shields have higher predicted doses. The dose reductions for weak shields are driven by both the removal of the assumption that all particles approach along the most penetrating horizontal incidence angle $\alpha$ and the increased passive shielding associated with the annular cylinder geometric scaling factor. The dose increases for strong shields are driven by the inclusion of low energy GCR particles entering the shield through the inner and inner transition surfaces. For example, for a $20\text{ m}$ tall, $1\text{ T} \times 1\text{ m}$ shield achieving a total dose equivalent of $477\text{ mSv/yr}$, less than $0.1\%$ of the total dose equivalent is contributed by inner and inner transition surface particles, while for a $20\text{ m}$ tall, $10\text{ T} \times 10\text{ m}$ shield, that percentage jumps to nearly $40\%$.

It is apparent that the diminishing returns of increasing shield bending power beyond about $20\text{ T}\cdot\text{m}$ are much more significant than predicted by the original model. Whereas the original model predicted an annual dose equivalent of approximately $80\text{ mSv/yr}$ for a $20\text{ m}$ tall, $10\text{ T} \times 10\text{ m}$ shield (approximately an $84\%$ reduction relative to the dose at that point protected only by the habitat's pressure vessel), the new model predicts a dose equivalent of $188\text{ mSv/yr}$, a reduction of only $63\%$. This finding generally agrees with a prior analysis of an infinitely-tall toroidal magnetic shield (Musenich et al., 2018), where it was argued that magnetic shields are not likely to be viable as a sole countermeasure if GCR dose reductions on the order of $90\%$ relative to free space are desired. However, smaller shields of about $10\text{–}20\text{ T}\cdot\text{m}$ still provide a significantly greater GCR dose reduction than equivalent-mass passive shields, and so active magnetic shields are still worth investigating for inclusion in a larger suite of radiation countermeasures.

> **Figure 6:**
> * **Left (Updated Model Design Trade Space):** Shield mass ($\log_{10}(\text{t})$, color shading from $1.2$ to $3.4$) and annual dose equivalent contours ($200$ to $400\text{ mSv/yr}$ in white lines) for $20\text{ m}$ tall shields with varied shield thickness $D$ ($1\text{–}10\text{ m}$) and flux density $B$ ($1\text{–}10\text{ T}$).
> * **Right (Mass & Dose Differences b/w Models):** Differences in predicted mass ($\Delta\text{Mass}$ in $\%$, blue shading from $20\%$ to $60\%$) and annual dose equivalent (line contours from $-20$ to $+60\text{ mSv/yr}$) between the original and updated models.

An optimal shield achieves a specified reduction in dose equivalent at a minimum mass. Identified optimal designs for shields ranging in height from $10\text{–}50\text{ m}$ and bending power from $1\text{–}100\text{ T}\cdot\text{m}$ are visualized (Figure 7). Across the range of dose reductions considered, larger shields with weaker magnetic fields are more mass efficient than smaller shields with stronger magnetic fields, consistent with the original model. This data also reveals an apparent lower bound on shield mass with respect to dose reduction:

$$
m_{\min} \approx 5.18 \times 10^{2.86 r}
$$

This exponential relationship could serve as a useful benchmark for broadly comparing the performance of solenoidal shields to other archetypal shield configurations without necessitating the selection of specific design variables. It is envisioned that ongoing work to produce a similar performance evaluation model for toroidal and hybrid shields will ultimately yield a similar relationship that can be used to characterize the relative performance of these broad classes of shield designs across an entire trade space.

> **Figure 7:** Minimum shield mass ($\text{t}$, log scale from $10^{1}$ to $10^{3}$) of various heights ($h_s = 10, 20, 30, 40, 50\text{ m}$) that achieve specified relative dose reductions $r$ ($0.2$ to $0.8$) and corresponding dose equivalents ($400$ down to $125\text{ mSv/yr}$). Relative dose reduction is defined with respect to the GCR dose received at a point protected only by the habitat pressure vessel ($514\text{ mSv/yr}$). Annotated Pareto-optimal designs include $1\text{ T} \times 8\text{ m}$, $2\text{ T} \times 4\text{ m}$, $2\text{ T} \times 5\text{ m}$, $3\text{ T} \times 4\text{ m}$, $3\text{ T} \times 5\text{ m}$, $4\text{ T} \times 4\text{ m}$, and $4\text{ T} \times 5\text{ m}$, bounded below by $m_{\min} \approx 5.18 \times 10^{2.86r}$.

While the updated model generally predicts worse mass-normalized performance of solenoidal shields than the original model, these shields are still shown to be significantly more performant than mass-equivalent passive shields (Figure 8). For the representative habitat described in Table 1, a supplementary active shield universally outperforms aluminum passive shields across all dose thresholds, and outperforms passive shields utilizing polyethylene when the requisite annual dose equivalent is below about $350\text{ mSv/yr}$ (approximately a $60\%$ reduction relative to the free space dose).

> **Figure 8:** Performance comparison of solenoidal magnetic shields (New Model vs. Original Model) to passive shields consisting of Aluminum, High Density Polyethylene (HDPE), and an equal Al/HDPE Mixture across shield masses from $0$ to $1000\text{ t}$. The protected habitat has the same characteristics as described in Table 1. The shields considered here are all $10\text{ m}$ tall and protect only the sidewall of the habitat, to facilitate comparison by ensuring that unshielded endcap contributions ($\sim 235\text{ mSv/yr}$) are the same for all designs considered.

## 5. Conclusions

The improved rapid analysis model presented here enables a more accurate quantification of the performance of solenoidal radiation shields without appreciably increasing the computational cost of the model. Introducing the gap scaling factor corrects a significant positive shield performance bias present in the original model. Improvements to the semi-analytical magnetic GCR attenuation model enable a more accurate description of the attenuated GCR environment reaching the habitat and have been verified using a Monte Carlo simulation of charged particle motion within a shield. Finally, the fully generalized magnetic flux integrals are capable of producing estimates of dose equivalent at any location within the habitat, not just along the axial centerline, which enables more thorough evaluation of shield performance. The combined effects of these updates to the rapid analysis model suggest that the original model underestimated the performance of small, weak shields and significantly overestimated the performance of larger shields with bending powers above $10\text{ T}\cdot\text{m}$. The updated model presented here provides better agreement with existing literature regarding the performance of magnetic shields of varying bending power, and suggests that significant reductions in astronaut GCR doses relative to free space by an order of magnitude or more are unlikely to be achieved using magnetic shields alone.

Ongoing efforts to further improve the utility of the model include an incorporation of a number of technological advancements that have been realized since the original model was developed in 2014, which will provide an updated understanding of present magnetic shielding capabilities using state-of-the-art technologies. Future planned efforts include further validation of the accuracy of the model via high-fidelity Monte Carlo simulation of selected shield designs, identification of other key performance-driving design variables, and an extension of the modeling approach to toroidal and hybrid shield designs, whose performance may vary significantly from the solenoidal designs considered here.

## Acknowledgments

The authors thank Dr. Scott Washburn for helping to clarify various aspects of the shield mass estimation process. This material is based upon work supported by the National Science Foundation Graduate Research Fellowship Program under Grant No. DGE 2040434. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author and do not necessarily reflect the views of the National Science Foundation.

---

## Appendix

### A. Example of Mass Estimation Process

Here we step through an example derivation of system mass as a function of shield design variables and technology performance parameters. This example is reproduced with minor adjustments from Washburn (2013). Consider the radial support component of the shield's structure subsystem. The magnetic pressure on an ideal, long, thin-walled cylindrical coil is given by

$$
P_{B} = \frac{B^{2}}{2\mu_{0}} \tag{A.1}
$$

(Iwasa and Marken, 1995). Pressure inside a cylinder is related to hoop stress by

$$
\sigma_{t} = \frac{P_{B}D}{2t_{w}} \tag{A.2}
$$

where $t_{w}$ is the thickness of the coil. Substituting Eq. (A.1) into Eq. (A.2) and including a factor of safety $F_{S}$ yields an equation for the maximum allowable hoop stress

$$
\sigma_{t,\max} = \frac{B^{2}DF_{S}}{4\mu_{0}t_{w}} \tag{A.3}
$$

Eq. (A.3) can be rearranged for the wall thickness $t_{w}$, from which an expression for the volume and mass of the radial support material necessary for each coil can be obtained

$$
m_{\text{radial}} = \rho_{\text{radial}}V_{\text{radial}} = \frac{\rho_{\text{radial}}B^{2}D^{2}\pi h_{s}F_{S}}{4\mu_{0}\sigma_{u,\text{radial}}} \tag{A.4}
$$

where $\rho_{\text{radial}}$ and $\sigma_{u,\text{radial}}$ are the mass density and the ultimate tensile strength of the radial support material. Eq. (A.4) provides a simple relationship between subsystem mass, key shield design parameters (magnetic flux density $B$, depth $D$ and height $h_{s}$) and technology performance parameters (material tensile strength $\sigma_{u}$ and mass density $\rho$), which enables evaluation of the influence of shield design and technology advancement on overall shield mass. When combined with similar relationships derived for other key subsystem components, subsystem-level mass estimates are produced, which in turn are summed to produce an overall mass estimate for the shield.

### B. Derivation of Magnetic Attenuation

One of the primary shortcomings of the original model was its inability to accurately predict the GCR environment inside a protected habitat. Specifically, the original model first assumes that all approaching particles are incident upon the shield along the most penetrating horizontal incidence angle $\alpha = 0$. Furthermore, the model is unable to account for inner and inner transition surface particles, since the double integrals describing the particle flux in the original model are constructed using spherical approach angles $\theta$ and $\phi$, which are defined with respect to the phantom and therefore fail to account for particles with $\dot{r} > 0$. While these approximations do greatly simplify the derivation of the magnetic cutoff relationships and their numerical complexity, they result in substantially different findings regarding the ideal configuration of a solenoidal shield. By reframing the flux integrals as surface integrals over the various surfaces of the shield, the magnetic attenuation to the incident GCR spectrum can be more accurately described. Here, the derivation of the updated surface flux integrals is presented.

#### B.1. Barrel Surface

Consider the scenario visualized in Figure 1. An annular cylindrical field of height $h_{s}$, inner radius $r_{i}$, outer radius $r_{o}$ and uniform flux density $B$ throughout is struck along the barrel surface by a GCR particle of rest mass $m$ and charge $q$ at polar angle $\theta$ defined with respect to the $+Z$ axis and horizontal incidence angle $\alpha$ defined with respect to the line tangent to $r_{o}$ at the point of intersection. That particle travels along an arc of radius $r_{g}$ until it reaches $r_{i}$, at which point it travels in a straight line until intersecting a spherical phantom located at radius $r_{p}$ along an azimuth $\phi$ defined with respect to $r_{p}$. From the right graphic of Figure 1, a purely geometrical relationship between $r_{g}$ and the shield dimensions and approach conditions can be computed using the law of cosines:

$$
r_{g} = \frac{r_{o}^{2} - r_{i}^{2}}{2(r_{o}\cos(\alpha) + r_{p}\cos(\phi))} \tag{B.1}
$$

Now, assuming that the phantom at $r_{p}$ has some small, finite radius $R$, a range of incidence angles $(\alpha - \Delta\alpha/2, \alpha + \Delta\alpha/2)$ and $(\theta - \Delta\theta/2, \theta + \Delta\theta/2)$ can yield a trajectory that ultimately strikes the phantom. The small angle approximation can be used to update Eq. (B.1) to

$$
r_{g} = \frac{r_{o}^{2} - r_{i}^{2}}{2(r_{o}\cos(\alpha) + (r_{p}\cos(\phi) \pm R))} \tag{B.2}
$$

which in turn can be solved for the window of horizontal incidence angles which yield trajectories that ultimately intersect the phantom:

$$
\Delta\alpha = \frac{2R}{r_{o}} \tag{B.3}
$$

The polar angle window can be computed as

$$
\Delta\theta = \frac{2R}{\sqrt{r_{o}'(r_{p},\phi)^{2} + (z - h_{p})^{2}}} \tag{B.4}
$$

where $z$ is the height at which the particle initially strikes the shield barrel region and where $r'(r_{p},\phi)$ is the distance to the edge of a circle of radius $r$ from a point located a distance $r_{p}$ from the center of $r$ along an azimuth $\phi$, i.e.,

$$
r'(r_{p},\phi) = -r_{p}\cos(\phi) + \sqrt{r^{2} - (r_{p}\sin(\phi))^{2}} \tag{B.5}
$$

Together, these expressions for $\Delta\alpha$ and $\Delta\theta$ can be used to compute the total solid angle from which particles incident upon an infinitesimal area element $dA = r_{o}d\phi dz$ located at $(r_{o}, z)$ can approach and strike the phantom:

$$
\begin{aligned}
\Delta\Omega &= \frac{\pi}{4}\int_{\alpha-\Delta\alpha/2}^{\alpha+\Delta\alpha/2}\int_{\theta-\Delta\theta/2}^{\theta+\Delta\theta/2}\sin(\theta')\,d\theta' d\alpha' \\
&\approx \frac{\pi}{4}\Delta\alpha\sin(\theta)\Delta\theta \\
&= \frac{\pi R}{2r_{o}}\left(\frac{r_{o}'(r_{p},\phi)}{\sqrt{r_{o}'(r_{p},\phi)^{2} + (z - h_{p})^{2}}}\right)\left(\frac{2R}{\sqrt{r_{o}'(r_{p},\phi)^{2} + (z - h_{p})^{2}}}\right) \\
&= \frac{\pi R^{2}r_{o}'(r_{p},\phi)}{r_{o}\left(r_{o}'(r_{p},\phi)^{2} + (z - h_{p})^{2}\right)}
\end{aligned} \tag{B.6}
$$

where the factor of $\pi/4$ converts from a rectangular solid angle element to an elliptical element. The cylindrical area element $dA$ must be scaled by a factor describing the projection of $dA$ with respect to the direction of the solid angle element:

$$
\begin{aligned}
dA_{\text{proj}} &= \sin(\theta)\sin(\alpha)dA \\
&= \frac{r_{o}'(r_{p},\phi)r_{o}}{\sqrt{r_{o}'(r_{p},\phi)^{2} + (z - h_{p})^{2}}}\operatorname{Re}\left[\sqrt{1 - \left(\frac{r_{o}^{2} - r_{i}^{2} - 2r_{p}\cos(\phi)r_{g}}{2r_{o}r_{g}}\right)^{2}}\right]d\phi dz
\end{aligned} \tag{B.7}
$$

where the $\operatorname{Re}[\cdots]$ term encodes the energy cutoff conditions by reexpressing $\sin(\alpha)$ as $\sqrt{1 - \cos(\alpha)^{2}}$. The cutoff energy occurs below the point where an approaching particle cannot breach the shield even with $\alpha = 0$. Putting it all together and selecting $R$ such that the phantom has a surface area of $1\text{ cm}^{2}$, the surface integral describing all GCR flux reaching point $(r = r_{p}, \phi = 0, z = h_{p})$ through the barrel surface is given by

$$
\begin{aligned}
\Phi_{b}(K) &= \Phi(K)\int_{0}^{2\pi}\int_{-\frac{h_{s}}{2}}^{\frac{h_{s}}{2}}\frac{d\Omega}{4\pi}dA_{\text{proj}} \\
&= \Phi(K)\int_{0}^{2\pi}\int_{-\frac{h_{s}}{2}}^{\frac{h_{s}}{2}}\frac{r_{o}'(r_{p},\phi)^{2}}{\left(r_{o}'(r_{p},\phi)^{2} + (z - h_{p})^{2}\right)^{3/2}}\operatorname{Re}\left[\sqrt{1 - \left(\frac{r_{o}^{2} - r_{i}^{2} - 2r_{p}\cos(\phi)r_{g}(K, r_{o}, \phi, z)}{2r_{o}r_{g}(K, r_{o}, \phi, z)}\right)^{2}}\right]dz d\phi
\end{aligned} \tag{B.8}
$$

where $\Phi(K)$ is the differential omnidirectional GCR flux of a particle of energy $K$ in $\text{cm}^{-2}\text{day}^{-1}\text{MeV}^{-1}$ and $r_{g}$ is the gyroradius of a particle entering the shield at a point $(r, \phi, z)$ on its surface with an initial velocity directed towards point $(r_{p}, 0, h_{p})$:

$$
r_{g}(K, r, \phi, z) = \frac{m_{0}c}{qB}\sqrt{\left(1 + \frac{K}{m_{0}c^{2}}\right)^{2} - 1}\left(\frac{r'(r_{p},\phi)}{\sqrt{r'(r_{p},\phi)^{2} + (z - h_{p})^{2}}}\right) \tag{B.9}
$$

In the limiting case where $r_{p} = 0$ (i.e., the phantom is located on the central axis of the habitat), $r'(r_{p},\phi) = r$ and all $\phi$ dependence is removed from the integrand, reducing Eq. (B.8) and all the following flux integrals to a single integral over the radial or axial coordinate and enabling a significant reduction in computational complexity.

The derivation of the remaining surface integrals follow a similar approach wherein an expression for $r_{g}$ is derived geometrically and used to form an expression for $\Delta\alpha$ and $d\Omega$. The projection factor $dA_{\text{proj}}$ is then computed, then the final surface integral is constructed as in the first step of Eq. (B.8).

#### B.2. Outer Transition

The derivation of GCR flux through the outer transition surface closely mirrors the barrel surface. The geometrical expression for the gyroradius is equivalent to Eq. (B.2) but with $r_{o} \to r$:

$$
r_{g} = \frac{r^{2} - r_{i}^{2}}{2(r\cos(\alpha) + (r_{p}\cos(\phi) \pm R))} \tag{B.10}
$$

which yields

$$
\Delta\alpha = \frac{2R}{r} \tag{B.11}
$$

where $r$ is the radial position of the cylindrical surface element $dA$. The polar angle window is given by

$$
\Delta\theta = \frac{4R}{\sqrt{4r^{2} + (h_{s} \pm 2h_{p})^{2}}} \tag{B.12}
$$

where the positive case applies to the bottom surface of the shield, and the negative to the top. The solid angle window is therefore given by

$$
\begin{aligned}
\Delta\Omega &= \frac{\pi}{4}\int_{\alpha-\Delta\alpha/2}^{\alpha+\Delta\alpha/2}\int_{\theta-\Delta\theta/2}^{\theta+\Delta\theta/2}\sin(\theta')\,d\theta' d\alpha' \\
&\approx \frac{\pi}{4}\Delta\alpha\sin(\theta)\Delta\theta \\
&= \frac{\pi R}{2r}\left(\frac{2r}{\sqrt{4r^{2} + (h_{s} \pm 2h_{p})^{2}}}\right)\left(\frac{4R}{\sqrt{4r^{2} + (h_{s} \pm 2h_{p})^{2}}}\right) \\
&= \frac{4\pi R^{2}}{4r^{2} + (h_{s} \pm 2h_{p})^{2}}
\end{aligned} \tag{B.13}
$$

The projected area element is given by

$$
\begin{aligned}
dA_{\text{proj}} &= \cos(\theta)\sin(\alpha)dA \\
&= \frac{h_{s} \pm 2h_{p}}{\sqrt{4r^{2} + (h_{s} \pm 2h_{p})^{2}}}\operatorname{Re}\left[\sqrt{1 - \left(\frac{r^{2} + r_{p}^{2} - r_{i}^{2} - 2(r + r_{g}(K, r, \phi, \mp\frac{h_{s}}{2}))r_{p}\cos(\phi)}{2rr_{g}(K, r, \phi, \mp\frac{h_{s}}{2})}\right)^{2}}\right]r\,d\phi dr.
\end{aligned} \tag{B.14}
$$

As before, choosing $R$ such that the spherical phantom has a surface area of $1\text{ cm}^{2}$, the flux of a GCR species with energy $K$ reaching the phantom through the outer transition surface is given by

$$
\Phi_{to}(K) = \Phi(K)\int_{0}^{2\pi}\int_{r_{i}'(r_{p},\phi)}^{r_{o}'(r_{p},\phi)}\frac{4r(h_{s} \pm 2h_{p})}{\left(4r^{2} + (h_{s} \pm 2h_{p})^{2}\right)^{3/2}}\operatorname{Re}\left[\sqrt{1 - \left(\frac{r^{2} + r_{p}^{2} - r_{i}^{2} - 2(r + r_{g}(K, r, \phi, \mp\frac{h_{s}}{2}))r_{p}\cos(\phi)}{2rr_{g}(K, r, \phi, \mp\frac{h_{s}}{2})}\right)^{2}}\right]dr d\phi \tag{B.15}
$$

#### B.3. Inner Surface

Particles entering the shield through the inner and inner transition surfaces behave differently from barrel and outer transition particles and thus the derivation proceeds a bit differently. Consider a particle entering the shield through the inner surface (Figure B1).

> **Figure B1:** Motion of a particle (red trajectory) entering the shield (blue annular region) along the inner surface ($r_i$) at horizontal angle $\alpha$ and striking the phantom at radial distance $r_p$ and azimuth $\phi$.

The law of sines yields a simple expression for $\alpha$:

$$
\cos(\alpha) = \frac{r_{p}}{r_{i}}\sin(\phi) \tag{B.16}
$$

As before, expanding the phantom from a point to a small sphere of radius $R$ enables reexpressing Eq. (B.16), which ultimately yields expressions for $\Delta\alpha$ and $\Delta\theta$:

$$
\cos(\alpha) = \frac{r_{p} \pm R\csc(\phi)}{r_{i}}\sin(\phi) \tag{B.17}
$$

which yields

$$
\Delta\alpha = \frac{2R}{r_{i}} \tag{B.18}
$$

and

$$
\Delta\theta = \frac{2R}{\sqrt{r_{o}'(r_{p},\phi)^{2} + (z - h_{p})^{2}}} \tag{B.19}
$$

As before, $\Delta\alpha$ and $\Delta\theta$ can be used to compute the solid angle element $\Delta\Omega$:

$$
\begin{aligned}
\Delta\Omega &= \frac{\pi}{4}\int_{\alpha-\Delta\alpha/2}^{\alpha+\Delta\alpha/2}\int_{\theta-\Delta\theta/2}^{\theta+\Delta\theta/2}\sin(\theta')\,d\theta' d\alpha' \\
&= \frac{\pi R^{2}r_{o}'(r_{p},\phi)}{r_{i}\left(r_{o}'(r_{p},\phi)^{2} + (z - h_{p})^{2}\right)}
\end{aligned} \tag{B.20}
$$

The projected area element for the inner surface is given by

$$
\begin{aligned}
dA_{\text{proj}} &= \sin(\theta)\sin(\alpha)dA \\
&= \frac{r_{o}'(r_{p},\phi)}{\sqrt{r_{o}'(r_{p},\phi)^{2} + (z - h_{p})^{2}}}\sqrt{1 - \left(\frac{r_{p}}{r_{i}}\sin(\phi)\right)^{2}}d\phi dz
\end{aligned} \tag{B.21}
$$

Eqs. (B.20) and (B.21) form the basis of the flux integral describing GCR flux through the inner surface:

$$
\begin{aligned}
\Phi_{i}(K) = \Phi(K)\Bigg[&\int_{0}^{2\pi}\int_{z_{\max}(K,\phi)}^{\frac{h_{s}}{2}}\frac{r_{o}'(r_{p},\phi)^{2}}{\left(r_{o}'(r_{p},\phi)^{2} + (z - h_{p})^{2}\right)^{3/2}}\sqrt{1 - \left(\frac{r_{p}}{r_{i}}\sin(\phi)\right)^{2}}dz d\phi \\
&+ \int_{0}^{2\pi}\int_{-\frac{h_{s}}{2}}^{z_{\min}(K,\phi)}\frac{r_{o}'(r_{p},\phi)^{2}}{\left(r_{o}'(r_{p},\phi)^{2} + (z - h_{p})^{2}\right)^{3/2}}\sqrt{1 - \left(\frac{r_{p}}{r_{i}}\sin(\phi)\right)^{2}}dz d\phi\Bigg]
\end{aligned} \tag{B.22}
$$

where the $z$ integration limits are determined by either the particle's energy cutoff or shield self-shadowing effects:

$$
z_{\lim}(K,\phi) = \operatorname{clamp}\left(\max(z_{\lim,K}(K,\phi), z_{\lim,s}(\phi)), \pm\frac{h_{h}}{2}, \pm\frac{h_{s}}{2}\right) \tag{B.23}
$$

where the $+$ case applies for $z_{\min}$ and the $-$ case for $z_{\max}$. The $\operatorname{clamp}(x, a, b)$ restricts $x$ to lie in the interval $[a, b]$. The energy and shadowing cutoffs are respectively given by

$$
z_{\lim,K}(K,\phi) = h_{p} \pm \operatorname{Re}\left[\sqrt{\left(\frac{2r_{g}(K, r_{o}, \phi, \pm h_{p})r_{o}'(r_{p},\phi)(r_{o} + r_{p}\sin(\phi))}{r_{o}^{2} - r_{i}^{2}}\right)^{2} - r_{o}'(r_{p},\phi)^{2}}\right] \tag{B.24}
$$

and

$$
z_{\lim,s}(\phi) = \frac{2h_{p}(r_{o} + r_{i}) \pm h_{s}r_{o}'(r_{p},\phi)}{2(r_{o}'(r_{p},\phi) + r_{o} + r_{i})} \tag{B.25}
$$

where, as before, the $+$ case applies for $z_{\min}$ and the $-$ case for $z_{\max}$.

#### B.4. Inner Transition

The geometry of particle motion through the inner transition surface is the most complicated to analyze. Consider a particle entering the shield along the inner transition surface (Figure B2).

> **Figure B2:** Motion of a particle entering the shield through the inner transition region at horizontal incidence angle $\alpha$ at a radius $r$ (black dot), moving along a circular arc of gyroradius $r_g$ (with center distance $p_g$) through the shield, exiting the inner wall $r_i$ at angle $\alpha_0$, and striking the phantom at $r_p, \phi$.

The law of cosines applied to the triangles $\Delta r_{i}r_{g}p_{g}$ and $\Delta rr_{g}p_{g}$ yields the following expression for $\alpha_{0}$:

$$
\cos(\alpha_{0}) = \frac{(r^{2} - r_{i}^{2}) + 2rr_{g}\cos(\alpha)}{2r_{i}r_{g}} \tag{B.26}
$$

The law of sines yields an additional expression for $\alpha_{0}$:

$$
\cos(\alpha_{0}) = \frac{r_{p}\sin(\phi)}{r_{i}} \tag{B.27}
$$

Eqs. (B.26) and (B.27) can be combined to yield an expression for $\alpha$:

$$
\cos(\alpha) = \frac{2r_{p}r_{g}\sin(\phi) - (r^{2} - r_{i}^{2})}{2rr_{g}} \tag{B.28}
$$

As in the previous cases, expanding the phantom from a point to a small sphere of radius $R$ enables reexpressing Eq. (B.28):

$$
\cos(\alpha) = \frac{2(r_{p} \pm R\csc(\phi))r_{g}\sin(\phi) - (r^{2} - r_{i}^{2})}{2rr_{g}} \tag{B.29}
$$

which yields

$$
\Delta\alpha = \frac{2R}{r} \tag{B.30}
$$

and

$$
\Delta\theta = \frac{4R}{\sqrt{4r^{2} + (h_{s} \pm 2h_{p})^{2}}} \tag{B.31}
$$

where, as before, the $+$ case corresponds to the bottom surface and the $-$ case to the top. Once again, the solid angle element can be computed using $\Delta\alpha$ and $\Delta\theta$:

$$
\begin{aligned}
\Delta\Omega &= \frac{\pi}{4}\int_{\alpha-\Delta\alpha/2}^{\alpha+\Delta\alpha/2}\int_{\theta-\Delta\theta/2}^{\theta+\Delta\theta/2}\sin(\theta')\,d\theta' d\alpha' \\
&= \frac{4\pi R^{2}}{4r^{2} + (h_{s} \pm 2h_{p})^{2}}
\end{aligned} \tag{B.32}
$$

and the projected area element is given by

$$
\begin{aligned}
dA_{\text{proj}} &= \cos(\theta)\sin(\alpha)dA \\
&= \frac{h_{s} \pm 2h_{p}}{\sqrt{4r^{2} + (h_{s} \pm 2h_{p})^{2}}}\operatorname{Re}\left[\sqrt{1 - \left(\frac{r^{2} + r_{p}^{2} - r_{i}^{2} - 2(r + r_{g}(K, r, \phi, \mp\frac{h_{s}}{2}))r_{p}\cos(\phi)}{2rr_{g}(K, r, \phi, \mp\frac{h_{s}}{2})}\right)^{2}}\right]r\,d\phi dr \tag{B.33/B.34}
\end{aligned}
$$

Putting it all together, the flux through the inner transition surface is given by

$$
\Phi_{ti}(K) = \Phi(K)\int_{0}^{2\pi}\int_{r_{i}'(r_{p},\phi)}^{r_{\max}(K,\phi)}\frac{4r(h_{s} \pm 2h_{p})}{\left(4r^{2} + (h_{s} \pm 2h_{p})^{2}\right)^{3/2}}\operatorname{Re}\left[\sqrt{1 - \left(\frac{r^{2} + r_{p}^{2} - r_{i}^{2} - 2(r + r_{g}(K, r, \phi, \mp\frac{h_{s}}{2}))r_{p}\cos(\phi)}{2rr_{g}(K, r, \phi, \mp\frac{h_{s}}{2})}\right)^{2}}\right]dr d\phi \tag{B.35}
$$

where the upper limits of integration in $r$ are given by

$$
r_{\max}(K,\phi) = \operatorname{clamp}\left(\frac{(r_{o}^{2} - r_{i}^{2})(h_{s} \pm 2h_{p})}{4r_{g}(K, r, \phi, h_{p})(r_{o} + r_{p}\sin(\phi))}\operatorname{Re}\left[\sqrt{1 - \left(\frac{r_{o}^{2} - r_{i}^{2}}{2r_{g}(K, r, \phi, h_{p})(r_{o} + r_{p}\sin(\phi))}\right)^{2}}\right], r_{i}'(r_{p},\phi), r_{o}'(r_{p},\phi)\right) \tag{B.36}
$$

#### B.5. Endcap Surface

The derivation of the expression describing GCR flux through the endcap surface largely follows that of the outer transition region, minus the magnetic attenuation component. The solid angle element for the endcap is given by Eq. (B.13), while the projected area element is given by

$$
\begin{aligned}
dA_{\text{proj}} &= \cos(\theta)\sin(\alpha)dA \\
&= \frac{h_{s} \pm 2h_{p}}{\sqrt{4r^{2} + (h_{s} \pm 2h_{p})^{2}}}r\,d\phi dr
\end{aligned} \tag{B.37}
$$

Together, these yield the flux integral describing GCR flux through the endcap surface:

$$
\Phi_{e}(K) = \Phi(K)\int_{0}^{2\pi}\int_{0}^{r_{i}'(r_{p},\phi)}\left(\frac{4r(h_{s} - 2h_{p})}{\left(4r^{2} + (h_{s} - 2h_{p})^{2}\right)^{3/2}} + \frac{4r(h_{s} + 2h_{p})}{\left(4r^{2} + (h_{s} + 2h_{p})^{2}\right)^{3/2}}\right)dr d\phi \tag{B.38}
$$

All 5 flux integrals are then numerically integrated in MATLAB to produce the resulting GCR flux incident upon the spherical phantom. This attenuated spectrum is then passed to HZETRN2020, which handles the nuclear physics and interactions and energy deposition calculations.

### C. Monte Carlo Validation

The Monte Carlo simulation used to validate the new magnetic attenuation model is further discussed here. A GCR proton is initialized at a random point on a sphere of radius $r_{\text{inf}} = 100\text{ m}$, much greater than the longest dimension of the shield. A spherical cap is then generated with pole aligned with the $-\hat{r}$ (i.e., radial) direction and half-angle given by

$$
D = \arctan\left(\frac{\max(h_{s}/2, r_{o})}{r_{\text{inf}}}\right) \tag{C.1}
$$

The proton's initial velocity is then randomly rotated under the constraint that it is directed towards a point along this spherical cap. Setting $D$ in the manner above ensures the particle flux upon the shield is entirely isotropic, minimizing any biases that may be introduced via other methods, while minimizing the number of generated particles that miss the shield entirely.

The particle is then evolved forwards in time, travelling towards the shield. When the particle is outside the shield annular cylinder, it is assumed that no other forces act upon it and so continues to travel in a straight line. Therefore, the particle can be immediately moved to the point where it initially intersects the shield (or the point where it exits the simulation domain, should it miss the shield entirely). Once inside the shield annular cylinder, the particle is evolved using the pure-$B$ Boris algorithm (Boris, 1971), wherein the particle is rotated according to the influence of the magnetic field, accounting for relativistic effects:

$$
\mathbf{p}_{i+1} = \mathbf{p}_{i} + (\mathbf{p}_{i} \times \mathbf{T}) \times \mathbf{S} \tag{C.2}
$$

where $\mathbf{T}$ and $\mathbf{S}$ are given by

$$
\mathbf{T} = \frac{q\,\Delta t}{2m\gamma_{i}}\mathbf{B} \tag{C.3}
$$

$$
\mathbf{S} = \frac{2\mathbf{T}}{1 + \mathbf{T}\cdot\mathbf{T}} \tag{C.4}
$$

where the timestep $\Delta t$ is set to $0.223/V$.

By applying a rotation to the relativistic momentum, the Boris algorithm preserves the magnitude of the momentum much more accurately than traditional solution methods (e.g., Runge-Kutta). Traditional methods include associated truncation errors that accumulate and will significantly alter the long-term trajectories of relativistic particles.

This process is repeated to create a set of incident particles that, when a sufficiently large number of particles are generated, adequately represent the isotropic GCR environment encountered in deep space. The proportion of particles striking a spherical phantom at each energy is recorded. To enable comparison with the analytical methods, this proportion is then normalized by the proportion of particles that strike the phantom when the shield is removed (approximately $0.0035$ for the process described in this section).

---

## References

* Ainsbury, E.A., Bouffler, S.D., Dörr, W., Graw, J., Muirhead, C.R., Edwards, A.A., Cooper, J., 2009. Radiation Cataractogenesis: A Review of Recent Studies. *Radiation Research* 172, 1–9. URL: http://www.bioone.org/doi/10.1667/RR1688.1, doi:[10.1667/RR1688.1](https://doi.org/10.1667/RR1688.1).
* Al Zaman, M.A., Monira, N.J., 2023. Shielding effectiveness of different polymers and low-density hydrides in a combined radiation shield for crewed interplanetary space missions. *Radiation Physics and Chemistry* 205, 110706. URL: https://linkinghub.elsevier.com/retrieve/pii/S0969806X22007691, doi:[10.1016/j.radphyschem.2022.110706](https://doi.org/10.1016/j.radphyschem.2022.110706).
* Battiston, R., Burger, W.J., Calvelli, V., Musenich, R., Choutko, V., Datskov, V.I., Torre, A.D., Venditti, F., Gargiulo, C., Laurenti, G., Lucidi, S., Harrison, S., Meinke, R., 2011. *Active Radiation Shield for Space Exploration Missions*. Technical Report 4200023087/10/NL/AF. Perugia, Italy.
* Boris, J.P., 1971. Relativistic Plasma Simulation – Optimization of a Hybrid Code, in: *Proceedings of the Conference on the Numerical Simulation of Plasmas (4th)*, Defense Technical Information Center, Fort Belvoir, VA. pp. 3–50. URL: http://www.dtic.mil/docs/citations/ADA023511, doi:[10.21236/ADA023511](https://doi.org/10.21236/ADA023511).
* Calvelli, V., Musenich, R., Tunesi, F., Battiston, R., 2017. A Novel Configuration for Superconducting Space Radiation Shields. *IEEE Transactions on Applied Superconductivity* 27, 1–4. URL: https://ieeexplore.ieee.org/document/7792167/, doi:[10.1109/TASC.2016.2642638](https://doi.org/10.1109/TASC.2016.2642638).
* Case, D., 2021. *Astronaut Radiation Protection for Long Duration Missions: Integrating Passive Radiation Shielding into Space Habitat Design*. Doctoral Thesis. University of Colorado, Boulder. Boulder, CO.
* Chesny, D.L., Levin, G.A., Persons, L.E., Durrance, S.T., 2020. Galactic Cosmic Ray Shielding Using Spherical Field-Reversed Array of Superconducting Coils. *Journal of Spacecraft and Rockets* 57, 1222–1231. URL: https://arc.aiaa.org/doi/10.2514/1.A34710, doi:[10.2514/1.A34710](https://doi.org/10.2514/1.A34710).
* Cucinotta, F.A., 2010. *Radiation Risk Acceptability and Limitations*. URL: https://three.jsc.nasa.gov/articles/AstronautRadLimitsFC.pdf.
* Davis, C.M., DeCicco-Skinner, K.L., Roma, P.G., Hienz, R.D., 2014. Individual Differences in Attentional Deficits and Dopaminergic Protein Levels following Exposure to Proton Radiation. *Radiation Research* 181, 258–271. URL: http://www.bioone.org/doi/10.1667/RR13359.1, doi:[10.1667/RR13359.1](https://doi.org/10.1667/RR13359.1).
* Ferrone, K., Guan, F., Ma, J., Peterson, L., Willis, C., Kry, S., 2021. Reducing space radiation cancer risk with magnetic shielding. *Advances in Space Research* 68, 153–160. URL: https://linkinghub.elsevier.com/retrieve/pii/S0273117721001940, doi:[10.1016/j.asr.2021.03.002](https://doi.org/10.1016/j.asr.2021.03.002).
* Ferrone, K., Willis, C., Guan, F., Ma, J., Peterson, L., Kry, S., 2023. A Review of Magnetic Shielding Technology for Space Radiation. *Radiation* 3, 46–57. URL: https://www.mdpi.com/2673-592X/3/1/5, doi:[10.3390/radiation3010005](https://doi.org/10.3390/radiation3010005).
* Francisco, D., 2023. *NASA Spaceflight Human-System Standard - Volume 1: Crew Health*. NASA Technical Standard NASA-STD-3001. NASA. URL: https://standards.nasa.gov/sites/default/files/standards/NASA/C//nasa-std-3001-vol-1-rev-c-signature.pdf.
* Gilbert, E.S., 2009. Ionising radiation and cancer risks: What have we learned from epidemiology? *International Journal of Radiation Biology* 85, 467–482. URL: http://www.tandfonline.com/doi/full/10.1080/09553000902883836, doi:[10.1080/09553000902883836](https://doi.org/10.1080/09553000902883836).
* Griffiths, D.J., 2013. *Introduction to electrodynamics*. Fourth edition ed., Pearson, Boston.
* Hadley, M.M., Davis, L.K., Jewell, J.S., Miller, V.D., Britten, R.A., 2016. Exposure to Mission-Relevant Doses of $1\text{ GeV/n}$ $^{48}\text{Ti}$ Particles Impairs Attentional Set-Shifting Performance in Retired Breeder Rats. *Radiation Research* 185, 13–19. URL: http://www.bioone.org/doi/10.1667/RR14086.1, doi:[10.1667/RR14086.1](https://doi.org/10.1667/RR14086.1).
* Hassler, D.M., Zeitlin, C., Wimmer-Schweingruber, R.F., Ehresmann, B., Rafkin, S., Eigenbrode, J.L., et al., 2014. Mars' Surface Radiation Environment Measured with the Mars Science Laboratory's Curiosity Rover. *Science* 343, 1244797. URL: https://www.science.org/doi/10.1126/science.1244797, doi:[10.1126/science.1244797](https://doi.org/10.1126/science.1244797).
* Iwasa, Y., Marken, K.R., 1995. Case Studies in Superconducting Magnets: Design and Operational Issues. *Physics Today* 48, 68–68. URL: https://pubs.aip.org/physicstoday/article/48/10/68/408145/Case-Studies-in-Superconducting-Magnets-Design-and, doi:[10.1063/1.2808214](https://doi.org/10.1063/1.2808214).
* Jewell, J.S., Duncan, V.D., Fesshaye, A., Tondin, A., Macadat, E., Britten, R.A., 2018. Exposure to $\le 15\text{ cGy}$ of $600\text{ MeV/n}$ $^{56}\text{Fe}$ Particles Impairs Rule Acquisition but not Long-Term Memory in the Attentional Set-Shifting Assay. *Radiation Research* 190, 565. URL: https://bioone.org/journals/radiation-research/volume-190/issue-6/RR15085.1/Exposure-to-15-cGy-of-600-MeV-n-56Fe-Particles/10.1667/RR15085.1.full, doi:[10.1667/RR15085.1](https://doi.org/10.1667/RR15085.1).
* Macias, B.R., Lima, F., Swift, J.M., Shirazi-Fard, Y., Greene, E.S., Allen, M.R., Fluckey, J., Hogan, H.A., Braby, L., Wang, S., Bloomfield, S.A., 2016. Simulating the Lunar Environment: Partial Weightbearing and High-LET Radiation-Induce Bone Loss and Increase Sclerostin-Positive Osteocytes. *Radiation Research* 186, 254–263. URL: http://www.bioone.org/doi/10.1667/RR13579.1, doi:[10.1667/RR13579.1](https://doi.org/10.1667/RR13579.1).
* Musenich, R., Calvelli, V., Giraudo, M., Vuolo, M., Ambroglini, F., Battiston, R., 2018. The Limits of Space Radiation Magnetic Shielding: An Updated Analysis. *IEEE Transactions on Applied Superconductivity* 28, 1–5. URL: http://ieeexplore.ieee.org/document/8233176/, doi:[10.1109/TASC.2017.2785805](https://doi.org/10.1109/TASC.2017.2785805).
* Norman, R.B., Clowdsley, M., Slaba, T., Heilbronn, L., Zeitlin, C., Kenny, S., Crespo, L., Giesy, D., Warner, J., McGirl, N., Castellanos, L., Srikrishna, A., Beach, M., Reddell, B., Singleterry, R., 2017. *Early Results from the Advanced Radiation Protection Thick GCR Shielding Project*, Huntsville, AL. URL: https://ntrs.nasa.gov/citations/20170005580.
* Ozasa, K., Grant, E.J., Kodama, K., 2018. Japanese Legacy Cohorts: The Life Span Study Atomic Bomb Survivor Cohort and Survivors' Offspring. *Journal of Epidemiology* 28, 162–169. URL: https://www.jstage.jst.go.jp/article/jea/28/4/28_JE20170321/_article, doi:[10.2188/jea.JE20170321](https://doi.org/10.2188/jea.JE20170321).
* Patel, Z., Huff, J., Saha, J., Wang, M., Blattnig, S., Wu, H., Cucinotta, F., 2015. *Risk of Cardiovascular Disease and Other Degenerative Tissue Effects from Radiation Exposure*. Evidence Report. National Aeronautics and Space Administration. URL: https://ntrs.nasa.gov/api/citations/20150016006/downloads/20150016006.pdf.
* Siew, K., Nestler, K.A., Nelson, C., D'Ambrosio, V., Zhong, C., Li, Z., et al., 2024. Cosmic kidney disease: an integrated pan-omic, physiological and morphological study into spaceflight-induced renal dysfunction. *Nature Communications* 15, 4923. URL: https://www.nature.com/articles/s41467-024-49212-1, doi:[10.1038/s41467-024-49212-1](https://doi.org/10.1038/s41467-024-49212-1).
* Simon, M., Latorella, K., Martin, J., Cerro, J., Lepsch, R., Jefferies, S., Goodliff, K., Smitherman, D., McCleskey, C., Stromgren, C., 2017. NASA's advanced exploration systems Mars transit habitat refinement point of departure design, in: *2017 IEEE Aerospace Conference*, IEEE, Big Sky, MT, USA. pp. 1–34. URL: http://ieeexplore.ieee.org/document/7943662/, doi:[10.1109/AERO.2017.7943662](https://doi.org/10.1109/AERO.2017.7943662).
* Slaba, T., Blattnig, S., Badavi, F., 2010. Faster and more accurate transport procedures for HZETRN. *Journal of Computational Physics* 229, 9397–9417. URL: https://linkinghub.elsevier.com/retrieve/pii/S0021999110005048, doi:[10.1016/j.jcp.2010.09.010](https://doi.org/10.1016/j.jcp.2010.09.010).
* Slaba, T., Wilson, J., Werneth, C., Whitman, K., 2020. Updated deterministic radiation transport for future deep space missions. *Life Sciences in Space Research* 27, 6–18. URL: https://linkinghub.elsevier.com/retrieve/pii/S2214552420300456, doi:[10.1016/j.lssr.2020.06.004](https://doi.org/10.1016/j.lssr.2020.06.004).
* Vuolo, M., Giraudo, M., Musenich, R., Calvelli, V., Ambroglini, F., Burger, W., Battiston, R., 2016. Monte Carlo simulations for the space radiation superconducting shield project (SR2S). *Life Sciences in Space Research* 8, 22–29. URL: https://linkinghub.elsevier.com/retrieve/pii/S221455241600002X, doi:[10.1016/j.lssr.2015.12.003](https://doi.org/10.1016/j.lssr.2015.12.003).
* Washburn, S., 2013. *A Model for the Rapid Evaluation of Active Magnetic Shielding Design*. Doctoral Thesis. University of Colorado, Boulder. Boulder, CO. URL: https://scholar.colorado.edu/concern/graduate_thesis_or_dissertations/2z10wq42f.
* Washburn, S., Blattnig, S., Singleterry, R., Westover, S., 2014. Analytical-HZETRN model for rapid assessment of active magnetic radiation shielding. *Advances in Space Research* 53, 8–17. URL: https://linkinghub.elsevier.com/retrieve/pii/S0273117713006169, doi:[10.1016/j.asr.2013.09.038](https://doi.org/10.1016/j.asr.2013.09.038).
* Washburn, S., Blattnig, S., Singleterry, R., Westover, S., 2015. Active magnetic radiation shielding system analysis and key technologies. *Life Sciences in Space Research* 4, 22–34. URL: https://linkinghub.elsevier.com/retrieve/pii/S2214552414000686, doi:[10.1016/j.lssr.2014.12.004](https://doi.org/10.1016/j.lssr.2014.12.004).
* Werneth, C., De Wet, W., Townsend, L., Maung, K., Norbury, J., Slaba, T., Norman, R., Blattnig, S., Ford, W., 2021. Relativistic Abrasion-Ablation De-excitation Fragmentation (RAADFRG) model. *Nuclear Instruments and Methods in Physics Research Section B: Beam Interactions with Materials and Atoms* 502, 118–135. URL: https://linkinghub.elsevier.com/retrieve/pii/S0168583X21002275, doi:[10.1016/j.nimb.2021.06.016](https://doi.org/10.1016/j.nimb.2021.06.016).
* Westover, S., Meinke, R., Nerolich, S., Washburn, S., Battiston, R., Burger, W., Kasaboski, D., Davies, F., 2014. *Magnet Architectures and Active Radiation Shielding Study (MAARSS) - Phase II Final Report*. Technical Report. NASA Johnson Space Center. Houston, TX.
* Willey, J.S., Britten, R.A., Blaber, E., Tahimic, C.G., Chancellor, J., Mortreux, M., Sanford, L.D., Kubik, A.J., Delp, M.D., Mao, X.W., 2021. The individual and combined effects of spaceflight radiation and microgravity on biologic systems and functional outcomes. *Journal of Environmental Science and Health, Part C* 39, 129–179. URL: https://www.tandfonline.com/doi/full/10.1080/26896583.2021.1885283, doi:[10.1080/26896583.2021.1885283](https://doi.org/10.1080/26896583.2021.1885283).