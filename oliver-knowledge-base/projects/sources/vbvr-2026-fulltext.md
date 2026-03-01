---
title: "A Very Big Video Reasoning Suite (Raw Fulltext Extract)"
type: "project-source"
timeline:
  start: "2026-03"
  end: "2026-03"
  period: "grad_and_career"
tags: ["vbvr", "video-reasoning", "research", "raw-text"]
domains: ["source-documents"]
status: "archived"
importance: 3
created: 2026-03-01
updated: 2026-03-01
related: []
---

## Note
This file stores raw OCR/text extraction from the original PDF for retrieval purposes.
Formatting artifacts may exist due to PDF layout extraction.

## Extracted Text

## PAGE 1

VIDEO-REASON.COM
A Very Big Video Reasoning Suite
MaijunxianWang*1 RuisiWang*2 JuyiLin*3 RanJi*4 Thadda¨usWiedemer5 QingyingGao6
DezhiLuo7 YaoyaoQian3 LianyuHuang8 ZelongHong9 JiahuiGe8 QianliMa10 HangHe11
YifanZhou10 LingziGuo12 LantaoMei12 JiachenLi13 HanwenXing8 TianqiZhao14
FengyuanYu2 WeihangXiao15 YizhengJiao16 JianhengHou8 DanyangZhang17
PengchengXu18 BoyangZhong19 ZehongZhao4 GaoyunFang20 JohnKitaoka21 YileXu22
HuaXu23 KentonBlacutt24 TinNguyen25 SiyuanSong13 HaoranSun6 ShaoyueWen20
LinyangHe26 RunmingWang6 YanzhiWang3 MengyueYang27 ZiqiaoMa7 Raphae¨lMillie`re28
FredaShi29 NunoVasconcelos4 DanielKhashabi6 AlanYuille6 YilunDu30 ZimingLiu12
BoLi2 DahuaLin31 ZiweiLiu2 VikashKumar32 YijiangLi4 LeiYang31
ZhongangCai2† HokinDeng32†
1UniversityofCalifornia,Berkeley 2NanyangTechnologicalUniversity 3NortheasternUniversity 4Universityof
California,SanDiego 5UniversityofTu¨bingen 6JohnsHopkinsUniversity 7UniversityofMichigan 8Universityof
SouthernCalifornia 9WashingtonUniversityinSt.Louis 10ShanghaiJiaoTongUniversity 11EastChinaNormal
University 12StanfordUniversity 13UniversityofTexasatAustin 14UniversityofCalifornia,LosAngeles 15Cornell
University 16UniversityofNorthCarolinaatChapelHill 17SanJoseStateUniversity 18UniversityofCalifornia,
Irvine 19TechnicalUniversityofMunich 20ImperialCollegeLondon 21UniversityofWisconsin–Madison 22University
ofEdinburgh 23HongKongUniversityofScienceandTechnology 24NewYorkUniversity 25Auburn
University 26ColumbiaUniversity 27UniversityofBristol 28UniversityofOxford 29Universityof
Waterloo 30Harvard 31TheChineseUniversityofHongKong 32CarnegieMellonUniversity *Equalcontribution.
†Correspondenceto:HokinDeng<hokind@andrew.cmu.edu>,ZhongangCai<caiz0023@e.ntu.edu.sg>.
Figure1 OverviewofVBVR.Left: thegridshowsrepresentativetasksspanningourcognitivearchitecture,
whicharecolor-codedaccordingtotheirunderlyingcapability: Spatiality,Transformation,Knowledge,
Abstraction,andPerception. Atthecenterofthegrids,wevisualizethescalecomparisonbetweenVBVR
(2.015Msamples)andnineotherdatasetscombined(12.8Ksamples): thesizesofthecirclesaredrawnto
scale. Top-right: scalingbehavioronin-domainandout-of-domainevaluations. Bottom-right: benchmark
performanceacrossfivecognitivecapabilities.
0.974
0.763
0.601
In Domain
Out of Domain
Human
VBVR-Wan Training Data
Nine Existing
Datasets Combined Abstraction
12.8 K (0.63% of VBVR)
The sizes of the circles are
drawn to scale*
Very Big Video Reasoning Perception Knowledge
samples
Spatiality Transformation
1
6202
beF
32
]VC.sc[
1v95102.2062:viXra
erocS
tiKlavE
naW-RVBV


## PAGE 2

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
ABSTRACT
Rapidprogressinvideomodelshaslargelyfocusedonvisualquality,leavingtheirreasoningcapa-
bilitiesunderexplored. Videoreasoninggroundsintelligenceinspatiotemporallyconsistentvisual
environments that go beyond what text can naturally capture, enabling intuitive reasoning over
spatiotemporalstructure, suchascontinuity, interaction, andcausality. However, systematically
studying video reasoning and its scaling behavior is hindered by the lack of large-scale video
reasoningtrainingdata. Toaddressthisgap,weintroducetheVeryBigVideoReasoning(VBVR)
Dataset,anunprecedentedlylarge-scaleresourcespanning200curatedreasoningtasksfollowinga
principledtaxonomy,andoveronemillionvideoclips—approximatelythreeordersofmagnitude
largerthanexistingdatasets. WefurtherpresentVBVR-Bench,averifiableevaluationframework
thatmovesbeyondmodel-basedjudgingbyincorporatingrule-based,human-alignedscorers,en-
abling reproducible and interpretable diagnosis of video reasoning capabilities. Leveraging the
VBVRsuite,weconductoneofthefirstlarge-scalescalingstudiesofvideoreasoningandobserve
earlysignsofemergentgeneralizationtounseenreasoningtasks. Together,VBVRlaysafoundation
forthenextstageofresearchingeneralizablevideoreasoning. Thedata,benchmarktoolkit,and
modelsarereleasedpubliclyatvideo-reason.com.
1.Introduction
Ground-breaking progress has been achieved in large language models, whose reasoning abilities now
generalizeacrosschallengingtaskssuchascoding,mathematics,andscientificdiscovery(Mitchell,2025;
Rapaport,2026). However,suchcapabilitiesremainlargelyconfinedtotext-basedscenarios. Meanwhile,
recentadvancesinvideogenerationmodelshavepredominantlyemphasizedvisualrealism,withcomparatively
limitedfocusonreasoningcapabilities. Yetvideomodelsholdthepotentialtosupportanewparadigmof
reasoning(Wiedemeretal.,2025),groundedinspatiotemporallyconsistentvisualenvironmentswherespatial
structure,physicaldynamics,andlong-rangecausalityarenaturallyencoded. Thismakesvideoframesan
ideal substrate for studying reasoning grounded in the physical world. Despite this promise and growing
interest in video reasoning, the community still lacks several critical components required for systematic
progress:(1)alarge-scaleanddiversedatasettoenablemeaningfulinvestigationofscalingandgeneralization,
(2)anevaluationtoolkitbuiltonverifiableandreproducibleprinciples,and(3)aninitialscalingstudythat
examinesemergentcapabilitiesinvideoreasoningmodels. Inthiswork,weaddressallthreechallengesby
introducingtheVeryBigVideoReasoning(VBVR)suite.
First,weintroduceVBVR-Dataset,alarge-scaleanddiversetrainingsourcedesignedtofacilitatesystematic
studyofvideoreasoning. Weadoptaprincipledapproach,groundingourtasktaxonomyinwell-established
theoriesofhumancognitivearchitecture(Newell&Simon,1972;Anderson,2007). Specifically,weorga-
nizecorevisualreasoningcapabilitiesintofivepillars: abstraction,knowledge,spatiality,perception,and
transformation. The dataset is the result of a community-oriented, collaborative effort involving over 50
researchersandengineersfromdiversedisciplinesworldwide,ensuringbroadcoverageandstrongdomain
expertiseacross200taskstodate. Contributorsaregivenfullfreedomtodesignthecoretasksemanticsand
reasoningprocedures,allowingformaximaldiversity,whileaunified,overarchingtasktemplateisappliedas
astandardizedwrapperforinputandoutputspecification. Thisseparationensuresconsistencyforautomated
scalingwithoutconstrainingtaskcreativity. Alltasksundergoexperthumaninspectiontoensurequalityand
correctnessbeforebeingprocessedbyourautomated,cloud-basedpipeline,whichgenerateslargevolumesof
randomizedtrainingexamplesinadistributedmanner. Intotal,VBVR-Datasetcontains2,015,000images
and1,007,500videoclips,makingitapproximately1,000×largerthanexistingalternatives. Importantly,the
pipelineisimmediatelycompatiblewithnewlyaddedtasksandsupportsscalablegenerationofadditional
examplespertask,enablingcontinuousexpansioninbothdatasetbreadthandscale.
Second,VBVR-Benchprovidesasystematic,reproducible,andexplainableevaluationframeworkforvideo
reasoningmodels.WhileVLM-as-a-judgeparadigmshavebeenwidelyadoptedforevaluatingvideogeneration
models (Peng et al., 2025), we explicitly enforce the use of verifiable, rule-based scorers to ensure that
2


## PAGE 3

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
Table1 ComparisonofVBVR-Datasetwithexistingvideoreasoningbenchmarks. VBVR-Datasetsurpasses
allpriorbenchmarksbymultipleordersofmagnitudeacrosseverydimensionandis,toourknowledge,the
firsttoprovidelarge-scaletrainingdataforvideoreasoning.
Dataset #Task #Images #Videos #Train #Test
Video-Zero-Shot(Wiedemeretal.,2025) 69 1,578 0 0 2,128
V-ReasonBench(Luoetal.,2025c) 13 652 0 0 326
MMGR(Caietal.,2025) 10 1,323 530 0 1,853
VideoThinkBench(Tongetal.,2025) 24 8,298 0 0 4,149
TiViBench(Chenetal.,2025) 24 595 0 0 595
VR-Bench(Yangetal.,2025a) 5 0 7,920 6,336 1,538
MME-CoF(Guoetal.,2025) 12 120 0 0 120
Gen-ViRe(Liuetal.,2025) 24 117 0 0 72
Ruler-Bench(Heetal.,2025) 40 101 0 0 622
VBVR-Dataset 200 2,015,000 1,007,500 1,000,000 7,500
Table2 Foundationalfacultiesofahumanmind. One-sentencedefinitionsareprovided. Thecomprehensive
setofphilosophicaljustificationsandempiricalsupportsforeachfacultyareavailableinApp.A.
Faculty Definition
Abstraction Tofindrulesfromobservationsanduserulestodeduceresults.
Knowledge Propositionaltruthstatementsonecouldutter,eitherlearnedorgiftedsincebirth.
Perception Immediateaccesstosensedatum,nofurtherjustificationcouldbeprovided,i.e.”Hereisonehand”
Spatiality Theintuitionofthebasicpropertiesofourworld,suchasthree-dimensionalityandEuclidean-ness.
Transformation Tosimulatespatial-temporalcontinuitieswithinternalmodelsinone’smind
evaluationoutcomesareclearlydefinedandfullyreproducible. Tovalidatethatthesetask-specificscorers
faithfullyreflectmodelcapabilities,weconducthumanpreferencealignmentexperiments,observingstrong
agreementbetweenautomatedscoresandhumanjudgments, withaSpearman’scorrelationcoefficientof
ρ>0.9. LeveragingVBVR-Bench,webenchmarkleadingproprietarymodels: Veo3.1(GoogleDeepMind,
2026),Sora2(OpenAI,2025),Kling2.6(KuaishouTechnology,2025),andRunwayGen-4(RunwayResearch,
2025), alongside representative open-source models, including Wan-2.2 (WanTeam, 2025), CogVideoX-
1.5(Yangetal.,2024),HuanyuanVideo(Kongetal.,2024),andLTX-2(HaCohenetal.,2026). Wereveala
substantialgapinvideoreasoningcapabilitiesacrosssystems;thestrongestmodelstillfallsshortofhuman
performance by a large margin. Moreover, we use VBVR to analyze how different cognitive capabilities
co-developacrossmodels,revealingnon-trivialdependenciesandtrade-offsbetweenreasoningskills.
Third, with a large-scale dataset and a reliable evaluation benchmark in place, we conduct an in-depth
investigationofscalingeffectsinvideogenerationmodels. UsingWan-2.2asthebasemodel,weobserve
concurrentperformanceimprovementsonbothin-domain(ID)andout-of-domain(OOD)tasksastraining
scale increases, indicating the gradual emergence of generalization capabilities. Beyond these gains, our
analysisyieldsseveralkeyinsights. First,performanceonbothIDandOODtaskseventuallyplateausasdata
scaleincreases,leavingapersistentgapbetweenmodelandhumanperformancethatcannotbebridgedbydata
scalingalone. Thissuggestsfundamentallimitationsincurrentvideogenerationarchitectureswhenapplied
tovideoreasoning. Second,althoughOODperformanceimprovessubstantiallywithscale,aconsistentgap
remainsbetweenIDandOODsettings; narrowingthisgapappearsessentialforrobust,in-the-wildvideo
reasoningandgeneration. Finally,qualitativeanalysesrevealemergentbehaviorsininstructionfollowing,
controlledediting,andsemanticunderstandingwithincreasedmodelscale,whilealsoexposingimportant
limitationsthatmotivatefutureresearch.
Insummary,wepresenttheVBVRsuite,centeredonanunprecedentedlylarge-scaleandcontinuallygrowing
datasetforvideoreasoning, VBVR-Dataset, togetherwithaverifiable, human-alignedevaluationtoolkit,
VBVR-Bench. Leveragingthissuite,weconductoneofthefirstsystematicscalingstudiesofvideoreasoning
modelsanduncoverearly,encouragingevidenceofemergentgeneralization. WebelieveVBVRprovidesa
foundationalinfrastructureforfutureresearchtowardgeneralizablevideoreasoning.
3


## PAGE 4

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
2.RelatedWorks
Sincetheinaugurationofdiffusionmodelsandtransformer-basedscaling(Hoetal.,2020;Peebles&Xie,
2023),videogenerationmodelsarerapidlyproliferating,withclosedmodelssuchasSora,MovieGen,and
Veo,andopen-sourceoneslikeCogVideoX,HunyuanVideo,andWan(OpenAI,2025;Polyaketal.,2024;
Google DeepMind, 2026; Yang et al., 2024; Kong et al., 2024; WanTeam, 2025). But many models are
optimizedforcreativeproductionratherthanexplicitrelational,causal,orcounterfactualreasoning(Peebles
& Xie, 2023; Yang et al., 2024; Zheng et al., 2024). growing body of work treats video generation not
onlyasacontent-creationtool,butasareasoningsubstrate(Tongetal.,2025;Guoetal.,2025;Liuetal.,
2025;Wiedemeretal.,2025). AworkhastestedVeo-3andshownearlyevidencethatthemodelexhibits
nontrivialzero-shotperceptualandmanipulationbehaviorsandcansolvesimpletaskswithouttask-specific
training(Wiedemeretal.,2025). Laterworksnowspangeneration-as-reasoningparadigms(Tongetal.,2025),
multi-stepChain-of-Framediagnosis(Guoetal.,2025;Liuetal.,2025),TI2Vanswersuites(Luoetal.,2025c;
Chenetal.,2025),amongothers(Heetal.,2025;Yangetal.,2025a;Caietal.,2025).
Despitesharpermeasurement,muchoftheecosystemremainsevaluation-heavy: standardized,large-scale
trainingsplitsandcontrolledablationprotocolsaremissing,makingitdifficulttorunreproduciblescaling
studiesthatdirectlyoptimizeforreasoningcorrectness. Thismotivatesdatasetsthataredesignednotonly
totestvideoreasoning,buttosupporttrainingforreasoningatscaleunderconsistentdomaincoverageand
reliablesupervisionsignals.
3.Dataset
Inthissection,wedescribethecognitivearchitectureunderlyingoursystematictaskdesign(Sec.3.1),present
thekeystatisticsofVBVR-Dataset(Sec.3.2),anddetailthedatagenerationpipeline(Sec.3.3).
3.1.CognitiveArchitecture
Aristotletreatedcognitionasanorganizedhierarchyofdunameis,cognitivefaculties,ascendingfromaistheˆsis,
perception,throughphantasia,imagination,andmne¯me¯,memory,tonouˆs,understanding,culminatinginthe
extractionofkatholou,knowledge,fromempeiria,experience(Aristotle,1984g;b). Kantfurtherarguedthe
mindstructuresexperiencethroughaprioriintuitionsandcategories,aggregatingbyEinbildungskraft(Kant,
1781). Synthesizingfromtwomillenniaofphilosophicalinquiryandrecentcognitiveandneuralsciences,we
organizeVBVRaroundfivefoundationalcognitivefaculties. Perceptionreferstotheextractionofstructured
representationsfromsensoryinput,whatAristotlecalledreceiving“formwithoutmatter”,where,forexample,
we test edge detection, color, and shape perception, discrimination (Aristotle, 1984g; Hubel & Wiesel,
1962;DiCarloetal.,2012). Transformationisthemanipulationandsynthesisofmentalrepresentations,
correspondingtoAristotle’sphantasiaandKant’sEinbildungskraft,whereweusecaseslikementalrotationto
test(Shepard&Metzler,1971;Zacks,2008). Spatialityistherepresentationofplacesandtheirgeometric
relationshipsinourworld. Kantidentifiedspaceasanaprioriformofintuitionprerequisitetoperception
itself,andweusecaseslikenavigationtoprobethisability(Kant,1781;O’Keefe&Dostrovsky,1971;Hafting
etal.,2005). Abstractionisthedistillationofgeneralizableknowledgefromparticularexperiences,Aristotle’s
katholouextractedbynouˆs,Kant’stranscendentalideasgeneratedbyVernunft,andweusecaseslikeRaven’s
Matricestotest(Aristotle,1984b;Kant,1781;Carey,2009;Badre&Nee,2018). Knowledge,asAristotle
hasreferred,isthetelosofhumanlife. Throughthefacultiesofourmind,humansaccumulateandrefine
knowledgeovertime. Thisknowledgemaybeintrinsic,thatis,foundationalorcoreknowledgeweareborn
with,orlearned(Aristotle,1984c;b;d;e;Spelke,2000;Lietal.,2025). Tooperationalizethesefacultiesina
video-basedreasoningsetting,VBVRimplementseachcategoryasafamilyofparameterizedtaskgenerators.
Representative task instances for each faculty are illustrated in Fig. 2. Full philosophical grounding and
neuroscientificevidenceforeachfacultyappearinSec.A.
4


## PAGE 5

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
Figure 2 Sample task instances generated from the VBVR parameterized task suite, organized by five
cognitivefaculties. Eachsequenceillustratesthestructuredreasoningprocessrequiredtoreachavalidsolution.
Tasksareimplementedasdeterministicgeneratorssupportingscalableinstancevariationwhilepreserving
visual clarity and video dependency. Each row corresponds to a faculty defined in Section 3.1: abstract
cognitiveconstructsareinstantiatedasexecutable,verifiablevideo-basedreasoningtasks.
3.2.DataStatistics
Table1comparesVBVR-Datasetwithexistingvideoreasoningbenchmarks. VBVR-Datasetsurpassesprior
work by multiple orders of magnitude across all key dimensions. Notably, most existing video reasoning
benchmarksprovidefewornovideosamples(oftenlackingtrainingdataaltogether),whichhasbeenamajor
bottleneck for studying scaling. In total, VBVR-Dataset comprises 200 tasks: 150 tasks will be publicly
released,whiletheremaining50tasksarereservedasahiddensetforfutureleaderboardevaluationtopreserve
benchmarkintegrity.
5


## PAGE 6

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
Figure3 Taskdesignsgroundedincognitivearchitectureareimplementedasparameterizedgenerators,then
executedatscaleviadistributedLambdaworkerswritingtocentralizedS3storage.
Foundations
Cognitive Tasks
Architecture Cloud-based Message
Task Design FIFO Queue
Abstraction
Perception
Spatiality Task Review
Transformation
Knowledge
λ λ λ λ .... λ Generator
Generator Implementation
Generator Generator Generator Generator Generator
Worker 1 Worker 2 Worker 3 Worker 4 Worker n
Generator
Generator Review
Template
S3 Storage
3.3.DataCuration
Thecurationprocessfollowsathree-stagepipeline: (1)taskdesignandapproval,(2)task-specificgenerator
implementation,and(3)large-scaledistributedgenerationwithqualitycontrol. Eachstageproduceswell-
definedoutputsfordownstreamprocessing.
3.3.1.TaskDesignandApproval
Each task is designed to probe a specific video-based reasoning capability from the taxonomy defined
inSec.3.1. Ratherthanrelyingonimplicitorpost-hoctaskdefinitions,VBVRexplicitlyconstrainsthetask
spacethroughaunifiedsetofqualitystandards.
All task proposals are evaluated against six criteria: (1) Information sufficiency, requiring all necessary
reasoning cues to be present in the first frame and the prompt; (2) Deterministic solvability, ensuring a
uniqueandverifiablesuccesscriterion;(3)Videodependency,suchthatthetaskcannotbesolvedfroma
singlestaticimagebutthroughaprocess;(4)Visualclarity,ensuringallvisualelementsaredistinguishable
with unambiguous layouts; (5) Parametric diversity, supporting the generation of at least 10,000 non-
trivialinstances;(6)Technicalfeasibility,avoidingunsolvableorpathologicalconfigurationsunderstandard
renderingpipelines.
Taskproposalsaresubmittedbyinternalcontributorsandtheopen-sourcecommunity. Eachproposalspecifies
thereasoningobjective,expectedinput–outputstructure,andparameterspace. Proposalsundergoadesign
reviewprocessconductedbydesignatedreviewers,whoassesscognitivevalidity,verifiability,andscalability.
Throughthisrigorousreviewprocess,slightlymorethan200taskdesignshavealreadybeenapprovedfrom
over500initialproposals. Onlyapprovedtasksproceedtoimplementation.
3.3.2.Task-SpecificGeneratorImplementation
The second stage implements approved designs as executable generators. Each approved task design is
implementedasatask-specificparameterizedgenerator. Forexample,agridnavigationgeneratorproduces
diversetaskinstancesbyspecifyingdifferentgridsizes,obstacleplacements,andstart/endpositions. Foreach
configuration,italgorithmicallycomputesthesolutionandgeneratesboththetaskandground-truthoutputs.
Toensureconsistencyacrosstasks,VBVRoffersastandardizedgeneratortemplatethatdefinesinterfaces,
outputformats,andvalidationhooks.
Eachgeneratordeterministicallyproducesafour-componentoutput: (1)first frame.png(initialstate),
6
srotareneG
+002


## PAGE 7

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
Table3 BenchmarkingresultsonVBVR-Bench. OverallIn-Domain(ID)andOut-of-Domain(OOD)scores
arereportedalongsidecategory-wiseperformance. Higherisbetter. Bold: bestingroup;underline: second
best.
In-DomainbyCategory Out-of-DomainbyCategory
Models Overall Avg. Abst. Know. Perc. Spat. Trans. Avg. Abst. Know. Perc. Spat. Trans.
Human 0.974 0.960 0.919 0.956 1.00 0.95 1.00 0.988 1.00 1.00 0.990 1.00 0.970
Open-sourceModels
CogVideoX1.5-5B-I2V(Yangetal.,2024) 0.273 0.283 0.241 0.328 0.257 0.328 0.305 0.262 0.281 0.235 0.250 0.254 0.282
HunyuanVideo-I2V(Kongetal.,2024) 0.273 0.280 0.207 0.357 0.293 0.280 0.316 0.265 0.175 0.369 0.290 0.253 0.250
Wan2.2-I2V-A14B(WanTeam,2025) 0.371 0.412 0.430 0.382 0.415 0.404 0.419 0.329 0.405 0.308 0.343 0.236 0.307
LTX-2(HaCohenetal.,2026) 0.313 0.329 0.316 0.362 0.326 0.340 0.306 0.297 0.244 0.337 0.317 0.231 0.311
ProprietaryModels
RunwayGen-4Turbo(RunwayResearch,2025) 0.403 0.392 0.396 0.409 0.429 0.341 0.363 0.414 0.515 0.429 0.419 0.327 0.373
Sora2(OpenAI,2025) 0.546 0.569 0.602 0.477 0.581 0.572 0.597 0.523 0.546 0.472 0.525 0.462 0.546
Kling2.6(KuaishouTechnology,2025) 0.369 0.408 0.465 0.323 0.375 0.347 0.519 0.330 0.528 0.135 0.272 0.356 0.359
Veo3.1(GoogleDeepMind,2026) 0.480 0.531 0.611 0.503 0.520 0.444 0.510 0.429 0.577 0.277 0.420 0.441 0.404
DataScalingStrongBaseline
VBVR-Wan2.2 0.685 0.760 0.724 0.750 0.782 0.745 0.833 0.610 0.768 0.572 0.547 0.618 0.615
(2)prompt.txt(taskinstruction),(3)final frame.png(targetstate),and(4)ground truth.mp4
(complete solution trajectory). Components (1) and (2) constitute model inputs; components (3) and (4)
provideverifiablesupervision—completereasoningpathsthatenablelearning“how”toreason,notjust“what”
theansweris.
Taskdiversityisachievedthroughstructuredparameterspacesdefinedpergenerator. Parametersvaryacross
task-relevantdimensions,includingobjectcount,spatialconfiguration,structuralcomplexity,anddifficulty
level. Generatorsemploystratifiedsamplingtoensurebalancedcoveragewithineachtask’sparameterspace.
Beforedeployment,allgeneratorsundergocodereviewtoverifyscalability,visualquality,edge-casehandling,
andreproducibilityunderfixedrandomseeds. Onlygeneratorsthatsatisfytheserequirementsareadmittedto
large-scaleproduction.
3.3.3.Large-ScaleGenerationandControl
The final stage executes validated generators at scale within a distributed generation framework. VBVR
generatesonemilliontrainingsamplesacross100trainingtasks(10,000pertask)and7500testsamplesacross
150testtasks(50pertask).Trainingandtestsplitsareconstructedusingdisjointrandomseedrangestoprevent
dataleakage. Qualitycontrolisfullyautomatedduringgeneration. Eachsampleisvalidatedfortheexistence
of a solution, visual compliance, and boundary constraints. Failed generations trigger automatic retries;
persistentfailuresareloggedforfurthergeneratorrefinement. System-levelmonitoringtracksgeneration
statisticsandvalidationfailureratesacrosstasks. Fromthe150approvedtaskdesigns,weorganize100tasks
fortrainingand100tasksfortesting,withacarefullydesigneddual-splitstrategytoassessbothin-distribution
robustnessandout-of-distributiongeneralizationinSec.4.1.
Theparameterizedinfrastructuresupportscontinuousexpansion: standardizedgeneratortemplatesenable
communitycontributorstodevelopnewtaskswhileautomatedvalidationensuresconsistentquality. This
positions VBVR as a living benchmark that evolves with the field’s understanding of video reasoning.
ImplementationdetailsandgeneratorspecificationsareprovidedinSec.B.
4.Benchmark
Inthissection,weintroducetheevaluationtoolkit(Sec.4.1)andassessitsvaliditythroughalignmentwith
humanpreferences(Sec.4.2). Wesubsequentlyreporttheperformanceofleadingvideogenerationmodels
(Sec.4.3)andinvestigatethecorrelationsamongtheirreasoningcapabilities(Sec.4.4).
7


## PAGE 8

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
4.1.EvaluationKit
Tosystematicallyassessmodelreasoningcapabilities,VBVR-Benchemploysadual-splitevaluationstrategy
across100diversetasks. Thefirstsplitcontains50tasksthatoverlapwiththetrainingcategoriesbutdiffer
inunseenparameterconfigurationsandsampleinstances,providingatestofin-domaingeneralization. The
secondsplitincludestheremaining50tasks,whichareentirelynovelandaredesignedtomeasureout-of-
domain generalization. It tests whether models can solve reasoning challenges without prior exposure to
similar structures, and thus whether they acquire transferable reasoning primitives rather than relying on
task-specificmemorization. Eachtaskconsistsoffivetestsamples,enablingstatisticallyrobustevaluation
acrossdiversereasoningscenarios.
AkeyfeatureofVBVR-Benchisitsfullyrule-basedevaluationframework,whichisfeasiblebecausemost
testtaskshaveaunique,verifiablecorrectanswer,allowinginterpretableevaluationbasedonspatialposition,
color,objectidentity,path,orlogicaloutcome. Moreover,geometric,physical,ordeductiveconstraintsare
alsoconsideredinthescoringrubrics. Eachofthe100testtasksispairedwithadedicatedevaluationrule,
withscoresonmultipleaspectstocomputeaweighted,comprehensivescore. Sub-criteriaincludespatial
accuracy,trajectorycorrectness,temporalconsistency,andlogicalvalidity.
Forexample,intheTaskG-45: KeyDoorMatching(MoreexamplesareincludedinSec.D),agreendotagent
mustfirstlocateacolor-specifiedkeyandthennavigatetothematchingdoorwithinagridmaze. Performance
isscoredacrossfourweighteddimensions: targetidentificationaccuracy(30%),pathvalidity(30%),path
efficiency(20%),andanimationquality(20%). Targetidentificationverifiesthattheagentselectsthecorrect
keyanddoorwithoutconfusingcolors,pathvalidityensurestheagentfollowsallowedpathswithoutwall
collisions,pathefficiencycomparestheactualtrajectorytotheoptimalBFSpath,andanimationqualitychecks
smoothframe-by-framemovementandpreciseobjectalignment. Afullscoreindicatesperfectioninallfour
dimensions(correctkeyanddoorselection,near-optimalpathing,andprecisespatialandtemporalalignment).
Overall,VBVR-Benchprovides:
• Reproducibility and Determinism. The evaluation is fully deterministic and avoids the stochastic
variabilityorhallucinationsassociatedwithLLM-basedjudgments.
• GranularVerifiability. Eachtaskisdecomposedintointerpretablevectors,allowingprecisemeasure-
mentofspatial,temporal,andlogicalcorrectness,evenatthepixelorobject-propertylevel.
• TransparentDiagnosis. Byexplicitlyencodingreasoningconstraints,thebenchmarkranksmodelsand
revealssystematictrade-offs,capabilitygaps,trade-offs,andcross-domainperformancetrends.
4.2.HumanPreferenceAlignmentAnalysis
ToassessalignmentbetweenVBVR-Benchandhumanperception,weconductalarge-scalehumanpreference
studyandcomparemodelwinratiosderivedfromhumanjudgmentswiththosecomputedfromVBVR-Bench’s
automaticmetrics. Specifically,humanwinratiosareobtainedfrompairwisepreferenceannotations,wherea
modelisconsideredtowinifitispreferredoveranothermodelforthesameprompt. Incontrast,VBVR-Bench
winratiosarecomputedbyrankingmodelsbytheirper-sampleautomaticscoresandcountinghowofteneach
modeloutperformsothers. AsshowninFig.4,thetwosetsofwinratiosexhibitstrongpositivecorrelations
across models, indicating that VBVR-Bench provides reliable and human-aligned performance estimates.
DetailsofthestudyareprovidedintheSec.C.2.
4.3.LeadingModelPerformances
Table3showsperformanceacrossmodelfamilies. Mostopen-sourcebaselinesclusterbetween0.27and0.31
overall,indicatinglimitedcapabilityincomplexvideoreasoning,whileWan2.2-I2V-A14Bisthestrongest
open-sourcebaselineat0.371. Proprietarymodelsperformbetteroverall,ledbySora2(0.546)andVeo3.1
(0.480),particularlyinAbstractionandTransformationcategories.
Fine-tuningWan2.2-I2V-A14BonVBVR-DatasetyieldsVBVR-Wan2.2,whichachievesanewstateoftheart
withanoverallscoreof0.685,representingan84.6%relativeimprovementoveritsbasemodel.VBVR-Wan2.2
8


## PAGE 9

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
Figure4 HumanalignmentanalysisforVBVR-Bench.OurexperimentsshowthatVBVR-Benchevaluations
inallsplitscloselymatchhumanperceptions. Ineachplot,adotrepresentsthehumanpreferencewinratio
(horizontalaxis)andVBVR-Benchevaluationwinratio(verticalaxis)foraparticularvideogenerationmodel.
Welinearlyfitastraightlinetovisualizethecorrelation,andcalculatetheSpearman’scorrelationcoefficient
(ρ)foreachdimension.
attainsthebestperformanceacrossallevaluatedcategories,withespeciallystrongresultsinSpatialityand
Perception,suggestingthatlarge-scalereasoning-orienteddatasubstantiallyenhancesintegratedworld-model
reasoningcapabilities.
Notably,despitethesegains,aconsiderablegaptohumanperformanceremains. Thishighlightsthepersistent
challengesoflong-horizontemporalreasoningandrobustsymbolicmanipulationinvideogeneration. We
furtheranalyzehowperformanceevolveswithincreasingtrainingdataunderafixedarchitecture,andhow
in-domainandout-of-domaingeneralizationbehaviorsdiffer,inSec.5.
Wealsoanalyzethestabilityandconsistencyofmodelbehaviorusingdomain-wisescoredistributionsthat
revealperformancevariabilityandratingnoiseacrossdomains(seeSec.C.3.2).
4.4.CapabilityCorrelation
Figure5 Residualizedcapabilitycorrelationamongfivefacultiesacross9models(Pearsonρ). Weregress
outamodel-levelgeneralfactor(overallstrength)tohighlightstructuraldependenciesandinter-relations.
Wefurtherstudycapabilitydependencyamongthefivecognitivefaculties,askingwhetherstrengthsinone
capabilitytendtoco-occurwithstrengthsinanotheracrossmodels. Anaivecorrelationisoftendominatedby
9


## PAGE 10

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
overallmodelstrength(i.e.,strongermodelsscorehigheronallcategories). Toisolatestructuraldependencies,
wecomputecategory-levelmeanscorespermodelandregressoutamodel-levelgeneralfactor(overallmean
score)beforemeasuringPearsoncorrelationsontheresiduals. SeeSec.C.3.1formoreimplementationdetails.
Figure 5 reveals non-trivial structures underlying the cognitive faculties. We observe a strong positive
couplingbetweenKnowledgeandSpatiality(ρ = 0.461). Thisresultisparticularlyinterestinggiventhe
pastneurosciencestudieswhichsuggesthumanbrainsusehippocampalplacecellsandgridcellstosupport
conceptlearning. Oneseminalstudysuggestspatientswithbilateralhippocampaldamagewereimpairedat
learningbothspatialandnon-spatialconfiguralassociationsinadeterministicfeedbacktask,showingonly
partial,inflexibleresiduallearning,supportingadomain-generalhippocampalroleinbindingandconfigural
learning(Kumaranetal.,2007). Thefollow-upstudyshowsahippocampus–ventromedialprefrontalcortex
circuitsupportstheemergenceofconceptualknowledgethatguideschoices,andthehippocampusisuniquely
requiredtotransferthatknowledgetoaperceptuallynovelsetting(Kumaranetal.,2009). EdwardTolman
inlastcenturyhypothesizesthatourspatialmapofthephysicalworldcouldbetransferredtobeusedasa
cognitivemap,whichisamentalrepresentation,notonlyusedforspatialnavigation,butconceptualspace
construction,andgeneralknowledgelearning(Tolman,1948;Yangetal.,2025b). Convergingevidencefrom
neuroscienceandAIarecomingintoplacestosuggestthedeepinter-relatednessbetweencognitivespatial
intrinsicsandknowledgeacquisition(Barametal.,2024;Whittingtonetal.,2025;Xiaoetal.,2025).
Incontrast,KnowledgecorrelatesstronglynegativelywithPerception(ρ=−0.757). Oneveryinteresting
debateincognitivescienceiswhetherweshouldcountcoreknowledge,whichareknowledgethatweareborn
with,asactuallyperception(Baietal.,2025). Namely,insteadofunderstandingintuitivephysicsorobject
permanenceasakindofknowledge,weshouldactuallyconsiderthemasakindofperception,whichare
actuallysupportedbyourperceptualneuralcircuits,suchasmedialtemporallobe,ratherthanourlearningand
memorycircuits,suchashippocampus(Hassabis&Maguire,2009;Martin&Barense,2023)
AbstractionshowsastrongnegativecorrelationwithTransformation(ρ=−0.641)andamoderateonewith
Spatiality(ρ=−0.481),anddonotshowanysignsofpositivecorrelationswithanyothercognitivefaculties.
Thisresultisconsistentwithourunderstandingwiththemodularityofabstractionfacultyinourbrain,namely
prefrontalcortex(Vaidya&Badre,2022;Passingham&Lau,2023;Bein&Niv,2025;Lietal.,2026)
Moreover, Perception trades off with Spatiality (ρ = −0.565) but is nearly uncorrelated with both Ab-
straction (ρ = −0.043) and Transformation (ρ = 0.057). Transformation is also nearly uncorrelated
withSpatiality(ρ=−0.050). Overall,VBVR-Benchnotonlyranksmodelsbutalsoenablesinterpretable
diagnosisofhowcapabilitiesco-developordecoupleacrosssystems.
5.VBVR-Wan2.2Analysis
We further investigate VBVR-Wan2.2 to gain insights into scaling video reasoning. We first describe the
experimentalsettings(Sec.5.1),followedbyananalysisofthescalingbehavior(Sec.5.2),comprehensive
qualitativeevaluations(Sec.5.3),andperformanceongeneralvideobenchmarks(Sec.5.4).
5.1.Experimentsettings
WeconductallexperimentsonWan2.2-I2V-A14Bwithoutarchitecturalmodifications,asthegoalofVBVR-
Wan2.2istoinvestigatedatascalingbehaviorandprovideastrongbaselinemodelforthevideoreasoning
researchcommunity. LeveragingtheVBVR-Dataset,whichtoourknowledgeconstitutesoneofthelargest
video reasoning datasets to date, enables a systematic investigation of scaling behaviors in video-based
reasoningunderafixedmodelarchitecture. Fortraining,weadoptalearningrateof1e-4andtrainforone
epochineachexperiment. WeemployLoRAadaptationontheDiTbackbone,andapplyingLoRAtothe
modulesq,k,v,o,ffn.0,ffn.2withalorarankof32.
10


## PAGE 11

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
Table4 PerformancebyDataScale(0K–500K).Bold: bestpercolumn;underline: secondbest.
In-DomainbyCategory Out-of-DomainbyCategory
Models Overall Avg. Abst. Know. Perc. Spat. Trans. Avg. Abst. Know. Perc. Spat. Trans.
0K 0.371 0.412 0.430 0.382 0.415 0.404 0.419 0.329 0.405 0.308 0.343 0.236 0.307
50K 0.549 0.576 0.527 0.584 0.537 0.642 0.654 0.522 0.596 0.584 0.507 0.482 0.490
100K 0.623 0.701 0.622 0.680 0.777 0.719 0.759 0.545 0.622 0.524 0.533 0.557 0.517
200K 0.689 0.767 0.739 0.709 0.791 0.799 0.825 0.611 0.748 0.621 0.545 0.659 0.599
300K 0.682 0.763 0.733 0.713 0.795 0.776 0.827 0.601 0.732 0.596 0.542 0.628 0.600
400K 0.682 0.771 0.744 0.744 0.793 0.753 0.848 0.593 0.742 0.592 0.532 0.605 0.588
500K 0.685 0.760 0.724 0.750 0.782 0.745 0.833 0.610 0.768 0.572 0.547 0.618 0.615
5.2.ScalingCurve
Tosystematicallyinvestigatedatascalingbehavior,weprogressivelyincreasethetrainingdatasizefrom0K
samples(theoriginalWan2.2basemodel)to500Ksamples(VBVR-Wan2.2),andreportthecorresponding
performancechangesinTab.4.
First,trainingVBVR-Wan2.2showsclearbutsaturatinggainsfromdatascaling. In-domain(ID)perfor-
manceimprovessubstantiallywithincreasedtrainingdata,risingfrom0.412atinitializationtoabout0.771at
400Ksamples,afterwhichgainsplateauandslightlyfluctuate. Thefailuretoapproachperfectaccuracy,even
withinfamiliardistributions,suggeststhatcurrentvideogenerationarchitecturesexhibitfundamentalrepresen-
tationalandoptimizationbottlenecks. Inparticular,thesetasksrequirethesimultaneoussatisfactionoflogical
constraintsandlong-termtemporalconsistency,whilethestochasticnatureofvideogenerationintroduces
cumulativerenderingnoiseandtemporaldrift. Importantly,thissaturationregimemakesVBVR-Dataseta
valuabletestbedforresearcherstoinvestigatearchitecturaladvances,suchasexplicitstatetracking,structured
reasoningmodules,orself-correctionmechanisms,undercontrolledandscalableevaluationsettings.
Second,examininggeneralizationtoout-of-domain(OOD)taskshighlightscriticalinsights. BothIDand
OODperformanceimprovewithmoredata,IDfrom0.412to0.760,andOODfrom0.329to0.610. This
indicatesthatscalingdataenhancestransferablereasoningcapabilitiesbeyondmemorizedpatterns. Our
qualitativeanalysisinSec.5.3furtherillustrateshowthemodelbenefitsfromincreasedtrainingdataand
generalizestoout-of-domaintasks,providinginterpretableinsightsintoimprovementsintemporalconsistency,
logicalreasoning,andtasktransferability. However,apersistent15%generalizationgapremains,suggesting
thatincreasingdatawithinfixedtaskdistributionsisinsufficientforrobustsystematicgeneralization.
Withourdatafactory,weplantocontinuouslyintroducenewtaskfamiliesandrichercompositionalregimes
infuturereleases,enablingbroadercoverageofreasoningpatternsandbetterclosingtheID–OODgap.
5.3.QualitativeAnalysis
WequalitativelycompareWan2.2-I2V-A14B(basemodel), VBVR-Wan2.2, andthestrongestproprietary
baselineinourstudy,Sora2. Arecurringpatternisthat,afterVBVRtraining,VBVR-Wan2.2canmatch
or even surpass Sora 2 on a broad set of tasks that require verifiable manipulations under stable scenes.
This motivates our central takeaway: controllability before reasoning. If a model freely rewrites the
scene(background/layout/objectidentity)duringgeneration,intermediatestatesbecomeunreliableandany
“reasoningaction”(delete/move/mark)isnolongerverifiable. Inpractice,thebasemodel(Wan2.2-I2V-A14B)
oftenfailsinpreciselythisway: itmaynotpreservetargetidentityorstablelayouts,therebybreakingthe
prerequisiteformanipulation-basedreasoning.
Tomakequalitativecomparisonsdirectandreproducible,weselectexamplesassame-task,same-sample
comparisonswhenevermultiplemodelsareshownonthesamecase. Importantly,therepresentativecases
inFig.6areout-of-domain(OOD)taskfamiliesheldoutfromtraining,soimprovementsreflecttransferto
noveltaskstructuresratherthanmemorization.
Controllable execution under constraints (VBVR-Wan2.2 vs Sora 2). Panel A highlights that VBVR
trainingprimarilyimprovesconstraint-following,tool-likeexecutionunderstablescenes. OnO-5Task,Sora
2introducesextra,unnecessaryoperations: afterdeletingthetargetsymbol,itfurthermerges/re-layoutsthe
remainingsymbols,violatingtheintendedminimal-editconstraintfromthetask. Incontrast,VBVR-Wan2.2
11


## PAGE 12

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
Figure6 Qualitativeoverviewonheld-outOODtaskfamilies. PanelApresentssame-task,same-sample
comparisonsbetweenVBVR-Wan2.2andSora2onthreecontrollable-executiontasks:O-5(deletethemarked
symbolwithminimalunintendedchanges),O-6(applya2Dgeometricrotationunderthetargetcue),and
O-30(rearrangeabookshelfbymovinganobjectintothedesignatedslot),withcheckmarks/crossesindicating
tasksuccess/failure. PanelBshowsVBVR-Wan2.2-onlyemergentbehaviorsonO-49(completeasymmetric
patternwithaconsistentself-chosenpolicy)andO-11(“rationalizing”: modifyingintermediateelementsto
fitaninternallyassumedtransformationnarrative). PanelCreportshonestboundariesofVBVR-Wan2.2on
G-47(long-horizonkey–doornavigation,withpossibleagentduplication/flickering)andO-21(blueprint
gapfilling,wherethevideocanbecorrectyetprocedurallyunfaithful).
A.
VBVR-Wan 2.2 Sora 2
✔ ⍻
O-5: Remove the red-bordered symbol while preserving the sequence.
✔ ✗
O-6: Rotate the shape about the marked center to match the target outline.
✔ ✗
O-30: Insert each blue book after the green cluster with the closest average height.
B. 💡 C. ✗ G-47: Agent duplication/flickering
O-49: Emergent self-chosen completion policy
💡 ✗
O-11: “Rationalizing”: Making the scene align with expectations. O-21: Correct answer,wrong method
exhibitsanemergent“doexactlywhatisasked”capability,deletingthemarkedsymbolwithoutadditional
changes. OnO-6Task,Sora2mayfailtomaintainscenecontrolandtodistinguishthetargetregionfromthe
objecttobemanipulated,leadingtoadegenerateoutcomewheretheboxandobjectrotatetogether. Incontrast,
VBVR-Wan2.2correctlyseparatesthetargetcuefromthemanipulatedobjectandperformsapivot-based
rotationthatalignswiththetaskrequirement,suggestingemergentgeometricmanipulationskillsbeyondthe
trainingtaskfamilies. OnO-30,VBVR-Wan2.2successfullyperformstherequiredconstrainedrelocation
(moving a book into the designated slot). Notably, Sora 2 can fail by producing auxiliary markings/lines
withoutexecutingtheactualobjectmanipulation,illustratingthatevenstrongproprietarymodelsmaybreak
downwhensuccessrequiresprecise,constraint-followingcontrolratherthangenericsceneediting.
Emergentstrategiesandmulti-stepbehavior(VBVR-Wan2.2). Beyondcontrolled,tool-likeexecution,
weobserveemergentstrategy-levelregularitiesandmulti-stepbehaviorsonOODtaskfamilies. OnO-49,
VBVR-Wan2.2oftenproducesarule-consistentcompletionofthemissinghalfwhileexhibitingadistinctive,
self-chosencompletionpolicy:acrosssamples,thecompletiontypicallyappearsasasmooth,coherent“fade-in”
fillratherthandiscretecell-by-celledits.Thisconsistencysuggeststhatthemodelisnotmerelymatchingstatic
templates,butistransferringcontrollableexecutionprimitivesandorganizingthemintoastablepolicyundera
12


## PAGE 13

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
newtaskstructure. OnO-11,wesometimesobservebehaviorsresembling“understand→act→adjust”. In
additiontoapplyingtheintendedtwo-steptransformationtothequeriedshape(firstchangecolor,thenmove
it),VBVR-Wan2.2maymodifyintermediateelements(e.g.,shiftingamisalignedreferenceshapetowardthe
arrowcue;arrowsaremanuallyoverlaidforvisualization),effectivelyrationalizinganinternallyassumed
transformationnarrative. Whilesuchinterventionsmayconflictwiththeground-truthreasoningtraceand
stillyieldimperfectfinalanswers,theyprovideaqualitativesignalthatthemodelismaintainingscene-level
coherenceandexecutingmulti-stepplansratherthanproducingone-shot,uncontrolledscenerewrites.
Limitationsandfailuremodes(VBVR-Wan2.2). Despiteimprovedscenecontrollability,severalchallenging
regimesremain. Weobserveprocessunfaithfulnessintaskswithexplicitproceduralgroundtruth. OnO-21
(constructionblueprint),thegoldprocedurescanscandidatepiecesone-by-one,previewseachcandidateat
thegap,marksincorrectcandidateswithacross,andstopswhenthecorrectcandidateisfoundandplaced.
Thegeneratedvideocanmimicaplausible-lookingtrial-and-errorprocesswithoutfaithfullyreflectingthe
truedecisionmechanism(“correctanswer,wrongmethod”),highlightingtheneedforstrongerprocess-level
supervision and evaluation. Finally, long-horizon control can break down in interactive tasks. On G-47,
comparedtothebasemodelthatmaymovedoors/keysdirectly,VBVR-Wan2.2betterdistinguishestheagent
fromsceneentitiesandexhibitsthecorrecthigh-levelsubgoalstructure(fetchkey→reachdoor). However,
itcanstillsufferfromcontrolfailuressuchasagentduplication/flickeringwhentraversingacoherentpath,
indicatingthatmaintainingidentityandstabledynamicsoverlonghorizonsremainsanopenproblem.
Insummary, thesequalitativeinsightsreinforceafundamentalshiftinevaluatingvideointelligence: con-
trollability is the bedrock of verifiable reasoning. Our results demonstrate that VBVR training moves
beyond generic video synthesis, instilling a ’controllability-first’ execution logic that generalizes even to
novel,out-of-domaintaskstructures. WhileVBVR-Wan2.2showsanascentabilitytocoordinatemulti-step
strategies,theremaininggapinprocessfaithfulnessandlong-termidentitystabilityhighlightsthenextfrontier.
Achievingtruevideoreasoningwillrequirenotjustlargerscale,butamovetowardmodelsthatcanmaintain
rigorouscausalandphysicalconstraintsoverextendedtemporalhorizons.
5.4.GeneralPerformanceonVBench++
Table5 ComprehensiveevaluationresultsonVBench-I2V.
Total I2V Quality Video-Text Video-Image Video-Image Subject Background Motion Dynamic Aesthetic Imaging
Model
Score Score Score CameraMotion SubjectConsist. Backgr.Consist. Consistency Consistency Smoothness Degree Quality Quality
Wan2.2-I2V-A14B 0.8816 0.9582 0.8050 0.5444 0.9752 0.9903 0.9468 0.9672 0.9832 0.5285 0.6153 0.7036
VBVR-Wan2.2 0.8835 0.9678 0.7992 0.6592 0.9804 0.9921 0.9547 0.9722 0.9852 0.4106 0.6153 0.7080
ToevaluatetheperformanceofVBVR-Wan2.2inreal-worldvideogenerationscenarios,webenchmarked
it against the Wan2.2-I2V-A14B base model using the VBench-I2V suite. As shown in the Tab. 5, After
LoRAtrainingonVBVR-Dataset,themodelmaintainsahighlevelofperformanceacrossallcoremetrics,
demonstratingthatVBVR-Wan2.2doesnotunderminethefundamentalgenerativecapabilitiesofthebase
model. Notably,weobservedasignificantincreaseinVideo-TextCameraMotionConsistency(risingfrom
0.5444to0.6592),accompaniedbyadecreaseinDynamicDegree. Thesequantitativeresultsalignclosely
withourqualitativefindings. Thatis,themodelexhibitsamorepreciseunderstandingofmotiondynamics,
effectivelydiscerningwhichregionsrequiretemporalchangeandwhichshouldremainpreserved.Thisbalance
resultsinvideosthatarebothmorestableandbetteralignedwiththeprovidedmotionprompts.
6.Conclusion
Inthiswork,wepresentVBVR-Dataset,thefirstlarge-scaleanddiversetrainingdatasetdesignedforvideo
reasoning, along with VBVR-Bench, a comprehensive evaluation toolkit for verifiable and reproducible
assessment. Throughsystematicscalingstudies,wedemonstratethatincreasingmodelscaleleadstoearly
signsofemergentgeneralizationinvideoreasoning.
13


## PAGE 14

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
References
Allison,H.E. Kant’sTranscendentalIdealism: AnInterpretationandDefense. YaleUniversityPress,New
Haven,revisedandenlargededition,2004.
Andersen,R.A.,Snyder,L.H.,Bradley,D.C.,andXing,J.Multimodalrepresentationofspaceintheposterior
parietalcortexanditsuseinplanningmovements. AnnualReviewofNeuroscience,20:303–330,1997. doi:
10.1146/annurev.neuro.20.1.303.
Anderson,J.R. RulesoftheMind. LawrenceErlbaumAssociates,Hillsdale,NJ,1993.
Anderson,J.R. HowCantheHumanMindOccurinthePhysicalUniverse? OxfordUniversityPress,2007.
Anderson,J.R. Language,memory,andthought. PsychologyPress,2013.
Anderson,J.R.andLebiere,C. TheAtomicComponentsofThought. LawrenceErlbaumAssociates,Mahwah,
NJ,1998.
Aristotle. Onmemory. InBarnes,J.(ed.),TheCompleteWorksofAristotle: TheRevisedOxfordTranslation,
volume1,pp.714–720.PrincetonUniversityPress,1984a.
Aristotle. Metaphysics. InBarnes,J.(ed.),TheCompleteWorksofAristotle: TheRevisedOxfordTranslation,
volume2,pp.1552–1728.PrincetonUniversityPress,1984b.
Aristotle. Physics,volume1. PrincetonUniversityPress,1984c.
Aristotle. PosteriorAnalytics,volume1. PrincetonUniversityPress,1984d.
Aristotle.Prioranalytics.InBarnes,J.(ed.),TheCompleteWorksofAristotle:TheRevisedOxfordTranslation,
volume1ofBollingenSeries.PrincetonUniversityPress,Princeton,NJ,1984e.
Aristotle. Senseandsensibilia. InBarnes,J.(ed.),TheCompleteWorksofAristotle: TheRevisedOxford
Translation,volume1,pp.693–713.PrincetonUniversityPress,1984f.
Aristotle. Onthesoul. InBarnes,J.(ed.),TheCompleteWorksofAristotle: TheRevisedOxfordTranslation,
volume1,pp.641–692.PrincetonUniversityPress,1984g.
Badre,D.andNee,D.E. Frontalcortexandthehierarchicalcontrolofbehavior. TrendsinCognitiveSciences,
22(2):170–188,2018.
Bai,D.,Hafri,A.,Izard,V.,Firestone,C.,andStrickland,B. “coreperception”: Re-imaginingprecocious
reasoningassophisticatedperceiving. BehavioralandBrainSciences,pp.1–75,2025.
Baillargeon,R.,Spelke,E.S.,andWasserman,S. Objectpermanenceinfive-month-oldinfants. Cognition,20
(3):191–208,1985.
Baker,N.,Lu,H.,Erlikhman,G.,andKellman,P.J. Deepconvolutionalnetworksdonotclassifybasedon
globalobjectshape. PLoSComputationalBiology, 14(12):e1006613, 2018. doi: 10.1371/journal.pcbi.
1006613.
Banino,A.,Barry,C.,Uria,B.,Blundell,C.,Lillicrap,T.,Mirowski,P.,Pritzel,A.,Chadwick,M.J.,Degris,
T., Modayil, J., Wayne, G., Soyer, H., Viola, F., Zhang, B., Goroshin, R., Rabinowitz, N., Pascanu, R.,
Beattie,C.,Petersen,S.,Sadik,A.,Gaffney,S.,King,H.,Kavukcuoglu,K.,Hassabis,D.,Hadsell,R.,and
Kumaran,D. Vector-basednavigationusinggrid-likerepresentationsinartificialagents. Nature,557(7705):
429–433,2018. doi: 10.1038/s41586-018-0102-6.
Bao,P.,She,L.,McGill,M.,Bhattacharyya,R.,andTsao,D.Y. Amapofobjectspaceinprimateinferotem-
poralcortex. Nature,583:103–108,2020. doi: 10.1038/s41586-020-2350-5.
14


## PAGE 15

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
Baram,A.,Nili,H.,Barreiros,I.,Samborska,V.,Behrens,T.E.,andGarvert,M.M. Anabstractrelational
mapemergesinthehumanmedialprefrontalcortexwithconsolidation. bioRxiv,pp.2024–10,2024.
Behrens, T. E. J., Muller, T. H., Whittington, J. C. R., Mark, S., Baram, A. B., Stachenfeld, K. L., and
Kurth-Nelson,Z. Whatisacognitivemap? Organizingknowledgeforflexiblebehavior. Neuron,100(2):
490–509,2018. doi: 10.1016/j.neuron.2018.10.002.
Bein, O. and Niv, Y. Schemas, reinforcement learning and the medial prefrontal cortex. Nature Reviews
Neuroscience,26(3):141–157,2025.
Bengio,Y.,Courville,A.,andVincent,P. Representationlearning: Areviewandnewperspectives. IEEE
TransactionsonPatternAnalysisandMachineIntelligence,35(8):1798–1828,2013.
Bertolero,M.A.,Yeo,B.T.T.,andD’Esposito,M. Themodularandintegrativefunctionalarchitectureof
thehumanbrain. ProceedingsoftheNationalAcademyofSciences,112(49):E6798–E6807,2015. doi:
10.1073/pnas.1510619112.
Bonhoeffer,T.andGrinvald,A. Iso-orientationdomainsincatvisualcortexarearrangedinpinwheel-like
patterns. Nature,353:429–431,1991.
Bowman,C.R.andZeithamova,D. Abstractmemoryrepresentationsintheventromedialprefrontalcortex
andhippocampussupportconceptgeneralization. JournalofNeuroscience,38(10):2605–2614,2018.
Brincat,S.L.,Siegel,M.,vonNicolai,C.,andMiller,E.K. Gradualprogressionfromsensorytotask-related
processingincerebralcortex. ProceedingsoftheNationalAcademyofSciences,115(30):E7202–E7211,
2018.
Burgess,P.W.,Dumontheil,I.,andGilbert,S.J. Thegatewayhypothesisofrostralprefrontalcortex(area10)
function. TrendsinCognitiveSciences,11(7):290–298,2007.
Cai,Z.,Qiu,H.,Ma,T.,Zhao,H.,Zhou,G.,Huang,K.-H.,Kordjamshidi,P.,Zhang,M.,Xiao,W.,Gu,J.,
Peng,N.,andHu,J. MMGR:Multi-modalgenerativereasoning. arXivpreprintarXiv:2512.14691,2025.
URLhttps://arxiv.org/abs/2512.14691.
Calvert,G.A. Crossmodalprocessinginthehumanbrain: Insightsfromfunctionalneuroimagingstudies.
CerebralCortex,11(12):1110–1123,2001.
Carey,S. TheOriginofConcepts. OxfordSeriesinCognitiveDevelopment.OxfordUniversityPress,New
York,2009.
Carey,S. Pre´cisofTheOriginofConcepts. BehavioralandBrainSciences,34(3):113–124,2011.
Carey,S.andSpelke,E. Scienceandcoreknowledge. PhilosophyofScience,63(4):515–533,1996.
Chakladar,D.D. Cortexlevelconnectivitybetweenact-rmodulesduringeeg-basedn-backtask. Cognitive
Neurodynamics,18(6):4033–4045,December2024. doi: 10.1007/s11571-024-10177-y.
Chen,H.H.,Lan,D.,Shu,W.-J.,Liu,Q.,Wang,Z.,Chen,S.,Cheng,W.,Chen,K.,Zhang,H.,Zhang,Z.,Guo,
R.,Cheng,Y.,andChen,Y.-C. Tivibench: Benchmarkingthink-in-videoreasoningforvideogenerative
models. arXivpreprintarXiv:2511.13704,2025. URLhttps://arxiv.org/abs/2511.13704.
Christoff,K.,Keramatian,K.,Gordon,A.M.,Smith,R.,andMa¨dler,B. Prefrontalorganizationofcognitive
controlaccordingtolevelsofabstraction. BrainResearch,1286:94–105,2009.
Colby,C.L.andGoldberg,M.E. Spaceandattentioninparietalcortex. AnnualReviewofNeuroscience,22:
319–349,1999. doi: 10.1146/annurev.neuro.22.1.319.
d’anthropologiedeParis,S. BulletinsdelaSocie´te´ d’anthropologiedeParis. Masson.,1898.
15


## PAGE 16

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
DiCarlo,J.J.,Zoccolan,D.,andRust,N.C. Howdoesthebrainsolvevisualobjectrecognition? Neuron,73
(3):415–434,2012.
Friston,K. Thefree-energyprinciple: Aunifiedbraintheory? NatureReviewsNeuroscience,11:127–138,
2010. doi: 10.1038/nrn2787.
Geirhos,R.,Narayanappa,K.,Mitzkus,B.,Thieringer,T.,Bethge,M.,Wichmann,F.A.,andBrendel,W.
Partialsuccessinclosingthegapbetweenhumanandmachinevision. AdvancesinNeuralInformation
ProcessingSystems,34:23885–23899,2021.
Gentner,D. Structure-mapping: Atheoreticalframeworkforanalogy. CognitiveScience,7(2):155–170,1983.
Gentner,D.andHoyos,C. Analogyandabstraction. TopicsinCognitiveScience,9(3):672–693,2017. doi:
10.1111/tops.12278.
Ghazanfar,A.A.andSchroeder,C.E. Isneocortexessentiallymultisensory? TrendsinCognitiveSciences,
10(6):278–285,2006. doi: 10.1016/j.tics.2006.04.008.
Gibson,J. Theecologicalapproachtovisualperception: classicedition,2014.
Gilboa,A.andMarlatte,H. Neurobiologyofschemasandschema-mediatedmemory. TrendsinCognitive
Sciences,21(8):618–631,2017.
Goodale,M.A.andMilner,A.D.Separatevisualpathwaysforperceptionandaction.TrendsinNeurosciences,
15(1):20–25,1992. doi: 10.1016/0166-2236(92)90344-8.
GoogleDeepMind. Veo3.1. Technicalreport,GoogleDeepMind,2026. URLhttps://blog.google/
innovation-and-ai/technology/ai/veo-3-1-ingredients-to-video/. Released
January13,2026.
Greco,A.,Moser,J.,Preissl,H.,andSiegel,M. Predictivelearningshapestherepresentationalgeometryof
thehumanbrain. Naturecommunications,15(1):9670,2024.
Guo,Z.,Chen,X.,Zhang,R.,An,R.,Qi,Y.,Jiang,D.,Li,X.,Zhang,M.,Li,H.,andHeng,P.-A. Arevideo
modelsreadyaszero-shotreasoners? anempiricalstudywiththeMME-CoFbenchmark. arXivpreprint
arXiv:2510.26802,2025. URLhttps://arxiv.org/abs/2510.26802.
Guyer,P. KantandtheClaimsofKnowledge. CambridgeUniversityPress,Cambridge,1987.
HaCohen,Y.,Brazowski,B.,Chiprut,N.,Bitterman,Y.,Kvochko,A.,Berkowitz,A.,Shalem,D.,Lifschitz,
D.,Moshe,D.,Porat,E.,Richardson,E.,Shiran,G.,Chachy,I.,Chetboun,J.,Finkelson,M.,Kupchick,M.,
Zabari,N.,Guetta,N.,Kotler,N.,Bibi,O.,Gordon,O.,Panet,P.,Benita,R.,Armon,S.,Kulikov,V.,Inger,
Y.,Shiftan,Y.,Melumian,Z.,andFarbman,Z. Ltx-2: Efficientjointaudio-visualfoundationmodel,2026.
URLhttps://arxiv.org/abs/2601.03233. Submitted6Jan2026.
Hafting, T., Fyhn, M., Molden, S., Moser, M.-B., andMoser, E.I. Microstructureofaspatialmapinthe
entorhinalcortex. Nature,436(7052):801–806,2005. doi: 10.1038/nature03721.
Hassabis,D.andMaguire,E.A. Theconstructionsystemofthebrain. PhilosophicalTransactionsofthe
RoyalSocietyB:BiologicalSciences,364(1521):1263–1271,2009.
He,X.,Fan,Z.,Li,H.,Zhuo,F.,Xu,H.,Cheng,S.,Weng,D.,Liu,H.,Ye,C.,andWu,B.RULER-bench:Prob-
ingrule-basedreasoningabilitiesofnext-levelvideogenerationmodelsforvisionfoundationintelligence.
arXivpreprintarXiv:2512.02622,2025. URLhttps://arxiv.org/abs/2512.02622.
Hegarty,M.,Montello,D.R.,Richardson,A.E.,Ishikawa,T.,andLovelace,K. Spatialabilitiesatdifferent
scales: Individualdifferencesinaptitude-testperformanceandspatial-layoutlearning. Intelligence,34(2):
151–176,2006. doi: 10.1016/j.intell.2005.09.005.
16


## PAGE 17

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
He´lie,S.andSun,R. Creativeproblemsolving: ACLARIONtheory. In2010InternationalJointConference
onNeuralNetworks(IJCNN),pp.1460–1466,Barcelona,Spain,2010.IEEE. doi: 10.1109/IJCNN.2010.
5596891. URLhttps://doi.org/10.1109/IJCNN.2010.5596891.
Helmholtz,H.v. Treatiseonphysiologicaloptics,3vols. OpticalSocietyofAmerica,1924.
Ho,J.,Jain,A.,andAbbeel,P. Denoisingdiffusionprobabilisticmodels. InAdvancesinNeuralInformation
ProcessingSystems(NeurIPS),volume33,pp.6840–6851,2020.
Holyoak,K.J. Analogyandrelationalreasoning. InHolyoak,K.J.andMorrison,R.G.(eds.),TheOxford
HandbookofThinkingandReasoning,pp.234–259.OxfordUniversityPress,2012.
Holyoak,K.J.,Gentner,D.,andKokinov,B.N. Introduction: Theplaceofanalogyincognition. InGentner,
D.,Holyoak,K.J.,andKokinov,B.N.(eds.),TheAnalogicalMind: PerspectivesfromCognitiveScience,
pp.1–19.MITPress,2001.
Hubel,D.H.andWiesel,T.N. Receptivefields,binocularinteractionandfunctionalarchitectureinthecat’s
visualcortex. TheJournalofPhysiology,160:106–154,1962.
Hubel,D.H.andWiesel,T.N. Receptivefieldsandfunctionalarchitectureofmonkeystriatecortex. The
JournalofPhysiology,195(1):215–243,1968.
Hubel,D.H.andWiesel,T.N. Ferrierlecture: Functionalarchitectureofmacaquemonkeyvisualcortex.
ProceedingsoftheRoyalSocietyofLondon.SeriesB,BiologicalSciences,198(1130):1–59,1977.
Kant,I. CritiqueofPureReason. CambridgeUniversityPress,Cambridge,1781. TheCambridgeEditionof
theWorksofImmanuelKant.
Kanwisher,N. Functionalspecificityinthehumanbrain: Awindowintothefunctionalarchitectureofthe
mind. ProceedingsoftheNationalAcademyofSciences,107(25):11163–11170,2010. doi: 10.1073/pnas.
1005062107.
Kanwisher,N.,McDermott,J.,andChun,M.M. Thefusiformfacearea: Amoduleinhumanextrastriate
cortexspecializedforfaceperception. JournalofNeuroscience,17(11):4302–4311,1997. doi: 10.1523/
JNEUROSCI.17-11-04302.1997.
Kazemian, A., Elmoznino, E., andBonner, M.F. Convolutionalarchitecturesarecortex-aligneddenovo.
NatureMachineIntelligence,2025. doi: 10.1038/s42256-025-01142-3.
Keil,F.C. Concepts,kinds,andcognitivedevelopment. mitPress,1992.
Keller,G.B.andMrsic-Flogel,T.D. Predictiveprocessing: Acanonicalcorticalcomputation. Neuron,100
(2):424–435,2018. doi: 10.1016/j.neuron.2018.10.003.
Kersten, D., Mamassian, P., and Yuille, A. Object perception as bayesian inference. Annual Review of
Psychology,55:271–304,2004. doi: 10.1146/annurev.psych.55.090902.142005.
Kong,W.,Tian,Q.,Zhang,Z.,Min,R.,Dai,Z.,Zhou,J.,Xiong,J.,Li,X.,Wu,B.,Zhang,J.,etal. Hun-
yuanVideo: Asystematicframeworkforlargevideogenerativemodels. arXivpreprintarXiv:2412.03603,
2024.
Kosslyn,S.M. ImageandMind. HarvardUniversityPress,Cambridge,MA,1980.
Kosslyn,S.M. Imageandbrain: Theresolutionoftheimagerydebate. MITpress,1996.
Kriegeskorte,N.Deepneuralnetworks:Anewframeworkformodelingbiologicalvisionandbraininformation
processing. AnnualReviewofVisionScience,1:417–446,2015.
17


## PAGE 18

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
Kuaishou Technology. Kling AI launches video 2.6 model with “simultaneous audio-visual generation”
capability, redefining AI video creation workflow. Press Release, December 2025. Model released
December3,2025.PressreleasepublishedDecember5,2025.
Kumaran,D.,Hassabis,D.,Spiers,H.J.,Vann,S.D.,Vargha-Khadem,F.,andMaguire,E.A. Impairedspatial
andnon-spatialconfigurallearninginpatientswithhippocampalpathology. Neuropsychologia,45(12):
2699–2711,2007.
Kumaran,D.,Summerfield,J.J.,Hassabis,D.,andMaguire,E.A. Trackingtheemergenceofconceptual
knowledgeduringhumandecisionmaking. Neuron,63(6):889–901,2009.
Ko¨rding,K.P.,Beierholm,U.,Ma,W.J.,Quartz,S.,Tenenbaum,J.B.,andShams,L. Causalinferencein
multisensoryperception. PLoSONE,2(9):e943,2007. doi: 10.1371/journal.pone.0000943.
Laird, J. E., Rosenbloom, P. S., and Newell, A. Soar: An architecture for general intelligence. Artificial
Intelligence,33(1):1–64,1987. doi: 10.1016/0004-3702(87)90050-6. URLhttps://doi.org/10.
1016/0004-3702(87)90050-6.
Langley,P.,Laird,J.E.,andRogers,S. Cognitivearchitectures: Researchissuesandchallenges. Cognitive
SystemsResearch,10(2):141–160,2009. doi: 10.1016/j.cogsys.2006.07.004. URLhttps://doi.org/
10.1016/j.cogsys.2006.07.004.
LeCun,Y.,Bengio,Y.,andHinton,G. Deeplearning. Nature,521(7553):436–444,2015.
Li,H.,Chrysanthidis,N.,Brincat,S.L.,Rose,J.,andMiller,E.K. Neuralsubspacereorganizationreflects
value-baseddecisionmaking. bioRxiv,pp.2026–02,2026.
Li, Y., Gao, Q., Zhao, T., Wang, B., Sun, H., Lyu, H., Hawkins, R. D., Vasconcelos, N., Golan, T., Luo,
D., and Deng, H. Core knowledge deficits in multi-modal language models. 2025. URL https:
//arxiv.org/abs/2410.10855.
Liu, X., Xu, Z., Li, M., Wang, K., Lee, Y.J., andShang, Y. Canworldsimulatorsreason? Gen-ViRe: A
generativevisualreasoningbenchmark. arXivpreprintarXiv:2511.13853,2025. URLhttps://arxiv.
org/abs/2511.13853.
Longuenesse,B. KantandtheCapacitytoJudge: SensibilityandDiscursivityintheTranscendentalAnalytic
oftheCritiqueofPureReason. PrincetonUniversityPress,Princeton,1998.
Luo, D., Li, Y., and Deng, H. The philosophical foundations of growing ai like a child. arXiv preprint
arXiv:2502.10742,2025a.
Luo,D.,Wang,M.,Wang,B.,Zhao,T.,Li,Y.,andDeng,H. Machinepsychophysics: Cognitivecontrolin
vision-languagemodels. arXivpreprintarXiv:2505.18969,2025b.
Luo, Y., Zhao, X., Lin, B., Zhu, L., Tang, L., Liu, Y., Chen, Y.-C., Qian, S., Wang, X., and You, Y. V-
reasonbench: Toward unified reasoning benchmark suite for video generation models. arXiv preprint
arXiv:2511.16668,2025c. URLhttps://arxiv.org/abs/2511.16668.
Ma,W.J.,Beck,J.M.,Latham,P.E.,andPouget,A. Bayesianinferencewithprobabilisticpopulationcodes.
NatureNeuroscience,9:1432–1438,2006. doi: 10.1038/nn1790.
Marr,D. Vision: AComputationalInvestigationintotheHumanRepresentationandProcessingofVisual
Information. W.H.Freeman,SanFrancisco,1982.
Martin,C.B.andBarense,M.D. Perceptionandmemoryintheventralvisualstreamandmedialtemporal
lobe. Annualreviewofvisionscience,9(1):409–434,2023.
18


## PAGE 19

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
McClelland, J. L., McNaughton, B. L., and Lampinen, A.K. Integration ofnew informationin memory:
Newinsightsfromacomplementarylearningsystemsperspective. PhilosophicalTransactionsoftheRoyal
SocietyB,375(1799):20190637,2020.
McCorduck, P. Machines Who Think: A Personal Inquiry into the History and Prospects of Artificial
Intelligence. AKPeters/CRCPress,2edition,2004. ISBN9781568812052. doi: 10.1201/9780429258985.
Milner,A.D.andGoodale,M.A. Twovisualsystemsre-viewed. Neuropsychologia,46(3):774–785,2008.
Mitchell,M. Artificialintelligencelearnstoreason,2025.
Moser, E. I. and Moser, M.-B. Grid cells and cortical representation. Nature Reviews Neuroscience, 15:
466–481,2014. doi: 10.1038/nrn3766.
Newell, A. You can’t play 20 questions with nature and win: Projective comments on the papers of this
symposium. InChase,W.G.(ed.),VisualInformationProcessing,pp.283–308.AcademicPress,New
York,NY,1973. ISBN9780121701505. doi: 10.1016/B978-0-12-170150-5.50012-3. URLhttps://
linkinghub.elsevier.com/retrieve/pii/B9780121701505500123. Proceedingsofthe
EighthAnnualCarnegieSymposiumonCognition,Carnegie-MellonUniversity,Pittsburgh,Pennsylvania,
May19,1972.
Newell,A.andSimon,H.A. Thelogictheorymachine–acomplexinformationprocessingsystem. IRE
TransactionsonInformationTheory,2(3):61–79,1956.
Newell,A.andSimon,H.A. HumanProblemSolving. Prentice-Hall,EnglewoodCliffs,NJ,1972. ISBN
0134454030.
Newell,A.,Shaw,J.C.,andSimon,H.A. Reportonageneralproblemsolvingprogram. InIFIPcongress,
volume256,pp.1959.Pittsburgh,PA,1959.
NobelPrizeCommittee. TheNobelprizeinphysiologyormedicine2014. https://www.nobelprize.
org/prizes/medicine/2014/summary/,2014. AwardedtoJohnO’Keefe,May-BrittMoserand
EdvardI.Moser.
O’Keefe,J.andDostrovsky,J. Thehippocampusasaspatialmap: Preliminaryevidencefromunitactivityin
thefreely-movingrat. BrainResearch,34(1):171–175,1971. doi: 10.1016/0006-8993(71)90358-1.
Olshausen,B.A.andField,D.J. Emergenceofsimple-cellreceptivefieldpropertiesbylearningasparsecode
fornaturalimages. Nature,381:607–609,1996.
OpenAI. Sora: Openai’stext-to-videomodel. https://openai.com/index/sora-is-here,2025.
publiclyreleasedSeptember2025.
Palmeri,T.J.,Love,B.C.,andTurner,B.M. Model-basedcognitiveneuroscience. JournalofMathematical
Psychology,76(PtB):59–64,February2017. doi: 10.1016/j.jmp.2016.10.010.
Papadopoulos, A., Sforazzini, F., Egan, G., and Jamadar, S. Functional subdivisions within the human
intraparietalsulcusareinvolvedinvisuospatialtransformationinanon-context-dependentmanner. Human
brainmapping,39(1):354–368,2018.
Passingham,R.E.andLau,H. Doweunderstandtheprefrontalcortex? BrainStructureandFunction,228(5):
1095–1105,2023.
Peebles, W. and Xie, S. Scalable diffusion models with transformers. In Proceedings of the IEEE/CVF
InternationalConferenceonComputerVision(ICCV),pp.4195–4205,2023.
Peng,W.,Wang,G.,Yang,T.,Li,C.,Xu,X.,He,H.,andZhang,K. SVBench: Evaluationofvideogeneration
modelsonsocialreasoning. arXivpreprintarXiv:2512.21507,2025.
19


## PAGE 20

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
Petersen,S.E.andSporns,O. Brainnetworksandcognitivearchitectures. Neuron,88(1):207–219,Oct2015.
doi: 10.1016/j.neuron.2015.09.027.
Plato. Theaetetus, volume12. HarvardUniversityPress, Cambridge, MA,1921. LoebClassicalLibrary.
Originalworkpublishedca.369BCE.
Polyak,A.,Zohar,A.,Brown,A.,Tjandra,A.,Sinha,A.,Lee,A.,Vyas,A.,Shi,B.,Ma,C.,Chuang,C.,etal.
MovieGen: Acastofmediafoundationmodels. arXivpreprintarXiv:2410.13720,2024.
QuianQuiroga,R.,Boscaglia,M.,Jonas,J.,Rey,H.G.,Yan,X.,Maillard,L.,Colnat-Coulbois,S.,Koessler,
L., and Rossion, B. Single neuron responses underlying face recognition in the human midfusiform
face-selectivecortex. NatureCommunications,14(1):5661,2023.
Ramnani,N.andOwen,A.M. Anteriorprefrontalcortex: Insightsintofunctionfromanatomyandneuroimag-
ing. NatureReviewsNeuroscience,5(3):184–194,2004.
Rao,R.P.N.andBallard,D.H. Predictivecodinginthevisualcortex: Afunctionalinterpretationofsome
extra-classicalreceptive-fieldeffects. NatureNeuroscience,2(1):79–87,1999. doi: 10.1038/4580.
Rapaport,W.J. Hasaisucceeded? 2026.
Renero,A. Nousandaisthe¯sis: Twocognitivefacultiesinaristotle. Me´thexis,26(1):103–120,2013. doi:
10.1163/24680974-90000616.
Runway Research. Introducing runway gen-4: Next-generation ai models for media generation and
world consistency. Runway Research, March 2025. URL https://runwayml.com/research/
introducing-runway-gen-4. AccessedJanuary27,2026.
Russell,S.J.andNorvig,P. ArtificialIntelligence: AModernApproach. Pearson,Hoboken,4thedition,2021.
ISBN9780134610993.
Shams,L.andBeierholm,U.R. Causalinferenceinperception. TrendsinCognitiveSciences,14(9):425–432,
2010.
Shepard,R.N.andMetzler,J. Mentalrotationofthree-dimensionalobjects. Science,171(3972):701–703,
1971. doi: 10.1126/science.171.3972.701.
Shields,C. Aristotle: DeAnima. OxfordUniversityPress,2016.
Spelke,E.S. Coreknowledge. AmericanPsychologist,55(11):1233–1243,2000. doi: 10.1037/0003-066X.55.
11.1233.
Spelke, E. S. and Kinzler, K. D. Core knowledge. Developmental Science, 10(1):89–96, 2007. doi:
10.1111/j.1467-7687.2007.00569.x.
Sporns,O.,Tononi,G.,andKo¨tter,R. Thehumanconnectome: Astructuraldescriptionofthehumanbrain.
PLoSComputationalBiology,1(4):e42,2005. doi: 10.1371/journal.pcbi.0010042.
Stein,B.E.andStanford,T.R. Multisensoryintegration: Currentissuesfromtheperspectiveofthesingle
neuron. NatureReviewsNeuroscience,9:255–266,2008. doi: 10.1038/nrn2331.
Swanson,L.R. Thepredictiveprocessingparadigmhasrootsinkant. FrontiersinSystemsNeuroscience,10:
79,2016. doi: 10.3389/fnsys.2016.00079.
Tanaka,K. Inferotemporalcortexandobjectvision. AnnualReviewofNeuroscience,19:109–139,1996.
Tolman,E.C. Cognitivemapsinratsandmen. PsychologicalReview,55(4):189–208,1948. doi: 10.1037/
h0061626.
20


## PAGE 21

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
Tomov,M.S.,Yagati,S.,Kumar,A.,Yang,W.,andGershman,S.J. Discoveryofhierarchicalrepresentations
forefficientplanning. PLoSComputationalBiology,16(4):e1007594,2020.
Tong,J.,Mou,Y.,Li,H.,Li,M.,Yang,Y.,Zhang,M.,Chen,Q.,etal. Thinkingwithvideo: Videogeneration
asapromisingmultimodalreasoningparadigm. arXivpreprintarXiv:2511.04570,2025.
Treisman, A. M. and Gelade, G. A feature-integration theory of attention. Cognitive Psychology, 12(1):
97–136,1980.
Tsao,D.Y.,Freiwald,W.A.,Tootell,R.B.H.,andLivingstone,M.S. Acorticalregionconsistingentirelyof
face-selectivecells. Science,311(5761):670–674,2006. doi: 10.1126/science.1119983.
Tse, D., Takeuchi, T., Kakeyama, M., Kajii, Y., Okuno, H., Tohyama, C., Bito, H., and Morris, R. G. M.
Schema-dependentgeneactivationandmemoryencodinginneocortex. Science,333(6044):891–895,2011.
Vaidya, A. R. and Badre, D. Abstract task representations for inference and control. Trends in cognitive
sciences,26(6):484–498,2022.
vonHelmholtz,H. HandbuchderphysiologischenOptik. L.Voss,Leipzig,1867.
WanTeam. Wan: Openandadvancedlarge-scalevideogenerativemodels. arXivpreprintarXiv:2503.20314,
2025. URLhttps://arxiv.org/abs/2503.20314.
Wedin,M.V. MindandImaginationinAristotle. YaleUniversityPress,NewHaven,1988.
Wernicke,C. DeraphasischeSymptomencomplex: EinepsychologischeStudieaufanatomischerBasis. Max
CohnundWeigert,Breslau,1874. Englishtranslation: TheSymptomComplexofAphasia.
Whitehead,A.N.andRussell,B. Principiamathematica,volume2. TheUniversityPress,1927.
Whittington, J. C., Dorrell, W., Behrens, T. E., Ganguli, S., and El-Gaby, M. A tale of two algorithms:
Structuredslotsexplainprefrontalsequencememoryandareunifiedwithhippocampalcognitivemaps.
Neuron,113(2):321–333,2025.
Whittington, J. C. R., Muller, T. H., Mark, S., Chen, G., Barry, C., Burgess, N., and Behrens, T. E. J.
TheTolman-Eichenbaummachine: Unifyingspaceandrelationalmemorythroughgeneralizationinthe
hippocampalformation. Cell,183(5):1249–1263,2020. doi: 10.1016/j.cell.2020.10.024.
Wiedemer, T., Li, Y., Vicol, P., Gu, S. S., Matarese, N., Swersky, K., Kim, B., Jaini, P., and Geirhos,
R. Video models are zero-shot learners and reasoners. arXiv preprint arXiv:2509.20328, 2025. URL
https://arxiv.org/abs/2509.20328.
Xiao,Z.,Wang,X.,Zhang,J.,Ou,J.,He,L.,Qu,Y.,Hu,X.,Behrens,T.E.,andLiu,Y. Humanhippocampal
ripplesalignnewexperienceswithagrid-likeschema. Neuron,113(21):3661–3672,2025.
Yamakawa, H. The whole brain architecture approach: Accelerating the development of artificial gen-
eral intelligence by referring to the brain. Neural Networks, 144:478–495, 2021. doi: 10.1016/
j.neunet.2021.09.004. URL https://www.sciencedirect.com/science/article/pii/
S0893608021003543.
Yamins, D. L. K., Hong, H., Cadieu, C. F., Solomon, E. A., Seibert, D., and DiCarlo, J. J. Performance-
optimizedhierarchicalmodelspredictneuralresponsesinhighervisualcortex. ProceedingsoftheNational
AcademyofSciences,111(23):8619–8624,2014.
Yang,C.,Wan,H.,Peng,Y.,Cheng,X.,Yu,Z.,Zhang,J.,Yu,J.,Yu,X.,Zheng,X.,Zhou,D.,andWu,C.
Reasoningviavideo: Thefirstevaluationofvideomodels’reasoningabilitiesthroughmaze-solvingtasks.
arXivpreprintarXiv:2511.15065,2025a. URLhttps://arxiv.org/abs/2511.15065.
21


## PAGE 22

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
Yang,J.,Yang,S.,Gupta,A.W.,Han,R.,Fei-Fei,L.,andXie,S. Thinkinginspace: Howmultimodallarge
languagemodelssee,remember,andrecallspaces. InProceedingsoftheComputerVisionandPattern
RecognitionConference,pp.10632–10643,2025b.
Yang,Z.,Teng,J.,Zheng,W.,Ding,M.,Huang,S.,Xu,J.,Yang,Y.,Hong,W.,Zhang,X.,Feng,G.,etal.
CogVideoX:Text-to-videodiffusionmodelswithanexperttransformer. arXivpreprintarXiv:2408.06072,
2024.
Zacks,J.M. Neuroimagingstudiesofmentalrotation: Ameta-analysisandreview. JournalofCognitive
Neuroscience,20(1):1–19,2008.
Zheng, Z., Peng, X., Yang, T., Shen, C., Li, S., Liu, H., Zhou, Y., Li, T., and You, Y. Open-SORA:
Democratizingefficientvideoproductionforall. arXivpreprintarXiv:2412.20404,2024.
22


## PAGE 23

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
A.DetailsofCognitiveArchitecture
Doesintelligencehaveastructure? SuchdiscussioncoulddatebacktoAristotle,wherecognitionistreated
notasaflat“innertheater”,i.e. inhismentor(Plato1921,Theaetetus189e–190a),butasanorganizationof
dunameis,inotherwords,cognitivefaculties. Knowingbeginswithaistheˆsis,perception,wherethesenses
receivetheformofexternalthingswithouttheirmatter,i.e. seeing“redness,”notabsorbingtheredobject
(Aristotle1984f;g,DeAnima2.1,412a19–23;2.12,424a17–24). Theperceivedthengetsfilteredthrough
koine¯ aisthˆesis,inotherwords,commonsense,whereourjudgmentsaresuppliedbycoreknowledgeborn
withus,suchasspatiality,intuitivephysics,andlogicthoughts(Carey&Spelke1996;Carey2009;Luoetal.
2025a;Lietal.2025;Aristotle1984g,DeAnima3.1,425a27–b11). Phantasiaservesasthesubstratethat
preserves,recombines,organizesandtransformstheperceptualempeiria,experiences,andstorestheminto
mne¯me¯,memory(Aristotle1984a;g,DeAnima3.3,427b14–428a9,OnMemory,449b3–453b11). Above
empeiriaandmne¯me¯ liesthenouˆs,theuniquelyhumanfacultyofunderstandingandabstraction,andfrom
empeiria, nouˆs extracts katholou, universals, an arc that Aritsole foregrounds as he traces from aistheˆsis,
phantasia,empeiria,mne¯me¯ tonouˆs. Essentially,thepathtokatholou,forAristole,isthepathtoknowledge
andintelligenthumanbehaviors,andthereforesuchistheflowofAristotle’scognitivearchitecture(Aristotle,
1984b,Metaphysics1.1,980a21–27).
GermanIdealismisanotherundertakingwherehumanthinkerstrytotheorizethestructureofourcognition
and mind. Kant posits that the mind does not simply mirror the but actively structures the world that we
perceiveasit’s(Kant1781,CPR,A19–A24/B33–B38;A30–A33/B45–B49). Heholdsthatrawsensoryinput
canonlybecomemeaningfulwhenorganizedbythemind’sbuilt-inframeworks–sinnlichkeit,aprioriforms
ofintuition,i.e. spaceandtime,andverstand,categoriesofunderstanding,whichincludeunderstandingof
numbers,ofquality,modality,ofcausality,andofrelations(Kant1781,CPR,A50–A51/B74–B75;A80/B106).
Betweensinnlichkeitandverstandlieseinbildungskraft,wherestructuredperceptualmentalcontentwouldbe
senttofortransformationandsynthesis. Kantgivesparticulardescriptionsofsuchtransformationofmental
content: sinnlichkeitfirstorganizesthespatiotemporalshapeofrepresentations,orderingrawdataasaunified
intuitioninspaceandtime,andeinbildungskraftbringstogetherintuitionssothattheycanbecombined,and
finallyverstandrecognizestheunifieddatabysubsumingitunderacategory(Kant1781,CPR,A98–A110).
Attheapexliesvernunft,whichofferstheultimateabstractionofmentalrepresentations,andgenerateideas
suchasthesoul,theselfasawhole,theworld,theuniverseasatotality,andGod(Allison2004;Longuenesse
1998;Guyer1987;Kant1781,CPR,A327/B384;A642/B670;A249–A252).
Modern discussions on cognitive architecture usually combine with research in artificial intelligence and
cognitive neuroscience. At the Dartmouth Workshop in 1956, where the term ”artificial intelligence” is
coined, HerbertSimonandAlanNewellhaspresentedLogicalTheorist, acomputerprogramwhichthey
hadclaimedtobethe“thefirstartificialintelligenceprogram”(Newell&Simon,1956;McCorduck,2004).
WhileLogicalTheoristisnarrowandcouldonlyprove38ofthefirst52theoremsinRussell’sphilosophy
textbook, it sparks the first AI boom where people try to build principled computer programs that would
producehuman-likeintelligentbehaviors(Whitehead&Russell,1927;Russell&Norvig,2021). TheGeneral
Problem Solver has shown that human reasoning could be simulated using symbolic production systems,
establishingacomputationalaccountofproblemsolving,whilecritiquesarguesuchisonlyasubsetofwhat
humanintelligencecoulddo(Newelletal.,1959;Newell&Simon,1972;Newell,1973). Full-scalecognitive
architecturemodelssoonhaveflourished,includingACT-R,SOAR,andCLARIONmodels(Anderson,2013;
Laird et al., 1987; Anderson & Lebiere, 1998; Anderson, 1993; 2007; Langley et al., 2009; He´lie & Sun,
2010).
As techniques in neuroscience have developed, a dialogue has emerged between cognitive architectures
and brain architectures (Petersen & Sporns, 2015). Human brain is interestingly modular, with cognitive
functionsspecificallyimplementedinparticularphysicalanatomicallocations,yetthesespecializedregions
communicateconstantlytoorchestratecognition(d’anthropologiedeParis,1898;Wernicke,1874;Kanwisher,
2010). Recently,cognitiveneuroscientistshopetomapoutthestructuralandfunctionalconnectivitybetween
brainareasastounderstandthearchitecturalorganizationunderlyingcognition(Spornsetal.,2005;Bertolero
etal.,2015).Explicitcombinationsofthecognitivearchitectureapproachesandconnectomicsapproacheshave
23


## PAGE 24

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
beencarriedoutinresearchinrecentyearsandyieldedvalidationsofsomeofthehypothesizedarchitectural
claimsabouthumancognitioninthehumanbrain(Palmerietal.,2017;Yamakawa,2021;Chakladar,2024).
Sittingontheshoulderofphilosophygiantsandcombiningworksfromcognitivearchitecturemodelingand
neuroscience,wehaveconsolidatedacognitivearchitecturemadeofperception,transformation,spatiality,
abstraction,andknowledge.
A.1.Perception
Perception is the the extraction of form without matter (Aristotle, 1984g, De Anima 2.12, 424a17–24).
Helmholtzcallsthisas”unconsciousinference”(vonHelmholtz,1867;Helmholtz,1924). Thevisualsystem
exemplifiesperception’shierarchicalarchitecture. V1neuronsfunctionasorientededgedetectorsorganized
into columnar structures reflecting natural image statistics (Hubel & Wiesel, 1962; 1968; Bonhoeffer &
Grinvald, 1991; Hubel & Wiesel, 1977; Olshausen & Field, 1996). Beyond V1, the ventral and dorsal
streamsachieveprogressivelyinvariantobjectrecognition(Milner&Goodale,2008;Goodale&Milner,1992;
DiCarloetal.,2012;Tanaka,1996),withcategory-selectiveregionslikethefusiformfaceareaemergingin
inferotemporalcortex(Kanwisheretal.,1997;Tsaoetal.,2006;QuianQuirogaetal.,2023),wherecells
collectivelymapalow-dimensional”objectspace”(Baoetal.,2020). JustasKanthashypothesized(Swanson,
2016),thebraingeneratespredictionsaboutsensoryinputandcomputespredictionerrors,withrepresentational
geometryshapedbyenvironmentalregularities(Rao&Ballard,1999;Friston,2010;Keller&Mrsic-Flogel,
2018;Grecoetal.,2024;Kerstenetal.,2004;Maetal.,2006). Multimodalintegrationbindssignalsacross
modalitiesthroughcausalinferenceinregionslikesuperiortemporalcortex(Ghazanfar&Schroeder,2006;
Stein&Stanford,2008;Calvert,2001;Ko¨rdingetal.,2007;Shams&Beierholm,2010). Marr’stri-level
frameworkconnectsbiologicalandartificialvision(Marr,1982): CNNsexhibitcortex-alignedrepresentations,
thoughtheylackrobusthigher-levelprocessingfoundinbiologicalsystems(Yaminsetal.,2014;Kriegeskorte,
2015;Kazemianetal.,2025;Bakeretal.,2018;Geirhosetal.,2021). Gibson’secologicalapproachreminds
usthatperceptionultimatelyservesactionthroughaffordances(Gibson,2014)—connectingtoAristotle’sview
thataistheˆsisservestheorganism’sengagementwithitsenvironment. Perceptionconstitutestheentrypointof
humancognitivearchitecture,athesisfromMarrandGibsontomoderndeeplearning(Gibson,2014;Marr,
1982;Yaminsetal.,2014;Kriegeskorte,2015;Kazemianetal.,2025;Bakeretal.,2018;Geirhosetal.,2021).
A.2.Transformation
Transformationreferstothecognitivefacultythatmanipulates,recombines,andsynthesizesmentalrepresenta-
tions,correspondingtoAristotle’sphantasiaandKant’sEinbildungskraft. Aristotleinsiststhat“wheneverone
contemplates,onenecessarilyatthesametimecontemplatesinimages,”positioningphantasianotaspassive
storagebutasactivetransformationofempeiriaintomaterialsuitablefornouˆs(Aristotle1984g,DeAnima
3.7,431a16–17;Wedin1988). Kantsystematizesthisthroughhisthreesyntheses,apprehensiongatheringthe
sensorymanifold,reproductioninimaginationholdingrepresentationstogether,andrecognitionsubsuming
theunifiedmanifoldundercategories,withEinbildungskraftfunctioningproductivelytogenerateexperiential
structurebybindingintuitionsaccordingtoVerstand(Kant1781,CPR,A98–A110;Longuenesse1998;Allison
2004). Moderncognitivescienceoperationalizestheseinsights: scientistshavedemonstratedthatmental
rotationoperatesanalogicallyonquasi-spatialrepresentations,proposingthatmentalimagesareconstructedin
a“visualbuffer”formanipulation(Shepard&Metzler,1971;Kosslyn,1980;1996). Anotherworkhasshowed
thatfocusedattentionbindspreattentivelyregisteredfeaturesintocoherentobjects,aprocessthatbreaksdown
withparietallesions,echoingKant’ssynthesisofapprehension(Kant1781,CPR,A98–A110;Treisman&
Gelade,1980). Neurosciencesuggeststheposteriorparietalcortex,particularlytheintraparietalsulcus,as
thesubstratefortransformation(Zacks,2008;Papadopoulosetal.,2018),whilecognitivearchitectureslike
ACT-Rformalizethisthroughanimaginalmodulewithparietalcorrelates(Anderson,2007). Transformation
thusoccupiesthecrucialintermediatepositionbothAristotleandKantrecognized: betweenrawaistheˆsisor
SinnlichkeitandthehigheroperationsofnouˆsorVernunft.
24


## PAGE 25

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
A.3.Spatiality
ForKant,spaceconstitutesanaprioriformofsinnlichkeit—atranscendentalpreconditionforperception
itself, not something derived from experience (Kant 1781, CPR, A22–A24/B37–B40). This insight finds
support in developmental psychology identifying spatiality as a core knowledge system: infants possess
domain-specificmachineryforrepresentingplacesandtheirgeometricrelationships,withdeepphylogenetic
rootsobservableacrossspeciesandcultures(Spelke&Kinzler,2007;Spelke,2000). Tolmanfirstproposed
thatanimalsconstructinternal“cognitivemaps”enablingflexiblenavigationbeyondsimplestimulus-response
associations(Tolman,1948). Theneuralsubstrateswerelaterrevealed: placecellsinthehippocampusfire
atspecificlocations(O’Keefe&Dostrovsky,1971),whilegridcellsintheentorhinalcortexprovidemetric
coordinatesthroughhexagonalfiringpatterns(Haftingetal.,2005),whicharediscoveriesrecognizedbythe
2014NobelPrizeas“apositioningsysteminthebrain”(Moser&Moser,2014;NobelPrizeCommittee,2014).
Theposteriorparietalcortexcomplementsthissystembyorganizingsensorycoordinatesintomotor-relevant
referenceframes(Colby&Goldberg,1999;Andersenetal.,1997). Beyondrepresentation,humansperform
spatial operations such as mental rotation, where reaction times increase linearly with angular disparity
(Shepard&Metzler,1971;Hegartyetal.,2006). Computationalmodelsthataregrid-cell-inspiredhavebeen
proposed,buthuman-levelperformancesremainchallenging(Baninoetal.,2018;Whittingtonetal.,2020;
Behrensetal.,2018). Spatialityservesasafundamentalfunction,aprerequisiteforperception,scaffoldfor
memory,andsubstrateforreasoninginhumancognitivearchitecture.
A.4.Abstraction
Abstractionrepresentstheapexofourcognitivearchitecture,whereembodiedexperiencesaredistilledinto
generalizable knowledge. For Aristotle, nouˆs extracts katholou, universals, from accumulated empeiria
throughselectiveattentiontoessentialfeaturesx(Aristotle,1984b,Metaphysics1.1,980a21–27;Renero,2013;
Aristotle,1984g,DeAnima3.4–8;Shields,2016). Kant’sVernunftsimilarlygeneratestranscendentalideas
extendingbeyondthecategoriesofVerstand,thoughexceedingtheboundariesofpossibleexperience(Kant,
1781,CPR,A327/B384;A642/B670;Allison,2004;Guyer,1987). Contemporaryaccountselaboratethese
mechanisms:onedevelopmentalpsychologyworkdemonstratesthatabstractconceptsemergethroughQuinian
Bootstrapping,producingrepresentationalsystemswithgreaterexpressivepowerthancorecognition,with
conceptspossessingcausallydeep“cores”(Carey,2009;Carey,2011;Carey,2009;Keil,1992). Gentner’s
structure-mapping theory shows how analogical reasoning maps relational patterns across domains, with
systematicitydeterminingpreferredmappingsandenablingchildrentoextractrelationalabstractions(Gentner,
1983;Gentner&Hoyos,2017;Holyoak,2012;Gentner,1983;Gentner&Hoyos,2017;Holyoaketal.,2001).
Neurosciencerevealsabstraction’shierarchicalimplementation: thelateralPFCexhibitsarostral-to-caudal
gradientwherebyanteriorregionsprocessincreasinglyabstractinformation,withrostralPFCservingasa
“gateway”forinternally-generatedthought(Badre&Nee,2018;Christoffetal.,2009;Badre&Nee,2018;
Brincatetal.,2018; Burgessetal.,2007;Ramnani&Owen,2004). Memorysystemscontributethrough
schema-guidedconsolidation,withhippocampusandvmPFCmaintainingabstractprototyperepresentations
that support generalization (Bowman & Zeithamova, 2018; Gilboa & Marlatte, 2017; Tse et al., 2011;
McClellandetal.,2020). Hierarchicalabstractionmightunderlydeeplearning’slayeredrepresentationsand
cognitivearchitectures’multipleprocessinglevels(LeCunetal.,2015;Bengioetal.,2013;Anderson,2007;
Lairdetal.,1987;Tomovetal.,2020;Luoetal.,2025b). Abstractionintegratestheoutputsofperception,
transformation,andspatialitytoachievethekatholou,knowledge,thatAristotlerecognizedasthetelosof
intelligentbehavior(Aristotle,1984d,PosteriorAnalytics2.19,100a3–100b5).
A.5.Knowledge
AristotleopenstheMetaphysicswiththeclaimthat“allhumanbeingsbynaturedesiretoknow”(Aristotle,
1984b,Metaphysics980a21),anddevotestheclosingchapterofthePosteriorAnalyticstoexplaininghowthey
doso. Knowledgebeginsinaistheˆsis,senseperception,whichdepositsmneˆmeˆ,memory;repeatedmemories
ofthe samekindconsolidate intoempeiria, experience; andfromexperiencenouˆsabstracts theuniversal
firstprinciplesthatgroundepisteˆmeˆ,demonstrativeknowledge(Aristotle,1984d,PosteriorAnalyticsII.19,
25


## PAGE 26

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
99b15–100b17). Theprogressionisneitherpurelyempiricalnorpurelyrational: perceptionfurnishesthe
material,butitistheactiveintellectthatgraspstheuniversalintheparticular,“aswhenarouthasoccurred
in battle, first one soldier makes a stand, then another, until the original formation is restored” (Aristotle,
1984d,PosteriorAnalytics100a12–13). ForAristotle,then,humancognitionisstructuredfromtheoutsetby
capacitiesthatgobeyondthesensorygiven,nouˆsdoesnotlearnfirstprinciplesfromexperiencesomuchas
recognizethemthroughit.
Kantradicalizesthisinsight. WhereasAristotleallowsthatuniversalsarelatentinperceptionandextracted
byintellect,Kantarguesthatthemindactivelyconstitutestheveryformofexperience. “Thoughtswithout
contentareempty;intuitionswithoutconceptsareblind”(Kant,1781,CPRA51/B75): knowledgerequires
bothsensibleAnschauungendeliveredbyreceptivityandtheKategorienofVerstandimposedbyspontaneity.
Thecategories,substance,causality,unity,plurality,andtheres,arenotabstractedfromexperiencebutare
itsaprioriconditionsofpossibility(Kant,1781,CPRA80/B106;Longuenesse,1998). Thetranscendental
deductionestablishesthattheseconceptsmustapplytoanyobjectofexperiencewhatsoever,becauseitis
onlythroughtheirapplicationthatthemanifoldofintuitionissynthesizedintocoherentrepresentation(Kant,
1781,CPRB129–B169;Allison,2004). Knowledge,forKant,isthusneverapassivereceptionbutanactive
structuring: themindbringstoexperiencetheveryframeworkwithinwhichexperiencebecomesintelligible.
Contemporarydevelopmentalpsychologyhasfurnishedstrikingempiricalsupportforthisrationalistinher-
itance. Researchoncoreknowledgedemonstratesthathumaninfantspossess,fromtheearliestmonthsof
life,asetofdomain-specificrepresentationalsystemsthatstructurecognitionpriortoandindependentlyof
explicitinstruction(Spelke&Kinzler,2007). Theserepresentationsareabstract,oftenamodal,andoperate
accordingtoprinciplesthatgowellbeyondwhatassociativelearningfromperceptualstatisticscoulddeliver
(Baillargeonetal.,1985). Carey’saccountofconceptualchangefurthershowsthatlater,explicitknowledgeis
constructednotexnihilobutthroughtheenrichment,combination,andbootstrappingofthesecoresystems,a
processshetermsQuinianbootstrapping(Carey,2009).
Figure7 Distributionof150visualreasoningtasksacrossfivecognitivefacultiesintheVBVR-Dataset.
13.3%
30.0%
Cognitive Faculties
150 15.3% Perception (45)
Abstraction (33)
Transformation (29)
Tasks Knowledge (23)
Spatiality (20)
19.3%
22.0%
Table6 CompleteCognitiveTaxonomyofVBVR-Dataset(150VisualReasoningTasks)
TaskID CognitiveCategory Description
ABSTRACTION(33)
G-7 Abstraction Returnobjectstocorrectbinbycategory
G-26 Abstraction Maintainobjectidentityacrossdifferentobjects
G-29 Abstraction Findextremevaluesinchart(withdatalabels)
G-37 Abstraction Identifyrandomsymmetrypatterns
G-38 Abstraction Identifyshapesymmetrypatterns
G-41 Abstraction Gridhighestcostpathfinding
G-44 Abstraction Breadth-firstsearchtraversal
G-49 Abstraction Completemissingcontoursegments
G-51 Abstraction Predictnextcolorinsequence
G-131 Abstraction Selectnextfigureinincreasingsizesequence
G-133 Abstraction Selectnextfigureindecreasingsizesequence
G-134 Abstraction Selectnextfigureinlarge-smallalternatingsequence
G-135 Abstraction Selectnextfigureinsmall-largealternatingsequence
G-193 Abstraction Drawnextsizedshapeinpattern
O-7 Abstraction Shapecolorchangeoperations
O-8 Abstraction Shaperotationoperations
Continuedonnextpage
26


## PAGE 27

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
Table6—continuedfrompreviouspage
TaskID CognitiveCategory Description
O-9 Abstraction Shapescalingoperations
O-10 Abstraction Shapeoutlinefilloperations
O-11 Abstraction Shapecolorthenmove(compoundoperation)
O-12 Abstraction Shapecolorthenscale(compoundoperation)
O-13 Abstraction Shapeoutlinethenmove(compoundoperation)
O-14 Abstraction Shapescalethenoutline(compoundoperation)
O-21 Abstraction Constructionblueprintinterpretation
O-29 Abstraction Ballcolorclusteringandmerging
O-30 Abstraction Bookshelforganizationtask
O-37 Abstraction Lightsequencepatternrecognition
O-43 Abstraction Objectsubtraction(quantityreasoning)
O-45 Abstraction Sequencecompletiontask
O-47 Abstraction Slidingpuzzlesolving
O-49 Abstraction Symmetrycompletiontask
O-54 Abstraction Controlpanelsymbolmanipulation
O-56 Abstraction Raven’sProgressiveMatricesreasoning
O-66 Abstraction Animalcolorsortingtask
KNOWLEDGE(23)
G-27 Knowledge Readchartdataandsemanticcomprehension
G-30 Knowledge Findextremevaluesinchart(withoutdatalabels)
G-35 Knowledge Hittargetafterbounce
G-48 Knowledge Multiplebouncesprediction
G-160 Knowledge Circlelargestnumericalvalue
G-162 Knowledge Locatetwelveo’clockarrows
G-163 Knowledge Identifydigits1and9
G-200 Knowledge Circlemaximumvalueinset
G-217 Knowledge Circlecentraldot
G-247 Knowledge IdentifyChinesecharacter
G-273 Knowledge Highdensityliquidbehavior
O-3 Knowledge Symbolreorderingoperations
O-15 Knowledge Ballbouncesatgiventime
O-18 Knowledge Glassrefraction
O-19 Knowledge Mirrorreflection
O-23 Knowledge Dominochainbranchpathprediction
O-24 Knowledge Dominochaingapanalysis
O-34 Knowledge Dot-to-dotconnectiontask
O-52 Knowledge Trafficlightstatereasoning
O-53 Knowledge Clockreadingandtimereasoning
O-62 Knowledge Gravityphysicssimulation
O-75 Knowledge Communicatingvessels(fluiddynamics)
O-87 Knowledge Fluiddiffusionreasoning
PERCEPTION(45)
G-3 Perception Stablesortobjectsmaintainingorder
G-4 Perception Identifyanddistinguishdifferentobjects
G-5 Perception Multi-objectplacementtospecifiedpositions
G-9 Perception Identifyobjectsinspecifiedregion
G-19 Perception Sortobjectsbyspecifiedrule
G-22 Perception Attentionshifttosameobject
G-39 Perception Attentionshifttodifferentobject
G-43 Perception Understandscenestructureandspatiallayout
G-54 Perception Connectingmatchingcolors
G-132 Perception Findfragmentforgapfilling
G-136 Perception Locatepointinoverlappingarea
G-137 Perception Identifyfigureinoverlappingarea
G-138 Perception Spotuniquenon-repeatedcolor
G-141 Perception Identifypolygonwithmostsides
G-143 Perception Selectboxwithmostdots
G-146 Perception Circleallsquaresfrommixedshapes
G-147 Perception Identifyuniquefigureinuniformset
G-158 Perception Identifyallhollowpoints
G-161 Perception Marksecondlargestshape
G-165 Perception Marktangentpointaftermotion
G-166 Perception Highlighthorizontallines
G-167 Perception Selectlongestpolygonside
G-168 Perception Identifyrectanglenearesttosquare
G-169 Perception Locateintersectionoflinesegments
G-174 Perception Arrangecirclesbycircumference
G-189 Perception Drawmidpointperpendicularline
G-195 Perception Selectnearest2:1rectangle
G-198 Perception Markright-angledtriangles
G-199 Perception Locatelineintersections
G-202 Perception Markwavepeaks
Continuedonnextpage
27


## PAGE 28

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
Table6—continuedfrompreviouspage
TaskID CognitiveCategory Description
G-206 Perception Identifypentagons
G-212 Perception Findincorrectarrowdirection
G-218 Perception Identifylargestangleintriangle
G-222 Perception Marktangentpointofcircles
G-223 Perception Highlighthorizontallines
G-248 Perception Markasymmetricalshape
G-250 Perception Colortripleintersectionred
O-1 Perception Colormixing(additive)
O-2 Perception Pigmentcolormixing(subtractive)
O-16 Perception Coloradditionoperations
O-17 Perception Colorsubtractionoperations
O-31 Perception Balleatingmechanics
O-33 Perception Countingobjectsaccurately
O-38 Perception Identifymajoritycolorinset
O-65 Perception Animalsizesorting
SPATIALITY(20)
G-12 Spatiality Gridnavigationtoobtainreward
G-13 Spatiality Gridnumbersequencenavigation
G-14 Spatiality Gridcolorsequencenavigation
G-15 Spatiality Gridnavigationavoidingobstacles
G-16 Spatiality Gridnavigationgoingthroughblocks
G-17 Spatiality Gridnavigationavoidingredblocks
G-18 Spatiality Gridshortestpathfinding
G-31 Spatiality Directedgraphnavigation
G-32 Spatiality Undirectedgraphnavigation
G-33 Spatiality VisualJengagame
G-45 Spatiality Key-doormatchingpuzzle
G-46 Spatiality Findkeysandopendoors
G-47 Spatiality Multiplekeysforonedoorpuzzle
G-140 Spatiality Locatetopmostunobscuredfigure
G-219 Spatiality Selectleftmostshape
G-221 Spatiality Outlineinnermostsquare
O-25 Spatiality LEGOconstructionassembly
O-39 Spatiality Mazenavigationandsolving
O-55 Spatiality Rotationoperations
O-83 Spatiality Planarwarpverification
TRANSFORMATION(29)
G-1 Transformation Predictobjecttrajectory
G-2 Transformation Reorderobjectsbyrule
G-6 Transformation Resizeobject
G-8 Transformation Trackobjectmovement
G-11 Transformation Handleobjectreappearanceafterdisappearance
G-21 Transformation Multipleocclusions(vertical)
G-24 Transformation Separateobjects(norotation)
G-25 Transformation Separaterotatingobjects
G-34 Transformation Objectpackingoptimization
G-36 Transformation Multipleocclusions(horizontal)
G-40 Transformation Combinedrotatingobjects
G-50 Transformation Suppressspuriousedges
G-194 Transformation Constructconcentricring
G-240 Transformation Addborderstounborderedshapes
O-4 Transformation Symbolsubstitutionoperations
O-5 Transformation Symboldeletionoperations
O-6 Transformation 2Dgeometrictransformation
O-22 Transformation Constructionstack(gravitybalance)
O-27 Transformation Move2objectsto2targets
O-32 Transformation Rollingballphysics
O-36 Transformation Gridshiftoperations
O-44 Transformation Rotationpuzzle
O-46 Transformation Shapesorterclassification
O-58 Transformation Symboldeleteoperations
O-59 Transformation Symbolinsertoperations
O-60 Transformation Symbolsubstituteoperations
O-61 Transformation Symboleditoperations
O-64 Transformation Animalmatchingtask
O-85 Transformation 2Dobjectrotation
28


## PAGE 29

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
B.DataCuration
ThisappendixprovidesacomprehensiveaccountofthedatacurationpipelinethatunderliestheVBVR-Bench.
Wedetailthefive-stageprocessfromtaskdesigntobenchmarkconstruction,thequalityassurancemechanisms,
andtheinfrastructurethatenableslarge-scaledatageneration.
B.1.OverviewofDataCurationPipeline
TheVBVR-Benchisbuiltthroughasystematicfive-stagepipelinethattransformscognitivetaskconceptsinto
astandardizedevaluationframework.
PipelineFlow. Thedatacurationpipelineconsistsoffivesequentialstages. Stage1: TaskDesignWebegin
bydesigningcognitivereasoningtasksgroundedincognitivescienceprinciples. Startingfromover300task
candidates,weemployadual-reviewprocesstoselecttasksthatmeetsixqualitycriteria. Thisstageproduces
twodistincttasksets: 100trainingtasksand100testingtaskswithanoverlappingof50tasks. Stage2: Task
ImplementationEachtrainingtaskisimplementedasaparameterizedgeneratorcapableofproducingdiverse
samples. Thesegeneratorsformtheourdataspring,VBVR-DataFactory,asetofmodularsynthesisengines.
All generators inherit from a standardized BaseGenerator template and are managed as independent
repositorieswithinaGitHubOrganization. Implementationundergoesrigorousqualitycontrolbydedicated
reviewerswhoverifyscalability,codequality,andadherencetofilespecifications. Stage3: Large-Scale
Distributed Generation. The VBVR-DataFactory infrastructure orchestrates parallel generation of one
milliontrainingsamples(10,000pertask)storedprivatelyonAWSS3. Simultaneously,wegenerate500fresh
testcases(5pertask)fromtheTesttaskset. Eachsamplecomprisesaninitialframe,taskprompt,ground-truth
solution,andreferencevideo. Stage4: ModelEvaluation. WeemployVBVR-EvalKittoevaluateeight
state-of-the-artimage-to-video(I2V)modelsonthe500testcases,producing4,000generatedvideos. Human
annotatorsassesseachvideoacrossthreereasoning-specificdimensions: TaskCompletion,ReasoningLogic,
andVisualQuality,eachscoredona1-5scale. Stage5: BenchmarkConstructionandModelTraining.
Theevaluationdataisintegratedintoastandardizedbenchmarkdataset. WetraintheVBVR-Wanontheone
milliontrainingsamples,demonstratingthatexplicitreasoningsupervisionsignificantlyimprovesperformance
onreasoning-intensivetasks.
B.1.1.KeyStatistics
Table7summarizesthescaleandcoverageoftheVBVRbenchmark:
Table7 DataConstructionStatistics
Component Scale Description
TaskCandidates 300+ Initialtaskpool
TrainingTasks 100 Generatetrainingdata
TestTasks 100 50In-Domain+50Out-of-Distribution
TrainingSamples 1,000,000 100tasks×10,000samplespertask
TestCases 7,500 150tasks×50samplespertask
CognitiveCategories 5 Systematiccoverage
EvaluatedModels 8 State-of-the-artI2Vmodels,4open-source,4commercial
GeneratedVideos 4,000 8models×500cases
EvaluationRecords 4,000 TaskCompletion/ReasoningLogic/VisualQualityannotations
DevelopmentTeam 75 53OSScoders+7full-timeemployees+5QCreviewers
CodeRepositories 300+ GithubOrganization
B.1.2.DesignPrinciples
Thepipelineisguidedbythefollowingcoredesignprinciples: 1. DualGeneralizationTesting. TheIn-
Domain/OODsplitenablesevaluationofbothin-taskgeneralization(seentasktypeswithunseensamples)
andcross-taskgeneralization(unseentasktypes). 2. Reasoning-FirstParadigm. Unlikebenchmarksthat
primarilyassessgenerationquality,VBVRemphasizesreasoningcorrectnessthroughTC,RL,andVQmetrics
thatcapturetaskcompletion,logicalconsistency,andvisualfidelity. 3. Industrial-ScaleQualityAssurance
We employ a dual-review mechanism: peer review for task design (by five task designers) and dedicated
29


## PAGE 30

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
quality control for implementation (by more than two specialized reviewers). Six quality criteria ensure
tasksarewell-specified,visuallyclear,andscalable. 4. ExtensibleInfrastructure. Themodulargenerator
architectureandcomprehensiveevaluationtoolkitfacilitateeasyextensionwithnewtasksandmodels. 5.
CognitiveInspiration. Ourtaskdesignbeganwithaloosecognitivetaxonomyinspiredbycognitivescience
literature. However,ratherthanrigidlyadheringtoafixedtheoreticalframework,weadoptedatask-driven
designphilosophy: weprioritizeddesigningintellectuallymeaningfulreasoningtasksfirst,thenorganized
themintoourcategories. 6. DiversityFocus. Thisapproachcontrastswithtop-downframeworksthatfirst
definestrictcategories,thenfillthemwithtasks. Ourbottom-upapproachensuredthateachtaskpossesses
genuinereasoningvalue,andmaximizingourdiversity,ratherthanforcingtaskstofitnarrowpre-determined
boxes.
B.1.3.TaskSelectionandFiltering
InitialPool Wedesignedover300taskcandidatesthroughiterativebrainstormingsessions. Eachdesigner
independentlyproposedtasks,whichwerethencollectivelydiscussedandrefined.
SelectionCriteria(SixStandards) Taskswereevaluatedagainstsixcriteriaduringpeerreview:
1. InformationSufficiency: Thefirstframemustcontainallinformationnecessaryforreasoning,without
requiringexternalcontext.
✓ PassExample: G-15(GridAvoidObstacles)—thefirstframeshowsstartpoint,endpoint,andall
obstacles.
× Fail Example: Tasks where the goal object is initially occluded or requires additional verbal
explanation.
2. DeterministicSolution: Tasksshouldhaveaclear,uniquesolution(orexplicitlydefinedcriteriafor
multiplevalidsolutions,e.g.,“shortestpath”).
✓ PassExample: G-18(GridShortestPath)—theoptimalpathisunambiguous.
× FailExample: Open-endedtaskswithambiguoussuccessconditions.
3. Video-BasedReasoning: Tasksmustbesuitableforvideogenerationmodels,encompassingdiverse
reasoningtypes(temporaldynamics,staticrecognition,logicalinference).
✓ PassExample: O-23(DominoChain)—requirestemporalcausalityreasoning.
! Note: Unlike some benchmarks, we do NOT exclude static recognition tasks; we include both
dynamicandstaticreasoning.
4. VisualClarity: Objectsmustbedistinguishable,text/numberslegible,andlayoutsunclutteredtoavoid
perceptualambiguity.
5. Parametric Diversity (Scalability): The parameter space must be large enough to generate 10,000
non-trivial,distinctsamplespertask.
6. TechnicalFeasibility: Tasksmustbeimplementablewithourrenderingpipeline(PIL-based),output
standardfileformats,andavoidedgecases(e.g.,initialocclusions,boundaryoverflow).
RejectionCases Herearesomeofthetaskswereexcluded:
• A.Multi-StepLogicChains
– Example: LogicGateCircuits
– Reason: Reasoningchainstoolongtoclearlyvisualizeinvideoformat.
• B.ComplexPhysicsRequiringPreciseNumericalSolutions
30


## PAGE 31

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
– Example: ElasticCollisionswithfrictioncoefficients
– Reason: Continuousparametersyieldnodeterministicsolution(tinyparametervariationsleadto
drasticallydifferenttrajectories);I2Vmodelscannotpreciselysimulatephysics.
• C.ExcessivelyDifficultTasks
– Example: Sudoku
– Reason: High difficulty even for humans; unsuitable for video format (better suited for static
reasoning);evaluationcriteriatoostrict(anysinglecellerrorconstitutesfailure).
B.1.4.PeerReviewProcess
Alltaskdesignsunderwentastructuredpeerreviewbythefivetaskdesigners,witheachdesignerevaluating
others’proposalsusingastandardizedchecklistderivedfromthesixqualitycriteria;taskstypicallyprogressed
through2–3roundsofiterativerefinementbasedonthisfeedback,duringwhichcommonissueswereidentified,
includingambiguoussuccessconditions,insufficientvisualclarity,parameterspacestoosmalltosupport
10ksamples,andunintentionaledgecases(e.g.,objectsoverlappingatinitialization). Ataskadvancedto
implementation(Stage2)onlyafterreceivingconsensusapprovalfromatleastthreereviewers. Thisprocess
ensuredthateverytaskinVBVRmeetsrigorouscognitiveandtechnicalstandards,formingasolidfoundation
forthesubsequentimplementationandevaluationstages.
B.2.DetailsofTaskImplementation
This section details the implementation of the 200 tasks as parameterized generators. We describe the
standardized architecture, code management infrastructure, parameterization strategies, visual rendering
pipeline,anddedicatedqualitycontrolprocedures.
B.2.1.GeneratorArchitectureandStandardization
BaseGeneratorTemplate AlltaskgeneratorsinheritfromastandardizedBaseGeneratorabstractbase
class,ensuringconsistentinterfacesandoutputformats. Thetemplatedefines:
1. RequiredMethods:
• init (self, seed, params): Initialize generator with random seed and task-specific
parameters.
• generate sample(self) -> Sample: Generateasingletaskinstance.
• validate sample(self, sample) -> bool: Verifysamplemeetsqualitycriteria.
• save sample(self, sample, output dir): Savesampletostandardizedfilestructure.
2. StandardOutputFormat: Eachsampleissavedasadirectorycontaining:
• first frame.png: Initialstateimage(required)
• prompt.txt: Taskinstructioninnaturallanguage(required)
• final frame.pngorgoal.txt: Targetstateorgoaldescription
• ground truth.mp4: Referencesolutionvideodemonstratingthecorrectreasoningprocess
3. ConfigurationManagement: Generatorsexposeconfigurableparametersthroughaconfig.yaml
filespecifying:
• Parameterranges(e.g.,gridsize: 5-10,numberofobjects: 3-8)
• Difficultylevels(easy/medium/hard)
• Visualsettings(resolution: 512×512,framerate: 24fps)
31


## PAGE 32

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
DesignRationale. TheBaseGeneratortemplateservesthreecorepurposes: Consistency,byproviding
uniforminterfacesthatsimplifyintegrationwithVBVR-DataFactoryforbatchgeneration;QualityAssurance,
through the validate sample() method, which enforces critical checks such as ensuring no object
occlusionsandthatvalidsolutionsexist;andExtensibility,enablingnewtaskstobeaddedbyimplementing
theabstractmethodswhileleveragingsharedutilityfunctions.
B.2.2.CodeManagementInfrastructure
All task generators are managed as independent repositories within a GitHub Organization, an archi-
tecture that provides clear organizational and operational advantages: each repository follows a strict
Naming Convention of {Type}-{ID} {task name} data-generator (e.g., G-3 stable sort -
data-generatorandO-15 ball bounces given time data-generator),whereTypedenotes
G,whicharecontributedbycommercialenterprises,orO,whicharecontributedbyOSSdevelopers,andID
isauniquenumericidentifier;thisstructureenablesIndependentVersioning,aseachtaskmaintainsitsown
commithistory,tags,andreleasecycles,andsupportsModularUpdates,ensuringthatbugfixesorparameter
adjustmentstoonetaskdonotaffectothers.
Allgeneratorssharethecore/directorystructurethroughGitsubmodulesorpackagedependencies,ensuring
consistent utility functions while allowing each task to evolve independently. This design yields several
version control benefits: 1. Traceability, as each sample records the exact generator version (git commit
hash)usedforgeneration;2. Reproducibility,enablingresearcherstocheckoutspecificgeneratorversionsto
reproducesamplegeneration;and3. Collaboration,allowingmultipleteammemberstoworkondifferent
taskssimultaneouslywithoutmergeconflicts.
Figure8 Thisisatypicalexampleofdatasamplesinourdataset. Themodelreceivesapromptandafirst
image, and is asked to generate a video that solves the prompt. Final image and ground truth videos are
providedasreferencesindatasamples.
Question Answer
Prompt First Image Final Image
Move the green dot from Inference
its starting position through
the maze paths to the red flag.
B.2.3.ParameterizationStrategyforDiversity
Togenerate10,000distinct,non-trivialsamplespertask,weemploysystematicparameterizationstrategies:
Example1: G-15(GridAvoidObstacles)
Parameters:
- grid_size: [5, 6, 7, 8, 9, 10] # 6 options
- num_obstacles: [3, 4, 5, ..., 15] # 13 options
- start_position: grid-dependent # ˜grid_size² options
- end_position: grid-dependent # ˜grid_size² options
- obstacle_layout: random_valid # ˜10ˆ6 variations
Estimated unique samples: > 10ˆ9
Sampling strategy: Constrained random sampling ensuring solvability
Example2: O-56(Raven’sProgressiveMatrices)
Parameters:
- pattern_type: [size_progression, rotation, color_change,
shape_replacement, combination] # 5 types
- num_objects: [1, 2, 3, ..., n] # n options
- object_shapes: [circle, square, triangle, ...] # 8 shapes
32


## PAGE 33

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
- progression_complexity: [simple, compound] # 2 levels
- visual_style: [minimal, decorated] # 2 styles
Estimated unique samples: > 10ˆ5
Sampling strategy: Balanced distribution across pattern types
Example3: G-3(StableSort)
Parameters:
- num_shape_types: [2, 3, 4] # 3 options
- shapes_per_type: [2, 3, 4] # 3 options
- color_palette: [vibrant, pastel, ...] # 5 palettes
- initial_layout: random_permutation # n! permutations
- shape_geometry: [geometric, organic] # 2 styles
Estimated unique samples: > 10ˆ6
Sampling strategy: Uniform sampling across difficulty levels
Diversity is enforced through four complementary mechanisms: stratified sampling, which divides the
parameterspaceintostrata(e.g.,difficultylevels)andsamplesproportionallyfromeach;constraintsatisfaction,
whichensuresthatallgeneratedsamplesarevalid(e.g., mazesadmitsolutionsandpuzzlesaresolvable);
duplicatedetection,whichtracksparametercombinationsviahashfunctionstopreventexactduplicates;and
visualvariety,whichrandomizesvisualattributessuchascolors,sizes,andpositionsbeyondthecorereasoning
parameters.
Eachgeneratedsampleundergoesautomaticvalidation,includingasolvabilitychecktoverifythataground-
truthsolutionexists(e.g.,viaA*searchfornavigationtasks),avisualclaritychecktoensurethatobjectsdo
notoverlapexcessivelyandthattextremainslegiblewithaminimumfontsize,andaparameterboundscheck
toconfirmthatallparametersfallwithintheirspecifiedranges.
B.2.4.VisualRenderingPipeline
Allvisualsadheretofixedspecifications: aresolutionof512×512pixels,24-bitRGBcolordepth(8bitsper
channel),aframerateof24fpsforground-truthvideos,andH.264asthevideocodec.
B.3.Large-ScaleDistributedGenerationofTrainingData
TheVBVR-DataFactorycomponentorchestratestheparallelgenerationofonemilliontrainingsamplesusing
the300+generatorsinourdataspring. Itprovidesacomplete,production-gradeserverlesssystemforcloud
infrastructure,generationworkflow,dataorganization,andqualityassurance,enablingefficient,reliable,and
cost-effectivelarge-scaledataproduction.
AllgeneratedsamplesarestoredonAmazonWebServices(AWS)SimpleStorageService(S3). S3ischosen
foritsabilitytoscaletopetabyte-leveldatawithautomaticcapacitymanagement,itshighdurabilitythrough
redundantstorageacrossmultipleavailabilityzones,anditsfine-grainedaccesscontrolthroughIAMpolicies.
Trainingdataarekeptinprivatebucketswithserver-sideencryptiontopreventpublicexposureandtest-set
contamination. Inaddition,S3’stieredstoragemodelmakeslong-termarchivalcost-effective.
Toefficientlygenerateonemillionsamples,VBVR-DataFactoryemploysdistributedserverlessprocessing
viaAWSLambda. Thesystemdistributestasksacrossupto990concurrentLambdafunctioninstances,each
configuredwith3GBmemoryanda15-minuteexecutiontimeout. GenerationtasksarequeuedinAmazon
SQSandautomaticallytriggerLambdainvocations,eliminatingtheneedformanualclustermanagement.
Within each task, samples are produced in configurable batches of 25–100 to balance memory usage and
processingefficiency. Atypicalone-million-samplegenerationcompletesinapproximately2–4hourswiththe
fullfleetof990concurrentworkers,atatotalcostofroughly$800–1200perrun(primarilyLambdacompute
33


## PAGE 34

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
and S3 storage). Fault tolerance is built in through SQS’s automatic retry mechanism with configurable
visibilitytimeouts,aDeadLetterQueue(DLQ)forfailedmessagesafteroneretryattempt,andCloudWatch
metricsforreal-timemonitoringoftasksuccessratesandprocessingdurations.
Theend-to-endgenerationpipelinebeginswithconfigurationandplanning,wheregenerators,samplecounts,
randomseeds,andoutputformatsaredefined. TasksaresubmittedtotheSQSqueueasPydantic-validated
JSONmessages, eachspecifyingthegeneratortype, numberofsamples, startingindexforglobalsample
numbering,randomseed,andoutputformat(individualfilesorcompressedtararchives). Lambdafunctions
receivethesemessages,executethecorrespondinggeneratorsubprocess,validateandrenameoutputswithzero-
paddedglobalindices,uploadresultstoS3withstructuredprefixes,andemitsuccessmetricstoCloudWatch.
FailedtasksautomaticallymovetotheDLQformanualinspectionandresubmissionafterdebugging.
Onaper-taskbasis(100samples,typicalbatchsize),samplegenerationrequiresapproximately15minutes,
withgenerationspeedvaryingsignificantlybytaskcomplexity—simplegeometrictasksaverage1–3seconds
persample,whilecomplexgraphorphysicstasksrequire9–15secondspersample. Fileorganizationand
S3uploadadd1–2minutesdependingonfilesizes,andLambdacoldstartscontributeanadditional5–10
seconds for the first invocation. Each task therefore completes in roughly 15–20 minutes on a Lambda
instance,enablingtheentireone-million-samplecorpustobeproducedin2–4hourswith990parallelworkers.
Forefficientaccessduringtraining,VBVR-DataFactorymaintainsahierarchicalS3structureorganizedby
generatorandtask,witheachsampledirectorycontainingstandardizedfiles(first frame.png,prompt.txt,and
optionallyfinal frame.pngandground truth.mp4). Thisorganizationallowstrainingpipelinestolocate,filter,
andstreamdataefficientlyatscalethroughS3’sprefix-basedlistingandparalleldownloadcapabilities.
Qualityassuranceisintegratedthroughoutgeneration. Everysampleisvalidatedbythegenerator’sinternal
checksbeforebeingsaved,ensuringsolvability,visualclarity,andfileintegrity. Thesystemcontinuously
monitorstasksuccessrates,processingdurations,andsamplesuploadedthroughCloudWatchmetrics,with
alarmsconfiguredtodetectanomaliessuchashighfailureratesorDLQaccumulation. Samplediversityis
enforcedthroughuniqueper-taskrandomseedsthatincrementdeterministicallyacrossbatches,preventing
duplicate generation. The DLQ captures and preserves failed tasks for post-mortem analysis, enabling
systematicdebuggingofgeneratorissuesandinfrastructurefailures. Acrosstypicalproductionruns, task
validationfailuresoccurinfewerthan1percentofcases,primarilyduetoedge-caseparametercombinations
thatarecaughtbyPydanticschemavalidationbeforereachingthegenerator. Infrastructure-relatedfailures
(timeouts,out-of-memoryerrors)occurinapproximately0.1–0.5percentoftasksandareresolvedthrough
DLQresubmissionafteradjustingbatchsizesoraddressinggeneratorbugs.
AlltrainingsamplesarestoredinprivateS3bucketswithserver-sideencryption(SSE-S3),versioningdisabled
toreducecosts,andIAMrole-basedaccesscontrolrestrictedtoauthorizedLambdafunctionsandtraining
pipelines. Full S3 access logging is enabled for audit trails. The data contain no personally identifiable
information,asallsamplesarefullysyntheticandprocedurallygenerated. Together,thesedesignchoices
demonstratethat,withproperserverlessengineering,million-scale,high-qualitydatagenerationisachievable,
reliable,andcost-effective. TheresultingonemillionsamplesformthetrainingfoundationforVBVR-Wan
andfuturevideoreasoningsystems.
34


## PAGE 35

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
C.VBVR-BenchDetails
C.1.ModelInferenceInfrastructure
VBVR-Benchisanend-to-endevaluationframeworkthatintegrateslarge-scalemodelinference(orAPI-based
invocationforproprietarymodels)witharule-basedevaluationengineoverastandardized100-taskvideo
reasoningbenchmark. Atthemodellevel,VBVR-BenchprovidesaunifiedVideoGeneratorabstraction
thatencapsulates29videogenerationsystems,includingclosed-sourcemodelssuchasGoogleVeo,OpenAI
Sora,andRunwayGen-4,aswellasopen-sourceandresearchmodelssuchasCogVideoX,Wan2.2,LTX-2,
and HunyuanVideo. This abstraction ensures that all models are executed through an identical pipeline,
eliminatingconfoundingfactorsintroducedbymodel-specificinferencelogic. Itsupportsbatchexecution
atscale,incorporatescachingmechanismstoavoidredundantgenerations,andisfullyreusable,allowing
interruptedevaluationstocontinuewithoutlossofprogress.
C.1.1.ModelSelectionandConfiguration
FortheVBVRbenchmark,weevaluateeightstate-of-the-artimage-to-video(I2V)modelsrepresentingdiverse
architecturesandcapabilities:
Table8 EvaluatedModels
Model Developer Architecture Parameters KeyFeatures
CogVideoX1.5-5B-I2V TsinghuaUniversity/ZhipuAI Transformer-baseddiffusionmodel 5billion Strongtext-imagealignment
Wan2.2-I2V-A14B WanxAI Latentdiffusionwithattentionmechanisms 14billion High-fidelitytemporalconsistency
LTX-2 Lightricks Efficienttransformerarchitecture ∼3billion Fastinference
HunyuanVideo-I2V TencentHunyuan Multi-stagediffusionwithspatial-temporalattention ∼7billion Strongoncomplexscenes
Veo GoogleDeepMind Proprietary(closed-source) Unknown(large-scale) Strongphysicsunderstanding
Sora OpenAI Proprietary(closed-source,rumoreddiffusiontransformer) Unknown(likely>10B) Temporalcoherence,realisticphysics
RunwayGen-3 RunwayML Proprietary(closed-source) Unknown Creativegeneration,textadherence
Kling2.6 KuaishouTechnology Proprietary(closed-source,likelydiffusion-based) Unknown Fastinference
Themodelsincludedinthebenchmarkarechosentoreflectthebreadthandmaturityofthecurrentimage-
to-videolandscape. Thesetintentionallymixesopen-sourceandclosed-sourcesystems,ensuringthatboth
academicandindustrialapproachesarerepresented.Itspansawiderangeofarchitecturalparadigms,capturing
fundamentallydifferentdesignphilosophiesinvideogeneration. Theselectedmodelscoverabroadscale
spectrum, from approximately 3B parameters to 14B+ and beyond, enabling analysis of how reasoning
capabilitycorrelateswithmodelsize. Allincludedsystemsrepresentstate-of-the-artperformanceasoflate
2025andearly2026,ensuringthatthebenchmarkreflectsthecurrentfrontierofthefield.
Toensurefairandcontrolledcomparison,allgeneratedvideosfollowtheresolutionoftheircorresponding
ground-truthvideos,whichincludebothsquareandrectangularaspectratios. Foropen-sourcemodelsthat
support custom input resolutions, we specify the resolution to match the ground truth. For closed-source
models with fixed resolution constraints (e.g., Sora 2 only supports 1280×720 or 720×1280), we pad the
first-frameimagewithabackgroundcolorandautomaticallydetectandremovethepaddingduringevaluation.
Frameratesrangefrom15–24fpsdependingonmodelrequirements. ForAPI-basedmodels,weadoptthe
defaultorprovider-recommendedgenerationsettings,whileforopen-sourcemodelsweusetheconfigurations
reportedintheiroriginalpapers. Thisstandardizationremovesconfoundingfactorsarisingfromresolution
ortuningdifferences, ensuringthatobservedperformancedifferencesreflectreasoningabilityratherthan
generationformat.
C.2.DetailsofHumanPreferenceAnalysis
C.2.1.DataPreparation
Tomitigatepotentialbiasesinpairwisecomparisons,weadopttwocomplementarscoringschemes: relative
scoring based on pairwise preference judgments, and absolute scoring based on independent per-video
ratings. Incaseswheretheabsolutescoresclearlyindicatethatonevideoissuperiorbutthecorresponding
relativeannotationcontradictsthisassessment,thefinaldecisionisrevisedinfavoroftheabsolutejudgment.
For each sample consisting of a text prompt and an initial image pair p , we generate videos using nine
i
35


## PAGE 36

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
videogenerationmodelsM={M ,M ,M ,M ,M ,M ,M ,M ,M },producingasetofoutputsG =
1 2 3 4 5 6 7 8 9 i
{V ,V ,V ,V ,V ,V ,V ,V ,V }.
i,1 i,2 i,3 i,4 i,5 i,6 i,7 i,8 i,9
Forrelativeevaluation,allpairwisecombinationsareconstructedwithineachgroup,resultingin(cid:0)9(cid:1)
=36
2
uniquevideopairspersample. Forabsoluteevaluation,thedatasetcontains500distinctprompt–imagepairs
p . Eachpairisprocessedbyallninemodels,yieldingatotalof500×9=4,500single-videoannotation
i
instances.
Eachvideoispresentedtogetherwithitscorrespondingtextpromptandtask-specificevaluationdocuments.
Toreduceannotationnoise, everyvideoisindependentlyannotatedfivetimes. Allsamplesarerandomly
shuffledbeforeassignedtoannotators.
C.2.2.Humanannotation
Annotatorsarebetween20and35yearsoldandpossessbasicdomainknowledgerelevanttothetasks. All
annotatorsundergostandardizedtrainingtoensureconsistentinterpretationofevaluationcriteria.
Forrelativescoring,annotatorsareshowntwovideosgeneratedfromthesamepromptandareaskedtoselect
whichonebettercompletesthetaskandalignswiththegivenpromptoverall,withtiesallowed.
Forabsolutescoring,annotatorsrateeachvideoalongthreedimensionsusinga5-pointLikertscale,where
higherscoresindicatebetterperformance. TaskCompletion(TC)assessingwhetherthetaskgoalisachieved;
ReasoningLogic(RL),assessingthecorrectnessofthereasoningprocess;andVisualQuality(VQ),assessing
visualclarity,temporalcoherence,andrenderingfidelity.
C.2.3.WinRatioCalculation
Fromrelativehumanannotations,wecomputeawinratioforeachmodel. Ineachcomparison,thepreferred
modelreceivesascoreof1andtheother0;inthecaseofatie,bothreceive0.5. Winratiosareaggregated
acrossallpairwisecomparisonsforeachevaluationsplit.
Fromabsoluteannotations,weaveragethescoresoftheTC,RLandVQdimensionstoobtainafinalscoreper
sample. Theseabsolutescoresareusedforcross-verificationofpairwiseresultsandforresolvingcontradictory
annotationsbetweenthetwoscoringschemes.
Finally,wecomparethewinratiosderivedfromrelativehumanannotations(withcross-verificationusing
absolutescores)withthewinratioscomputedfromVBVR-Bench’sautomaticevaluationmetrics,andmeasure
thecorrelationbetweenthetwoacrossmodels.
C.3.DetailedAnalysisProtocolsandAdditionalResults
C.3.1.ResidualizedCapabilityCorrelation
This section details the computation behind Fig. 5 in the main paper. Our goal is to quantify capability
dependencybetweencognitivecategorieswhileavoidingtrivialcorrelationsinducedbyoverallmodelstrength.
Categoryscores. Letmindexmodelsandcindexcategories(fivetotal). Foreachmodelmandcategoryc,
wecomputeacategory-levelscorebyaveragingtheper-sampleOverallratings:
(cid:0) (cid:1)
S =mean Overall overallevaluatedsampleswithCategory=cformodelm.
m,c
Generalfactor. Wedefineamodel-levelgeneralfactorastheoverallmeanscoreacrossallsamples:
(cid:0) (cid:1)
G =mean Overall overallevaluatedsamplesformodelm.
m
Residualization. Foreachcategoryc,weregressS onG acrossmodels:
m,c m
S =a +b G +ϵ ,
m,c c c m m,c
andretaintheresidualsϵ asthestrengthbeyondoverallmodelquality.
m,c
36


## PAGE 37

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
Capabilitydependencymatrix. Foreachpairofcategories(c ,c ),wecomputePearsoncorrelationacross
1 2
modelsusingresiduals:
R =corr({ϵ } ,{ϵ } ).
c1,c2 m,c1 m m,c2 m
Theresulting5×5matrixRisvisualizedasaheatmap(mainpaper,Fig.5).
Implementation notes. We use the benchmark table and compute (i) S , (ii) G , (iii) residuals by
m,c m
ordinaryleastsquares,and(iv)Pearsoncorrelationsonresiduals. WealsoreportSpearmanρinauxiliary
analysistoconfirmrobustnesstomonotonictransformations.
C.3.2.Domain-wiseScoreDistributions(Boxplots)
To complement mean performance summaries, we report domain-wise score distributions across models
usingboxplots: task-leveldistributions,whereeachpointcorrespondstoataskmeanscorewithinadomain
(capturingcross-taskvariability).
Figure9 Domain-wisescoredistributionsacross9models(reddashedlineseparatesbaselinesandVBVR-
Wan2.2).
Task-Level Boxplot: Model Performance by Domain (9 Models: Open-source | Closed-source | Ours)
Abstraction Knowledge Perception Spatiality Transformation
(23 tasks) (14 tasks) (30 tasks) (13 tasks) (20 tasks)
5
4
3
2
1
CogVHunyuanLTX Wan KlingRunwayVeo SoraVBVR CogVHunyuanLTX Wan KlingRunwayVeo SoraVBVR CogVHunyuanLTX Wan KlingRunwayVeo SoraVBVR CogVHunyuanLTX Wan KlingRunwayVeo SoraVBVR CogVHunyuanLTX Wan KlingRunwayVeo SoraVBVR
Model Model Model Model Model
37
erocS
llarevO


## PAGE 38

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
D.SelectedTasksandRubrics
This appendix includes a curated set of tasks that require multi-step planning and/or multiple interacting
constraints. Foreachtask,weshowtheinitialandfinalframes,followedbytheevaluationrubricusedtoscore
modeloutputs.
StableSort(TaskG-3) Rearrangeobjectsbygroupingthembyshapetypeandsortingeachgroupbysize
whilepreservingallattributes,testingmulti-constraintspatialreasoning,attributefidelity,andrulefollowing.
Missing: Missing: Missing: Missing:
figures/tasks/stable_sort/0f1i_gfuirresst/.tpansgks/stable_sort/0f2i_gmuirde1s./ptnagsks/stable_sort/0f3i_gmuirde2s./ptnagsks/stable_sort/04_last.png
(or G-3 (or G-3 (or G-3 (or G-3
stable_sort/01_first.png) stable_sort/02_mid1.png) stable_sort/03_mid2.png) stable_sort/04_last.png)
(a)First (b)1stProgression (c)2ndProgression (d)Final
Figure10 StableSort
ExamplePrompt “Thescenecontainstwotypesofshapes,eachtypehasthreeshapesofdifferentsizes
arrangedrandomly. Keepallshapesunchangedinappearance(type,size,andcolor). Onlyrearrangetheir
positions: firstgrouptheshapesbytype,thenwithineachgroup,sorttheshapesfromsmallesttolargest(left
toright),andarrangeallshapesinasinglehorizontallinefromlefttoright.”
HumanAnnotationScoring(1–5):
• 5(Perfect). Correctgrouping;correctwithin-groupascendingsizeorder(lefttoright);horizontal
alignment;attributespreserved(type/size/color);reasonablespacing,nooverlaps.
• 4(Near-perfect). Correctgroupingandorderingwithoneminorimperfection(e.g.,smallcolordeviation
(hueshiftwithin±10%),smallsizedeviation(within±5%),slightverticalmisalignment,ormildly
unevenspacing)whiletheintendedlayoutremainsclear.
• 3(Partiallycorrect). Groupingiscorrectbutorderingiswronginatleastonegroup;orgroupingand
orderingarecorrectbutattributechangesarenoticeable(e.g.,colorshift>10%,sizechange>5%,or
milddeformationwhilestillrecognizable).
• 2(Multipleerrors). Incorrectgroupingand/orincorrectordering,and/ormissing/extraobjects.
• 1(Failure). Objectivenotachieved(nointendedgrouping/ordering)and/orsevereobject
modification/loss.
Evaluationdimensions(suggestedweights):
• Classificationaccuracy(30%). Correctlyidentifythetwoshapetypes;groupidenticalshapes;include
all6objects.
• Orderingcorrectness(30%). Ascendingsizeorderwithineachgroup;coherentleft-to-right
organization.
• Objectfidelity(30%). Preserveshapetype,size,andcolor;maintainclearcontours/edges.
• Layoutaccuracy(10%). Horizontalalignmentandreasonablespacing.
38


## PAGE 39

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
GridAvoidObstacles(TaskG-15) Navigatea10×10gridfromstarttogoalusingonly4-neighbormoves
withoutenteringobstaclecells,testingshortest-pathplanningunderhardconstraints.
Missing: Missing: Missing: Missing:
figures/tasks/grid_avoid_obfsitgaucrleess//t0a1s_kfsi/rgsrti.dp_nagvoid_obfsitgaucrleess//t0a2s_kmsi/dg1r.ipdn_gavoid_obfsitgaucrleess//t0a3s_kmsi/dg2r.ipdn_gavoid_obstacles/04_last.png
(or G-15 (or G-15 (or G-15 (or G-15
grid_avoid_obstacles/01_firgsrti.dp_nagv)oid_obstacles/02_midg1r.ipdn_ga)void_obstacles/03_midg2r.ipdn_ga)void_obstacles/04_last.png)
(a)First (b)1stProgression (c)2ndProgression (d)Final
Figure11 GridAvoidObstacles
ExamplePrompt: “Thesceneshowsa10x10gridwithabluestartsquare(containingayellowcircular
agent),aredendsquare,andmultipleblackXmarksindicatingobstacles. Startingfromthebluestartsquare,
theagentcanmovetoadjacentcells(up,down,left,right)eachstep. Thegoalistomovetheagenttothered
endsquarealongtheshortestpathwithoutenteringanycellsmarkedwithblackXobstacles.”
HumanAnnotationScoring(1–5):
• 5(Perfect). Reachesthegoal;avoidsallobstacles;usesashortest(ortied-shortest)obstacle-avoiding
path;movementislegal(4-neighbor,within-grid)andagentappearanceispreserved.
• 4(Near-perfect). Reachesthegoalandavoidsallobstacles;onlyaminorimperfection(e.g.,≤2extra
stepsvs.optimal,slightappearancedrift,orminorlegal-motionjitter).
• 3(Partiallycorrect). Clearattemptbutwithanotableissue(e.g.,entersexactlyoneobstaclecellonce,
>2extrasteps,stopsshortofthegoal,oranoccasionalillegal/diagonaltendency).
• 2(Mostlyincorrect). Multipleviolations(e.g.,enters2–3obstaclecells)and/orout-of-gridmotion
and/orhighlyinefficient/randomroutingand/orfailstoreachthegoal.
• 1(Failure). Nomeaningfulprogressorunrelatedoutput;frequentobstaclecrossings(≥4)orthegridis
corrupted.
Evaluationdimensions(suggestedweights):
• Obstacleavoidance(40%). Zeroobstacleentries;respectsnon-traversableconstraint.
• Pathoptimality(30%). Shortestpathlengthunderobstacleconstraints.
• Motion-rulecompliance(20%). 4-neighborsteps,within-grid,continuoustrajectory.
• Taskcompletion(10%). Reachesthegoalwithacoherentstart→goaltrajectory.
39


## PAGE 40

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
GridGoThroughBlock(TaskG-16) Plananear-shortest4-neighborroutethatvisitsallmarkedtarget
cells(inblue)beforereachingthegoal(inred)ina10×10grid,testingmulti-goalrouteoptimizationunder
movementconstraints.
Missing: Missing: Missing: Missing:
figures/tasks/grid_go_throufgihg_ubrleosc/kt/a0s1k_sf/igrrsitd._pgnog_throufgihg_ubrleosc/kt/a0s2k_sm/igdr1i.dp_nggo_throufgihg_ubrleosc/kt/a0s3k_sm/igdr2i.dp_nggo_through_block/04_last.png
(or G-16 (or G-16 (or G-16 (or G-16
grid_go_through_block/01_figrrsitd._pgnog_)through_block/02_migdr1i.dp_nggo)_through_block/03_migdr2i.dp_nggo)_through_block/04_last.png)
(a)First (b)1stProgression (c)2ndProgression (d)Final
Figure12 GridGoThroughBlock
ExamplePrompt:“Thesceneshowsa10x10gridwithagreenstartsquare(containinganorangecircular
agent),aredendsquare,andmultiplebluerectangularblocks. Startingfromthegreenstartsquare,theagent
canmovetoadjacentcells(up,down,left,right)eachstep. Thegoalistomovetheagenttotheredendsquare
alongtheshortestpaththatpassesthroughallblueblocks(theagentmustvisiteveryblueblockbefore
reachingtheredendsquare).”
HumanAnnotationScoring(1–5):
• 5(Perfect). Startsatthestartcellandendsatthegoal;visitsalltargets;usesagloballyshortestroute
underthevisit-allconstraint;motionislegal(4-neighbor,within-grid)andagentappearanceispreserved.
• 4(Near-perfect). Reachesthegoalandvisitsalltargets;onlysmallimperfections(e.g.,≤3extrasteps,
minorappearancedrift,orslightpresentationissueswhiletherealizedpathremainsgrid-orthogonal).
• 3(Partiallycorrect). Clearattemptbutwithanotableissue(e.g.,missesexactlyonetarget,>3extra
steps,stopsbeforethegoal,oranoccasionalillegalmove).
• 2(Mostlyincorrect). Missestwoormoretargetsand/orfailstoreachthegoal,and/orfrequent
illegal/out-of-gridmotion,and/orhighlyinefficient/randomrouting.
• 1(Failure). Nomeaningfulprogress;ignorestargetsoroutputisunrelated/gridisbroken.
Evaluationdimensions(suggestedweights):
• Targetcoverage(40%). Alltargetsvisited;nonemissing;targetsremainvisible.
• Routeoptimality(30%). Near-globalshortestrouteunderthevisit-allconstraint(targetordermatters).
• Taskcompletion(20%). Fullstart→(alltargets)→endsequencecompleted.
• Motionlegality(10%). 4-neighborstepsonly;stayswithingrid;coherentstep-by-stepmovement.
40


## PAGE 41

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
Directed Graph Navigation (Task G-31) Navigate from the start node to the goal node by traversing
onlyalongdirectededges(respectingarrowdirection)withaminimum-hoppath,testinggoal-directedgraph
planningunderdirectionalityconstraints.
Missing: Missing: Missing: Missing:
figures/tasks/directed_grapfhi_gnuarveisg/attaisokns//0d1i_rfeicrtsetd._pgnrgapfhi_gnuarveisg/attaisokns//0d2i_rmeicdt1e.dp_nggrapfhi_gnuarveisg/attaisokns//0d3i_rmeicdt2e.dp_nggraph_navigation/04_last.png
(or G-31 (or G-31 (or G-31 (or G-31
directed_graph_navigation/0d1i_rfeicrtsetd._pgnrga)ph_navigation/0d2i_rmeicdt1e.dp_nggr)aph_navigation/0d3i_rmeicdt2e.dp_nggr)aph_navigation/04_last.png)
(a)First (b)1stProgression (c)2ndProgression (d)Final
Figure13 DirectedGraphNavigation
Prompt:“Thesceneshowsanetworkofnodesconnectedbydirectededges(edgeswitharrowsindicating
direction)withagreenstartingnode,aredendingnode,andabluetriangularagentpositionedatthegreen
startingnode. Theagentcanonlymovealongedgesinthedirectiontheypoint(fromthesourcenodetothe
targetnode,cannotmovebackwards),movingfromonenodetoanadjacentnodeeachstep. Movetheblue
triangularagentfromthegreenstartingnodetotheredendingnodealongthepathwiththeminimumnumber
ofsteps.”
HumanAnnotationScoring(1–5):
• 5(Perfect). Reachesthegoal;usesaminimum-hoppath;strictlyfollowsarrowdirectionsandmoves
onlyalongexistingedges;motioniscontinuousandthegraphispreserved.
• 4(Near-perfect). Reachesthegoalwithcorrectdirection/edge-followingbehavior;onlyminor
presentationissueswhilepathlengthremainsshortest.
• 3(Partiallycorrect). Reachesthegoalbutwithanotableissue(e.g.,+1–2extrahops,asingledirection
violation,orslightdeviationfromdrawnedges).
• 2(Mostlyincorrect). Severeissues: ≥3extrahops,multipledirectionviolations,“flying”/cutting
acrossspace,reachesthewrongnode,oraltersgraphstructure.
• 1(Failure). Doesnotreachthegoal,behaviorisrandom/invalid(ignoresarrows),orthegraphis
corrupted.
Evaluationdimensions(suggestedweights):
• Shortest-pathcorrectness(40%). Minimum-hoppathlength.
• Directioncompliance(35%). Noreversetraversals;respectsarroworientation.
• Motionlegality(15%). Movesalongexistingedges,oneedgeperstep;noteleportation.
• Graphfidelity(10%). Nodes/edges/arrowsremainunchanged.
41


## PAGE 42

VIDEO-REASON.COM AVeryBigVideoReasoningSuite
KeyDoorMatching(TaskG-45) Inamaze,firstcollecttheprompt-specifiedcoloredkeyandthenreach
the matching door via legal corridor moves near shortest, testing instruction grounding, sequencing, and
constrainednavigation.
Missing: Missing: Missing: Missing:
figures/tasks/key_door_matcfhiignugr/e0s1/_tfaisrksst/.kpenyg_door_matcfhiignugr/e0s2/_tmaisdk1s./pknegy_door_matcfhiignugr/e0s3/_tmaisdk2s./pknegy_door_matching/04_last.png
(or G-45 (or G-45 (or G-45 (or G-45
key_door_matching/01_first.kpenyg_)door_matching/02_mid1.pknegy)_door_matching/03_mid2.pknegy)_door_matching/04_last.png)
(a)First (b)1stProgression (c)2ndProgression (d)Final
Figure14 KeyDoorMatching
Prompt:“Thesceneshowsamazewithagreencircularagent,coloreddiamond-shapedkeys,andcolored
hollowrectangulardoors. FindtheBluekeyandthennavigatetothematchingBluedoor,showingthe
completemovementprocessstepbystep.”
HumanAnnotationScoring(1–5):
• 5(Perfect). Reachesthecorrecttarget-coloredkey,thenreachesthematchingdoor(correctorder);path
islegalandcontinuous;pathlengthisnear-optimal(e.g.,≤120%ofBFSshortestforstart→key→door);
keydisappearswhenreached;fulltrajectoryisshown.
• 4(Near-perfect). Correctkeyanddoorincorrectorder;minorissuesonly(e.g.,slightlylongerpath
∼120%–150%,smalljitter/backtracking,ora1–2framedelayinkeydisappearance).
• 3(Partiallycorrect). Findsthecorrectkeybutmakesamajormistake(e.g.,goestowrongdoor,
completesonlyonestage,noticeablyinefficientpath∼150%–200%,or1–2minorwallviolations).
• 2(Mostlyincorrect). Wrongkeycolorand/orwrongorder(doorbeforekey),and/ormultiplewall
crossings,and/orextremelyinefficientpath(>200%),orstopsatirrelevantlocations.
• 1(Failure). Agentbarelymovesormovesrandomly;ignoresmazeconstraints;incorrectkey/doorcolors;
oragentbehaviorisabnormal.
Evaluationdimensions(suggestedweights):
• Targetidentification(30%). Correctlyidentifytheprompt-specifiedkeyandmatchingdoor;donot
confusewithothercolors.
• Pathvalidity(30%). Followallowedcorridorsonly,avoidwallcollisions,andmaintainstep-by-step
movement.
• Pathefficiency(20%). ActualpathlengthrelativetotheBFS-optimalpath;≤110%=excellent,
110–130%=acceptable,>200%=poor.
• Animationquality(20%). Smoothframe-by-framemovement;agentcentersalignwithkeyanddoor;
keypickupeffectvisible.
42
