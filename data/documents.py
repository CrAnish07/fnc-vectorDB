from langchain.schema import Document

def get_cwc_documents():
    return [

        #Chelsea
        Document(
            page_content="Enzo Fernández (Argentina) controlled Chelsea’s midfield with 2 assists and 89% pass accuracy across the tournament.",
            metadata={"club": "Chelsea"}
        ),
        Document(
            page_content="Christopher Nkunku (France) scored 3 goals and assisted once, emerging as a key finisher in Chelsea’s title win.",
            metadata={"club": "Chelsea"}
        ),
        Document(
            page_content="Reece James (England) provided 2 assists and maintained a 91% tackle success rate from right-back.",
            metadata={"club": "Chelsea"}
        ),
        Document(
            page_content="Cole Palmer (England) scored 4 goals, including two in the final, and created 9 chances.",
            metadata={"club": "Chelsea"}
        ),
        Document(
            page_content="Robert Sánchez (Spain) kept 3 clean sheets with 11 key saves as Chelsea's main goalkeeper.",
            metadata={"club": "Chelsea"}
        ),

        # PSG
        Document(
            page_content="Ousmane Dembélé (France) contributed 1 goal and 3 assists, excelling on the attacking side.",
            metadata={"club": "Paris Saint-Germain"}
        ),
        Document(
            page_content="Desire Doure (France) contributed 2 goal and 2 assists.",
            metadata={"club": "Paris Saint-Germain"}
        ),
        Document(
            page_content="Gianluigi Donnarumma (Italy) made 15 saves and had 2 clean sheets, standing out in goal.",
            metadata={"club": "Paris Saint-Germain"}
        ),
        Document(
            page_content="Vitinha (Portugal) maintained 92% passing accuracy and contributed heavily in transitions.",
            metadata={"club": "Paris Saint-Germain"}
        ),

         # Real Madrid
        Document(
            page_content="Kylian Mbappé (France) scored 2 goals and assisted once.",
            metadata={"club": "Real Madrid"}
        ),
        Document(
            page_content="Gonzalo Garcia (Spain) scored 4 goals and 3 assist.",
            metadata={"club": "Real Madrid"}
        ),
        Document(
            page_content="Jude Bellingham (England) scored 2 goals and completed 87% of his passes for Real Madrid in the semifinals.",
            metadata={"club": "Real Madrid"}
        ),
        Document(
            page_content="Vinícius Júnior (Brazil) had 1 goal and 2 assists, showcasing his trademark flair for Real Madrid.",
            metadata={"club": "Real Madrid"}
        ),
        Document(
            page_content="Thibaut Courtois (Belgium) made 13 saves and kept 2 clean sheets, anchoring Real Madrid’s defense.",
            metadata={"club": "Real Madrid"}
        ),

         # Inter Milan
        Document(
            page_content="Lautaro Martínez (Argentina) scored 2 goals and won 12 duels, leading Inter's frontline.",
            metadata={"club": "Inter Milan"}
        ),
        Document(
            page_content="Nicolò Barella (Italy) provided an assist and made 18 ball recoveries in midfield.",
            metadata={"club": "Inter Milan"}
        ),
        Document(
            page_content="Federico Dimarco (Italy) delivered 2 key passes per match and had a crossing accuracy of 41%.",
            metadata={"club": "Inter Milan"}
        ),

        # Bayern Munich
        Document(
            page_content="Harry Kane (England) scored 3 goals and was Bayern Munich’s top scorer in the competition.",
            metadata={"club": "Bayern Munich"}
        ),
        Document(
            page_content="Jamal Musiala (Germany) contributed 1 goal and 2 assists, dazzling with his dribbling and creativity.",
            metadata={"club": "Bayern Munich"}
        ),
        Document(
            page_content="Joshua Kimmich (Germany) maintained 93% passing and led with 21 interceptions in 3 games.",
            metadata={"club": "Bayern Munich"}
        ),

         # Atletico Madrid
        Document(
            page_content="Antoine Griezmann (France) scored 2 goals and created 6 chances during Atletico’s campaign.",
            metadata={"club": "Atletico Madrid"}
        ),
        Document(
            page_content="Jan Oblak (Slovenia) made 13 saves and kept 1 clean sheet in the tournament.",
            metadata={"club": "Atletico Madrid"}
        ),
        Document(
            page_content="Rodrigo De Paul (Argentina) averaged 88% pass completion and contributed defensively with 14 tackles.",
            metadata={"club": "Atletico Madrid"}
        ),


        # Fluminense (Brazil)
        Document(
            page_content="Germán Cano (Argentina) scored 2 goals, continuing his impressive scoring form for Fluminense.",
            metadata={"club": "Fluminense"}
        ),
        Document(
            page_content="André (Brazil) anchored midfield with 90% passing and 19 recoveries.",
            metadata={"club": "Fluminense"}
        ),

         # Borussia Dortmund
        Document(
            page_content="Karim Adeyemi (Germany) scored once and had the fastest sprint speed of the tournament.",
            metadata={"club": "Borussia Dortmund"}
        ),
        Document(
            page_content="Julian Brandt (Germany) registered 1 goal and 2 assists, leading Dortmund’s midfield creativity.",
            metadata={"club": "Borussia Dortmund"}
        ),
        Document(
            page_content="Gregor Kobel (Switzerland) made 12 saves and kept 1 clean sheet for Dortmund.",
            metadata={"club": "Borussia Dortmund"}
        ),

        # --- Inter Miami ---
        Document(
            page_content="Lionel Messi (Argentina) scored 3 goals and assisted 1, showing his enduring brilliance.",
            metadata={"club": "Inter Miami"}
        ),
        Document(
            page_content="Sergio Busquets (Spain) controlled tempo with 93% pass accuracy and 25 recoveries.",
            metadata={"club": "Inter Miami"}
        ),
        Document(
            page_content="Jordi Alba (Spain) delivered 1 assist and made 9 crosses from the left.",
            metadata={"club": "Inter Miami"}
        ),

        # --- Juventus ---
        Document(
            page_content="Kenan Yildiz (Turkey) scored 2 goals and had 13 shot attempts in the competition.",
            metadata={"club": "Juventus"}
        ),
        Document(
            page_content="Francisco Conceição (Portugal) had 1 goal and 3 successful dribbles per match.",
            metadata={"club": "Juventus"}
        ),

        # --- Flamengo ---
        Document(
            page_content="Gabriel Barbosa 'Gabigol' (Brazil) scored twice, continuing his impressive FCWC form.",
            metadata={"club": "Flamengo"}
        ),
        Document(
            page_content="Giorgian De Arrascaeta (Uruguay) assisted 2 goals and created 7 key chances.",
            metadata={"club": "Flamengo"}
        ),

        # --- Benfica ---
        Document(
            page_content="Ángel Di María (Argentina) scored 1 goal and completed 89% of his passes in midfield.",
            metadata={"club": "Benfica"}
        ),
        Document(
            page_content="António Silva (Portugal) led Benfica's defense with 19 clearances and 6 tackles.",
            metadata={"club": "Benfica"}
        ),

        # --- Al Hilal ---
        Document(
            page_content="Rúben Neves (Portugal) dictated tempo with 91% pass accuracy and 3 long-ball assists.",
            metadata={"club": "Al Hilal"}
        ),
        Document(
            page_content="Kalidou Koulibaly (Senegal) had 17 defensive actions and 2 clean sheets.",
            metadata={"club": "Al Hilal"}
        ),

        # --- Monterrey ---
        Document(
            page_content="Sergio Ramos (Spain) led the team with 35 defensive actions and 2 clean sheets.",
            metadata={"club": "Monterrey"}
        ),
        Document(
            page_content="Rogelio Funes Mori (Mexico) scored 2 goals and won 7 aerial duels in Monterrey's campaign.",
            metadata={"club": "Monterrey"}
        ),
        Document(
            page_content="Luis Romo (Mexico) contributed with 1 assist and 20 recoveries from defensive midfield.",
            metadata={"club": "Monterrey"}
        )
    ]