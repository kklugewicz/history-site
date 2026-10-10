"""Generate zones_americas.json. Run: python3 americas_gen.py"""
import json, os

Z = []


def z(id, name, lon, lat, *hist):
    Z.append({"id": id, "name": name, "lon": lon, "lat": lat,
              "history": [{"from": f, "faith": r, "note": n} for f, r, n in hist]})


B = -10000

# ---------------- Canada, Alaska, Greenland ----------------
z("alaska-southwest", "Kodiak and the Aleutians", -152.4, 57.8,
  (B, "folk", "Unangan (Aleut), Alutiiq and Yup'ik peoples followed shamans and honoured the spirits of sea mammals, weather and ancestors."),
  (1794, "orthodox", "Monks from Valaam, among them St Herman, came to Kodiak with the Russian traders, and the Aleuts and Alutiiq became Russian Orthodox, a faith they kept after the 1867 US purchase."))

z("alaska", "Alaska", -149.5, 62.0,
  (B, "folk", "Athabaskan peoples such as the Dena'ina and Koyukon, and the Inupiat to the north, held animist beliefs guided by shamans."),
  (1900, "protestant", "After the 1867 US purchase, Presbyterian, Methodist and Episcopal missions spread and the gold rushes of 1896 to 1902 brought mostly Protestant settlers, though nearly a third of Alaskans now claim no religion."))

z("yukon", "Yukon", -135.05, 60.72,
  (B, "folk", "Tagish, Tutchone, Inland Tlingit and other First Nations followed animist beliefs and the guidance of shamans."),
  (1890, "anglican", "Anglican missionaries under Bishop William Bompas converted many First Nations, and the 1898 Klondike gold rush brought a wave of mostly Protestant settlers."),
  (2015, "secular", "Yukon became one of the least religious places in North America, with 60 percent reporting no religion in the 2021 census."))

z("northwest-territories", "Northwest Territories", -114.37, 62.45,
  (B, "folk", "Dene peoples such as the Dogrib (Tlicho), Slavey and Chipewyan honoured animal spirits and followed prophets and shamans."),
  (1860, "catholic", "French Oblate missionaries working along the Mackenzie River fur trade posts from the 1850s converted most Dene to Catholicism."))

z("nunavut", "Nunavut and the Canadian Arctic", -68.5, 63.75,
  (B, "folk", "Dorset and then Thule Inuit hunters followed angakkuit (shamans) and honoured Sedna, the sea woman who rules the animals."),
  (1920, "anglican", "Conversions spread from Edmund Peck's Anglican mission begun on Baffin Island in 1894, and by the 1920s most Inuit of the eastern Arctic were Anglican."))

z("greenland", "Greenland", -51.7, 64.2,
  (B, "folk", "Saqqaq and Dorset Paleo-Eskimo hunters lived along the coasts with shamanic beliefs."),
  (985, "pagan-europe", "Erik the Red led Norse settlers from Iceland to found the Eastern and Western Settlements, the latter near today's Nuuk, worshipping Thor and Odin."),
  (1000, "christian", "Erik's wife Thjodhild built Greenland's first church at Brattahlid as the Norse settlers followed Iceland into Christianity."),
  (1054, "catholic", "After the Great Schism the Greenland Norse stayed with Rome, receiving their own bishop at Gardar in 1126."),
  (1350, "folk", "The Norse Western Settlement was abandoned around 1350 and the Eastern by about 1450, leaving Greenland to Thule Inuit who followed shamans and the sea goddess Sedna."),
  (1760, "lutheran", "Lutheran missions begun by Hans Egede at Nuuk in 1721, alongside Moravian stations, converted most West Greenland Inuit by the late 1700s; the Church of Greenland is still Lutheran."))

z("british-columbia", "British Columbia", -122.5, 49.6,
  (B, "folk", "Coast Salish, Kwakwaka'wakw, Haida and other peoples raised totem poles, held potlatches and winter dances and honoured guardian spirits."),
  (1858, "anglican", "The Fraser River gold rush and the new Crown colony brought British settlers, and the Church of England, beside Catholic, Methodist and Presbyterian missions, became the largest church."),
  (2021, "secular", "The 2021 census found 52 percent of British Columbians reporting no religion, the highest share of any Canadian province."))

z("alberta", "Alberta", -113.5, 52.0,
  (B, "folk", "Blackfoot (Siksika, Kainai, Piikani), Plains Cree and Tsuut'ina peoples held the Sun Dance and medicine bundle ceremonies."),
  (1900, "protestant", "The Canadian Pacific Railway and homestead settlement brought Methodist, Presbyterian and Lutheran farmers, and Alberta later became the heartland of Canadian evangelicalism."))

z("canadian-prairies", "Saskatchewan and Manitoba", -101.5, 50.5,
  (B, "folk", "Plains Cree, Assiniboine, Ojibwe and Dakota peoples honoured the Creator through the Sun Dance, sweat lodge and vision quest."),
  (1885, "protestant", "After the railway and the defeat of the Metis North-West Resistance of 1885, Ontario Protestants and European immigrants homesteaded the prairies, with Methodist and Presbyterian churches strongest."),
  (1960, "catholic", "Ukrainian Greek Catholic, German, Polish, French and Metis Catholics made the Catholic Church the largest in Saskatchewan and Manitoba by the 1960s, ahead of the United Church."))

z("ontario", "Ontario", -79.8, 43.9,
  (B, "folk", "Iroquoian Huron-Wendat, Neutral and Haudenosaunee farmers and Anishinaabe hunters held the Feast of the Dead and other spirit rites."),
  (1784, "anglican", "United Empire Loyalists fleeing the American Revolution settled Upper Canada, where the 1791 Constitutional Act set aside clergy reserves for the established Church of England."),
  (1830, "protestant", "Methodist circuit riders and camp meetings made Methodism the largest church of Upper Canada, and in 1925 Methodists joined Presbyterians in the United Church of Canada."),
  (1961, "catholic", "Postwar Italian, Portuguese, Polish and later Filipino and Latin American immigration made Catholics the largest church in Ontario, ahead of the United and Anglican churches."))

z("quebec", "Quebec", -71.25, 46.8,
  (B, "folk", "Iroquoian villagers of Stadacona and Hochelaga and Algonquian peoples such as the Innu honoured the spirits of animals, the sky and the dead."),
  (1608, "catholic", "Samuel de Champlain founded Quebec, and New France grew as a strictly Catholic colony whose church stayed central to French Canadian life after the 1763 British conquest until the 1960s Quiet Revolution."))

z("new-brunswick", "New Brunswick", -65.5, 46.2,
  (B, "folk", "Mi'kmaq, Wolastoqiyik (Maliseet) and Passamaquoddy peoples honoured the culture hero Glooscap and the spirits of land and sea."),
  (1610, "catholic", "French missionaries converted the Mi'kmaq and Wolastoqiyik, who became Catholic allies of the Acadian settlers and New France."),
  (1783, "protestant", "After the Acadian expulsion of 1755, Loyalists founded Saint John and Fredericton, and Baptist, Methodist, Anglican and Presbyterian settlers formed a Protestant majority."),
  (1950, "catholic", "The growth of returning Acadians and Irish Catholics made Catholics about half of New Brunswick's people by the mid 1900s."))

z("nova-scotia", "Nova Scotia", -63.6, 45.0,
  (B, "folk", "The Mi'kmaq of Mi'kma'ki honoured Kisu'lk the Creator and the culture hero Glooscap, guided by shamans called puoinaq."),
  (1610, "catholic", "The Mi'kmaq grand chief Membertou was baptised at Port-Royal, and the Mi'kmaq and the French settlers of Acadia became Catholic."),
  (1760, "protestant", "After Halifax was founded in 1749 and the Acadians were expelled in 1755, New England Planters, Loyalists and Scottish settlers made Nova Scotia mostly Baptist, Presbyterian, Methodist and Anglican."))

z("newfoundland", "Newfoundland and Labrador", -53.5, 47.8,
  (B, "folk", "The Maritime Archaic people and later the Beothuk, who coated themselves in red ochre, held animist beliefs; the Norse camp at L'Anse aux Meadows around 1000 left no lasting church."),
  (1610, "anglican", "English West Country fishermen settled the Avalon coast from the founding of Cupids in 1610, bringing the Church of England."),
  (1800, "catholic", "Heavy Irish immigration in the late 1700s and early 1800s made Catholics the largest church, ahead of the Anglicans and the Methodists of the outports."))

# ---------------- United States ----------------
z("new-england", "Southern New England", -71.4, 42.3,
  (B, "folk", "Algonquian peoples such as the Wampanoag, Massachusett and Narragansett honoured the creator Kiehtan and the spirit powers called manitou through their powwaws, or shamans."),
  (1630, "reformed", "Puritans of the Massachusetts Bay Company, following the Plymouth Pilgrims of 1620, built Calvinist Congregational churches that were established by law in Massachusetts until 1833."),
  (1880, "catholic", "Irish, French Canadian, Italian and Portuguese immigration made Catholics the largest religious group in Massachusetts, Rhode Island and Connecticut by the late 1800s."))

z("northern-new-england", "Northern New England", -71.0, 44.3,
  (B, "folk", "Abenaki and Penobscot peoples lived by hunting and planting and honoured the culture hero Gluskabe and the spirits of the land."),
  (1760, "reformed", "After the fall of New France in 1760 ended the Abenaki wars, Congregationalist settlers from southern New England flooded into New Hampshire, Vermont and Maine."))

z("new-york-city", "New York City and New Jersey", -74.0, 40.75,
  (B, "folk", "Lenape peoples honoured a creator and the manitou spirits of nature and held seasonal thanksgiving ceremonies."),
  (1625, "reformed", "The Dutch West India Company founded New Amsterdam with the Dutch Reformed Church as its official faith, and after the English took it in 1664 Reformed and Presbyterian churches stayed strongest."),
  (1850, "catholic", "Irish refugees from the Great Famine and German immigrants made Catholics the largest church in New York by the 1850s, later joined by Italians, Poles and Puerto Ricans."))

z("upstate-new-york", "Upstate New York", -76.2, 42.9,
  (B, "folk", "The Haudenosaunee, the Iroquois League said to be founded by the Peacemaker and Hiawatha, held Longhouse ceremonies of thanksgiving to the Creator."),
  (1790, "protestant", "After the Revolution the Iroquois lost most of their lands and Yankee settlers filled the region, which revivals made the Burned-over District of Methodists, Baptists and Presbyterians."),
  (1920, "catholic", "Irish, German, Italian and Polish workers in Buffalo, Rochester, Syracuse and Albany made Catholics the largest church in upstate New York by the early 1900s."))

z("pennsylvania", "Pennsylvania", -77.2, 40.6,
  (B, "folk", "Lenape and Susquehannock peoples honoured a creator and the spirits of nature through dances and the Big House ceremony."),
  (1682, "protestant", "William Penn's Quaker colony welcomed all faiths and drew Quakers, German Lutherans, Reformed, Mennonites and Amish, and Scots-Irish Presbyterians, a Protestant majority of many churches."))

z("chesapeake", "Virginia and Maryland", -77.4, 37.6,
  (B, "folk", "The Powhatan paramount chiefdom and neighbouring Algonquian peoples worshipped the creator Ahone and the feared spirit Okeus through priests and temples."),
  (1607, "anglican", "English colonists at Jamestown made the Church of England the established church of Virginia, and of Maryland from 1702 despite its founding as a Catholic refuge in 1634."),
  (1790, "protestant", "After Virginia's 1786 Statute for Religious Freedom disestablished the Episcopal Church, Baptist and Methodist revivals won most white and enslaved Black Virginians."))

z("carolinas", "The Carolinas", -79.5, 35.4,
  (B, "folk", "Catawba, Cherokee and other heirs of the Mississippian mound builders held the Green Corn ceremony and honoured the spirits of sacred fire and water."),
  (1670, "anglican", "English settlers founded Charles Town, and the Church of England was established by law in both Carolinas, though Quakers, Huguenots and Baptists were numerous."),
  (1790, "protestant", "Baptist and Methodist revivals of the Great Awakenings won most white Carolinians and, through Black preachers, the enslaved, making the region a stronghold of evangelical Protestantism."))

z("upland-south", "Tennessee and Kentucky", -86.0, 36.3,
  (B, "folk", "Mississippian chiefdoms and later Cherokee, Shawnee and Chickasaw peoples held seasonal rites honouring the sun, sacred fire and ancestors."),
  (1790, "protestant", "Settlers crossing the Appalachians brought Baptist, Methodist and Presbyterian faith, and the Cane Ridge revival of 1801 in Kentucky set off the frontier camp meeting movement."))

z("deep-south", "Georgia, Alabama and Mississippi", -86.3, 32.6,
  (B, "folk", "Mississippian mound centres such as Moundville and Etowah, and later the Creek, Choctaw and Chickasaw nations, honoured the sun and sacred fire in the Green Corn ceremony."),
  (1815, "protestant", "After the Creek War of 1814 and the later removal of the southern nations, cotton planters and the enslaved poured in, and Baptist and Methodist churches became the faith of white and Black Southerners."))

z("arkansas", "Arkansas", -92.3, 34.8,
  (B, "folk", "Caddo, Quapaw and Osage peoples, heirs of the mound builders, honoured a supreme being and the spirits of nature."),
  (1820, "protestant", "After the Louisiana Purchase settlers from Tennessee and Kentucky brought Baptist and Methodist churches to Arkansas Territory, created in 1819."))

z("florida", "Florida", -81.8, 28.8,
  (B, "folk", "Timucua, Apalachee, Calusa and Tequesta peoples worshipped the sun and moon and built temple mounds."),
  (1565, "catholic", "Pedro Menendez founded St Augustine, and Franciscan missions converted most Timucua and Apalachee by the mid 1600s."),
  (1704, "folk", "Carolina English and Creek allies destroyed the Apalachee and Timucua missions in raids of 1702 to 1704, and the Seminoles who later settled Florida kept their own traditions."),
  (1821, "protestant", "Florida passed to the United States, and Anglo-American settlers made it Baptist and Methodist, though Cuban and other Latin American migration later built a large Catholic community."))

z("louisiana", "South Louisiana", -91.3, 30.2,
  (B, "folk", "Natchez, Chitimacha and Caddo peoples, heirs of the mound builders, honoured the sun; the Natchez ruler, the Great Sun, kept an eternal temple fire."),
  (1718, "catholic", "The French founded New Orleans, the Code Noir required enslaved people to be baptised Catholic, and Acadian exiles from 1765 kept south Louisiana Catholic after the 1803 Louisiana Purchase."))

z("texas", "Texas", -97.5, 31.2,
  (B, "folk", "Caddo farmers with temple mounds, Tonkawa hunters and later Comanche and Apache horsemen followed their own spirit traditions."),
  (1718, "catholic", "Spain founded San Antonio and a chain of Franciscan missions, making Catholicism the ruling faith, though Comanche and Apache peoples still controlled most of Texas."),
  (1836, "protestant", "Anglo-American settlers, who by then outnumbered Tejanos about ten to one, won Texan independence, and Baptist and Methodist churches became dominant."))

z("south-texas", "South Texas", -98.4, 27.0,
  (B, "folk", "Coahuiltecan and Karankawa bands lived by hunting and gathering and held mitote dances led by shamans."),
  (1749, "catholic", "Jose de Escandon founded Spanish towns along the Rio Grande in Nuevo Santander, and the region's Tejano and Mexican American majority has stayed Catholic."))

z("oklahoma", "Oklahoma", -97.5, 35.5,
  (B, "folk", "Wichita and Caddo farmers, and later Comanche, Kiowa and Osage peoples, held Sun Dance and medicine bundle rites."),
  (1889, "protestant", "The Cherokee, Creek and other removed nations brought Baptist and Methodist churches, and the land runs from 1889 filled Oklahoma with Protestant settlers from the South."))

z("ohio", "Ohio", -82.8, 40.2,
  (B, "folk", "The Adena and Hopewell built burial mounds and earthworks such as the Great Serpent Mound, and later the Shawnee, Miami and Delaware honoured the Great Spirit."),
  (1795, "protestant", "The Treaty of Greenville opened Ohio to settlers from New England, Virginia and Pennsylvania, who brought Methodist, Baptist and Presbyterian churches."))

z("indiana-illinois", "Indiana and Illinois", -88.0, 40.2,
  (B, "folk", "Cahokia, the largest Mississippian city around 1100, and later Illinois, Miami and Potawatomi peoples held rites to the sun and the spirits of the land."),
  (1815, "protestant", "After the War of 1812 broke Native resistance, settlers from Kentucky and Ohio filled Indiana and Illinois with Methodist and Baptist churches, though Chicago later grew strongly Catholic."))

z("michigan", "Michigan", -84.6, 43.0,
  (B, "folk", "Anishinaabe peoples, the Ojibwe, Odawa and Potawatomi, honoured Gitche Manitou and kept the Midewiwin medicine society."),
  (1830, "protestant", "The Erie Canal brought Yankee settlers who made Michigan Methodist, Baptist and Presbyterian, later joined by Dutch Reformed and German Lutheran immigrants."))

z("upper-midwest", "Minnesota and Wisconsin", -92.5, 45.3,
  (B, "folk", "Dakota and Ojibwe peoples held Midewiwin, vision quest and medicine dance ceremonies honouring the Great Spirit."),
  (1870, "lutheran", "After the Dakota War of 1862, Norwegian, Swedish and German Lutheran homesteaders made Lutheranism the largest Protestant church of Minnesota and Wisconsin, closely rivalled by Catholics."))

z("missouri-iowa", "Missouri and Iowa", -92.5, 40.0,
  (B, "folk", "Osage, Missouria and Ioway peoples, and earlier Mississippian towns, honoured the sun, thunder beings and sacred bundles."),
  (1820, "protestant", "Settlers from Kentucky, Tennessee and Virginia brought Baptist and Methodist churches, while French Catholic St Louis and later German Catholics formed a large minority."))

z("northern-plains", "The Dakotas", -100.3, 46.5,
  (B, "folk", "The Lakota, Dakota, Mandan and Hidatsa held Sun Dance and vision quest rites to Wakan Tanka, the Great Mystery."),
  (1880, "lutheran", "The Great Dakota Boom brought Norwegian and German Lutheran homesteaders by the hundred thousand, while Catholic and Episcopal missions worked on the Lakota reservations."))

z("central-plains", "Kansas and Nebraska", -98.5, 39.8,
  (B, "folk", "Pawnee, Kansa, Osage and Cheyenne peoples held the Morning Star ceremony, buffalo rites and the Sun Dance."),
  (1860, "protestant", "The Kansas-Nebraska Act of 1854 and the Homestead Act of 1862 brought Methodist, Baptist and other Protestant settlers, and the Plains peoples were confined to reservations."))

z("colorado", "Colorado", -105.0, 39.6,
  (B, "folk", "Ancestral Puebloans built the cliff dwellings of Mesa Verde, and later Ute, Arapaho and Cheyenne peoples held the Bear Dance and Sun Dance."),
  (1860, "protestant", "The Pike's Peak gold rush of 1859 and the railroads brought Anglo-American settlers and Protestant churches, though Hispano villages in the south stayed Catholic."))

z("northern-rockies", "Montana and Wyoming", -109.0, 46.0,
  (B, "folk", "Blackfeet, Crow, Salish and Shoshone peoples held the Sun Dance and medicine bundle ceremonies."),
  (1880, "protestant", "Gold and copper mining, cattle ranching and the Northern Pacific Railway brought settlers who built Methodist, Lutheran and Presbyterian churches beside Catholic ones."))

z("idaho", "Idaho", -115.5, 44.0,
  (B, "folk", "Shoshone, Bannock and Nez Perce peoples sought guardian spirits through vision quests."),
  (1862, "protestant", "Gold strikes in the Boise Basin brought Protestant miners and farmers while Latter-day Saints settled the south-east, and Protestants together remain the largest group."))

z("nevada", "Nevada", -117.5, 39.3,
  (B, "folk", "Paiute, Shoshone and Washoe peoples of the Great Basin followed shamans; the Paiute prophet Wovoka began the Ghost Dance here in 1889."),
  (1860, "protestant", "The Comstock Lode silver rush of 1859 brought miners from across the country, making Nevada a mixed but mostly Protestant state, though Catholics are now the largest single church."))

z("utah", "Utah", -111.9, 40.6,
  (B, "folk", "Fremont farmers and later Ute, Southern Paiute and Shoshone peoples held the Bear Dance and other spirit ceremonies."),
  (1847, "protestant", "Brigham Young led the Latter-day Saints to the Salt Lake Valley; Mormons, still a majority of Utahns, appear under the Protestant colour only because this map has no separate Latter-day Saint category."))

z("new-mexico", "New Mexico", -106.0, 35.4,
  (B, "folk", "Ancestral Puebloans built Chaco Canyon, and the Pueblo peoples held kachina dances in kivas, later joined by Apache and Navajo peoples."),
  (1598, "catholic", "Juan de Onate colonised New Mexico, and Franciscan friars baptised the Pueblos and suppressed the kachina ceremonies."),
  (1680, "folk", "Po'pay led the Pueblo Revolt, which killed or expelled the Spanish and their friars and restored the old ceremonies for twelve years."),
  (1692, "catholic", "Diego de Vargas reconquered New Mexico, and the Catholicism of Hispano villages and Pueblos, often alongside Pueblo ritual, has remained the largest faith."))

z("arizona", "Arizona", -111.9, 33.6,
  (B, "folk", "The Hohokam built canals and ball courts, and their O'odham descendants and the Hopi, Apache and Navajo kept their own ceremonies."),
  (1880, "protestant", "Railroads and copper mining brought Anglo-American and Mormon settlers, and Protestant churches overtook the Catholic faith of the Hispanic towns and O'odham missions."))

z("northern-california", "Northern California", -121.9, 38.0,
  (B, "folk", "Ohlone, Miwok and Pomo peoples held Kuksu society dances and honoured the spirits of the land."),
  (1776, "catholic", "Franciscans founded Mission Dolores at San Francisco and other Bay Area missions, where many Ohlone were baptised and died of disease; Catholicism was the ruling faith."),
  (1849, "protestant", "The Gold Rush brought a flood of mostly Protestant Americans, alongside many Catholic Irish, Mexicans and Chileans, and Protestants became the largest group."))

z("southern-california", "Southern California", -118.0, 34.1,
  (B, "folk", "Tongva, Chumash and Cahuilla peoples followed shamans, and many joined the Chinigchinich religion of visions and toloache rites."),
  (1769, "catholic", "Junipero Serra founded the first Franciscan mission at San Diego, and the mission chain made the coastal peoples Catholic under Spanish and then Mexican rule."),
  (1885, "protestant", "The railroad land boom of the 1880s brought Midwestern Protestants who made Los Angeles a heavily Protestant city for decades."),
  (1990, "catholic", "Mexican and Central American immigration again made Catholics the largest religious group in Southern California."))

z("pacific-northwest", "Oregon and Washington", -122.6, 46.0,
  (B, "folk", "Chinook, Coast Salish and Kalapuya peoples held potlatches and winter spirit dances and honoured the salmon and guardian spirits."),
  (1843, "protestant", "Methodist and Presbyterian missions preceded the Oregon Trail migrations from 1843, which made Oregon and Washington settler lands with Protestant majorities, though a third now claim no religion."))

# ---------------- Mexico and Central America ----------------
z("central-mexico", "Central Mexico", -99.1, 19.4,
  (B, "folk", "Early hunters and the first maize farmers of the Valley of Mexico honoured the forces of nature and the dead."),
  (-1200, "mesoamerican", "Tlatilco took up Olmec-style ritual, and the valley later centred its worship on Teotihuacan's Pyramids of the Sun and Moon and, from 1325, on the Aztec Templo Mayor of Tenochtitlan."),
  (1521, "catholic", "Cortes conquered Tenochtitlan, Franciscans from 1524 baptised millions, and the Virgin of Guadalupe became the symbol of a Mexican Catholicism that survived the anticlerical laws and the Cristero War."))

z("gulf-coast-mexico", "Veracruz and Tabasco", -94.5, 18.1,
  (B, "folk", "Early farmers of the Gulf lowlands honoured spirits of rain, maize and the jaguar."),
  (-1200, "mesoamerican", "The Olmec of San Lorenzo and La Venta, the mother culture of Mesoamerica, carved colossal heads and worshipped jaguar-faced rain and maize gods."),
  (1521, "catholic", "Cortes landed at Veracruz in 1519, and after the fall of the Aztecs friars converted the Totonac, Nahua and Chontal Maya peoples of the Gulf coast."))

z("oaxaca", "Oaxaca", -96.7, 17.1,
  (B, "folk", "Early maize farmers of the Oaxaca valleys honoured the lightning god and their ancestors."),
  (-1200, "mesoamerican", "San Jose Mogote and later Monte Alban, the Zapotec capital from 500 BC, built temples and ball courts and used the Mesoamerican calendar, as did the Mixtec kingdoms."),
  (1529, "catholic", "Dominican friars followed the Spanish conquest and built churches like Santo Domingo de Oaxaca, though Zapotec and Mixtec villages kept many old rites within Catholic practice."))

z("west-mexico", "Jalisco and Michoacan", -103.0, 20.2,
  (B, "folk", "Early peoples of western Mexico honoured the dead in shaft tombs and the spirits of nature."),
  (-1000, "mesoamerican", "Shaft tomb and Teuchitlan cultures shared Mesoamerican ritual, and from about 1350 the Purepecha (Tarascan) state worshipped the fire god Curicaueri at Tzintzuntzan."),
  (1530, "catholic", "Nuno de Guzman's brutal conquest created Nueva Galicia and Franciscans evangelised the region, which became the Catholic heartland of the Cristero War in the 1920s."))

z("bajio-zacatecas", "Zacatecas and the Bajio", -102.0, 22.3,
  (B, "folk", "Chichimeca hunter-gatherers roamed the northern plateau honouring the sun and the spirits of the hunt, while frontier towns like La Quemada briefly held Mesoamerican temples."),
  (1550, "catholic", "Silver strikes at Zacatecas in 1546 and Guanajuato drew Spanish miners, and after the Chichimeca War ended around 1590 Franciscans and Christian Indian settlers made the region Catholic."))

z("northeast-mexico", "Nuevo Leon and Coahuila", -100.6, 26.0,
  (B, "folk", "Coahuiltecan and other hunter-gatherer bands of the northeast held mitote dances and peyote rites."),
  (1596, "catholic", "Diego de Montemayor founded Monterrey, and Spanish settlers with Tlaxcalan colonists and Franciscans made the northeast Catholic as its native peoples died out or were absorbed."))

z("chihuahua", "Chihuahua and Durango", -106.1, 28.0,
  (B, "folk", "Raramuri (Tarahumara), Tepehuan, Concho and later Apache peoples honoured the sun and moon and danced to bring rain."),
  (1640, "catholic", "Silver mining at Santa Barbara and Parral and Jesuit and Franciscan missions among the Raramuri made the north Catholic, though Raramuri ritual still blends both faiths."))

z("sonora", "Sonora and Sinaloa", -109.9, 28.0,
  (B, "folk", "Yaqui, Mayo, O'odham and Seri peoples held deer dances and other rites to the spirits of the desert."),
  (1620, "catholic", "Jesuit missionaries entered the Mayo and Yaqui valleys from 1614 to 1617, and the Yaqui built a distinctive Catholic ritual life around their eight pueblos."))

z("baja-california", "Baja California", -113.0, 27.8,
  (B, "folk", "Cochimi, Guaycura and Pericu bands painted the great murals of the Sierra de San Francisco and followed shamans."),
  (1697, "catholic", "The Jesuit Juan Maria de Salvatierra founded Loreto, the first lasting mission, and the peninsula's native peoples were baptised as epidemics destroyed their numbers."))

z("yucatan", "Yucatan", -89.3, 20.6,
  (B, "folk", "Early Maya farmers of the limestone plain honoured the rain and the sacred waters of the cenotes."),
  (-1000, "mesoamerican", "Maya cities such as Chichen Itza, Uxmal and Mayapan worshipped Chaac, Kukulcan and Itzamna with temple pyramids and offerings in sacred cenotes."),
  (1546, "catholic", "Francisco de Montejo completed the conquest of Yucatan, and Franciscan friars, among them Diego de Landa who burned Maya books in 1562, imposed Catholicism."))

z("chiapas", "Chiapas", -92.6, 16.7,
  (B, "folk", "Early hunters and farmers of the Chiapas highlands and Pacific coast honoured the earth and rain."),
  (-1000, "mesoamerican", "Mixe-Zoque and Maya peoples built Izapa and later Palenque, Tonina and Yaxchilan, centres of divine kingship, ancestor worship and the Maya calendar."),
  (1528, "catholic", "Diego de Mazariegos founded San Cristobal, and Dominicans such as Bartolome de las Casas, bishop from 1545, evangelised the Tzotzil and Tzeltal Maya."))

z("belize", "Belize", -88.7, 17.2,
  (B, "folk", "Early hunters and maize farmers lived in the forests of the Maya lowlands."),
  (-1000, "mesoamerican", "Maya cities such as Caracol, Lamanai and Altun Ha rose here, and Lamanai kept its temples in use until Spanish times."),
  (1798, "anglican", "British Baymen logging with enslaved Africans won the Battle of St George's Caye, and the Creole society of British Honduras became Anglican, Methodist and Baptist."),
  (1870, "catholic", "Mestizo refugees from Yucatan's Caste War and Garifuna settlers, served by Jesuits from 1851, made Catholics the largest church in Belize."))

z("guatemala", "Guatemala", -90.6, 14.8,
  (B, "folk", "Early foragers and maize farmers lived in the highlands and Peten lowlands."),
  (-1000, "mesoamerican", "Maya peoples built El Mirador, Kaminaljuyu and Tikal, kingdoms whose rulers led the worship of the maize god, the rain god Chaac and the ancestors."),
  (1524, "catholic", "Pedro de Alvarado conquered the Kiche and Kaqchikel kingdoms, and Dominicans and Franciscans made the highland Maya Catholic, often blending the saints with Maya rites; evangelicals now rival Catholics in number."))

z("honduras", "Honduras", -87.2, 14.3,
  (B, "folk", "Early foragers and farmers lived in the valleys of Honduras."),
  (-800, "mesoamerican", "Los Naranjos and later the Maya city of Copan and the Lenca chiefdoms shared Mesoamerican temple worship, the calendar and the ritual ballgame."),
  (1524, "catholic", "The Spanish conquest, completed after the defeat of the Lenca leader Lempira in 1537, brought Catholic missions and towns."),
  (2015, "protestant", "Pentecostal and other evangelical churches, growing fast since the 1980s, now count more Hondurans than the Catholic Church in several recent national surveys."))

z("el-salvador", "El Salvador", -89.2, 13.75,
  (B, "folk", "Early farmers lived among the volcanoes of the Pacific slope."),
  (-1000, "mesoamerican", "Chalchuapa with its Olmec-influenced pyramids, then Maya towns and later the Pipil (Nahua) lordship of Cuzcatlan, worshipped Mesoamerican gods."),
  (1528, "catholic", "Pedro de Alvarado's campaigns of 1524 to 1528 conquered Cuzcatlan, and San Salvador became a Catholic colonial town; the martyred archbishop Oscar Romero was made a saint in 2018."))

z("nicaragua", "Nicaragua", -86.25, 12.3,
  (B, "folk", "Chibchan-speaking farmers and fishers held animist beliefs before Mesoamerican peoples arrived."),
  (800, "mesoamerican", "Chorotega and later Nicarao (Nahua) migrants from Mexico settled the Pacific lowlands and brought Mesoamerican gods, the calendar and markets."),
  (1524, "catholic", "The Nicarao were baptised en masse under Gil Gonzalez Davila in 1523, and Francisco Hernandez de Cordoba founded Granada and Leon in 1524."))

z("mosquito-coast", "Mosquito Coast", -83.6, 14.0,
  (B, "folk", "Miskito, Mayangna and Rama peoples followed sukias, or shamans, and honoured the spirits of forest and sea."),
  (1880, "protestant", "Moravian missionaries arrived in 1849 under the British-protected Miskito Kingdom, and a great revival in 1881 made the Miskito overwhelmingly Moravian."))

z("costa-rica", "Costa Rica", -84.1, 9.95,
  (B, "folk", "Chibchan peoples like the Huetar and the Diquis, who carved the great stone spheres, honoured nature spirits and ancestors."),
  (1564, "catholic", "Juan Vazquez de Coronado founded Cartago, and the colony's mostly Spanish settlers made Catholicism the faith that remains the state religion under the constitution."))

z("panama", "Panama", -80.0, 8.6,
  (B, "folk", "Cueva, Ngabe and Guna peoples, makers of the gold work of Gran Cocle, honoured nature spirits and ancestors."),
  (1519, "catholic", "Pedrarias Davila founded Panama City, the first European city on the Pacific, and the isthmus became a Catholic crossroads of the Spanish empire."))

# ---------------- Caribbean ----------------
z("cuba", "Cuba", -79.5, 22.2,
  (B, "folk", "Taino and Ciboney peoples honoured zemis, spirit images of ancestors and nature, in ceremonies led by caciques and behique healers."),
  (1511, "catholic", "Diego Velazquez conquered Cuba, the Taino died out, and Catholicism, blended among enslaved Africans with Yoruba religion as Santeria, became the island's faith."),
  (1961, "secular", "Fidel Castro declared the revolution socialist, expelled priests and in 1976 made Cuba an atheist state; most Cubans stopped practising, though Santeria and private faith survived."),
  (1992, "catholic", "The 1992 constitution made Cuba a secular rather than atheist state, and papal visits from 1998 helped a Catholic revival, though Santeria remains widespread."))

z("haiti", "Haiti", -72.3, 18.9,
  (B, "folk", "Taino peoples honoured zemis, spirits of ancestors and nature, through ceremonies led by caciques and behique healers."),
  (1493, "catholic", "Columbus left a garrison at La Navidad in 1492 and Spanish rule wiped out the Taino; under France from 1697 enslaved Africans were baptised Catholic and blended it with African rites into Vodou."))

z("dominican-republic", "Dominican Republic", -70.4, 18.8,
  (B, "folk", "Taino chiefdoms honoured zemis and held areito dances to recount their myths."),
  (1496, "catholic", "Bartholomew Columbus founded Santo Domingo, later seat of the first cathedral and university in the Americas, and the colony became Catholic as the Taino perished."))

z("puerto-rico", "Puerto Rico", -66.4, 18.2,
  (B, "folk", "Taino peoples of Borinquen honoured zemis and played the ritual ballgame in stone-lined plazas."),
  (1508, "catholic", "Juan Ponce de Leon founded Caparra and Spanish rule made the island Catholic as the Taino collapsed; Catholics remain the largest group despite strong Pentecostal growth since US rule began in 1898."))

z("jamaica", "Jamaica", -77.3, 18.1,
  (B, "folk", "Taino peoples of Xaymaca honoured zemis, spirits of ancestors and nature."),
  (1509, "catholic", "Spanish settlers founded Sevilla la Nueva, and the Taino died out under forced labour and disease."),
  (1655, "anglican", "England seized Jamaica and established the Church of England, though most enslaved Africans brought in for sugar kept African beliefs such as Myal and Obeah."),
  (1830, "protestant", "Baptist and Methodist missions, with Black deacons like Sam Sharpe of the 1831 Baptist War, converted the enslaved, and after emancipation Baptists, then Adventists and Pentecostals, led."))

z("trinidad", "Trinidad and Tobago", -61.3, 10.5,
  (B, "folk", "Arawak and Carib peoples of Trinidad, the island the Spanish called Iere's land, honoured ancestral spirits."),
  (1592, "catholic", "Antonio de Berrio founded San Jose de Oruna, and Spanish rule and the French Catholic planters invited in 1783 made Catholics the largest group, beside later Hindu, Anglican and Pentecostal communities."))

# ---------------- South America ----------------
z("colombia-andes", "Colombian Andes", -74.1, 4.6,
  (B, "folk", "The Muisca of the Bogota plateau worshipped the sun god Sue and the moon goddess Chia and offered gold at sacred lakes like Guatavita, origin of the El Dorado legend."),
  (1538, "catholic", "Gonzalo Jimenez de Quesada conquered the Muisca and founded Bogota, and the missionary orders made New Granada a deeply Catholic land."))

z("colombia-caribbean", "Colombian Caribbean", -75.2, 10.0,
  (B, "folk", "Zenu and Tairona peoples, builders of the stone city in the Sierra Nevada, followed priests called mamos who still guide the Kogi today."),
  (1533, "catholic", "Santa Marta was founded in 1525 and Cartagena in 1533, and Cartagena became a seat of the Inquisition and the port where Peter Claver baptised enslaved Africans."))

z("colombia-south", "Southern Colombia", -76.6, 2.4,
  (B, "folk", "The San Agustin culture carved hundreds of stone guardian statues over tombs, and later chiefdoms honoured ancestors and nature spirits."),
  (1537, "catholic", "Sebastian de Belalcazar founded Popayan and Cali, and the south became a stronghold of colonial Catholicism."))

z("venezuela", "Venezuela", -66.9, 10.2,
  (B, "folk", "Timoto-Cuica farmers of the Andes and Carib and Arawak peoples of the coast honoured nature spirits, with shamans called piaches."),
  (1527, "catholic", "Spanish settlers founded Coro, and later Caracas in 1567, and Franciscan and Capuchin missions spread Catholicism across the coast and the llanos."))

z("venezuela-guayana", "Venezuelan Guayana", -63.5, 7.5,
  (B, "folk", "Warao, Pemon and Karina peoples of the Orinoco followed shamans, and the Pemon honour the tepui mountains as homes of spirits."),
  (1725, "catholic", "Catalan Capuchins founded missions along the Caroni from 1724, and Angostura, today's Ciudad Bolivar, became the Spanish capital of Guayana."))

z("ecuador-highlands", "Ecuadorian Andes", -78.5, -0.4,
  (B, "folk", "Highland chiefdoms of the Quitu, Caranqui and Canari peoples honoured mountains, the sun and moon and their ancestors."),
  (1470, "andean", "The Inca under Topa Inca and Huayna Capac conquered the northern Andes and imposed the cult of Inti, the sun, and Quito became a second Inca capital."),
  (1534, "catholic", "Sebastian de Belalcazar took Quito, and Franciscan, Dominican and Jesuit orders built its baroque churches and evangelised the Quichua highlands."))

z("ecuador-coast", "Ecuadorian coast", -79.9, -1.8,
  (B, "folk", "Valdivia villagers made some of the oldest pottery in the Americas around 3500 BC, and later Manteno seafarers honoured the sea and their ancestors."),
  (1538, "catholic", "The Spanish conquest and the founding of Guayaquil brought the coast under Catholic rule as its native population collapsed."))

z("peru-north", "Northern Peru", -78.8, -7.8,
  (B, "folk", "Early fishers and farmers of the north coast, such as those of Huaca Prieta, honoured the sea and their ancestors."),
  (-1500, "andean", "Cupisnique, then from about 100 AD the Moche with their Huacas of the Sun and Moon, and later the Chimu kingdom of Chan Chan built temple cults that the Inca absorbed."),
  (1534, "catholic", "Diego de Almagro founded Trujillo, and Catholic orders evangelised the Mochica-speaking peoples of the north coast."))

z("peru-coast", "Central Peruvian coast", -77.0, -11.8,
  (B, "folk", "Early fishing villages of the Peruvian coast honoured the sea and the dead."),
  (-2500, "andean", "Caral and the Norte Chico towns north of Lima raised the oldest monumental temples of the Americas, and later Pachacamac became the coast's great oracle shrine."),
  (1535, "catholic", "Francisco Pizarro founded Lima, capital of the Viceroyalty of Peru, whose archbishops, saints like Rose of Lima and Martin de Porres, and Inquisition made it South America's Catholic heart."))

z("peru-highlands", "Peruvian Andes", -72.0, -13.5,
  (B, "folk", "Early highland hunters and herders of llamas and alpacas honoured mountains, springs and their ancestors."),
  (-900, "andean", "Chavin de Huantar spread a highland temple cult, followed by Wari and from about 1400 the Inca, who worshipped Inti, Viracocha and the mountain apus from Cusco's Coricancha."),
  (1572, "catholic", "After the 1533 conquest of Cusco, Viceroy Toledo executed Tupac Amaru in 1572 and forced Andeans into Catholic reducciones, though worship of the apus survived alongside the saints."))

z("upper-amazon", "Peruvian Amazon", -73.25, -3.75,
  (B, "folk", "Amazonian peoples like the Shipibo, Ashaninka and Kukama followed shamans who used ayahuasca to deal with the forest spirits."),
  (1880, "catholic", "Jesuit missions of Maynas existed from 1638 to 1767, but the rubber boom from the 1880s, centred on Iquitos, created a mestizo Catholic majority, at terrible cost to native peoples."))

z("bolivia-altiplano", "Bolivian Altiplano", -68.2, -16.6,
  (B, "folk", "Early herders and farmers around Lake Titicaca honoured the mountains, the lake and the earth mother Pachamama."),
  (-1500, "andean", "Chiripa and Pukara temple builders were followed by Tiwanaku, a great ceremonial city from about 500 AD, and in the 1400s by the Inca, who held Lake Titicaca as the birthplace of the sun."),
  (1572, "catholic", "Spanish rule from 1538 and the Potosi silver mines brought missionaries, and Viceroy Toledo's resettlements from the 1570s made the Aymara and Quechua Catholic, blended with Pachamama worship."))

z("bolivia-lowlands", "Bolivian lowlands", -63.5, -16.5,
  (B, "folk", "Moxos peoples built raised fields and causeways in the Beni floodplains, and Chiquitano and Guarani peoples honoured forest spirits."),
  (1690, "catholic", "Jesuits founded the Moxos missions from 1682 and the Chiquitos missions from 1691, whose baroque churches still stand, and Santa Cruz grew as a Catholic frontier city."))

z("chile-north", "Northern Chile", -69.0, -22.5,
  (B, "folk", "The Chinchorro of the Atacama coast mummified their dead from about 5000 BC, two thousand years before Egypt."),
  (500, "andean", "San Pedro de Atacama and the oases came under the influence of Tiwanaku and later of the Inca, whose high Andean peak shrines held offerings and sacrifices."),
  (1540, "catholic", "Pedro de Valdivia crossed the Atacama on his way to conquer Chile, and the oasis peoples were brought into Catholic parishes."))

z("chile-central", "Central Chile", -70.8, -33.8,
  (B, "folk", "Picunche and Mapuche farmers honoured Ngenechen, the ancestors and nature spirits through machi shamans."),
  (1470, "andean", "The Inca under Topa Inca extended their empire and sun cult south to the Maipo river, near today's Santiago."),
  (1541, "catholic", "Pedro de Valdivia founded Santiago, and Chile became a Catholic colony and republic, though a fast-growing share of Chileans now have no religion."))

z("araucania", "Araucania", -72.6, -38.7,
  (B, "folk", "The Mapuche honoured Ngenechen and their ancestors through machi shamans and the nguillatun, and kept their independence from Spain after victory at Curalaba in 1598."),
  (1883, "catholic", "Chile's Occupation of the Araucania ended Mapuche independence, and Chilean and European settlers and Capuchin missions made the region Catholic, though evangelical churches are strong among the Mapuche."))

z("magallanes", "Magallanes and Tierra del Fuego", -70.9, -53.15,
  (B, "folk", "The Selk'nam, Kawesqar and Yaghan of Tierra del Fuego held the Hain initiation ceremony and believed in a supreme being, Temaukel."),
  (1885, "catholic", "Sheep ranching and gold rushes brought Chilean, Croatian and British settlers to Punta Arenas, Salesian missions gathered the surviving Selk'nam, and the native peoples were nearly destroyed."))

z("argentina-pampas", "Buenos Aires and the Pampas", -59.5, -34.8,
  (B, "folk", "Querandi and other Pampas hunters honoured the spirits of the land, later joined by Mapuche-speaking horsemen."),
  (1580, "catholic", "Juan de Garay refounded Buenos Aires, and Spanish and later mass Italian immigration made the Pampas firmly Catholic, the homeland of Pope Francis."))

z("argentina-northwest", "Argentine Northwest", -65.4, -24.8,
  (B, "folk", "The Condorhuasi, Aguada and Diaguita cultures of the valleys honoured the sun, thunder and the earth."),
  (1480, "andean", "The Inca conquered the Calchaqui valleys and built roads and peak shrines like Llullaillaco, where three child offerings were found frozen."),
  (1565, "catholic", "San Miguel de Tucuman was founded in 1565 and Salta in 1582, though the Calchaqui peoples resisted Spanish rule and Catholic missions until 1667."))

z("cuyo", "Cuyo (Mendoza)", -68.84, -32.9,
  (B, "folk", "Huarpe farmers of the Cuyo oases honoured the sun, the moon and the mountain spirits."),
  (1480, "andean", "The Inca extended the Qhapaq Nan road and their sun worship to the Huarpe of Mendoza and San Juan, and built a shrine on Aconcagua."),
  (1561, "catholic", "Pedro del Castillo founded Mendoza from Chile, and Jesuits and other orders converted the Huarpe."))

z("argentina-litoral", "Argentine Litoral", -60.0, -29.5,
  (B, "folk", "Guarani, Charrua and Chana peoples of the great rivers honoured forest and water spirits through shamans."),
  (1573, "catholic", "Juan de Garay founded Santa Fe in 1573 and Corrientes followed in 1588, and Jesuits built the Guarani reductions upriver, making the region Catholic."))

z("patagonia", "Argentine Patagonia", -68.0, -42.5,
  (B, "folk", "Tehuelche hunters and Mapuche who crossed the Andes followed shamans, and the Tehuelche told of the creator hero Elal."),
  (1879, "catholic", "The Conquest of the Desert ended native independence, and Argentine, Italian and Spanish settlers and Salesian missions made Patagonia Catholic, though Welsh settlers in Chubut from 1865 kept chapels."))

z("uruguay", "Uruguay", -56.0, -34.0,
  (B, "folk", "Charrua and Guarani peoples hunted and fished along the Uruguay river and the coast, honouring the spirits of nature."),
  (1726, "catholic", "Bruno Mauricio de Zabala founded Montevideo, and Spanish and later Italian immigrants made the country nominally Catholic."),
  (2010, "secular", "Separation of church and state in 1918 and the renaming of religious holidays made Uruguay Latin America's most secular country, where those with no religion now outnumber Catholics."))

z("paraguay", "Paraguay", -57.6, -25.3,
  (B, "folk", "Guarani farmers honoured Tupa and sought the Land Without Evil through shamans and prophets."),
  (1537, "catholic", "Spanish settlers founded Asuncion and married into Guarani families, and Jesuit reductions from 1609 made the Guarani one of the most Catholic peoples of the continent."))

z("brazil-pernambuco", "Pernambuco (north-east Brazil)", -35.5, -8.2,
  (B, "folk", "Tupi-speaking peoples such as the Potiguara and Caete honoured the thunder spirit Tupa and followed shaman prophets called pajes."),
  (1535, "catholic", "Duarte Coelho founded the captaincy of Pernambuco and the sugar town of Olinda, worked by enslaved Africans who were baptised Catholic."),
  (1630, "reformed", "The Dutch West India Company took Recife and ruled the north-east as Dutch Brazil, a Calvinist state that tolerated Catholics and Jews, though most people stayed Catholic."),
  (1654, "catholic", "Luso-Brazilian rebels expelled the Dutch, and Catholicism, alongside the African-rooted Xango religion, has remained the region's faith."))

z("brazil-bahia", "Bahia", -39.0, -12.8,
  (B, "folk", "Tupinamba and other Tupi peoples honoured Tupa and followed shaman prophets who preached the Land Without Evil."),
  (1549, "catholic", "Tome de Sousa founded Salvador as the capital of Brazil with the first Jesuits, and Bahia became Catholic, blended among enslaved Africans with the Yoruba-rooted Candomble."))

z("brazil-southeast", "Sao Paulo and Rio de Janeiro", -46.0, -23.0,
  (B, "folk", "Tupi peoples like the Tupiniquim and Tamoio honoured Tupa, the thunder, and sought the Land Without Evil."),
  (1554, "catholic", "Jesuits Manuel da Nobrega and Jose de Anchieta founded Sao Paulo and Rio de Janeiro followed in 1565, and immigration built a Catholic majority now challenged by fast Pentecostal growth."))

z("brazil-minas", "Minas Gerais", -44.0, -19.9,
  (B, "folk", "Botocudo, Puri and other Macro-Je forest peoples honoured spirits of the forest and the dead."),
  (1700, "catholic", "The gold rush of the 1690s drew settlers and enslaved Africans to Minas Gerais, where lay brotherhoods built the baroque churches of Ouro Preto."))

z("brazil-south", "Southern Brazil", -51.5, -29.0,
  (B, "folk", "Guarani, Kaingang and Charrua peoples honoured forest spirits and the Guarani creator Nhanderu."),
  (1737, "catholic", "Jesuit Guarani missions of the Seven Peoples from 1682 and Portuguese settlement from 1737 made the south Catholic, reinforced by Azorean, Italian and German Catholic settlers beside German Lutherans."))

z("brazil-center-west", "Central-West Brazil", -48.5, -16.0,
  (B, "folk", "Je-speaking peoples like the Xavante, Bororo and Kayapo held village ceremonies and honoured the spirits of the cerrado."),
  (1725, "catholic", "Bandeirantes found gold at Cuiaba in 1718 and Goias in 1725, bringing Catholic settlers to the interior, where Brasilia was built as the new capital in 1960."))

z("brazil-amazon", "Brazilian Amazon", -60.0, -3.1,
  (B, "folk", "Amazonian peoples, some living in large chiefdoms along the river before European diseases, followed shamans who mediated with forest spirits."),
  (1880, "catholic", "Missions dated back to the 1600s, but the rubber boom from the 1870s brought masses of Catholic migrants from the north-east and made Manaus a booming Catholic city."))

z("brazil-para", "Para and the Amazon mouth", -48.5, -1.45,
  (B, "folk", "The Marajoara culture built mounds and painted urns on Marajo island, and Tupinamba peoples later honoured Tupa along the coast."),
  (1616, "catholic", "The Portuguese founded Belem, and Jesuit missions under Antonio Vieira gathered the native peoples; its Cirio de Nazare procession is now one of the world's largest Catholic festivals."))

z("guyana", "Guyana", -58.4, 6.5,
  (B, "folk", "Lokono (Arawak), Carib and Warao peoples of the coast and the Wapishana and Macushi of the savannas followed shamans called piaimen."),
  (1627, "reformed", "The Dutch West India Company founded the Essequibo and Berbice plantation colonies, worked by enslaved Africans under Dutch Reformed rule."),
  (1814, "anglican", "Britain took the colonies, and after emancipation in 1838 most Afro-Guyanese joined Anglican, Methodist and Congregational churches while indentured Indians brought Hinduism and Islam."),
  (1990, "protestant", "Pentecostal and other evangelical churches grew to become the largest religious group, with Hindus about a quarter of the population."))

z("suriname", "Suriname", -55.2, 5.6,
  (B, "folk", "Lokono (Arawak), Kalina (Carib) and Trio peoples followed shamans and honoured forest spirits."),
  (1667, "reformed", "The Dutch took Suriname from England under the Treaty of Breda and built a plantation colony under Dutch Reformed rule, worked by enslaved Africans, many of whom fled to form Maroon nations."),
  (1863, "protestant", "Moravian missions active since 1735 became the largest church among Afro-Surinamese after emancipation in 1863, and Protestants remain narrowly the largest group beside Hindus, Catholics and Muslims."))

z("french-guiana", "French Guiana", -52.6, 4.8,
  (B, "folk", "Kalina, Lokono, Palikur and Wayampi peoples followed shamans and honoured forest spirits."),
  (1664, "catholic", "France settled Cayenne, and Jesuit missions, Catholic settlers and enslaved Africans baptised under the Code Noir made Catholicism the colony's faith."))

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zones_americas.json")
json.dump(Z, open(out, "w"), ensure_ascii=False, indent=1)
print(len(Z), "zones written to", out)
