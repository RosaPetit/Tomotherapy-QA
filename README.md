# Tomotherapy-QA

The implementation of IMRT represented an important step in oncological radiotherapy. Compared to conventional 3D-conformal therapy, IMRT was a substantial improvement in the ability to precisely respect the volume and boundaries of the tumour and to effectively increase the protection of surrounding normal tissues. This increase in conformation of dose in turn makes it possible to escalate the dose to the target without increasing normal tissue toxicity.

The concept of Tomotherapy was originally born from Dr. Thomas Mackie and Paul Reckwerdt of the University of Wisconsin and consisted of a CT unit that integrated a linear accelerator inside. This design allowed to treat patients with IMRT technique with many advantages over other systems, such as the ability to obtain MVCT images to verify the positioning of the patient before the treatment and the reconstruction of the delivered dose using the CT detectors, among others. 
 These tools opened the possibility of correcting minimal variations in treatments, solidifying the concept of adaptive and conformational radiotherapy.


Role of pre-treatment quality assurance in Tomotherapy

The different degrees of freedom that IMRT has in helical Tomotherapy lead to increased uncertainties due to the dynamic nature and dosimetric variability of the treatment. Therefore, the verification of treatment plans is a standard and essential part of the workflow in planning patients treated with IMRT in helical Tomotherapy today. This implies a challenge for medical physicists in the development of tools and metrics that ensure and guarantee the quality assurance (QA) of the plans to be delivered to the patient. 

Currently, there are several methods to verify plans in IMRT. QA method choice and its implementation closely depend on the needs of the environment, such as the availability of equipment, the regulations of the clinical area, and the workflow in the radiotherapy department.

One of the most adopted procedure in Tomotherapy pre-treatment verification QA  consists in the evaluation of the deviation between a calculated dose and a measured one (single- point absolute measurement) together with the analysis of the gamma index, after the treatment plan is computed on an appropriate phantom.


For this purpose, Tomotherapy planning system includes a software, better know as DQA (Delivery Quality Assurance), to compute the plan dose in a phantom selected by the user. The phantom is then irradiated under the treatment conditions to obtain the measured dose and the gamma index is evaluated. As we will discuss later, this index includes the comparison of the dose distributions from a geometric point of view (by studying the displacement between the reference and the  measured dose distributions) and from a dosimetric point of view (by punctually evaluating the difference between planned and delivered doses).  

The selected pre-treatment QA strategy also needs to be evaluated to validate the appropriateness of the choice and its ability to evidenced changes in  the performance of the system over time. This is why AAPM TG No. 218 establishes universal tolerance and action limits derived from previous research, conducted by international protocols and societies. This text also provides procedures to establish tolerance and action limits at the local level through a statistical process control (SPC).

Tolerance limits are defined as the limits where a process is considered to be operating normally, that is, subject only to random errors. Results out of tolerance limits provide an indication that a system is deviating from normal operation  and investigation of causes should be started.

In contrast, the action limits can be defined as the quantity that the quality measures are allowed to deviate without risk of harm to the patient, namely, they represent the variation of the verification process that can be accepted and indicate the starting point where the action necessarily needs to take place as the process is outside the expected parameters (defining limit values for when corrective action is required).

This is where the statistical process control comes. MacGregor said the objective of SPC is to monitor the performance of a process over time in order to verify that the process is remaining in a "state of statistical control". Such a state of control is said to exist if certain processes or product variables remain close to their desired values and the only source of variation is "common cause" variation, that is, the variation which affects the process all the time is essentially unavoidable within the current process.

The objective of this work is setting tolerance and action limits for different anatomical sites for pre-treatment verification using SPC, as described in AAPM TG No. 218 and provide a retrospective analysis of the  execution over the time of the DQA methods performed with the ArcCheck ™ dosimetric system (Sun Nuclear) in the radiotherapy center of the Azienda Ospedaliera Universitaria Senese, for intensity-modulated (IM) treatments delivered with Tomotherapy$^{TM}$ (Accuray). 
