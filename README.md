#### Jérémy Martin
#### 2025-03-27
## Mini-Project
This mini-project has been made in the context of the Programming and Data Analysis class at PSE.

# Key Factors Influencing Road Accidents in Belgium and Policies for Mitigation

## Introduction
### The Global Burden of Road Accidents

Road traffic accidents are a significant public health and economic issue worldwide. According to the World Health Organization (*WHO, 2023*), approximately **1.35 million people** die each year as a result of road crashes, and between **20 to 50 million** more suffer non-fatal injuries, often resulting in long-term disabilities.

Beyond the human cost, road accidents impose **substantial economic burdens**, estimated at **3% of global GDP** due to medical expenses, loss of productivity, and infrastructure damage (*WHO, 2023*). These challenges are particularly pressing in urbanized and densely populated countries, where increasing vehicle ownership and traffic congestion contribute to road safety risks.

In Europe, road safety policies have successfully reduced fatalities over the past two decades, yet disparities remain between countries and regions. Belgium, as a Western European country with a highly developed road network, faces **persistent challenges** in reducing traffic accidents, particularly in urban areas and among vulnerable road users.

### Road Accidents in Belgium: The Need for Data-Driven Policies

Belgium has made considerable progress in road safety, but the Federal Public Service (FPS) for Mobility and Transport reported that in 2022, road accidents still resulted in **over 50,000 injuries and fatalities**. Despite strict traffic regulations, factors such as speeding, road conditions, weather conditions, time of day, and collision type continue to play a role in accident severity.

Understanding these determinants is essential for designing effective traffic regulations, road infrastructure improvements, and targeted enforcement strategies. Policymakers require **empirical, data-driven research** to optimize resources and implement measures that **maximize road safety impact**.

### Literature Review: Key Factors affecting Road Accidents

The study of road accidents has been an essential area of research in transportation safety, with scholars investigating the various factors that contribute to accident occurrence and severity. The literature identifies multiple key determinants, including time of occurrence, road conditions, collision type, driver impairment, and methodological approaches to accident modeling.

One of the most well-documented factors influencing accident severity is the time of occurrence, particularly differences between daytime and nighttime crashes. Research has consistently shown that nighttime and weekend accidents tend to be more severe due to reduced visibility, higher speeds, and increased incidence of impaired driving. Studies have found that impaired vision and fatigue at night lead to delayed reaction times, which can exacerbate the severity of crashes. Moreover, peak traffic congestion during rush hours contributes to a high frequency of accidents, although these tend to be less severe compared to high-speed crashes occurring at night (*Elvik, 2013*).

Road and environmental conditions also play a significant role in both accident frequency and severity. Highways and regional roads, due to their higher speed limits, often experience more severe crashes, whereas urban roads tend to have a higher frequency of accidents but lower severity due to reduced speeds and greater congestion. Research suggests that well-lit roads help mitigate accident risks, particularly at night, as street lighting has been shown to significantly reduce crash rates and improve driver visibility (*Sullivan & Flannagan, 2002*). In contrast, adverse weather conditions such as rain and fog increase accident risks due to reduced traction and limited visibility, leading to a greater likelihood of multi-vehicle collisions.

Another critical determinant is collision type, as different types of crashes exhibit varying levels of severity. Studies indicate that head-on collisions and side-impact crashes result in the highest fatality rates, whereas rear-end crashes, while frequent, are generally less severe due to lower impact forces (*Zou et al., 2017*). The nature of the collision is closely related to road design, with intersections being high-risk locations for side-impact crashes, while highways experience more frontal collisions due to overtaking and high-speed maneuvers.

The state of the driver is an equally important factor in accident severity. Alcohol consumption has been widely recognized as a leading contributor to road fatalities, as intoxicated drivers exhibit reduced cognitive abilities, slower reaction times, and impaired motor control. Studies show that the risk of severe injury or death increases significantly with higher blood alcohol concentrations, reinforcing the importance of strict drink-driving laws and enforcement (*WHO, 2023*). Beyond alcohol, other impairments such as fatigue, drowsiness, and medical conditions have also been found to influence accident risk. Research highlights that drivers with certain health conditions, such as sleep apnea or neurological disorders, are more likely to be involved in high-severity crashes, emphasizing the need for regular medical screenings for at-risk individuals (*Haque et al., 2012*).

In terms of statistical methodologies, **Poisson and Negative Binomial regression models** have been widely used in road accident analysis due to their suitability for **count data**. Poisson regression is particularly useful when modeling accident frequencies, as it assumes that the mean and variance of accident counts are equal, making it an appropriate choice when analyzing crash occurrence rates. However, when overdispersion is present (meaning the variance exceeds the mean), Negative Binomial regression is preferred as it accounts for additional variability in accident data (*Lord et al., 2005*). **Logistic regression models** have also been frequently applied to predict accident severity, particularly when categorizing outcomes as fatal or non-fatal. The choice of statistical model is crucial for deriving reliable insights, as improper modeling can lead to biased estimates and incorrect policy implications.

This literature review establishes that road accidents are a **multifaceted issue** influenced by temporal, environmental, vehicular, and human factors. It also underscores the importance of appropriate statistical modeling in drawing meaningful conclusions from accident data.

### Research Question & Objectives of this Study

Despite extensive research on road accidents, gaps remain in the literature, particularly in region-specific studies analyzing localized traffic patterns and risk factors. In the Belgian context, there is a need for empirical research examining how road type, time of occurrence, and collision type interact to influence accident frequency. This study seeks to answer the following research question: *What are the key factors influencing the occurrence of road accidents in Belgium, and how do these factors affect accident risk?*

By leveraging empirical evidence from actual accident reports, this research will assist policymakers, urban planners, and law enforcement agencies in designing targeted interventions to reduce the incidence of road accidents in Belgium.

### Overview of Datas

The dataset used in this study is the *TF_ACCIDENTS_2023* open dataset from the official statistics website of the Belgian government. It contains detailed records of road accidents that occurred in Belgium in 2023, providing crucial information on the time, location, road conditions, collision types, and severity of accidents. This makes it highly relevant for analyzing the factors influencing accident frequency.

Given the research question, this dataset is particularly suitable as it enables the examination of accident occurrence patterns and the assessment of how environmental and temporal factors contribute to road safety risks.
