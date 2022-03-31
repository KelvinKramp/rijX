import urllib

welcome_message_whatsapp = "Stuur een bericht naar RijRotterdam"
welcome_message_whatsapp = urllib.parse.quote(welcome_message_whatsapp, safe='')
welcome_message_whatsapp = "https://wa.me/31683825634?text=" + welcome_message_whatsapp

title1 = """
Een rijbewijskeuring voorbereiden kan ingewikkeld zijn.
"""
text1 = """
RijRotterdam is opgezet om u zo goed mogelijk door een rijbewijskeuring te begeleiden. Communicatie met ons betekent altijd direct contact met een kundige keuringsarts. Er zijn geen secretaresses en managers. Door regelzaken te automatiseren en de management lagen eruit te halen kunnen we rompslomp voorkomen en tevens de prijs van een rijbewijskeuring verlagen.
"""

title2 = """
Waarom rijrotterdam?
"""

text2 = """
We hebben gemerkt dat mensen onnodig veel geld kwijt zijn aan een keuring. Als zorgverleners vinden wij het onverantwoord om een relatief groot bedrag te vragen voor een keuring die gemiddeld 5 tot 10 minuten duurt. 
Van dit geld kan u andere dingen doen die belangrijk zijn voor u gezondheid. Door RijRotterdam op te zetten willen we bijdragen aan uw algemene welzijn. 
"""

title3 = """Hoe maak ik een afspraak?"""
text3 = """
U kan een afspraak maken of komen naar ons inloopspreekuur. Op dit moment zijn we werkzaam in Rotterdam en Capelle aan den IJssel. 
<br>
<br>
De keuring bestaat uit een aantal korte vragen en onderzoeken om uw gezondheid te evalueren. De keuring duurt 5 tot 15 minuten als u gezond bent en u uzelf goed heeft voorbereid. 
Bent u zaken in de voorbereiding vergeten of heeft u één of meerdere aandoeningen dan kan het langer duren. 
<br>

<br>

"""
text3b = """
 mee:
<div><br></div>
<ul>
<li>Uw unieke ZD-code. </li>
<div>
Deze is te vinden op de formulier van het CBR). U kan deze ook later aan ons doorgeven, maar de verwerking van uw keuring duurt dan langer. Als u komt voor een taxipas dan neemt u de papieren gezondheidsverklaring en uw keuringsformulier mee. 
</div>
<div><br></div>
"""

title4 = """Hoe bereid ik mij voor?"""
text4 = """ 
De eerste stap die u moet nemen is het invullen van een gezondheidsverklaring. 
<br>

<br>
Binnen uiterlijk 10 dagen ontvangt u bericht van het CBR met uw verwijzing en het keurverslag. 
Het verslag hoeft u niet zelf in te vullen dit doet de arts.
<br>
<br>
Op het keurverslag staat een ZD-code. Deze neemt u mee naar de keuring bij RijRotterdam. 
Als u een keurverslag heeft gekregen voor een medisch specialist (bv. oogarts, cardioloog of psychiater) dan moet u bij een medisch specialist een afspraak maken.   
"""

title5 = """ Wat neem ik mee?"""
text5 = """U neemt de volgende zaken mee naar een keuring:
<br>
<br>
<ul>
<li><h3>Uw ZD-code</h3></li>
<p>
Neem het formulier met de ZD-code mee. ZD staat voor ZorgDomein. Dit is het systeem waarmee de meeste artsen en specialisten digitaal met elkaar communiceren. 
Eventueel kan u de ZD-code ook later aan ons doorgeven, maar de verwerking van uw keuring duurt dan langer. 
Als u komt voor een taxipas of touringscarchauffeurs keuring dan heeft u geen ZD-code nodig, maar dan neemt u de papieren gezondheidsverklaring en uw keuringsformulier mee. 
</p><br>
<li><h3>Uw rijbewijs of paspoort</h3></li>
<p>
We hebben een identiteitsbewijs nodig om te verifieren dat u het bent.  
</p><br>
<li><h3>Uw bril</h3></li>
<p>
Alleen als u uw bril nodig heeft voor veraf (“tv-bril”). De bril is nodig om u zicht te meten. 
</p><br>
<li><h3>Uw urine</h3></li>
<p>
Neem urine mee in een potje. U kan een potje bij de apotheek of drogist kopen. Als u geen urine meeneemt dan zal u moeten plassen in een potje tijdens de keuring en duurt de keuring langer. 
</p><br>
<li><h3>Medicatie overzicht</h3></li>
<p>
Indien u voor meer dan alleen een 75+ keuring of medische keuring komt neem dan uw medicatie-overzicht of medicijn doosjes mee (aan te vragen bij huisarts / apotheek)
</p><br>
<li><h3>Indien nodig, bloeddruk meting huisarts</h3></li>
<p>
Het is niet noodzakelijk een bloeddruk meting van de huisarts of thuis mee te nemen. Echter kan het wel zaken vergemakkelijken. Sommige mensen hebben namelijk een hoge bloeddruk 
in de buurt van zorgpersoneel (de zogenaamde "witte-jassen hypertensie"). Dit kan leiden tot een langere tijdsduur van de keuring of aanvullende vragen van het CBR. 
</p><br>
</ul>
"""

title6 = """Hoe krijg ik de uitslag? """
text6 = """Vanaf het moment dat het keuringsrapport is ontvangen door het CBR is de status van uw aanvraag binnen één 
week te zien in Mijn CBR. Bent u gezond en zijn er geen aanvullende vragen naar aanleiding van de keuring dan duurt het op basis van 
onze ervaring een aantal dagen voordat het CBR reageert. Heeft het CBR extra vragen dan kan u een foto van de aanvullende vragen 
mailen via onze beveiligde email platform zodat wij zo snel mogelijk de aanvullende informatie aan het CBR kunnen doorgeven.

<br>
<br>
Als u goedkeuring heeft gehad van het CBR dan kan u naar het gemeentehuis om uw rijbewijs te verlengen!
"""

title7 = """Het CBR heeft aanvullende vragen, wat moet ik doen?"""
text7 = """Formulieren met aanvullende vragen kunt u sturen naar: info@rijrotterdam.nl of via whatsapp. Wij streven ernaar binnen 3 werkdagen de aanvullende vragen te beantwoorden.  """

texts_landingpage = {
    "title1":title1, "text1":text1, "title2":title2, "text2":text2, "title3":title3, "text3":text3, "title4":title4, "text4":text4, "title5":title5, "text5":text5, "title6":title6, "text6":text6, "title7":title7, "text7":text7
}

title1_inloop = """
Datums inloopspreek uur
"""

text1_inloop = """
Op dit moment staan er de volgende inloopspreekuren gepland:
<br>
 - van 14:00 tot 17:00 op vrijdagmiddag in Capelle aan den IJssel
 <br>
 - van 14:00 tot 17:00 op vrijdagmiddag in Rotterdam
 
 <br>
  <br> <br>

<img
src="/static/img/incarpackage_small.jpg"
style="margin-bottom: 20px;   margin-left: auto;
margin-right: auto;
 box-shadow: 4px 10px 30px #deeaf5;
width: 100%;
border-radius: 10px;"
/>

"""

texts_inloopspreekuur = {
    "title1":title1_inloop, "text1":text1_inloop, "title2":title5, "text2":text5
}

title1_mijnkeuring = """
Mijn keuringsverslag
"""

text1_mijnkeuring= """
Medische metingen die plaats vinden zijn uw eigendom, u heeft daarom altijd recht op inzage. Wij maken de inzage makkelijk voor u met mijnkeuringsverslag. 
Na een keuring kan u uw rapport via deze pagina opvragen. 
Via een beveiligde mail verbinding ontvangt u het rapport wat naar het CBR is gegaan. 
"""

texts_mijnkeuring = {
    "title1": title1_mijnkeuring, "text1": text1_mijnkeuring
}

title1_aboutus = "Ons team"
title1b_aboutus = """
Een betere vorm van zorg 
"""
text1_aboutus = """
Technologie staat vaak in de weg in plaats van dat het ons helpt. 
Dit kan en moet anders. Wij zijn een team artsen en software developers die samen betere vorm van zorg willen bieden. 
Ons doel is om artsen en patienten dichter bij elkaar te brengen.
<br><br>
Ons team bestaat uit: 
<br>
"""

title2_aboutus = """
Open source
"""

title2b_aboutus = """
Open source software als de weg tot een beter welzijn 
"""

text2_aboutus = """
We willen dat minder artsen afhankelijk worden van het huidige complexe en logge zorgsysteem. We geloven dat het democratiseren van de technische middelen die de gezondheidszorg efficienter maken zal leiden tot kwalitatief betere zorg op de langere termijn.
<br><br>
De sjablooncode van deze website is openbaar. Mochten er artsen, verpleegkundigen of fysiotherapeuten zijn die hun diensten willen aanbieden met hetzelfde sjabloon dan hoeven zij enkel de code te downloaden, eenvoudige aanpassingen te maken en te gebruiken voor het medisch doel waarvoor zij dit willen gebruiken.

<br><br>
Wat is het voordeel ten opzichte van bijvoorbeeld WordPress? Ten eerste WordPress is niet veilig: 
<a href="https://www.hipaavault.com/hipaa-wordpress/is-wordpress-hipaa-compliant/#:~:text=Simply%20because%20at%20its%20core,by%20a%20host%20of%20vulnerabilities." style="text-decoration: underline;">
"out-of-the-box WordPress software is not secure for the storage or transfer of protected health information (PHI)."
</a>. Door deze website te koppelen aan Zivver, ZorgMail of SmartLockr kan je veilig patienten gegevens verzenden en ontvangen van patienten, clienten en collega zorgverleners. 
<br><br>
Ten tweede, wordt er continu gewerkt om de functies van de administratie zo gebruikersvriendelijk mogelijk te maken voor zorgprofessionals
 en te zorgen dat deze up-to-date zijn met de laatste ICT ontwikkelingen. Dit is een proces wat buiten de sfeer van open source software erg traag gaat en vaak 
 helemaal stil staat. Door samenwerking met de open source community is vaak veel meer mogelijk. <br><br> 
"""

title3_aboutus = """
Vacatures
"""

title3b_aboutus = """
Overzichtelijke management systemen
"""

text3_aboutus = """
Wil je bij ons komen werken als arts, stuur dan een bericht via onze contactpagina. We hebben een overzichtelijk boekingssysteem gemaakt door en voor artsen. Bij ons zijn er geen verborgen overhead kosten. <br><br>
Ben je een arts en zzper en wil je ook keuringen doen en wil je helemaal zelf aan de slag, gebruik onze software. Je kan de code aanpassen voor jouw persoonlijke visie op verbetering van de zorg. Je hebt een zorgdomein account nodig en een google marketing account zodat klanten jou kunnen vinden. Je kan de instructies voor het lanceren van jouw website volgen op de GitHub pagina. 
Als je basiskennis hebt van HTML dan zou het niet langer dan een paar uur moeten duren om alles gereed te krijgen. Kom je er desondanks toch niet uit dan kan je ons vragen om je verder te helpen.
<br><br>
Door technologie beter te gebruiken sta je in direct contact met patienten op ale niveaus. Dit betekent voor patienten een snelle afhandeling en voor jou minder rompslomp. 
"""

texts_aboutus = {
    "title1": title1_aboutus,"title1b": title1b_aboutus, "text1": text1_aboutus,
    "title2": title2_aboutus, "title2b": title2b_aboutus, "text2": text2_aboutus,
    "title3": title3_aboutus, "title3b": title3b_aboutus, "text3": text3_aboutus
}


title1_contact = "Onbeantwoorde vragen?"
title1b_contact = "Neem contact met ons op"
text1_contact = ""
texts_contact = {
    "title1": title1_contact, "title1b": title1b_contact, "text1": text1_contact,
}

title1_inhoudkeuring = """
De inhoud van een keuring
"""
title1b_inhoudkeuring = """
"""
text1_inhoudkeuring = """
<h3>Tijdens de keuring</h3>
<p>
Tijdens de keuring wordt gekeken of iemand aan de normen voldoet om zelfstandig en veilig een voertuig te besturen. De arts beoordeelt de algemene lichamelijke en geestelijke conditie. Indien nodig wordt er gekeken naar specifieke onderdelen van de gezondheid zoals het functioneren van armen, benen of de wervelkolom. Daarnaast wordt de bloeddruk gemeten en het bloed of de urine gecontroleerd op diabetes. Bij de rijbewijskeuring test de arts ook de gezichtsscherpte (zonder en met eventuele bril of contactlenzen).
</p>
<br>
<h3>Medicatie</h3>
<p>
Neem een lijst met medicijnen mee als u deze gebruikt en u voor een keuring voor diabetes, nieren, psychiatrie, longen of overige ziekten komt. Als u komt voor een keuring nieren neem dan ook de restfunctie van de nieren mee. U kan een uitdraai hiervan vragen aan uw internist, nefroloog of huisarts.  
</p>
<br>
<h3>Bloeddruk</h3>
<p>
De bloeddruk kan hoger dan gewoonlijk zijn tijdens een keuring. Dit noemt met "witte-jassen hypertensie". U hoeft zich niet per se gespannen of gestresst te voelen om een hoge bloeddruk te hebben. Dit kan zich ook voordoen terwijl u zich niet gespannen voelt. De mate van stress die u ervaart is geen goede indicator voor de bloeddruk. Als u bekend bent met een hoge bloeddruk is het handig om thuismeting mee te nemen of een meting van de huisarts mee te nemen. De thuismetingen moeten wel zijn gedaan met een geijkte bloeddrukmeter. Dit betekent dat de bloeddrukmeter moet zijn gecontroleerd door de huisarts om te zien of er meetfouten in zitten. 
</p>
<br>
<h3>Urine</h3>
<p>
De urine wordt onderzocht op suiker. Als u suikerziekte (diabetes) heeft dan plast u meer suiker uit dan normaal. Dit kan terug worden gezien in de urine. In sommige gevallen doet de arts een onderzoek die ook gelijk kijkt naar andere dingen in de urine. Dit lkunnen zaken zijn zoals afweercellen, rode bloedcellen of bacterien in de urine. Als u de uitslag hiervan wilt hebben kan u dat bespreken met de arts.  
</p>
<br>
<br>
<div style="text-align: center;
justify-content:center;">
<img
src="/static/img/urine.jpg"
style="margin-bottom: 20px;   margin-left: auto;
margin-right: auto;
 box-shadow: 4px 10px 30px #deeaf5;
width: 50%;
border-radius: 10px;"
/>
</div>
              
<br>
<br>
<h3>Gezichtsscherpte</h3>
<p>
Tijdens de keuring wordt ook gekeken naar uw gezichtsscherpte. Er wordt een zogenaamde visuskaart op afstand gebruikt. U moet zeggen waar de opening in een cirkel zit.  Als u boven de 0.5 scoort tijdens deze test dan is uw gezichtsscherpte voldoende voor het autorijden. Lager scoren dan de norm kan aan verschillende zaken liggen. Het kan zijn dat uw bril of lenzen niet goed zijn afgesteld, maar wat we ook vaak tegenkomen is staar. Dit is een aandoening die veel voorkomt bij ouderen en goed te behandelen is door een oogarts. Om te vermijden dat men afgekeurd wordt op een onvoldoende gezichtsvermogen kan men van tevoren naar een opticien gaan. 
</p>
<br>
<p>
Hieronder ziet u hoe het zicht wordt getest. U vertelt telkens waar de opening zit: boven, links, rechts of onder. 
</p>
<br>
<div style="text-align: center;
justify-content:center;">
<img
src="/static/img/landoltc.png"
style="margin-bottom: 20px;   margin-left: auto;
margin-right: auto;
width: 25%; box-shadow: 4px 10px 30px #deeaf5;
width: 50%;
border-radius: 10px;"
/>
</div>

<br>
<br>
<h3>Gezichtsveld</h3>
<p>
Het gezichtsveld onderzoek bestaat uit een klein onderzoek waarbij de arts kijkt naar de grootte van uw gezichtsveld. In zeldzame gevallen, vooral op oudere leeftijd, kunnen mensen onbewust een aandoening (bv. een beroerte) hebben gehad die ertoe leidt dat een deel van het zicht wegvalt. In dit geval kan het gevaarlijk zijn om auto te rijden. 
</p>
<br>
"""

texts_inhoudkeuring = {
    "title1": title1_inhoudkeuring, "title1b": title1b_inhoudkeuring, "text1": text1_inhoudkeuring,
}