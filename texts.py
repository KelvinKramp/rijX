import urllib


welcome_message_whatsapp = "Stuur een bericht naar RijRotterdam"
welcome_message_whatsapp = urllib.parse.quote(welcome_message_whatsapp, safe='')
welcome_message_whatsapp = "https://wa.me/31683825634?text=" + welcome_message_whatsapp

title1 = """
Kundige artsen, korte lijntjes, scherpe prijzen.
"""
text1 = """
Wij bieden keuringen aan op locaties in en rond Rotterdam
op werkdagen en in weekenden, overdag en 's avonds. U kunt bij ons terecht voor 75+ keuringen,
groot rijbewijskeuringen, taxi/touringcarchauffeurskeuringen en thuiskeuringen. Onze BIG geregistreerde artsen
 helpen u verder tegen een scherp tarief.
<br>
<br>
"""

title2 = """
Waarom RijRotterdam?
"""

text2 = """
We hebben gemerkt dat er bij andere keuringsbedrijven vaak onnodig veel geld wordt gevraagd voor een keuring. 
Daarnaast zijn mensen meestal ook een bedrag kwijt aan regelzaken in de voorbereiding van een keuring. 
Als zorgverleners vinden wij dit onterecht. RijRotterdam doet keuringen voor een eerlijke prijs. 
Van het geld dat u overhoudt, kunt u andere dingen doen die belangrijk zijn voor uw gezondheid &#128521;
<br>
<br>
"""

title3 = """Hoe maak ik een afspraak?"""
text3 = """
U kan een afspraak maken of naar ons inloopspreekuur komen. Momenteel zijn we werkzaam in Rotterdam Overschie, Rotterdam Feyenoord en Rotterdam Oost/Capelle aan den IJssel.
<br>
<br>
De keuring bestaat uit een aantal korte vragen en onderzoeken om uw gezondheid te evalueren. De keuring duurt 10 tot 15 
minuten als u gezond bent en uzelf goed heeft voorbereid. Bent u zaken in de voorbereiding vergeten of heeft u één of 
meerdere aandoeningen, dan kan de keuring langer duren.
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
Als u een keurverslag heeft gekregen voor een medisch specialist (bv. oogarts, cardioloog of psychiater) dan moet u niet bij ons, maar bij een medisch specialist een afspraak maken.   
"""

title5 = """ Wat neem ik mee?"""
text5 = """U neemt de volgende zaken mee naar een keuring:
<br>
<br>
<ul>
<li><h3>Uw ZD-code</h3></li>
<p>
Neem het formulier met de ZD-code mee. ZD staat voor ZorgDomein. Dit is het systeem waarmee de meeste artsen en specialisten digitaal met elkaar communiceren. Eventueel kunt u de ZD-code ook later aan ons doorgeven. De verwerking van uw keuring duurt daardoor wel langer. Als u komt voor een taxipas- of touringcarchauffeurskeuring, dan heeft u geen ZD-code nodig, maar u neemt dan uw gezondheidsverklaring en keuringsformulier mee.
</p><br>
<li><h3>Uw rijbewijs of paspoort</h3></li>
<p>
We hebben een identiteitsbewijs nodig om te verifiëren dat u het bent. 
</p><br>
<li><h3>Uw bril</h3></li>
<p>
Neem deze alleen mee als u uw bril nodig heeft voor veraf (tv-bril). De bril is nodig om uw zicht te meten.
</p><br>
<li><h3>Uw urine</h3></li>
<p>
Neem uw eigen urine mee in een potje. U kan een potje bij de apotheek of drogist kopen. Als u geen urine meeneemt, dan zal u tijdens de keuring moeten plassen in een potje. De keuring zal hierdoor langer duren.  
</p><br>
<li><h3>Medicatie overzicht</h3></li>
<p>
Indien u voor meer dan alleen een 75+-keuring of medische keuring komt, neem dan uw medicatieoverzicht of medicijndoosjes mee (aan te vragen bij huisarts/ apotheek).
</p><br>
<li><h3>Indien nodig, bloeddruk meting huisarts</h3></li>
<p>
Het is niet noodzakelijk een bloeddrukmeting van de huisarts of thuis mee te nemen. Echter, het kan wel zaken vergemakkelijken. Sommige mensen hebben namelijk een hoge bloeddruk in de buurt van zorgpersoneel (de zogenaamde ‘witte-jassen hypertensie’). Dit kan ertoe leiden dat de keuring langer duurt of dat het CBR aanvullende vragen stelt.
</p><br>
</ul>
"""

title6 = """Hoe krijg ik de uitslag? """
text6 = """
Vanaf het moment dat het keuringsrapport is ontvangen door het CBR is de status van uw aanvraag binnen één 
week te zien in <u><a href="https://www.cbr.nl/nl/service/nl/artikel/inloggen-op-mijn-cbr-2.html"> Mijn CBR</a></u>. Bent u gezond en zijn er geen aanvullende vragen naar aanleiding van de keuring dan duurt het op basis van 
onze ervaring een aantal dagen voordat het CBR reageert. Heeft het CBR extra vragen dan kunt u de aanvullende vragen 
mailen via onze beveiligde e-mail platform zodat wij zo snel mogelijk de aanvullende informatie aan het CBR kunnen doorgeven.

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
Datums inloopspreekuur
"""

text1_inloop = """
Op dit moment staan onderstaande inloopspreekuren gepland. Houd er rekening mee dat in het geval van drukte, wij u niet altijd kunnen helpen. 
Als u gegarandeerd wilt zijn van een afspraak dan raden wij u aan deze van tevoren bij ons in te plannen. 
<u><a href="/prijzen">Klik hier<a></u> om de prijzen te bekijken. U kan na de keuring
betalen contant of d.m.v. een Tikkie. 
<br><br>
<h3>
Corkstraat 46, 3047AC Rotterdam Overschie:
</h3>
 <br>
  <p>
 - van 15:00 tot 16:00 op zaterdagmiddag 14 mei.</p>
 <br> <br>
 <h3>
Kanaalweg 33 2903LR Capelle aan den IJssel:
</h3>
 <br>
  <p>
 - van 15:00 tot 16:00 op donderdagmiddag 12 mei.</p>
 <br>
  <br> 
 <h3>
Olympiaweg 4 3077 AL Rotterdam:
</h3>
 <br>
 <p>
 - Volgt.</p>
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
Medische metingen die plaatsvinden zijn uw eigendom. U heeft daarom altijd recht op inzage. Wij maken de inzage voor u makkelijk met Mijnkeuringsverslag. Na een keuring kan u uw rapport via deze pagina opvragen. Via een beveilgde e-mail ontvangt u het rapport dat na de keuring naar het CBR is verstuurd.
"""

texts_mijnkeuring = {
    "title1": title1_mijnkeuring, "text1": text1_mijnkeuring
}

title1_aboutus = "Ons team"
title1b_aboutus = """
Een betere vorm van zorg 
"""
text1_aboutus = """
Technologie staat ons vaak in de weg in plaats van dat het ons helpt. Dit kan en moet anders. Wij zijn een organisatie 
die een betere vorm van zorg wil bieden. Ons doel is om artsen en patiënten dichter bij elkaar te brengen.
<br>
"""

title2_aboutus = """
Visie
"""

title2b_aboutus = """
Bevordering van het welzijn 
"""

text2_aboutus = """
We willen dat minder patiënten en artsen afhankelijk worden van het huidige complexe en logge zorgsysteem. 
We geloven dat het democratiseren van de technische middelen die gezondheid bevorderen zal leiden tot kwalitatief betere zorg op de lange termijn.
Hierbij staat privacy hoog in het vaandel. In tegenstelling tot vele andere concurrenten die rijbewijskeuringen doen
maken wij gebruik van beveiligde en versleutelde digitale communicatie.  
"""

title3_aboutus = """
Vacatures
"""

title3b_aboutus = """
Overzichtelijke management systemen
"""

text3_aboutus = """
Wil je helemaal zelf aan de slag, gebruik dan onze software. Je kan alles aanpassen voor jouw persoonlijke visie op 
verbetering van de zorg. Je hebt een ZorgDomein- en ZorgMail- account nodig voor de communicatie en daarnaast 
een Google Ads-account, zodat mensen jouw dienst kunnen vinden. De gedetailleerde instructies voor het lanceren
 van jouw website kan je <u><a href="https://github.com/KelvinKramp/rijX" target=_blank>hier<a></u> vinden. Kom je er niet uit? Vraag ons om hulp.
<br><br>
Door betere software sta je in direct contact met patiënten op ale niveaus. Dit betekent voor patiënten een veilige en moeiteloze afhandeling en voor jou minder omslachtigheid! 
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
Tijdens de keuring wordt gekeken of iemand aan de normen voldoet om zelfstandig en veilig een voertuig te besturen. De arts beoordeelt de algemene lichamelijke en geestelijke conditie. Indien nodig wordt gekeken naar specifieke onderdelen van de gezondheid, zoals het functioneren van de armen, benen of wervelkolom. Daarnaast wordt de bloeddruk gemeten en het bloed of de urine gecontroleerd op diabetes. Bij de rijbewijskeuring test de arts ook de gezichtsscherpte (zonder en met eventuele bril of contactlenzen).
</p>
<br>
<h3>Medicatie</h3>
<p>
Neem een lijst mee van de medicijnen die u gebruikt als u voor een keuring voor diabetes, nieren, psychiatrie, longen of overige ziekten komt. Als u komt voor een keuring van de nieren, neem dan ook de restfunctie van de nieren mee. U kan een uitdraai hiervan vragen aan uw internist, nefroloog of huisarts.  
</p>
<br>
<h3>Bloeddruk</h3>
<p>
De bloeddruk kan tijdens een keuring hoger zijn dan gewoonlijk. Dit noemt men ‘witte-jassen hypertensie’. U hoeft zich niet per se gespannen of gestrest te voelen om een hoge bloeddruk te hebben. Dit kan zich namelijk ook voordoen terwijl u zich niet gespannen voelt. De mate van stress die u ervaart is geen goede indicator voor de bloeddruk. Als u bekend bent met een hoge bloeddruk, is het handig om de thuismeting mee te nemen of een meting van de huisarts mee te nemen. De thuismetingen moeten wel zijn gedaan met een geijkte bloeddrukmeter. Dit betekent dat de bloeddrukmeter moet zijn gecontroleerd door de huisarts om te zien of er meetfouten in zitten. 
</p>
<br>
<h3>Urine</h3>
<p>
De urine wordt onderzocht op suiker. Als u suikerziekte (diabetes) heeft ,dan plast u meer suiker uit dan normaal. Deze verhoogde hoeveelheid suiker in de urine kan worden gedetecteerd in de urine.
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
Tijdens de keuring wordt ook gekeken naar uw gezichtsscherpte. Er wordt een zogenaamde visuskaart op afstand gebruikt. Hieronder ziet u hoe het zicht wordt getest. U vertelt telkens waar de opening zit: boven, links, rechts of onder. Als u boven de 0.5 scoort tijdens deze test, dan is uw gezichtsscherpte voldoende om te mogen autorijden. Lager scoren dan de norm kan aan verschillende zaken liggen. Het kan zijn dat uw bril of lenzen niet goed zijn afgesteld, maar wat we ook vaak tegenkomen is staar. Dit is een aandoening die veel voorkomt bij ouderen en goed te behandelen is door een oogarts. Om te vermijden dat men wordt afgekeurd op een onvoldoende gezichtsvermogen, kan men van tevoren een oogmeting laten doen bij een opticien.
</p>
<br>
<p>
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

