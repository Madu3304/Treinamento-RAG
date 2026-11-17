**arXiv:2611.00005v1 [physics.med-ph] 12 Aug 2026**

# Quantitative $T_{2}^{*}$ Fidelity in Accelerated Radial Ultrashort-Echo-Time MRI of the Lumbar Cartilage Endplate

## A synthetic computational validation study

**Yousef Riyazifar**
Independent Researcher
Karlsruhe, Germany
y.riyazifar@gmail.com
ORCID: [0009-0007-6548-8800](https://orcid.org/0009-0007-6548-8800)

*Manuscript draft for scientific review. All experimental results reported here are synthetic; no patient, volunteer, physical-phantom, or scanner raw data were used in the final validation.*

---

## Simple Summary

The cartilage endplate is a thin tissue layer between the vertebral body and the intervertebral disc. Its short transverse relaxation makes conventional MRI insensitive to part of its signal, whereas ultrashort-echo-time (UTE) MRI can preserve this rapidly decaying component. Quantitative $T_{2}^{*}$ mapping may provide information about endplate composition, but accelerating a UTE acquisition changes the reconstruction problem and may alter the measured biomarker even when the reconstructed image appears sharp. We created a fully synthetic multi-coil radial UTE framework of the lumbar spine and compared conjugate-gradient SENSE, joint multi-echo FISTA, and direct model-based $T_{2}^{*}$ reconstruction across increasing undersampling. In a final frozen Monte Carlo experiment, the direct model was accurate at low and moderate acceleration, while severe undersampling produced systematic $T_{2}^{*}$ underestimation. Joint-FISTA produced the lowest image error but not the best quantitative $T_{2}^{*}$ fidelity. These findings show why accelerated quantitative MRI should be evaluated using the final biomarker, not image appearance alone, and define a testable framework for subsequent validation with physical phantoms and Siemens 3-T raw data.

## Abstract

**Background/Objectives:** The lumbar cartilage endplate (CEP) is a short-$T_{2}^{*}$ structure whose composition has been linked to disc health. UTE MRI enables direct CEP visualization, but acceleration and reconstruction may alter quantitative $T_{2}^{*}$ even when image quality improves. This study evaluated how radial undersampling and reconstruction strategy affect CEP $T_{2}^{*}$ fidelity in a controlled synthetic setting.

**Methods:** A $96 \times 96$ sagittal lumbar phantom with five CEP levels (ground-truth $T_{2}^{*}$ $24, 22, 20, 18$, and $16\text{ ms}$) was simulated with six UTE echoes ($\text{TE}$, $0.244\text{–}25.2\text{ ms}$), eight receive coils, and radial sampling. Fully sampled reference data used 302 spokes; retrospective accelerations $R = 1, 2, 4, 6$, and $8$ used $302, 151, 76, 50$, and $38$ spokes, respectively. Reconstructions were CG-SENSE, frozen joint multi-echo FISTA, and a direct nonlinear model estimating $\rho$ and $R_{2}^{*}$ from k-space. Reconstruction settings were frozen before final validation. Twenty independent complex-noise realizations were evaluated per acceleration. Primary endpoints were CEP $T_{2}^{*}$ RMSE, bias, within-CEP dispersion, echo-decay fidelity, and 95% bootstrap confidence intervals.

**Results:** Direct model-map RMSE increased from $0.172\text{ ms}$ (95% CI, $0.153\text{–}0.191$) at $R = 1$ to $0.800\text{ ms}$ ($0.766\text{–}0.836$) at $R = 4$, $1.472\text{ ms}$ ($1.386\text{–}1.557$) at $R = 6$, and $2.256\text{ ms}$ ($2.182\text{–}2.331$) at $R = 8$. At $R = 4$, joint-FISTA had lower image NRMSE than the direct model ($0.132$ vs. $0.203$), whereas the direct map had lower level-wise $T_{2}^{*}$ RMSE than CG-SENSE and joint-FISTA ROI fits ($0.800$ vs. $1.448$ and $1.288\text{ ms}$; estimators differed). At $R = 8$, CG-SENSE ROI fitting had the lowest $T_{2}^{*}$ RMSE ($1.501\text{ ms}$), whereas the direct model showed systematic underestimation (bias, $-2.136\text{ ms}$; concordance correlation coefficient, $0.723$; Bland-Altman limits, $-3.605$ to $-0.668\text{ ms}$).

**Conclusions:** Image fidelity and quantitative biomarker fidelity diverged under radial acceleration. In this synthetic framework, $R = 4$ represented a promising operating point for direct CEP $T_{2}^{*}$ mapping, whereas $R = 8$ produced substantial bias and spatial instability. Scanner, phantom, and in vivo validation are required before clinical translation.

**Keywords:** ultrashort echo time; UTE; cartilage endplate; lumbar spine; $T_{2}^{*}$ mapping; radial MRI; quantitative MRI; model-based reconstruction; compressed sensing; Monte Carlo validation

---

## 1. Introduction

The cartilaginous endplate is a thin interface between vertebral bone and the intervertebral disc and contributes to solute transport between the vertebral marrow and disc. Conventional spin-echo MRI provides limited direct signal from short-$T_{2}$ components of the endplate, while ultrashort-echo-time (UTE) methods can visualize structures that decay before conventional echo times \[1\]. Subsequent work established that CEP $T_{2}^{*}$ measured with very short echo times is sensitive to biochemical composition, including glycosaminoglycan and water content, although the measurement is strongly orientation dependent \[2\].

*In vivo* quantitative studies have further supported the biological relevance of CEP $T_{2}^{*}$. Wang et al. reported spatial variation and repeatability of lumbar CEP $T_{2}^{*}$ and observed associations between lower CEP $T_{2}^{*}$ and more advanced adjacent disc degeneration in younger participants \[3\]. In patients with chronic low back pain, CEP composition remained associated with adjacent nucleus-pulposus composition after adjustment for demographic factors \[4\]. UTE morphology has also been associated with disc degeneration in cadaveric and patient studies \[5, 6\]. More recently, dual-inversion-recovery-prepared UTE has enabled high-contrast CEP depiction in the spine at $3\text{ T}$ \[7\].

A major obstacle to quantitative UTE MRI is acquisition time. Radial sampling is attractive for short-TE imaging, but acceleration reduces the number of spokes supporting each echo and increases streaking, noise amplification, and the risk that reconstruction alters the relative signal amplitudes across echo times. This distinction is especially important for relaxometry: a reconstruction can produce a visually sharp image while changing the decay slope that determines $T_{2}^{*}$. The problem is not unique to UTE. Model-based quantitative MRI methods have shown that parameter maps can be estimated directly from undersampled raw data by incorporating the MR signal model into the inverse problem \[8, 9, 10\].

The present study was designed as a synthetic stress test rather than a clinical validation. We asked whether image-domain and model-based reconstruction strategies preserve a predefined lumbar $T_{2}^{*}$ biomarker as radial undersampling increases. The reconstruction-development phase was completed before a final frozen Monte Carlo validation. Our primary objective was to characterize quantitative $T_{2}^{*}$ fidelity across acceleration factors and to test whether image fidelity and biomarker fidelity provide concordant rankings of reconstruction methods.

## 2. Materials and Methods

### 2.1. Study Design and Synthetic Ground Truth

This was a fully synthetic computational study. No patients, volunteers, animals, physical phantoms, or scanner raw data were used; institutional review board approval and informed consent were therefore not applicable. The final validation was intentionally separated from reconstruction development: all reconstruction and regularization parameters were frozen before the V4.4 Monte Carlo experiment, noise seeds were fixed prospectively, and no tuning was performed on the final validation realizations.

A stylized sagittal lumbar phantom ($96 \times 96$ matrix) represented five motion segments from L1-L2 through L5-S1 and included CEP, nucleus pulposus, annulus fibrosus, vertebral marrow, cortical/subchondral bone, and paraspinal muscle compartments. Five level-specific CEP $T_{2}^{*}$ values ($24, 22, 20, 18$, and $16\text{ ms}$ from L1-L2 to L5-S1) spanned the literature-anchored *in vivo* range reported for higher- and lower-$T_{2}^{*}$ CEP composition-like states \[3\]. These values were not used as diagnostic categories. CEP orientation relative to $B_{0}$ was held fixed because the magic-angle dependence of CEP $T_{2}^{*}$ can be as large as the biological differences of interest \[2\].

### 2.2. UTE Signal and Multi-Coil Radial Acquisition Model

The synthetic UTE timing was based on an *in vivo* multi-echo UTE-Cones protocol reported for CEP composition imaging: repetition time $32\text{ ms}$, flip angle $19^{\circ}$, and six echo times of $0.244, 5.2, 10.2, 15.2, 20.2$, and $25.2\text{ ms}$ \[3\]. Tissue-dependent proton-density/$T_{1}$ amplitude factors were combined with mono-exponential $T_{2}^{*}$ decay. For the direct reconstruction, all echo-independent amplitude terms were absorbed into a complex $\rho$ map, so that the predicted echo signal was modeled as

$$
S_{e}(r) = \rho(r)\exp\left[-TE_{e}R_{2}^{*}(r)\right], \qquad T_{2}^{*}(r) = \frac{1}{R_{2}^{*}(r)}. \tag{1}
$$

Eight smooth synthetic receive-coil sensitivity maps were used. A matched radial forward/adjoint operator generated complex multi-coil k-space. The dense reference used $302$ spokes. Acceleration factors $R = 1, 2, 4, 6$ and $8$ corresponded to $302, 151, 76, 50$, and $38$ spokes, respectively. Complex Gaussian k-space noise was added at the fixed final normalized setting ($\sigma \approx 0.004975$ per complex channel). This noise level was selected for the computational experiment and was not calibrated to reproduce clinical repeatability.

### 2.3. Reconstruction Methods

* **CG-SENSE.** Multi-coil least-squares reconstruction was performed using an unregularized conjugate-gradient sensitivity-encoding formulation. This served as a conventional data-consistent iterative comparator \[11\].
* **Joint multi-echo FISTA.** A data-consistent FISTA reconstruction used a shared Haar-wavelet group-sparsity prior across the echo dimension. The relative threshold ($5 \times 10^{-5}$) had been selected in a separate development/calibration experiment and was frozen before the final Monte Carlo validation. FISTA was included because sparse regularization can substantially improve image fidelity under undersampling while potentially changing relative echo amplitudes \[12, 13\].
* **Direct model-based $T_{2}^{*}$ reconstruction.** A nonlinear inverse formulation jointly estimated the complex $\rho$ map and the real $R_{2}^{*}$ map from all echo k-space data. Analytical gradients propagated data residuals through the exponential signal model. Earlier development experiments tested wavelet regularization of $\rho$ and edge-aware spatial regularization of $R_{2}^{*}$; both calibration procedures selected zero regularization. Accordingly, the final model used $\rho$ regularization $= 0$ and $R_{2}^{*}$ edge-aware $\beta = 0$ with $75$ nonlinear iterations. This choice avoided introducing a smoother but biased map after calibration showed that increased parameter regularization reduced voxel variance at the cost of greater $T_{2}^{*}$ error. Direct parameter estimation follows the broader model-based quantitative MRI framework established for accelerated relaxometry \[8, 9, 10\].

### 2.4. Quantitative Endpoints

For CG-SENSE and joint-FISTA, signal was averaged within each predefined synthetic CEP level at each echo and fitted to a mono-exponential decay, producing a regional ROI-fit $T_{2}^{*}$. The direct model additionally produced a $T_{2}^{*}$ parameter map; the mean $T_{2}^{*}$ within each CEP level was the primary direct-map estimate. Because these are different estimators, they were labeled explicitly and were not treated as identical measurement pipelines.

For each Monte Carlo realization, quantitative endpoints included level-wise $T_{2}^{*}$ RMSE and mean absolute error, mean direct-map bias, median within-CEP voxel standard deviation, and the fraction of valid direct-map CEP voxels. Echo-decay fidelity was assessed using relative echo gain: $S_{\text{recovered}}(TE)/S_{\text{truth}}(TE)$, normalized by the corresponding first-echo gain. The RMS deviation of this normalized gain from $1$ quantified echo-shape distortion. Mean image normalized RMSE across echoes was a secondary endpoint because image error does not directly measure quantitative relaxometry fidelity.

### 2.5. Frozen Monte Carlo Validation and Statistical Analysis

Twenty independent noise realizations were generated for each acceleration factor, yielding $100$ final validation reconstructions per method. The representative $R = 8$ realization used for imaging figures was selected after all runs as the case with direct-map RMSE closest to the $R = 8$ median, rather than by visual appearance.

Results are reported as means with 95% confidence intervals obtained from $2000$ deterministic non-parametric bootstrap resamples of the $20$ realization-level values. At $R = 8$, direct-model agreement was further evaluated over $100$ level-by-realization observations (five CEP levels $\times$ $20$ realizations) using ordinary least-squares slope/intercept, Lin's concordance correlation coefficient (CCC), mean bias, and Bland-Altman 95% limits of agreement. No null-hypothesis significance testing was used for method ranking; interpretation emphasized effect sizes, confidence intervals, and estimator-specific failure modes.

**Table 1: Frozen synthetic acquisition and reconstruction design.**

| Component | Final frozen setting |
| :--- | :--- |
| Matrix/geometry | $96 \times 96$ sagittal stylized lumbar phantom; five CEP levels |
| CEP ground truth | L1-L2 to L5-S1: $24, 22, 20, 18, 16\text{ ms}$ |
| UTE timing | TR $32\text{ ms}$; flip angle $19^{\circ}$; TE $0.244, 5.2, 10.2, 15.2, 20.2, 25.2\text{ ms}$ |
| Receive array | $8$ synthetic coils |
| Radial sampling | $R = 1/2/4/6/8$: $302/151/76/50/38$ spokes |
| Final Monte Carlo | $20$ independent noise realizations per $R$; $100$ total |
| CG-SENSE | Unregularized multi-coil least-squares reconstruction |
| Joint-FISTA | Shared multi-echo Haar-wavelet prior; frozen threshold $5 \times 10^{-5}$ |
| Direct model | Joint $\rho/R_{2}^{*}$ nonlinear inversion; $75$ iterations |
| Final regularization | $\rho$ wavelet threshold $= 0$; $R_{2}^{*}$ edge-aware $\beta = 0$ |

## 3. Results

### 3.1. Direct $T_{2}^{*}$ Accuracy Degraded Progressively with Acceleration

All $100$ frozen Monte Carlo realizations completed successfully. Direct model-map level-wise $T_{2}^{*}$ RMSE increased monotonically with radial undersampling: $0.172\text{ ms}$ (95% CI, $0.153\text{–}0.191$) at $R = 1$; $0.284\text{ ms}$ ($0.260\text{–}0.306$) at $R = 2$; $0.800\text{ ms}$ ($0.766\text{–}0.836$) at $R = 4$; $1.472\text{ ms}$ ($1.386\text{–}1.557$) at $R = 6$; and $2.256\text{ ms}$ ($2.182\text{–}2.331$) at $R = 8$. Mean direct-model bias was $-0.120, -0.247, -0.728, -1.395$, and $-2.136\text{ ms}$, respectively, indicating increasing negative bias with acceleration.

Spatial parameter stability also deteriorated with undersampling. Median within-CEP voxel standard deviation increased from $2.175\text{ ms}$ at $R = 1$ to $3.108\text{ ms}$ at $R = 2$, $5.802\text{ ms}$ at $R = 4$, $7.402\text{ ms}$ at $R = 6$, and $7.884\text{ ms}$ at $R = 8$. The direct map nevertheless returned valid values for all synthetic CEP voxels across the final validation.

### 3.2. Image Fidelity and Quantitative $T_{2}^{*}$ Fidelity Ranked Methods Differently

At $R = 4$, joint-FISTA produced the lowest mean image NRMSE ($0.132$; 95% CI, $0.132\text{–}0.132$), compared with $0.203$ for model-predicted echoes and $0.255$ for CG-SENSE. However, the direct model-map level-wise $T_{2}^{*}$ RMSE was $0.800\text{ ms}$ ($0.766\text{–}0.836$), whereas CG-SENSE and joint-FISTA ROI-fit RMSEs were $1.448\text{ ms}$ ($1.382\text{–}1.510$) and $1.288\text{ ms}$ ($1.253\text{–}1.325$), respectively. These comparisons involve different estimators but demonstrate that the method producing the lowest image error did not necessarily produce the lowest quantitative $T_{2}^{*}$ error.

The divergence became more pronounced at severe undersampling. At $R = 8$, joint-FISTA again had the lowest image NRMSE ($0.162$), followed by the direct model predicted echoes ($0.262$) and CG-SENSE ($0.349$). In contrast, CG-SENSE ROI fitting had the lowest regional $T_{2}^{*}$ RMSE ($1.501\text{ ms}$; 95% CI, $1.404\text{–}1.608$), followed by the direct model map ($2.256\text{ ms}$; $2.182\text{–}2.331$), model-predicted echo ROI fitting ($3.654\text{ ms}$; $3.591\text{–}3.716$), and joint-FISTA ROI fitting ($3.842\text{ ms}$; $3.820\text{–}3.866$). Thus, severe undersampling reversed the ranking suggested by image NRMSE.

### 3.3. Echo-Decay Distortion and High-Acceleration Failure Mode

Echo-shape error increased with acceleration for all methods but differed substantially by reconstruction strategy. At $R = 8$, the RMS deviation of normalized relative echo gain from unity was $0.0666$ for CG-SENSE, $0.1601$ for the direct model, and $0.1766$ for joint-FISTA. The combination of low image NRMSE and larger echo-shape distortion in joint-FISTA illustrates how image-domain regularization can alter the relative TE-dependent signal required for relaxometry.

**Table 2: Final Monte Carlo quantitative performance across acceleration. Direct model-map and ROI-fit values are different estimators and should not be interpreted as identical measurement pipelines.**

| $R$ | Spokes | Direct map RMSE, ms (95% CI) | CG ROI-fit RMSE, ms (95% CI) | Joint-FISTA ROI-fit RMSE, ms (95% CI) | Direct bias / voxel SD, ms |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $1$ | $302$ | $0.172$ ($0.153\text{–}0.191$) | $0.178$ ($0.151\text{–}0.204$) | $0.632$ ($0.606\text{–}0.657$) | $-0.120$ / $2.175$ |
| $2$ | $151$ | $0.284$ ($0.260\text{–}0.306$) | $0.422$ ($0.395\text{–}0.449$) | $0.612$ ($0.584\text{–}0.638$) | $-0.247$ / $3.108$ |
| $4$ | $76$ | $0.800$ ($0.766\text{–}0.836$) | $1.448$ ($1.382\text{–}1.510$) | $1.288$ ($1.253\text{–}1.325$) | $-0.728$ / $5.802$ |
| $6$ | $50$ | $1.472$ ($1.386\text{–}1.557$) | $1.735$ ($1.687\text{–}1.784$) | $2.787$ ($2.755\text{–}2.817$) | $-1.395$ / $7.402$ |
| $8$ | $38$ | $2.256$ ($2.182\text{–}2.331$) | $1.501$ ($1.404\text{–}1.608$) | $3.842$ ($3.820\text{–}3.866$) | $-2.136$ / $7.884$ |

**Table 3: Image fidelity and echo-shape fidelity at moderate and severe acceleration.**

| $R$ | CG image NRMSE | Joint-FISTA image NRMSE | Model image NRMSE | CG echo error | Joint-FISTA echo error | Model echo error |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $4$ | $0.2548$ | $0.1321$ | $0.2027$ | $0.0518$ | $0.0628$ | $0.0720$ |
| $8$ | $0.3491$ | $0.1616$ | $0.2617$ | $0.0666$ | $0.1766$ | $0.1601$ |

Across the $100$ level-by-realization direct-model observations at $R = 8$, agreement with ground truth was moderate ($\text{CCC}$, $0.723$). The regression slope was $0.836$ with an intercept of $1.137\text{ ms}$. Mean bias was $-2.136\text{ ms}$, and the Bland-Altman 95% limits were $-3.605$ to $-0.668\text{ ms}$. Because both limits were below zero, the high-acceleration error represented systematic underestimation rather than random scatter centered on the ground truth. Level-wise direct-model bias at $R = 8$ ranged from $-3.25\text{ ms}$ at L1-L2 to $-1.51\text{ ms}$ at L5-S1, with the largest within-CEP voxel dispersion in the upper levels.

## 4. Discussion

This frozen synthetic Monte Carlo study produced three main findings. First, direct model-based CEP $T_{2}^{*}$ mapping was quantitatively accurate at low and moderate radial acceleration, with a level-wise RMSE below $1\text{ ms}$ through $R = 4$. Second, reconstruction methods were ranked differently by image NRMSE and by the final $T_{2}^{*}$ biomarker. Joint-FISTA consistently produced the lowest image NRMSE but developed larger quantitative error and echo-shape distortion at higher acceleration. Third, severe $R = 8$ undersampling exceeded the stable operating range of the current direct model, producing systematic $T_{2}^{*}$ underestimation, reduced concordance, and large within-CEP voxel dispersion.

The divergence between image fidelity and biomarker fidelity is the central methodological result. Sparse image-domain regularization is designed to suppress aliasing and noise in reconstructed images. Relaxometry, however, depends on ratios between signals acquired at different echo times. If regularization shrinks or redistributes signal differently across echoes, the resulting image series can appear cleaner while the fitted decay slope is biased. The $R = 8$ results demonstrate this explicitly: joint-FISTA had approximately half the image NRMSE of CG-SENSE yet more than twice the regional $T_{2}^{*}$ RMSE. For quantitative MRI, reconstruction should therefore be validated against the final biological parameter rather than using image quality alone as a surrogate endpoint.

Direct model-based reconstruction was introduced to constrain the echo series to a physically consistent exponential decay. This approach improved level-mean $T_{2}^{*}$ recovery at moderate undersampling and follows prior nonlinear inverse methods that estimate relaxation maps directly from undersampled data \[8, 9, 10\]. Nevertheless, the simple signal model was not sufficient at $R = 8$. The direct map became noisy and systematically underestimated $T_{2}^{*}$. Several mechanisms may contribute. Strong undersampling leaves insufficient data to estimate a spatially varying $R_{2}^{*}$ field robustly; averaging a heterogeneous reconstructed parameter field also yields a mixture of exponentials at the ROI level. In addition, the present forward model is intentionally idealized and does not include off-resonance, gradient delays, actual 3D Cones/DIR-UTE preparation, fat-water interactions, or scanner-specific trajectory errors.

The behavior of CG-SENSE at $R = 8$ is also informative. Although CG-SENSE had the worst image NRMSE of the three iterative methods, its ROI-fit $T_{2}^{*}$ RMSE and echo-shape fidelity were better than those of joint-FISTA and the direct model. In this synthetic experiment, spatial artifacts can partially average within the known CEP ROI while preserving relative decay across TE. This does not imply that CG-SENSE is preferable for clinical CEP imaging, where the true segmentation is unknown and streaking may compromise localization; rather, it emphasizes that regional parameter estimation and spatial image quality are distinct endpoints.

The results suggest $R = 4$ as a practical target for the next translational experiment. At this acceleration, the direct model-map RMSE was $0.800\text{ ms}$ with a narrow bootstrap confidence interval, while the experiment still showed substantial acceleration relative to the $302$-spoke reference. We deliberately interpret $R = 6$ as a borderline stress test and $R = 8$ as a failure-mode condition rather than attempting to present all accelerations as successful. Such a bounded conclusion is more useful for sequence development because it defines where scanner validation should begin.

The lumbar CEP is particularly challenging because it is thin, orientation dependent, and adjacent to tissues with very different susceptibility and fat content. Fields et al. showed that CEP $T_{2}^{*}$ at $3\text{ T}$ changes markedly with orientation relative to $B_{0}$ \[2\]. The present synthetic study held orientation fixed, meaning that the reported reconstruction errors should not be interpreted as total *in vivo* measurement error. Likewise, the predefined synthetic masks remove the segmentation uncertainty that would be present in human imaging. Prior UTE studies demonstrate that CEP morphology can be visualized and related to disc degeneration in cadaveric and clinical settings \[1, 5, 6, 7\]. Related quantitative UTE work in the musculoskeletal system has likewise emphasized noise robustness and the need for staged validation before clinical translation \[14\]. Robust CEP mapping will require explicit control of orientation, partial volume, and sequence-specific contrast.

This study has limitations. The anatomy, tissue parameters, receive coils, and radial operator were synthetic. The tissue values were literature-anchored but were not patient-specific, and the level-wise $T_{2}^{*}$ range was used as a controlled test pattern rather than as a diagnostic label. The encoding operator was matched between simulation and reconstruction, which is more favorable than real scanner conditions. We did not model motion, $B_{0}/B_{1}$ inhomogeneity, gradient delay, trajectory error, fat-water effects, partial volume, true 3D Cones sampling, or dual-inversion preparation. Noise was not calibrated to clinical repeatability. Finally, comparisons between the direct map and ROI-fit baselines involve different estimators and therefore should be interpreted as endpoint behavior, not as a definitive head-to-head clinical performance ranking.

The next phase should replace the matched synthetic operator with measured Siemens 3-T non-Cartesian trajectories and raw-data scaling, followed by coil-sensitivity estimation, gradient-delay and off-resonance correction, and physical phantom validation. A small repeatability experiment on a physical short-$T_{2}^{*}$ phantom would substantially strengthen the quantitative claims before human testing. Once scanner fidelity is established, the same frozen endpoints—$T_{2}^{*}$ bias, precision, echo-shape preservation, and acceleration dependence—can be applied to healthy-volunteer and patient data.

## 5. Conclusions

In a fully synthetic frozen Monte Carlo study of accelerated radial UTE MRI, image reconstruction quality did not reliably predict quantitative lumbar CEP $T_{2}^{*}$ fidelity. Direct model-based reconstruction maintained sub-millisecond level-wise $T_{2}^{*}$ RMSE through $R = 4$ but developed increasing negative bias and spatial instability at higher acceleration. Joint-FISTA provided superior image NRMSE yet greater $T_{2}^{*}$ distortion at severe undersampling. These findings support endpoint-aware validation of accelerated quantitative MRI and motivate scanner/phantom translation beginning near $R = 4$ rather than further synthetic algorithm tuning.

## Ethics Statement

This work is a fully synthetic computational study. No human participants, animals, physical specimens, or identifiable clinical data were used. Institutional review board approval and informed consent were therefore not applicable.

## Data and Code Availability

The current manuscript draft describes a synthetic computational framework. Final repository, code-availability, and data-sharing statements should be completed by the author group before submission.

## References

1. W. C. Bae, S. Statum, Z. Zhang, et al. "Morphology of the Cartilaginous Endplates in Human Intervertebral Disks with Ultrashort Echo Time MR Imaging." *Radiology* 266.2 (2013). doi: [10.1148/radiol.12121181](https://doi.org/10.1148/radiol.12121181).
2. A. J. Fields, M. Han, R. Krug, and J. C. Lotz. "Cartilaginous End Plates: Quantitative MR Imaging with Very Short Echo Times Orientation Dependence and Correlation with Biochemical Composition." *Radiology* 274.2 (2015), pp. 482–489. doi: [10.1148/radiol.14141082](https://doi.org/10.1148/radiol.14141082).
3. L. Wang et al. "Evaluation of Human Cartilage Endplate Composition Using MRI: Spatial Variation, Association with Adjacent Disc Degeneration, and In Vivo Repeatability." *Journal of Orthopaedic Research* 39 (2021), pp. 1470–1478. doi: [10.1002/jor.24787](https://doi.org/10.1002/jor.24787).
4. N. B. Bonnheim, L. Wang, A. A. Lazar, et al. "The Contributions of Cartilage Endplate Composition and Vertebral Bone Marrow Fat to Intervertebral Disc Degeneration in Patients with Chronic Low Back Pain." *European Spine Journal* 31 (2022), pp. 1866–1872. doi: [10.1007/s00586-022-07206-x](https://doi.org/10.1007/s00586-022-07206-x).
5. T. Finkenstaedt, P. Siriwananrangsun, K. Masuda, et al. "Ultrashort Time-to-Echo MR Morphology of Cartilaginous Endplate Correlates with Disc Degeneration in the Lumbar Spine." *European Spine Journal* 32.7 (2023), pp. 2358–2367. doi: [10.1007/s00586-023-07739-9](https://doi.org/10.1007/s00586-023-07739-9).
6. Z. Ji, Y. Li, W. Dou, Y. Zhu, Y. Shi, and Y. Zou. "Ultra-short Echo Time MR Imaging in Assessing Cartilage Endplate Damage and Relationship Between Its Lesion and Disc Degeneration for Chronic Low Back Pain Patients." *BMC Medical Imaging* 23 (2023), p. 60. doi: [10.1186/s12880-023-01014-5](https://doi.org/10.1186/s12880-023-01014-5).
7. J. S. Athertya, J. Lo, X. Chen, et al. "High Contrast Cartilaginous Endplate Imaging in Spine Using Three Dimensional Dual-Inversion Recovery Prepared Ultrashort Echo Time (3D DIR-UTE) Sequence." *Skeletal Radiology* 53 (2024), pp. 881–890. doi: [10.1007/s00256-023-04503-4](https://doi.org/10.1007/s00256-023-04503-4).
8. K. T. Block, M. Uecker, and J. Frahm. "Model-Based Iterative Reconstruction for Radial Fast Spin-Echo MRI." *IEEE Transactions on Medical Imaging* 28.11 (2009), pp. 1759–1769. doi: [10.1109/TMI.2009.2023119](https://doi.org/10.1109/TMI.2009.2023119).
9. T. J. Sumpf, M. Uecker, S. Boretius, and J. Frahm. "Model-Based Nonlinear Inverse Reconstruction for T2 Mapping Using Highly Undersampled Spin-Echo MRI." *Journal of Magnetic Resonance Imaging* 34.2 (2011), pp. 420–428. doi: [10.1002/jmri.22634](https://doi.org/10.1002/jmri.22634).
10. T. J. Sumpf, A. Petrovic, M. Uecker, F. Knoll, and J. Frahm. "Fast T2 Mapping with Improved Accuracy Using Undersampled Spin-Echo MRI and Model-Based Reconstructions with a Generating Function." *IEEE Transactions on Medical Imaging* 33.12 (2014), pp. 2213–2222. doi: [10.1109/TMI.2014.2333370](https://doi.org/10.1109/TMI.2014.2333370).
11. K. P. Pruessmann, M. Weiger, M. B. Scheidegger, and P. Boesiger. "SENSE: Sensitivity Encoding for Fast MRI." *Magnetic Resonance in Medicine* 42.5 (1999), pp. 952–962.
12. A. Beck and M. Teboulle. "A Fast Iterative Shrinkage-Thresholding Algorithm for Linear Inverse Problems." *SIAM Journal on Imaging Sciences* 2.1 (2009), pp. 183–202. doi: [10.1137/080716542](https://doi.org/10.1137/080716542).
13. M. Lustig, D. Donoho, and J. M. Pauly. "Sparse MRI: The Application of Compressed Sensing for Rapid MR Imaging." *Magnetic Resonance in Medicine* 58.6 (2007), pp. 1182–1195. doi: [10.1002/mrm.21391](https://doi.org/10.1002/mrm.21391).
14. S. Sedaghat, J. I. Park, E. Fu, Y. Jung, and H. Jang. "Ultrashort Echo Time Double Echo Steady-State MRI for Quantitative Conductivity Mapping in the Knee: A Feasibility Study." *Tomography* 12 (2026), p. 18. doi: [10.3390/tomography12020018](https://doi.org/10.3390/tomography12020018).

---

## Figures

> **Figure 1: Representative median-performing $R = 8$ realization.**
> * **Top row (A–D):** Synthetic ground-truth reference, CG-SENSE, joint-FISTA, and direct model-predicted first-echo magnitude images of the sagittal lumbar phantom.
> * **Bottom row (E–H):** Corresponding regional CEP $T_{2}^{*}$ visualization overlaid on the five intervertebral levels (color scale from $14$ to $25\text{ ms}$).
> * *Note:* The $R = 8$ case was selected by median direct-model RMSE, not visual appearance. The panel is a stress-test/failure-mode example and should not be interpreted as the preferred operating point.

> **Figure 2: Spatial stability of the direct model at $R = 8$ across 20 frozen noise realizations.**
> * **Panels (A–D):** Ground-truth CEP $T_{2}^{*}$, $R = 8$ Monte Carlo mean direct $T_{2}^{*}$ map, Monte Carlo mean bias, and Monte Carlo voxelwise standard deviation (SD), illustrating systematic underestimation and high spatial variance under severe radial undersampling.
> * **Panels (E–F):** Zoomed lower-lumbar crops at L4-L5 ($15.8\text{ ms}$) and L5-S1 ($14.5\text{ ms}$) showing representative regional maps and voxel-level heterogeneity.

> **Figure 3: Frozen Monte Carlo performance across $R = 1, 2, 4, 6$, and $8$ ($20$ noise realizations per acceleration).**
> * **Panel A (Quantitative robustness):** CEP $T_{2}^{*}$ RMSE ($\text{ms}$) across $R$ for CG-SENSE ROI-fit, Joint-FISTA ROI-fit, Model-predicted echo ROI-fit, and Direct model map.
> * **Panel B (Direct-map spatial dispersion):** Median within-CEP voxel SD ($\text{ms}$) rising monotonically from $2.175\text{ ms}$ ($R=1$) to $7.884\text{ ms}$ ($R=8$).
> * **Panel C (Multi-echo decay-shape preservation):** RMS deviation of relative echo gain from $1$ across $R$.
> * **Panel D (Image fidelity - secondary endpoint):** Mean image NRMSE across $R$, demonstrating the divergence between lower image error (Joint-FISTA) and quantitative biomarker fidelity. All error bars indicate 95% bootstrap confidence intervals.

> **Figure 4: High-acceleration $R = 8$ distributions and level-wise behavior.**
> * **Panel A:** Realization-level CEP $T_{2}^{*}$ RMSE ($\text{ms}$) distributions across all 20 realizations per estimator (CG ROI, Joint ROI, Model ROI, Model direct).
> * **Panel B:** Level-wise mean $T_{2}^{*}$ bias ($\text{ms}$) from L1-L2 to L5-S1 comparing CG-SENSE ROI, Joint-FISTA ROI, and Direct model map.
> * **Panel C:** Direct-model level-wise $T_{2}^{*}$ recovery ($\text{ms}$) versus ground truth across levels L1-L2 through L5-S1.
> * **Panel D:** Spatial dispersion (within-CEP voxel SD, $\text{ms}$) by spinal level at $R = 8$, showing highest variance in upper lumbar levels (L1-L2). Together, these panels demonstrate that the $R = 8$ failure mode is systematic and spatially heterogeneous rather than a single unfavorable realization.

> **Figure 5: $R = 8$ agreement and echo-decay fidelity.**
> * **Panel A ($R = 8$ agreement | $\text{CCC} = 0.723$):** Scatter plot and ordinary least-squares (OLS) regression line ($y = 0.836x + 1.137$) comparing recovered direct $T_{2}^{*}$ against true CEP $T_{2}^{*}$ relative to the identity line.
> * **Panel B (Bland-Altman agreement at $R = 8$):** Difference (Recovered $-$ True $T_{2}^{*}$, $\text{ms}$) versus mean $T_{2}^{*}$, showing a mean bias of $-2.136\text{ ms}$ and 95% limits of agreement from $-3.605$ to $-0.668\text{ ms}$.
> * **Panels C & D (L4-L5 and L5-S1 decay-shape preservation):** Multi-echo relative echo-gain curves across $\text{TE}$ ($0\text{–}25.2\text{ ms}$) comparing CG-SENSE, Joint-FISTA, and Model-based reconstruction against the ideal unity line, demonstrating reconstruction-dependent distortion of the TE decay.