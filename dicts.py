
fieldmap = {
        'pheno_asddx' : {
                1 : {'autistic' : [1,2]}, #Autism, Pdd
                0 : {'autistic' : [3,4]}, #Asperger's, Other
                2 : {'autistic' : 5}   }, #NA
                                
        'pheno_epidx' : {
                1 : {'status' : 1}, #Yes
                0 : {'status' : 2}   }, #No
                
        'pheno_epitype' : {
                1 : {'childhood_syndromes___7' : 1, #Epilepsy with myoclonic absences
                     'childhood_syndromes___11' : 1, #Childhood absencse epilepsy
                     'adoladult_syndromes' : [1,2,6]   }, #JAE, JME, Epilepsy with GTCs alone  
                2 : {'childhood_syndromes___2' : 1, #Early onset benign childhood occipital epilepsy
                     'childhood_syndromes___4' : 1, #BECTS
                     'childhood_syndromes___5' : 1, #ADNFLE
                     'childhood_syndromes___6' : 1, #Late onset childhood occipital epilepsy
                     'adoladult_syndromes' : [4,5], #ADEAF, Other familial temporal lobe epilepsies
                     'infancy_syndromes' : [4,5]   }, #Benign infantile epilepsy, Benign familial infantile epilepsy          
                3 : {'epil_etiology' : [4,5,10,16], #Stroke, Hypoxic-Ischemic Encephalopathy, Mesial Temporal Sclerosis, Malformations of cortical/other brain development
                     'neuro_condit___1' : 1, #Ischemic Stroke
                     'neuro_condit___4' : 1}, #Primary brain tumor (benign)
                4 : {'childhood_syndromes___8' : 1, #Lennox-Gastaut Syndrome
                     'childhood_syndromes___9' : 1, #ESES
                     'childhood_syndromes___10' : 1, #Landau-Kleffner Syndrome
                     'neonatal_syndromes' : 3, #Ohtahara Syndrome
                     'infancy_syndromes' : [2,6]}   }, #West Syndrome, Dravet Syndrome
                
        'pheno_iddx' : {
                1 : {'intelletual_ability' : [4,5,6,7]}, #Codes 1 - 4
                0 : {'intelletual_ability' : [1,2,3]}  }, #Codes 5 - 7
                
        'pheno_id_level' : {
                1 : {'intelletual_ability' : 4}, #Code 4
                2 : {'intelletual_ability' : 5}, #Code 3
                3 : {'intelletual_ability' : 6}, #Code 2
                4 : {'intelletual_ability' : 7}, #Code 1
                7 : {'intelletual_ability' : 99}   }, #Unknown

        'pheno_ddtype' : {
                1 : {'verbal_nonverbal' : 3}, #Verbally Delayed
                2 : {'motor___1' : 1}  },   #Motor Delay
                
        'pheno_devregr' : {
                1 : {'dev_reg' : 1}, #Yes
                0 : {'dev_reg' : 0}   }, #No (Varies from norm for NYU Codebook)
                
        'pheno_verbdel' : {
                1 : {'verbal_nonverbal' : 3}, #Verbally Delayed
                0 : {'verbal_nonverbal' : 1}, #Verbal
                '' : {'verbal_nonverbal' : [2,99]}    }, #Non-Verbal, Unknown
        
        'pheno_nonverb' : {
                1 : {'verbal_nonverbal' : 2}, #Non-Verbal
                0 : {'verbal_nonverbal' : 1}, #Verbal
                '' : {'verbal_nonverbal' : [3,99]}   }, #Verbally Delayed, Unkknown
            
        'pheno_motor' : {
                1 : {'motor___1' : 1, #Motor Delay
                     'motor___2' : 1, #Hypotonia
                     'motor___3' : 1}, #Catatonia
                0 : {'motor___99' : 1}   }, #None  
        
        'pheno_motor_list' : {
                1 : {'motor___1' : 1}, #Motor Delay
                2 : {'motor___2' : 1}, #Hypotonia
                3 : {'motor___3' : 1}, #Catatonia
                100 : {'motor___98' : 1}}, #Other
                
        'pheno_hasmri' : {
                1 : {'mri' : 1}, #Yes
                0 : {'mri' : 2}   }, #No
                
        'pheno_mrires' : {
                0 : {'mri_normality' : 1}, #Normal
                1 : {'mri_normality' : 2}   }, #Abnormal
                
        'pheno_mrilat' : {
                1 : {'mrilat' : 1}, #Left
                2 : {'mrilat' : 2}, #Right
                3 : {'mrilat' : 3}, #Bilateral
                4 : {'mrilat' : 4}   }, #Unclear/Unspecified
                
        'pheno_mricortloc' : {
                1 : {'mricortloc___1' : 1}, #Frontal polar
                2 : {'mricortloc___2' : 1}, #Mesial Occipital
                3 : {'mricortloc___3' : 1}, #Mesial Frontal
                4 : {'mricortloc___4' : 1}, #Lateral Occipital
                5 : {'mricortloc___5' : 1}, #Dorsal Lateral Frontal
                6 : {'mricortloc___6' : 1}, #Basal Occipital
                7 : {'mricortloc___7' : 1}, #Orbital Frontal
                8 : {'mricortloc___8' : 1}, #Temporal Polar
                9 : {'mricortloc___9' : 1}, #Mesial Parietal
                10 : {'mricortloc___10' : 1}, #Mesial Temporal
                11 : {'mricortloc___11' : 1}, #Insula
                12 : {'mricortloc___12' : 1}, #Lateral Temporal
                13 : {'mricortloc___13' : 1}, #Dorsal Lateral Parietal
                99 : {'mricortloc___99' : 1}   }, #Unclear/Unspecified
                
        'pheno_mrisubcortloc' : {
                1 : {'mrisubcortloc___1' : 1}, #Periventricular
                2 : {'mrisubcortloc___2' : 1}, #Grey-White Matter Junction
                3 : {'mrisubcortloc___3' : 1}, #White matter - Other
                4 : {'mrisubcortloc___4' : 1}, #Callosum
                5 : {'mrisubcortloc___5' : 1}, #Thalamus
                6 : {'mrisubcortloc___6' : 1}, #Basal Ganglia
                99 : {'mrisubcortloc___99' : 1}   }, #Unclear/Unspecified
                
        'pheno_mrifeats' : {
                1 : {'mrifeats___1' : 1}, #Dysgenesis
                2 : {'mrifeats___2' : 1}, #Agenesis
                3 : {'mrifeats___3' : 1}, ##Hypoplasia
                4 : {'mrifeats___4' : 1}, #Hyperplasia
                5 : {'mrifeats___5' : 1}, #Atrophy
                6 : {'mrifeats___6' : 1}, #Hypertrophy
                7 : {'mrifeats___7' : 1}, #Cortical Thickening
                8 : {'mrifeats___8' : 1}, #Cortical Thinning
                9 : {'mrifeats___9' : 1}, #Heterotopic Tissue vs/ Migration Abnormality
                10 : {'mrifeats___10' : 1}, #Decreased Grey-White Matter
                11 : {'mrifeats___11' : 1}, #Overgrowth in Cortical White Matter
                12 : {'mrifeats___12' : 1}, #Maliform-Related White Matter Signal Abnormality
                13 : {'mrifeats___13' : 1}, #Abnormal Patterns of Growth
                14 : {'mrifeats___14' : 1}, #Loss of architecture (Specific to Hippocampus)
                15 : {'mrifeats___15' : 1}, #Cystic (Including Multicystic)
                99 : {'mrifeats___99' : 1}   }, #Unclear/Unspecified
                
        'pheno_haseeg' : {
                1 : {'eegformat___1' : 1}, #Report (Yes)
                0 : {'eegformat___1' : 0}  }, #Report (No)
        
        'pheno_eegres' : {
                0 : {'interict_abnormalities' : 2}, #No
                1 : {'interict_abnormalities' : 1}   }, #Yes
                
        'pheno_comorbid_psych_list' : {
                1 : {'psychcondit___6' : 1}, #Depression
                10 : {'psychcondit___5' : 1}, #ADD/ADHD
                15 : {'psychcondit___1' : 1}, #Anxiety
                20 : {'psychcondit___4' : 1}, #OCD
                25 : {'compulsive___99' : 0}, #None (No)
                30 : {'psychcondit___3' : 1}, #Schizophrenia
                35 : {'psychcondit___2' : 1}, #Bipolar
                100 : {'psychcondit___99' : 1}  }, #Other
        
        'pheno_comorbid_neuro_list' : {
                10 : {'neuro_condit___1' : 1}, #Ischemic Stroke
                15 : {'neuro_condit___2' : 1}, #Aneurysm
                20 : {'neuro_condit___3' : 1, #Primary Brain Tumor (Malignant)
                        'neuro_condit___4' : 1}, #Primary Brain Tumor (Benign)
                100 : {'neuro_condit___99' : 1}   }, #Other
        
        'pheno_comorbid_nonpsych_list' : {
                1 : {'comorbidity_history___2' : 1}, #Sleep Disorder
                15 : {'comorbidity_history___5' : 1}   }, #GI Disorder
        
        'pheno_prevgentest' : {
                1 : {'genetic_test_perf' : 1}, #Yes
                0 : {'genetic_test_perf' : 2}, #No
                '' : {'genetic_test_perf' : 3}   }, #Unknown

        'pheno_seiz_onset' : {
                1 : {'major_seizure_type' : 3}, #Partial
                2 : {'major_seizure_type' : [1,2]}, #Generalized, Symptomatic Generalized
                3 : {'major_seizure_type' : 99}  }, #Unknown
                
                
        'pheno_familyhx_asd_nucext' : {
                1 : {'motherhist___2' : 1, #History of Autism
                       'fatherhist___2' : 1, #History of Autism
                       'sib1hist___2' : 1, #History of Autism
                       'sib2hist___2' : 1, #History of Autism
                       'sib3hist___2' : 1, #History of Autism
                       'sib4hist___2' : 1, #History of Autism
                       'sib5hist___2' : 1}, #History of Autism
                2 : {'matgrandmahist___2' : 1, #History of Autism
                     'matgrandpahist___2' : 1}   }, #History of Autism
                
        'pheno_familyhx_asd_nuc_det' : {
                1 : {'motherhist___2' : 1},
                2 : {'fatherhist___2' : 1}  },
             
        'pheno_familyhx_epi_nucext' : {
                1 : {'motherhist___1' : 1, #History of Epilepsy
                       'fatherhist___1' : 1, #History of Epilepsy
                       'sib1hist___1' : 1, #History of Epilepsy
                       'sib2hist___1' : 1, #History of Epilepsy
                       'sib3hist___1' : 1, #History of Epilepsy
                       'sib4hist___1' : 1, #History of Epilepsy
                       'sib5hist___1' : 1}, #History of Epilepsy
                2 : {'matgrandmahist___1' : 1, #History of Epilepsy
                     'matgrandpahist___1' : 1}   }, #History of Epilepsy
                   
        'pheno_familyhx_epi_nuc_det' : {
                1 : {'motherhist___1' : 1},
                2 : {'fatherhist___1' : 1}   },               

        }
      
MSSM = {
        'pheno_asddx' : 'yesno',
        'pheno_asdaod_mo' : 'age_autism',
        'pheno_asdaod_approx' : 'age_autism',
        'pheno_epidx' : 'radio',
        'pheno_epitype' : 'checkbox',
        'pheno_epiaos_mo' : 'age_epil_onset',
        'pheno_epiaos_approx' : 'age_epil_onset',
        'pheno_iddx' : 'yesno',
        'pheno_id_level' : 'radio',
        'pheno_ddtype' : 'checkbox',
        'pheno_devregr' : 'yesno',
        'pheno_verbdel' : 'yesno',
        'pheno_nonverb' : 'yesno',
        'pheno_nonverb_words' : 'ever_firstword',
        'pheno_motor' : 'yesno',
        'pheno_motor_list' : 'checkbox',
        'pheno_hasmri' : 'yesno',
        'pheno_mrires' : 'radio',
        'pheno_mrires_abn_descr' : 'mri_abnorm_descrip',
        'pheno_mrilat' : 'radio',
        'pheno_mricortloc' : 'checkbox',
        'pheno_mrisubcortloc' : 'checkbox',
        'pheno_mrifeats' : 'checkbox',
        'pheno_haseeg' : 'yesno',
        'pheno_eegres' : 'radio',
        'pheno_comorbid_psych_list' : 'checkbox',
        'pheno_comorbid_neuro_list' : 'checkbox',
        'pheno_comorbid_nonpsych_list' : 'checkbox',
        'pheno_prevgentest' : 'yesno',
        'pheno_genmut' : 'specifyetiology',
        'pheno_genmut_mut_other' : 'gen_test_results',
        'pheno_seiz_onset' : 'checkbox',
        'pheno_familyhx_asd_nucext' : 'checkbox',
        'pheno_familyhx_asd_nuc_det' : 'checkbox',
        'pheno_familyhx_epi_nucext' : 'checkbox',
        'pheno_familyhx_epi_nuc_det' : 'checkbox',
        
        }        
