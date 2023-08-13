# GreatSaltLakeCrisisAnalysis

A Decision Analysis of Mitigation Strategies for the Great Salt Lake Desiccation Crisis
Jeremy Hadfield
ENGS 172: Climate Change and Engineering
Final Term Project
12 May 2023

## Final term paper
Link here: [please email jeremy.hadf@gmail.com for the PDF of the full report] 

## Introduction
The Great Salt Lake (GSL) in Utah is shrinking at an alarming rate. The largest saltwater
lake in the Western Hemisphere has nearly halved in size, and in 2022 it reached its lowest level
on record (Meng 2019). GSL’s volume has decreased by 67%, with about 75% of the loss driven
by water use and 25% due to a millennial drought amplified by global climate change
(Wurtsbaugh 2022). This is not the first time a major saline lake has dried up due to human
influence: in the 1960s, water diversion from the Aral Sea led to a 90% decrease in its water
volume. As a result, the climate became harsher, yields from fishing and agriculture collapsed,
and millions of people suffered from dust, pollution, and water scarcity. This disaster could have
been avoided. Utah’s beloved and iconic lake is now careening toward a similar crisis—but it is
not too late to avert. Without rapid action to avert this desiccation (drying) crisis, the Great Salt
Lake as we know it could disappear, and an invaluable ecosystem will be gone.

## This part of the project: Stakeholder analysis and values-based mental model
To understand different perspectives on these questions and surface other important
questions, I wanted to conduct a series of exploratory consultations with key stakeholders to
understand their interests, concerns, and their potential influence on decision-making. I chose
this method because it is an important supplement to the more quantitative analysis. Without
directly listening to the people involved in the decisions and those who are impacted by the lake
drying up, I will not be able to understand the values, difficulties, tradeoffs, and concerns that are
at play in the GSL crisis. This qualitative information will help identify potential synergies and
conflicts among stakeholders, as well as areas for collaboration and compromise. This analysis
will inform more inclusive and sustainable solutions to address the GSL desiccation crisis. I also
aim to represent several distinct groups in my conversations, including local government,
environmental organizations, local residents, industries operating in the area, researchers and
academics, and indigenous peoples with ties to the lake. Below are some of the stakeholders that
I reached out to schedule a conversation on this topic, aiming to represent different groups:

● Benjamin Abbott – professor of ecosystem ecology, lead author of a report on the crisis.

● Lynn de Freitas – executive director of Friends of Great Salt Lake.

● Jaimi Butler – coordinator of the Great Salt Lake Institute at Westminster College.

● Brent Taylor – CEO of Compass Minerals, a company that extracts salt from the GSL.

● Darren Parry – former chairman of the Northwestern Band of the Shoshone Nation.

● John Luft – wildlife biologist at the Utah Division of Wildlife Resources.

● Sydney Schuler – local who has led activism & awareness campaigns on the GSL crisis.

See Appendix B for more information on the groups I reached out to and how I reached
out to them to request consultations. In total, I reached out to over 20 different people to schedule
interviews. Of these, only 3 responded and scheduled a time to meet, and I was only able to
complete two consultations before the deadline. I aimed to create a transcript from each of these
conversations, then code these transcripts and organize the responses into categories, recording
the key concerns, values, questions, and system components that these stakeholders identify.
Coding the transcripts enables quantification of those concepts’ frequency and distribution.
Finally, I usd the approaches described in Helgeson et al (2022) and Cooper et al (2022)
to map out the levers and impacts relevant to the GSL crisis and display the different values
attached to these system components. This graph is a work in progress and is not final or
authoritative, but it is informed by my interviews with stakeholders and my automated analysis.

### Automated stakeholder analysis
In seeking a comprehensive understanding of stakeholder perspectives on the GSL drying
crisis, I employed a technology-based approach to supplement traditional interviews. This
proved instrumental in generating representative, detailed responses from over 30 different
stakeholder groups. See the details in Appendix C. Because I was able to complete only a few
conversations with stakeholders, I decided to supplement the process with an automated
approach. To add more info & help understand stakeholder perspectives, I leveraged technology:
1. Web scraping: I collected and analyzed content from 100+ internet links that discuss the
GSL drying crisis. This method allows sampling the online discussion on the issue.
2. Simulated “interviews” with stakeholders: I used the LangChain framework & the
state-of-the-art AI model GPT-3.5 to automatically generate representative, detailed,
first-person responses to 10+ questions for 30 different stakeholder groups.
Since LLMs (Large Language Models) like the GPT (Generative Pretrained Transformer)
models are trained on real responses from the internet & beyond, they can “average” their
training data and give semi-representative responses of the available responses, which are rooted
in real human responses. These methods are experimental and are not meant to replace actual
conversations with stakeholders.

I conducted this process partly to inform my stakeholder analysis, but also just to explore whether it is possible and to understand the advantages and disadvantages of this approach. There are several key limitations with this process. For instance,
LLMs just predict the most likely next token in a sequence of words but can sometimes generate
erroneous information, misrepresent situations, or merely repeat likely responses without
contributing novel or intriguing content. Therefore, these tools should primarily serve as a means
to add to our understanding human perspectives built through careful listening and interviewing.

I created a list of stakeholders and questions, and used this info to generate AI responses,
where the AI acts as a representative of the stakeholder to semi-intelligently respond to the
questions. To analyze the AI-generated responses, I used data visualizations like word mapping,
along with sentiment analysis, aggregating perspectives by stakeholder groups, and categorizing
the values, facts, methods, and solutions in the responses using AI. See visualizations in
Appendix A, figures 8-11, which show more analysis of the AI-generated and scraped responses.

While this approach yielded a significant amount of information, it was not without its
limitations. Many of the AI-generated responses lacked depth and could be construed as overly
generic. Few of them yielded concrete, interesting, and novel information that would have
surfaced in real human interviews. However, the most promising aspect of this process was the
potential to automate the coding process, which does not require generating new content and
often follows a prespecified approach. This could simplify the time-consuming task of coding
responses from transcripts. Looking ahead, this automated coding process shows substantial
promise for future research. With process supervision, prompt engineering, and gradual
verification of each step, the results could significantly improve. Ultimately, however, the
success of this approach hinges on actual human stakeholder feedback. While AI and automated
processes offer intriguing possibilities for stakeholder analysis, their true value may lie in their
ability to augment and enhance traditional methods. By combining these cutting-edge tools with
careful listening and genuine stakeholder interactions, we can gain a more comprehensive
understanding of complex issues like the GSL drying crisis.

### Visualizations from the process
![image](https://github.com/jerhadf/GreatSaltLakeCrisisAnalysis/assets/16784270/fed71091-0dd7-41e4-881d-bd72fcf6940d)
Figure 9: Bar chart of words used in response to the values question - “What are the most
important values that shape your opinions on the Great Salt Lake and its future? Explain why.”

![image](https://github.com/jerhadf/GreatSaltLakeCrisisAnalysis/assets/16784270/798f5c52-9c4b-4270-9cd5-7a1450398f07)
Figure 10: Frequency of words used in response to values question, grouped by stakeholder
type.

![image](https://github.com/jerhadf/GreatSaltLakeCrisisAnalysis/assets/16784270/ef2668ac-fa30-41a7-b9ac-c8877c1dc7da)
Figure 11: Several graphs of sentiment analysis - higher values indicate higher sentiment. The
score ranges from -1 (most extreme negative) to +1 (most extreme positive), and is an index of
the positivity or negativity of the words used to describe the crisis.

![image](https://github.com/jerhadf/GreatSaltLakeCrisisAnalysis/assets/16784270/fc71bc01-9d03-4714-a404-3dec963232f1)

![image](https://github.com/jerhadf/GreatSaltLakeCrisisAnalysis/assets/16784270/7074e1d9-84d3-42b2-8401-6af7fa1b0fac)

![image](https://github.com/jerhadf/GreatSaltLakeCrisisAnalysis/assets/16784270/b1dd346d-3d90-4ae5-bdc4-317f9ec6a591)

### Appendix C: Details on Automated Stakeholder Analysis
See all details necessary to understand or replicate this process at my public Github link to the
repository, which contains all the code and documentation: https://github.com/jerhadf/GreatSaltLakeCrisisAnalysis

See also the list of stakeholder groups that I used to generate responses for, and the list of
questions I wrote to ask these groups and generate responses to with AI.
Figure 4: Snapshot of code used to generate stakeholder responses to questions with AI
Stakeholder Groups List
1. "Utah Department of Natural Resources"
2. "Utah Division of Water Resources"
3. "Friends of Great Salt Lake"
4. "Great Salt Lake Institute"
5. "Salt Lake City Residents"
6. "Mineral Extraction Industry"
7. "Tourism Industry in Utah"
8. "Academic Researchers on Great Salt Lake"
9. "Native American Tribes with Ties to Great Salt Lake"
10. "Environmental Activists in Utah"
11. "Local Businesses in Salt Lake City"
12. "Outdoor Recreation Enthusiasts in Utah"
13. "Wildlife Conservation Organizations in Utah"
14. "Agricultural Sector in Utah"
15. "Fishing Industry in Utah"
16. "Real Estate Developers in Salt Lake City"
17. "Air Quality Management Agencies in Utah"
18. "Public Health Officials in Utah"
19. "Local Media Outlets in Salt Lake City"
20. "Federal Environmental Agencies (e.g., EPA)"
21. "Utah State Legislators"
22. "Brine Shrimp Harvesters"
23. "Utah Religious Communities"
24. "Spencer J. Cox, Governor of Utah"
25. "Utah Department of Environmental Quality"
26. "Utah Department of Transportation"
27. "Utah Geological Survey"
28. "Great Salt Lake Advisory Council"
29. "Great Salt Lake Audubon"
30. "Young people and youth groups in Utah"

#### Questions for stakeholders
1. “How does the Great Salt Lake drying up affect your personal and professional life?
Provide specific stories or facts from your life.”
2. “What are the advantages or disadvantages of living near the Great Salt Lake? Provide
concrete examples.”
3. “What are the most important values that shape your opinions on the Great Salt Lake and
its future? Please explain why.”
4. “What do you think are the worst impacts of the Great Salt Lake drying up on the
environmental, economic, and social aspects of Utah and beyond?”
5. “What are the most important contributing factors that lead to the Great Salt Lake drying
up?”
6. “What do you think is the best possible solution to prevent or mitigate the Great Salt
Lake drying up? Why?”
7. “What are your views on the current policies or initiatives on the Great Salt Lake and its
water management?”
8. “What are the most difficult obstacles that are stopping effective solutions from being
implemented to manage water and stop the Great Salt Lake from drying up?”
9. “Who do you think are the most important actors that have a stake or influence in the
Great Salt Lake crisis?”
10. “How do you personally communicate or collaborate with other stakeholders or actors on
the Great Salt Lake issue?”

### Values-based mental model
<img width="573" alt="image" src="https://github.com/jerhadf/GreatSaltLakeCrisisAnalysis/assets/16784270/0f03ccd3-5294-4077-9c1e-caf2b77fccf0">

Using the results of the stakeholder consultations,the automated analysis, and my
understanding of the Great Salt Lake drying crisis, I created a map of the system including the
system components, decision levers, and key values. While this map is very incomplete and is
not meant to be authoritative, it provides a guideline and an initial draft of how a more complete
values-based mental model could be created. The map is also editable on Figma at this link: 

https://www.figma.com/file/21N4KcIHPJ57jgPveYa8pp/GSL_system?type=whiteboard&node-id=0%3A1&t=BivMOrecNwEIkcPN-1 
