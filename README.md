# Cours-UGA-Econ-Python-L3
 
Matériel pour le cours d'introduction à Python en écononomie en L3 à l'UGA, Faculté d'Économie.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MWUrda/Cours-UGA-Econ-Python-L3.git/HEAD)

## Installation

1. **Anaconda**
   
   1.1. **Distribution**.
   
   - Remarque: L'installation risque d'échouer si le nom d'utilisateur de votre ordinateur contient un espace ou des caractères
               spéciaux (æ, ø, å, ê, â, î, ô, û, ä, ö, ë, ï, ü, ÿ, etc.). La ​​solution la plus simple consiste à modifier
               votre nom   d'utilisateur (sinon, vous devrez installer Anaconda dans un répertoire dont le chemin ne contient pas
               votre nom d'utilisateur).
     
   a. Téléchargez *Anaconda Individual Edition* (dernière version) depuis [https://www.anaconda.com/products/individual].
   
   b. Lancez le programme d'installation (les paramètres par défaut conviennent)

   - Remarque: en cas de problème, effectuez une [désinstallation](https://www.anaconda.com/docs/getting-started/anaconda/uninstall)                 complète. Installez une version antérieure d'Anaconda depuis les [archives](https://repo.anaconda.com/archive/).
   
   1.2. **Extensions**.

   a. Ouvrez le programme Anaconda Prompt (Windows) ou le Terminal (Mac) (sur Mac, le terminal est une application déjà présente sur        votre ordinateur et indépendante d'Anaconda, mais vous devez tout de même installer Anaconda pour que les commandes ci-dessous        y fonctionnent).

   b. Exécutez les commandes suivantes une par une en suivant les instructions(vous pouvez faire des "copier-coller" :

   conda update --all

   conda install -c conda-forge nodejs

   conda install -c conda-forge ipympl

   conda install -c conda-forge ipywidgets

2. **Git**
   
   2.1. Rendez-vous sur [https://github.com/] et inscrivez-vous.

   2.2. Téléchargez *Git* depuis [https://git-scm.com/]
 
   - Remarque: Pour MaC rendez-vous sur cette [page](https://git-scm.com/install/mac). Le plus simple est de télécharger                   [Homebrew](https://brew.sh/), puis de saisir la commande suivante dans le terminal : *brew install git* (lorsqu'un mot de             passe vous est demandé, tapez-le et appuyez sur Entrée ; rien ne s'affiche à l'écran tant que vous n'avez pas appuyé sur              *Entrée*).

   2.3. Exécutez le programme d'installation (les paramètres par défaut conviennent).

3. **VSCode**

   3.1. Téléchargez VSCode sur (https://code.visualstudio.com/)

   3.2. Lancez le programme d'installation (les paramètres par défaut conviennent)

   3.3. Ouvrez VSCode

   3.4. Appuyez sur *Ctrl+Maj+X* (ou sélectionnez « Extensions » dans la barre d'activité située à gauche)

      - Sur Mac : *Cmd⌘+Maj+X*

   3.5. Installez l'extension Python

   3.6. Appuyez sur *Ctrl+Maj+P* pour ouvrir la palette de commandes

      - Sur Mac : *Cmd⌘+Maj+P*

   3.7. Tapez « Python: Select Interpreter » et choisissez l'option incluant « Anaconda3 » dans le chemin d'accès

   3.8. Appuyez sur *Ctrl+æ (ou Ctrl+` ou Ctrl+j)* pour ouvrir le terminal dans VSCode

      - Sur Mac : *Cmd⌘+Maj+C* (ouvre le terminal de l'ordinateur)

   3.9. Exécutez la commande : *git config --global user.email "VOTRE E-MAIL"*

   3.10. Exécutez la commande : *git config --global user.name "VOTRE NOM D'UTILISATEUR GITHUB"*
         (Notez que ces deux dernières étapes ne généreront aucun affichage en retour)


