import streamlit as st

# Content general
# ---------------

def title_page():
    st.title("The long Fight of the norwegian Sami for Recognition")
    st.write("This WebApp was desighned to show the work of the Study Week Human and Social Sciences at the Seminar for Nordic Studies at the University of Basel.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/1b/Sami_flag.svg", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

def milestones_page():
    st.title("Introduction")
    st.write("The Norwegian state made a conscious effort over more than 100 years to assimilate the Sami. The policy was introduced in the field of culture “with schools as the battlefield and teachers as the frontline soldiers”. Language was the main subject being a measure and symbol of success of the policy. The so-called Fornorsking or English norweganization builds a spereate era of the Sami’s history both historically and in a contemporary perspective from around 1850-1980.")
    st.write("During the 19th century education became the cornerstone of any western state. The Sami which were clearly distinct people, living in certain places, in concentrated communities. This problem called for a national policy. While the policy of assimilation is inseparable from the emergence of any strong state Norway’s differentiates itself thought their determined, continuous and long-lasting conduct of their assimilation policy. This makes it morally problematic and sensitive to this very day.")
    st.image("Gian1.png")
    st.write("The Human Rights of the Sami")
    current_year = st.select_slider("Timeline", options=milestones.keys())
    milestone = milestones[current_year]
    milestone()
    st.title("Effects and todays Knowledge")
    st.write("The Norwegian state required the Sami to be something they’re not. The State’s efforts to make the Sami drop their language, change the basic values of their culture and extensively change their national identity were long lasting and determined. The restructuring of social institutions had a profound consequence on the individuals of the Sami community’s individual relationships with each other. The state’s efforts to eradicate all parts of Sami culture were only made easier through everyday racism and the Norwegians superiority complex. The states policies resulted in a massive downgrade of the Sami people and a feeling of powerlessness causing social unrest throughout the modernization and norweganization period. Experts agree that without the Finnish menace the government’s norweganization policy would not have been conducted as strictly over such a long period of time. The authorities policies against the Sami were characterized by national, social darwinistic and racist motives. The marginalization welts of assimilation measure in wide context. The powerlessness of the sami during the norweganization period left detrimental social-psychological consequences. When you receive such immense pressure from your surrounding and it is sufficiently strong and persistent this marks one’s self-image, undermines your own self-respect and self-esteem, at worst cause self-contempt and an exageratingly critical attitude towards own members of one’s group.")
    st.title("Identity and Self-Esteem")
    st.write("Norwegian literature contain numerous descriptions of school’s injustice towards children on the basis of social position and conditions of class. Famous Norwegian literature includes Bjørnstierne Bjørnson’s peasant stories and the novels of Arne Garborg contains examples of the abuse suffered by Sami scholars in the more than 50 boarding schools and 70 classrooms across Norway.")
    st.title("Social-Psychological Consequences")
    st.write("Going forward we ask ourselves: How did schoolchildren themselves experience their encounter with school? What were the consequences of the norwegianization policy for young people’s development in a critical phase of their lives?")

def Sami_page():
    st.write("Who are the Sami?")
    st.title("Definition")
    st.write("The Sami are indigenous inhabitants in Nordic countries. According to the law of Sami, a person is a Sami if they define themselves as Sami and if they speak Sami as their native language or if their ancestors are Sami. Today, the Sami are a minority in their own area called Sápmi. Sápmi is their traditional settlement area that extends over Finland, Norway, Sweden and Kola Peninsula in Russia. Overall, there are approximately 80’000-100’000 Sami in Sápmi.")
    st.image("http://homepagedesigner.telekom.de/imageprocessor/processor.cls/CMTOI/cm4all/com/widgets/PhotoToi/11/39/37/40/13cc12d4059/scale_1200_0%3Bdonotenlarge/13cc12d4059")
    st.title("The Life of the Sami People ")
    st.write("For hundreds of years, the Sami people spent their lives roaming around the forests of Scandinavia as hunter-gatherers following wild herds of reindeer. In order to sustain survival during the harsh winter the Sami would process reindeers and other animals like bears to food and clothes or even to build shelter. During summer they would fish and gather wild plants to eat. Their nomadic lifestyle required their housing to be lightweight and handy. The nights would be spent in a hide tent, a “Lavvu”. They also built permanent houses called “Gamma” or “Goahti”. Over the last century the Sami’s lifestyle has drastically changed. They continue to practice elements of their traditional lifestyle but most Sami live a lifestyle similar to a modern western suburban family. Today around 60 % engage in modern jobs in the tourism, music, media or art.")
    st.image("https://a4.pbase.com/g1/15/210915/2/103740811.Kfyh7Prg.jpg")
    st.title("The Religion of the Sami People")
    st.write("Early documents describe the Sami as pagans. The Sami used to practice a natural religion. According to their belief, the world was divided into three spheres: the subsurface, the earthly and the heavenly sphere. Every sphere has its own gods and beings. The Sami people were later christianized by the state and the church. Today the Sami’s old religion is not commonly practiced amongst members of the culture.")
    st.title("The Clothing of the Sami People")
    st.write("The traditional Sami garment is the “Gakti”. It is a long colorful tunica worn over leggings. The “Gakti” is traditionally blue, red and yellow. Originally, it was made from fur but later they used cotton, wool and silk. The Sami use silk scarves, silver jewelry and hats as accessories.")
    st.image("https://2.bp.blogspot.com/-x3mZjNyQcpI/Wdl4I_aqONI/AAAAAAAAZ8U/HmxIutGYZUo1HAXAPr2oP9nO0Bvo4eN1ACLcBGAs/s400/3.jpg")

def Language_page():
    st.write("Cultural and Linguistical Development")
    st.title("The Sami Language and it's Language Development")
    st.write("The Sami languages are part of the Finno-Ugric language family. The languages spoken in Finland, Russia, Sweden but mainly in Norway are often considered dialects of the same language. The most spoken language is northern Sami.")
    st.write("Though the language can be related to finish or Scandinavian languages their origins are unclear. It is presumed that the language first developed on the southern side of  Lake Onega and Lake Ladoga, spreadingfrom there. On their journey the Sami speaking people encountered dialects of other ancient languages which are extinct today, but they adapted some of their words into their own language making it difficult today to properly derive where the language originated from.")
    st.write("To this day Sami is largely transmitted orally. There is only little literature like newspaper reports or letters making it difficult to say how the language changed over time. Due to the lack of a uniform orthography Sami languages cannot be used easily in education or government. Most people that speak Sami today are bilingual in the native language of the country they live in.")
    st.write("The first ever written information about the Sami was published by a Roman called Tacitus in the year 98 B.C., calling the people Fenni. This proves that the Sami culture goes further back than most modern languages spoken today.")
    st.image("sami-map1.png")

def Human_page():
    st.write("Human Rights")
    st.title("The Definition of Human Rights")
    st.write("Human rights are rights we obtain simply based on being human. Interestingly, they are not granted by any states. Each state can adapt and include human rights in their own system of law, but they are not obliged to do so. These rights are fundamental for all human beings in our world, regardless of nationality, race, religion, sex, language or any other status. Human rights are quite basic, including for example, as in Article 1: All human beings are born free and equal in dignity and rights. The equality mentioned is based on the freedom of discrimination.")
    st.title("History of the Human Rights")
    st.write("The Great Assembly of the UN, established in 1948, published the Universal Declaration of Human Rights, which was the first legal document that protecting all human beings  universally. Before this we saw certain groups of people being discriminated in the constitution of each individual country. This was a big step in fighting against all kinds of discrimination, from racism to sexism, even though we do not stop at that.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Flag_of_the_United_Nations.svg")
    st.title("Adaptation of the Countries")
    st.write("All countries include at least one of the nine obligations in their national law system. 80% of the countries included four or more. If a country was to violate against a law, a trial will be held, because of the country’s violation of International Human Rights Law. The countries should consider those three points mentioned below.")
    st.title("The three Obligations")
    st.write("The obligation to respect means the States must refrain from interfering with or curtailing the enjoyment of human rights.")
    st.write("The obligation to protect requires States to protect individuals and groups against human rights abuses.")
    st.write("The obligation to fulfill means States must take positive action to facilitate the enjoyment of basic human rights.")


def Podcast_page():
    st.write("Podcast")
    st.title("Our Podcast")
    st.audio("Podcast_final.mp3", format = "audio/mp3", start_time=0)






# Milestones content
# ------------------



def milestone_year_1850():
    st.title("Transitional Phase")
    st.write("The history of the Sami’s can be divided into five phases. The first is the transitional phase lasting from 1850-1870. The first generation of Norwegian senior civil servants saw the Sami and their language as having an equal footing as the Norwegian’s, very much in accordance to the humanistic and romantic ideals of the period. N.V. Stockfleth firmly believed it was a human right to speak ones native language. This liberal idea was opposed by the Norwegian upper class, the Finnmark, especially as Stockfleth mentioned the equal footing of the Sami in terms of cultural policy. His ideas would be vehemently debated in the Storting, the Norwegian parliament, in 1848.")
    st.image("Gian2.jpeg")

def milestone_year_1851():
    st.title("First Phase")
    st.write("In the first phase of Sami assimilation the government focused its measures on Sami living in transitional districts. A special item in the Norwegian national budget, the Finnefondet or English Lappfund, was created in 1851 in order to bring about change in the language and culture of the Sami. This event marks the beginning of the period of assimilation of the Sami. Through this fund the Norwegian p arliament wanted to ensure “enlightenment” of the Sami people.")
    st.image("Gian3.jpeg")

def milestone_year_1860():
    st.title("Tromsø siocese suspicions")
    st.write("In the late 1860s the directors of Tromsø diocese became suspect of Sami teachers. They saw the policy of norweganization ‘‘as much a matter of welfare for the vast majority of the North Norwegian Lappish and Kven population. Norwegianisation paves the way for development and progress even for these people")
    st.image("Gian4.jpeg")

def milestone_year_1870():
    st.title("Consolidation Phase")
    st.write("During the consolidation phase from 1870-1905 the Storting tightened its measures. This was mainly due to the measures taken previously not having the desired effect and the Norwegian language even being in decline among the Sami people. While the measures taken in the first phase were motivated by civilizing and nationalistic consideration, the security policy was mainly highlighted for the measures taken during the consolidation phase. In 1880 the Storting decided all Sami children had to learn, speak, read and write in Norwegian. The clause mentioning the children’s rights to learn their native language was revoked. Teachers who were unable to demonstrate the desired results would not be given a wage increase. For a teacher in service for seven years this could result in a 23-30 % pay cut. Sami teachers saw no point in applying for the increase while it made Norwegian teachers financially dependent on the wage increase. This marked the final breakthrough for Norway’s strict norweganization policy. The final and most long-lived instruction was the Wexelsen decree issued in 1898. The Wexelsen decree saw that the use of the Sami language would strictly be limited to what was necessary, it even forbid children to speak their native tongue during brake time.")


def milestone_year_1905():
    st.title("Culmination Phase")
    st.write("During the culmination phase from 1905-1950 measures previously launched were consolidated and ideologies were firmly cemented. The Versailles peace treaty changed the borders of northern Fennoscandia and Norway now shared a common border with Finland and Russia. The security threat Norway faced grew larger after the Russian revolution. The inter-war years were marked by the shielding off from the Finnish and the inner offensive launched against the Sami. With Charles Darwin’s theory of evolution these ways of discrimination against the Sami people further progressed. In 1902 it became illegal for merchants to trade with people who didn’t speak Norwegian and schools were prohibited from using the Sami languages at all. This went on until after the Second World War when multiple studies were conducted on schools and the education system.")

def milestone_year_1921():
    st.title("Camouflaging the Norweganization Policy")
    st.write("In 1921 the ministry of education tried to camouflage the norweganization policy as “special grants for elementary schools in Finnmark’s rural districts.")

def milestone_year_1923():
    st.title("Christian Brygfield")
    st.write("The director of schools from 1923-1935 Christian Brygfield shaped the inter-war years fundamentally. His stubborn and rigorous practice rejected all points made by the Sami from a clearly racial point of view. According to him the assimilation of the Sami was a clearly indisputable civilizing task for the Norwegian state because of the Norwegian’s racial superiority.")

def milestone_year_1931():
    st.title("Finnmarksnemden")
    st.write("In 1931 the Finnmarksnemden or English the Finnmark board was established. A boarding school initiative was launched initially to serve as border fortification in Sami dominated areas.")

def milestone_year_1936():
    st.title("Elementary School Act")
    st.write("The elementary school act of 1936 established differential treatment the Sami and Kven. The Sami enjoyed special rights as they were seen as old indigenous of northern Fennoscandinavia while the Kven were viewed as old immigrants to Norway.")

def milestone_year_1950():
    st.title("Termination phase")
    st.write("During the termination phase from 1950-1980 the instructions from 1898 remained in force until the Sami commission’s recommendation debated in the Storting in 1963. In the 1960s the Sami obtained the right to practice their culture and beliefs openly. This changed everything for Sami in Norway. Sami was now allowed to be taught in school and the fear of the language going extinct was decreasing.")

def milestone_year_1979():
    st.title("Alta Controversy")
    st.write("The end of the Sami assimilation era is marked by the Alta controversy from 1979-1981. In 1978 the Norwegian Water Resources and Energy Directorate planned construction of a dam and a hydroelectric power plant which an artificial lake would be needed for. In order to construct the artificial lake the Sami village of Máze would have to be inundated. The directorate’s plan were met with strong opposition from the Sami resulting in the Alta controversy. The Alta controversy became a symbol of the Sami’s fight against the cultural discrimination faced by the Norwegian government in a collective aspect for both their political autonomy and their material rights.")
    st.image("Gian5.jpeg")

def milestone_year_1980():
    st.title("Sami Delegation Meetings")
    st.write("From 1980-1981 meetings were held with a Sami delegation. The Sami’s delegation was appointed by the Norwegian Sami Association, the Sami Reindeer Herder’s Association of Norway and the Norwegian Sami council. After the meetings committees to discuss the Sami’s cultural issues and one the Sami Rights Committee addressing the Sami’s legal relations were establishes as a result. The Sami Rights Committee proposed a body democratically elected by the Sami. This resulted in the Sami Act of 1987, the 1988 amendment of the Norwegian constitution and the adaptation of the Finnmark Act in 2005.")

def milestone_year_1987():
    st.title("Sami Act")
    st.write("The Sami Act of 1987 stipulated the responsibilities and powers of the Norwegian Sami parliament and was passed by the Norwegian Parliament on the 12th of June 1987 and took effect on the 14th of February 1989. The first session of the Sami parliament was opened by King Olav V and held on the 9th of October 1989. It sought to enable the Sami people to safeguard and develope their language, culture and way of of life.")
    st.image("Gian6.jpeg")

def milestone_year_1989():
    st.title("Sameting")
    st.write("Sami concerns only found little attention in Norwegian state politics. In addition assert themselves in the majority-based parliaments. In 1964 the Sami were granted advisory functions to the Norwegian parliament on Sami matters through the Sami council. The turning point came in 1989 when the Sami parliament, the Sameting, was opened. From this point on the Sami received further competences. Norways national broadcasting company, the NRK, has its own Sami division. They were now able to make their own decisions in areas like education. This is incredibly important for maters like material science. Most Sami artifacts, spread through museums across Europe, can not be conserved through traditional white-European conservation methods. The Sami language was only recently fixated in writing and through assimilation conservation methods were unable to be passed down. Today, institutions now try to recoup the knowledge lost and rediscover the Sami ways of conservation. Many fear that the rise of the internet will bring the incipient of  language death. The university of Tromsø has a big subject are for Sami languages in which they try to build a new technological linguistic infrastructure. ")
    st.image("Gian7.jpeg")




# Config
# ------

milestones = {1850: milestone_year_1850, 2051: milestone_year_1851, 1860: milestone_year_1860, 1870: milestone_year_1870, 1905: milestone_year_1905, 1921: milestone_year_1921, 1923: milestone_year_1923, 1931: milestone_year_1931, 1936: milestone_year_1936, 1950: milestone_year_1950, 1979: milestone_year_1979, 1980: milestone_year_1980, 1987: milestone_year_1987, 1989: milestone_year_1989}
sections = {"Home": title_page, "Who are the Sami?": Sami_page, "Cultural and Linguistical Development": Language_page, "Human Rights": Human_page, "The Human Rights of the Sami": milestones_page, "Podcast": Podcast_page}


# Run
#----


def main():
    st.set_page_config(layout="wide")
    st.sidebar.write("Contents")
    section = st.sidebar.selectbox("Jump to specific Sections", sections.keys())
    selected_section = sections[section]
    selected_section()

    
if __name__ == "__main__":
    main()
