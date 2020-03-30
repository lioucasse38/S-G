

# 4. Distribution spatiale du jet non-défléchi

Ainsi, dans un second temps, on vient étudier la distribution spatiale du jet non-défléchi. Le but concret de cette expérience est de venir déterminer les conditions optimales d'observation du phénomène de quantification spatiale. Or, on sait que de façon classique, sans l'application d'un champ magnétique non-uniforme, le faisceau ne sera pas dévié, d'où on obtiendra une distribution gaussienne qui aura pour maximum la position alignée avec la fente du four. Par la suite, on vient déterminer le rapport Signal sur Bruit à l'aide de la formule suivante : $\text{Signal}/\text{Bruit}$ : $(V_{pic} - V_{fond}) / V_{fond}$. A l'aide de Picolog, on utilise l'intensité à la place qui est fournie directement 

Lors de la réalisation de l'expérience, on commence par amener le courant du filament à 2.8A en attendant toujours la stabilisation, et la tension de la cage de Faraday à 5.0V.

On positionne le détecteur à l'une des extrémités, on démarre l'acquisition par l'ordinateur et l'oscilloscope, puis on sélectionne la position '+' avant de démarrer le moteur. On a alors un repère pour le moment où le détecteur a commencé à mesurer. On reproduit la même étape à la fin en arrêtant d'abord le moteur puis l'oscilloscope afin d'avoir un repère pour la fin de la mesure.

Dès lors, il est possible de calculer le temps passé pour effectuer la mesure à l'aide de ces deux repères, et, en sachant la distance parcourue en regardant la position de la vis micrométrique à chaque extrémité, nous pouvons obtenir une conversion des secondes vers les millimètres.

Nous réitérons ensuite l'opération pour différentes valeurs de $I_{détecteur}$ avec des valeurs fixes pour $V_{cage}$, puis nous pouvons évaluer le rapport $\text{Signal}/\text{Bruit}$ pour chaque prise de mesure. Nous obtenons alors que la valeur de $I_{détecteur}$ donnant le meilleur rapport $\text{Signal}/\text{Bruit}$ sera la valeur optimale à utiliser, puis à l'aide de cette valeur, nous faisons à présent varier $V_{cage}$ afin de déterminer quelle tension dans la cage de Faraday amène le meilleur rapport $\text{Signal}/\text{Bruit}$ 

Ainsi, les données obtenues sont présentées dans les tableaux suivants. Nous obtenons que les conditions optimales seront obtenues pour $I_{détecteur} = 2.9A$ et $V_{cage} = 5.0V$. Nous remarquons également que le pic résultant est asymétrique, ce qui peut amener plusieurs hypothèses:

- Au fur et a mesure que le détecteur se déplace, un dépôt de potassium se forme sur ce dernier, ce qui a pour effet d'ioniser des atomes qui ne sont pas forcément envoyés par le faisceau mais qui sont ionisés directement depuis le dépôt.
- Le détecteur se rapproche du maximum d'intensité du faisceau au début et s'en éloigne à la fin. 
- L'intensité du faisceau augmente avec le temps.

# 5. Distribution spatiale du jet défléchi

Par la suite, nous étudions le cas de la distribution spatiale du jet défléchi. Or, comme nous avons pu le voir en introduction, les atomes subissent une force à cause du champ magnétique non-uniforme et de leur moment magnétique de spin. Nous devons donc observer une déflexion du faisceau en deux si les atomes se trouvent dans leur état fondamental. Avec une analyse statistique du gaz de potassium et du faisceau qui en résulte ainsi que d'une étude des forces appliquées aux atomes de potassium, nous pouvons déterminer la déflexion des atomes avec la vitesse la plus probable fournit dans le protocole.

Ceci implique une déflexion en fonction du gradient du champ magnétique appliqué donnée par : $s_m = \pm \frac{d}{3T}(D + d/2)\frac{\mu_B}{k_B}\frac{\partial B}{\partial z}$ où D est la distance entre la fin de l'électro-aimant et la position du plan où les atomes sont observés, et d est la longueur que les atomes parcourent dans l'électro-aimant.

Il est aussi possible d'obtenir la valeur du champ magnétique moyen de l'électro-aimant à l'aide de la formule suivante : $B_{moyen} \approx a\times \frac{\partial B}{\partial z}$ où a est un paramètre de l'électro-aimant et qui vaut 5.5mm. La définition de ce terme est que si le champ magnétique était produit par deux fils parallèles de longueur infinie, a serait alors la moitié de la distance qui les séparent.

En ce qui concerne les manipulations, nous reproduisons celle effectuée pour le jet non-défléchi pour avoir des repères initiaux et finaux lors de l'acquisition des données. De plus, nous utilisons les paramètres optimaux trouvés précédemment pour le courant de détecteur et la tension de la cage de Faraday. Nous mesurons le profil du jet défléchi pour des valeurs de courant de bobine fixes.

DIAPO

Nous faisons également varier le courant appliqué dans la bobine de l'électro-amant pour faire varier le gradient du champ magnétique et prendre d'autres mesures du profil. Puis nous mesurons le position des pics s+ et s- par rapport au creux central, et avec la conversion de seconde vers millimètre, nous pouvons trouver la déflexion en mm.

De plus, avec D = 49.1cm et d = 9.5cm, on peut calculer la valeur du gradient du champ en fonction de $s$ et de $T$ d'après la formule de $\frac{\partial B}{\partial z}$, on peut en déduire le champ magnétique moyen.

Pour les résultats, nous obtenons un profil comme attendu ou le faisceau est séparé en deux, de part et d'autre du centre. Nous pouvons ainsi tracer les écarts s+ et s- obtenus en fonction du courant appliqué à la bobine. Ceci nous permet de faire un fit linéaire pour ensuite avoir la valeur du gradient du champ magnétique pour différents courants (à l'aide de la formule précédente), et ainsi en déduire la valeur du champ magnétique moyen pour différents courants.

Nous remarquons donc que la déflexion augmente avec le courant, ce qui était prévisible car le champ magnétique créé par l'électro-aimant augmente linéairement avec le courant. De plus, après avoir trouvé les valeurs de champ magnétique moyen en fonction du courant, on remarque que l'ordre de grandeur du champ magnétique est environ $0.4 \space T$, ce qui est raisonnable et cohérent selon notre configuration (les valeurs typiques de champ magnétique pour ce type)

# Conclusion

Les objectifs du laboratoire était de vérifier le comportement de la loi de Langmuir et de mesurer la distribution spatiale des jets défléchi et non-défléchi, on a démontré que le gaz de potassium se comportait bien selon cette loi, le bruit de fond aurait pu être soustrait pour pouvoir mesurer précisément les paramètres $\Lambda$ et $\Phi$. Quant aux mesures liées aux jets, on obtient bien des mesures selon les prédictions les plus récentes et on a vérifié la loi de la déflexion magnétique en calculant les écarts  $s_+$ et $s_-$ en faisant varier le gradient du champ.  

Ce qui met fin à notre présentation, merci de nous avoir écouté.