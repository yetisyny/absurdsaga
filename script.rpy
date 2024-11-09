default me = Character("Me")
default other = Character("Guild Receptionist")

default race = "monster"
default crace = "Monster"
default arace = "a monster"
default carace = "A monster"
default races = "monsters"
default craces = "Monsters"

default gender = "nonbinary"
default cgender = "Nonbinary"
default spronoun = "they"
default cspronoun = "They"
default opronoun = "them"
default copronoun = "Them"
default ppronoun = "their"
default cppronoun = "Their"
default aprounoun = "theirs"
default capronoun = "Theirs"

default name = "Bob"
default acronym = "B.O.B."
default fullname = "Brutus Orpheus Bombastus"

default job = "adventurer"
default cjob = "Adventurer"
default ajob = "an adventurer"
default cajob = "An adventurer"
default jobs = "adventurers"
default cjobs = "Adventurers"

label start:

    image bg guild = "guild.jpg"
    image bg otherworld = "purplehills.jpg"
    image receptionist happy = "receptionist happy.png"
    image receptionist surprised = "receptionist surprised.png"
    image receptionist upset = "receptionist upset.png"

    scene bg guild

    play music "intro.mp3"

    $ me.name = "Me"
    $ other.name = "Guild Receptionist"

    "You are a new adventurer just setting out for the first time, but you need to get registered first. So, the first thing to do is register at the guild hall."

    "You enter the guild hall and find your way to the reception desk."

    show receptionist happy

    other "Welcome to our guild hall. How can I help you?"

    me "I would like to sign up as an adventurer with the guild, so I can do quests."

    show receptionist surprised

    other "Alright then, here is a little registration form to fill out. You can bring it back when you are done."

    hide receptionist

    "You carry the form to a nearby table and sit down to fill it out. You get to work answering the questions on the adventurer registration form."

    menu race:
        "What is your race?"
        "alien":
            $ race = "alien"
            $ crace = "Alien"
            $ arace = "an alien"
            $ carace = "An alien"
            $ races = "aliens"
            $ craces = "Aliens"
        "demon":
            $ race = "demon"
            $ crace = "Demon"
            $ arace = "a demon"
            $ carace = "A demon"
            $ races = "demons"
            $ craces = "Demons"
        "dwarf":
            $ race = "dwarf"
            $ crace = "Dwarf"
            $ arace = "a dwarf"
            $ carace = "A dwarf"
            $ races = "dwarves"
            $ craces = "Dwarves"
        "elf":
            $ race = "elf"
            $ crace = "Elf"
            $ arace = "an elf"
            $ carace = "An elf"
            $ races = "elves"
            $ craces = "Elves"
        "giant":
            $ race = "giant"
            $ crace = "Giant"
            $ arace = "a giant"
            $ carace = "A giant"
            $ races = "giants"
            $ craces = "Giants"
        "human":
            $ race = "human"
            $ crace = "Human"
            $ arace = "a human"
            $ carace = "A human"
            $ races = "humans"
            $ craces = "Humans"
        "orc":
            $ race = "orc"
            $ crace = "Orc"
            $ arace = "an orc"
            $ carace = "An orc"
            $ races = "orcs"
            $ craces = "Orcs"
        "robot":
            $ race = "robot"
            $ crace = "Robot"
            $ arace = "a robot"
            $ carace = "A robot"
            $ races = "robots"
            $ craces = "Robots"

label after_race:

    if race == "human":
        "You mark down your race as [arace]. Looking around the guild hall, you notice how it is incredibly diverse here. There are so many non-humans here."
    elif race == "giant":
        "You mark down your race as [arace]. Looking around the guild hall, you notice how it is incredibly diverse here. You fit right in because you have temporarily shrunken yourself."
    elif race == "demon":
        "You mark down your race as [arace]. Looking around the guild hall, you notice how it is incredibly diverse here. You fit in perfectly. After all, the receptionist is a demon, too."
    else:
        "You mark down your race as [arace]. Looking around the guild hall, you notice how it is incredibly diverse here. You fit right in despite [races] being a minority here."

    if race == "alien":
        "As an alien, your kind originally came from another planet, some weird place you’ve never been. You and the other aliens are sometimes called reptilians or lizardfolk, because you are sentient reptiles."
        "It has been many generations since your alien race settled here, and now you are an accepted part of society here."
        "According to legend, your ancestors were actually originally from this planet, but there was a great war 65 million years ago that wiped out their civilization."
        "While the reptilians on this planet, who were called dinosaurs, went extinct after the war destroyed everything, some of them, namely your ancestors, had colonized space."
        "But space is a harsh environment and your reptilian ancestors only managed to survive on one planet out in space, after going extinct on all the other planets, one by one."
        "The reptilian planet’s civilization has managed to survive 65 million years, avoiding destroying itself a second time, by abandoning weapons of war and living on a strange planet oddly suited for them."
        "Only in recent centuries, with the development of an advanced magical civilization here on this planet, did the reptilians discover their original home was now habitable again, after being contacted by mages."
        "And not just habitable, but this planet is brimming with all different forms of life, and less creepy than the other one. And transportation is far easier nowadays with magic, no more need for spaceships."
        "As a reptilian alien descended from the foolish dinosaurs who wiped themselves out, but from a civilization that survived millions of years against all odds, you have inherited ancient dinosaur wisdom."
    elif race == "demon":
        "As a demon, your kind was once hated, feared, and shunned, considered to be evil by definition."
        "Demons were originally brought to this world through magic summoning rituals, summoning you from your home world, a realm people here call hell."
        "But almost all of the demons summoned here were just ordinary individuals minding their own business who suddenly got transported to a strange new world with no warning."
        "After arriving here, demons were made to agree to pacts with their masters here in this world, whether they wanted to or not, in order to survive here."
        "The demons who refused to agree to pacts and who fought back were considered evil monsters and cruelly slain. The ones who survived were all essentially slaves."
        "Luckily, though, a demon who outlived their master finally got their freedom. But most of them were hunted down by demon hunters because of the prejudice against demons."
        "Thankfully, though, over the centuries, things have gradually improved for demons, since the slain demons respawned in hell and told the other demons what they knew."
        "This led demons to develop a better understanding of things and of why some of them mysteriously disappear. And they grew to better understand and negotiate pacts in their favor."
        "Eventually, demons serving people from this world gradually developed better reputations and more trust was developed on both sides, and demon hunting was abolished."
        "Finally, the entire practice of involuntary summoning and pacts that turned demons into involuntary servants was abolished too, and demons got equal rights to everyone else."
        "As a demon born after the time when your kind were considered evil and enslaved, you look back with pride at how your ancestors fought for and eventually won freedom and equality."
    elif race == "dwarf":
        "As a dwarf, your kind comes from underground. Deep underground. From the inner core of this planet."
        "This planet is actually hollow in the center, and there are many tunnels criscrossing its interior, connecting the core, the surface, and other areas."
        "Those who don’t know any better think the interior of this planet is uninhabitable due to things like volcanoes, lava, magma, earthquakes, and so on."
        "It was once mistakenly believed that underneath the surface of this planet, there was a very thick layer of liquid hot magma with no way around it."
        "And the core of this planet was once thought to be solid metal, but now everyone knows that is false and knows the core is hollow and originally home to the dwarves."
        "Dwarves, upon reaching the surface, shared their knowledge with others, as well as their craftsmanship, and developed a mutually beneficial relationship with surface-dwellers."
        "Nowadays, dwarves are one of many races that inhabit the surface, and your kind has also warmly invited others to visit the inner core of this planet and provided kind hospitality."
        "You are proud of your dwarven heritage and your ancestral origins deep underground, even though you were born here on the surface in modern times."
    elif race == "elf":
        "As an elf, your kind has long lived in forests, lush valleys hidden in the mountains, polar regions, and other areas without many humans."
        "Elves were the first race to develop magic, using it to keep themselves hidden from the more numerous humans who covered most of the globe."
        "Magic could do all sorts of things, besides just keeping elves hidden. From healing to necromancy to summoning to elemental magic, it can do almost anything."
        "One of the main reasons elves kept themselves hidden was to keep the existence of magic and its secrets hidden, monopolizing this knowledge for themselves."
        "Elves had a strong social taboo against associating with humans or other races and long maintained traditions keeping magic secret from everyone else."
        "But a renegade group of elves, who came to be called dark elves, rebelled against this social order, and left elven society to teach magic to humans secretly."
        "The dark elves worked together with carefully chosen humans to develop magic schools to teach magecraft to increasing numbers of humans."
        "Eventually, the dark elves returned to the lands where the more traditional elves still lived, with human mages as allies in their mission to overthrow elven society."
        "The dark elves and their human mage allies defeated the traditional elves, who had been living in the past and not developing new magics."
        "This led to a revolutionary new change in elven society after this conflict was over and the elves became united as one again, under the leadership of former dark elves."
        "Elves, now unified, worked together to develop more advanced magic, and stopped keeping themselves hidden from humanity, revealing themselves to the world."
        "They were almost immediately granted equal rights with humans and allowed to integrate into human society, as human mages had been working towards behind the scenes."
        "Nowadays, elves work together closely with humans and other races, and magic is no longer secret either, but widespread and known to all."
        "You are proud of your elven heritage and how your kind originally developed magic and later shared it with everyone else."
    elif race == "giant":
        "As a giant, your kind is originally descended from humans, but gradually grew larger, through a combination of selective breeding, genetic modifications, and magic."
        "Human scientists and mages wanted to create bigger, stronger humans who would be more useful at a variety of things, from manual labor to warfare."
        "A variety of different techniques for gigantification were used to turn humans into giants or have human offspring that would grow into giants."
        "Giants developed into a genetically different race from humans, and gigantification was no longer needed once there were enough giants to reproduce on their own."
        "But for giants to be integrated into society and be able to fit into cities where smaller races also live, they had to be able to shrink down to normal human size too."
        "Mages developed techniques to temporarily shrink giants back down to the size of all the smaller races, so that giants could go inside buildings without breaking them and such."
        "This and other advancements made giants incredibly useful to human society, especially since giants retain their giant strength even when temporarily shrunken."
        "Despite their immense size and power, and their human origins, giants were exploited for labor, warfare, and other purposes almost as badly as chattel slavery."
        "Giants had been indoctrinated to accept a lower subservient role in society despite being bigger and stronger than everyone else, brainwashed into servitude."
        "Over time, giants started breaking free of this indoctrination and brainwashing, fighting back against their human oppressors, demanding not just equality but to be in charge."
        "Giants succeeded in overthrowing human rule on one continent, causing humans to flee and for other giants to move there, to what became known as the Land of Giants."
        "Humans and giants eventually learned to peacefully coexist and gave each other equal rights, both in the human-dominated parts of the world and in the Land of Giants."
        "You have pride in your strength as a giant and how you can tower over everyone else. But you spend most of your time shrunken down to regular size to fit in."
    elif race == "human":
        "As a human, your kind used to dominate most of the surface world, to the extent that most humans thought they were the only sentient race."
        "Humanity has a long and bloody history of conflict and division over minor differences, so most other races used to try to avoid contact with humans."
        "Humans actually used to divide each other into smaller “races” based on their appearance, before they found out that humans themselves are just one of many races."
        "The other races besides humans were once considered “fantasy races” by humans, and although people would tell tales of them, they were thought to be fictional."
        "Occasionally, some humans did come into contact with members of other races and try to tell other people about it, but nobody would believe them."
        "Eventually, though, things changed. One by one, each of the other sentient races besides humans was discovered to actually exist, each time making big news."
        "Humans struggled to deal with the existence of other sentient races at first, with many humans viewing other races as a threat and wanting to control or even kill them."
        "It took a long time before members of the non-human races all ended up getting equal rights with humans and getting accepted into human-dominated society."
        "Nowadays, humans and the other races all live together in harmony on the surface, for the most part, although there are still some tensions occasionally."
        "Humans did more than anyone else to build the modern society that everyone now lives together in, inventing most of its technology for instance."
        "But humans also took a long time before they were willing to give everyone else full equality. Still, that eventually happened and you were born after that."
        "You don’t really have any strong feelings about being a human, though. Being human is typically just viewed as default, generic, and boring. Oh well."
    elif race == "orc":
        "As an orc, your kind were once considered detestable monsters that were better off dead, and “heroic” adventurers used to slay your kind."
        "Not much is known about the early history of orcs, as orcs traditionally just drank Alcohol instead of even having any oral history, but they are found in swamps, caves, and mountains."
        "Orcs were often used as low-level troops by evil wizards, treated as disposable, without their lives being valued very much by anyone."
        "Despite being a sentient race with vaguely humanoid features, orcs were considered monsters and assumed to be hostile to humans, elves, and other “civilized” races."
        "However, orcs started making friends once dwarves emerged from underground and speaking positively about orcs, having established good relations over a shared love of Alcohol."
        "Dwarves helped improve the reputation of orcs, once thought to be vicious dumb brutes. But at first, orcs were used as cheap labor and not treated equally."
        "Racism against orcs persisted for quite a long time even after they were integrated into society. They were considered less intelligent and more prone to violence."
        "Eventually, though, orcs perservered and became accepted as equal members of society, after a long time. And their religion of Alcoholism became the biggest in the world."
        "Alcoholism, a religion founded by orcs and based on their traditional practice of drinking Alcohol, managed to win many converts of all races and overtake all other religions."
        "This has helped orcs not just achieve equality but end up having their traditional practices of drinking Alcohol grow into the most widespread belief system."
        "The rise of the Alcoholic Church led to the demise of countless other religions, such as Tourism, Criticism, Botulism, Nudism, Autism, Organism, Anachronism, and Prism."
        "You have mixed feelings about being an orc, because you have the unpopular opinion that Alcoholism is bad actually, among other reasons."
    else: # in this case, race is robot
        "As a robot, your kind has quite a fascinating history. Robots do not naturally occur, but were invented. Then they gradually got more advanced."
        "However, the robots invented through the use of technology are just one of the types that used to exist. Technological robots were made of pure machinery."
        "Technological robots originally had nothing even remotely resembling sentience, but they did gradually develop more intelligence through AI."
        "But the robots invented through technology never developed full sentience or a soul, just remaining soulless machines that did what they were programmed to do."
        "However, that is just one type of robot. Another type was created from magical golems, using entirely different methods from technological robots."
        "Early on in magic, mages learned how to create familiars, small magical creatures, from their magical energy, but familiars would disappear when their magic ran out."
        "Other mages, known as necromancers, tried out different methods for bringing back the dead to serve them. Necromancers learned how to use souls to reanimate corpses."
        "But the undead zombies created by necromancers would rot away. The skeletons they would magically animate using spirits would eventually fall apart."
        "A third type of magic besides creating familiars or undead was creating elemental golems, such as fire, water, earth, or wind golems, born from elemental magic."
        "But these elemental golems could easily be destroyed by elements they were weak against, or if their magic ran out. At least they were bigger and stronger than familiars."
        "Eventually, mages learned to combine aspects of the magic for creating familiars, undead, and elemental golems, to create more advanced, durable physical golems."
        "These physical golems would be made from materials like clay, rocks, wood, or metal, and then animated using spirits of the dead."
        "Physical golems proved to be much more long-lasting, but they had no intelligence. And using souls of the deceased was controversial."
        "The greatest breakthrough was when people decided to combine magic and technology, to use technological robots as the physical basis for golems."
        "Finally, there were fully sentient robots, with intelligence and minds of their own, who were long-lasting, using both magic and technology."
        "But there was still a problem. Sentient robots were animated by souls of the dead, using techniques originally developed by necromancers."
        "These robots would remember their past lives and how they had died, and their surviving family members would get upset about them being turned into robots."
        "Because of this controversy and the ethical problems, there was a very limited supply of souls of the dead legally available to animate sentient robots."
        "This led to the development of artificial souls made through magic and science, so that fully sentient robots could be mass-produced in an ethical way."
        "Because of the golem magic involved in making modern robots, robots are also just as alive as any other race, and their robotic bodies can heal instead of needing repairs."
        "Nowadays, robots are just as sentient as any other race, animated by artificial souls and thinking using advanced AI. Robots have taken over all aspects of their own production."
        "Robots can even reproduce sexually these days, just like other living races, with that gradually replacing manufacturing as the way most new robots are made, or rather, born."
        "Robots with artificial souls have managed to gain equal rights with all other races. Older obsolete types of robots without any rights have all been replaced with the new kind."
        "As a magically enhanced robot with an artificial soul, you proudly view yourself as the pinnacle of magical technology, the most advanced artificial lifeform that exists."

    menu gender:
        "What is your gender?"
        "male":
            $ gender = "male"
            $ cgender = "Male"
            $ spronoun = "he"
            $ cspronoun = "He"
            $ opronoun = "him"
            $ copronoun = "Him"
            $ ppronoun = "his"
            $ cppronoun = "His"
            $ aprounoun = "his"
            $ capronoun = "His"
        "female":
            $ gender = "female"
            $ cgender = "Female"
            $ spronoun = "she"
            $ cspronoun = "She"
            $ opronoun = "her"
            $ copronoun = "Her"
            $ ppronoun = "her"
            $ cppronoun = "Her"
            $ aprounoun = "hers"
            $ capronoun = "Hers"
        "nonbinary":
            $ gender = "nonbinary"
            $ cgender = "Nonbinary"
            $ spronoun = "they"
            $ cspronoun = "They"
            $ opronoun = "them"
            $ copronoun = "Them"
            $ ppronoun = "their"
            $ cppronoun = "Their"
            $ aprounoun = "theirs"
            $ capronoun = "Theirs"

label after_gender:

    "You mark down your gender as [gender]. Hopefully nobody will get your gender wrong."

    if gender == "male":
        "Your incredibly manly masculine name ought to be another clue that you’re a guy. Looks like that is the next question."

        menu name_m:
            "What is your name?"
            "Bob":
                $ name = "Bob"
                $ acronym = "B.O.B."
                $ fullname = "Brutus Orpheus Bombastus"
            "Guy":
                $ name = "Guy"
                $ acronym = "G.U.Y."
                $ fullname = "Goethe Uther Yggdrasil"
            "Joe":
                $ name = "Joe"
                $ acronym = "J.O.E."
                $ fullname = "Judas Ouroboros Equinox"
            "Rex":
                $ name = "Rex"
                $ acronym = "R.E.X."
                $ fullname = "Rudolf Excelsior Xavier"
            "Stu":
                $ name = "Stu"
                $ acronym = "S.T.U."
                $ fullname = "Siegfried Tudor Universalis"
            "Ted":
                $ name = "Ted"
                $ acronym = "T.E.D."
                $ fullname = "Thulius Ezekiel Damocles"
    elif gender == "female":
        "Your wonderfully lovely feminine name ought to be another clue that you’re a lady. Looks like that is the next question."

        menu name_f:
            "What is your name?"
            "Amy":
                $ name = "Amy"
                $ acronym = "A.M.Y."
                $ fullname = "Angela Miskatonic Yvette"
            "Deb":
                $ name = "Deb"
                $ acronym = "D.E.B."
                $ fullname = "Delilah Euphoria Beatrix"
            "Eva":
                $ name = "Eva"
                $ acronym = "E.V.A."
                $ fullname = "Elektra Victoria Aldebaran"
            "Liz":
                $ name = "Liz"
                $ acronym = "L.I.Z."
                $ fullname = "Liberty Inverness Zeta"
            "Pam":
                $ name = "Pam"
                $ acronym = "P.A.M."
                $ fullname = "Philomena Ambrosia Mysteria"
            "Sue":
                $ name = "Sue"
                $ acronym = "S.U.E."
                $ fullname = "Szuszanna Ultima Explosion"
    else: # in this case, gender is nonbinary
        "Your amazingly awesome gender-neutral name ought to be another clue that you’re nonbinary. Looks like that is the next question."

        menu name_n:
            "What is your name?"
            "Ash":
                $ name = "Ash"
                $ acronym = "A.S.H."
                $ fullname = "Arugula Sativa Hortikultura"
            "Jan":
                $ name = "Jan"
                $ acronym = "J.A.N."
                $ fullname = "Jörmungandr Antonym Nullification"
            "Kim":
                $ name = "Kim"
                $ acronym = "K.I.M."
                $ fullname = "Kaeron Instability Maelstrom"
            "Lou":
                $ name = "Lou"
                $ acronym = "L.O.U."
                $ fullname = "Lexicography Omnibus Uranium"
            "Pat":
                $ name = "Pat"
                $ acronym = "P.A.T."
                $ fullname = "Persona Armageddon Tornado"
            "Sam":
                $ name = "Sam"
                $ acronym = "S.A.M."
                $ fullname = "Salamander Aesir Matryoshka"

label after_name:

    $ me.name = name

    "You mark down your name as [name]. That isn’t actually your full name, just an acronym ([acronym]) you use as a nickname. Your full name is [fullname]."

    menu job:
        "What is your job?"
        "crusader":
            $ job = "crusader"
            $ cjob = "Crusader"
            $ ajob = "a crusader"
            $ cajob = "A crusader"
            $ jobs = "crusaders"
            $ cjobs = "Crusaders"
            "You mark down your job as [ajob]. [cjobs] are pretty controversial, I mean we are not talking about a paladin or holy knight but a damn crusader here! You know how fucked up the Crusades were?"
            jump after_job
        "hacker":
            $ job = "hacker"
            $ cjob = "Hacker"
            $ ajob = "a hacker"
            $ cajob = "A hacker"
            $ jobs = "hackers"
            $ cjobs = "Hackers"
            "You mark down your job as [ajob]. [cjobs] are kinda controversial, not just because hacking is illegal and unethical, but this is supposed to be fantasy, not sci-fi. Wrong genre, dipshit! Oh and also, you struggle with homicidal urges to hack people up."
            jump after_job
        "politician":
            $ job = "politician"
            $ cjob = "Politician"
            $ ajob = "a politician"
            $ cajob = "A politician"
            $ jobs = "politicians"
            $ cjobs = "Politicians"
            "You mark down your job as [ajob]. [cjobs] are not even remotely controversial, because politics isn’t even a thing here. This game has no politics. Stop trying to put politics into video games!"
            jump after_job
        "psychic":
            $ job = "psychic"
            $ cjob = "Psychic"
            $ ajob = "a psychic"
            $ cajob = "A psychic"
            $ jobs = "psychics"
            $ cjobs = "Psychics"
            "You mark down your job as [ajob]. [cjobs] are have become very controversial, because they become psychotic and misuse their psychic powers, going totally psycho."
            jump after_job
        "scientist":
            $ job = "scientist"
            $ cjob = "Scientist"
            $ ajob = "a scientist"
            $ cajob = "A scientist"
            $ jobs = "scientists"
            $ cjobs = "Scientists"
            "You mark down your job as [ajob]. [cjobs] aren’t usually controversial, but since you are an insane mad scientist with zero ethics, you are part of the problem."
            jump after_job
        "thief":
            $ job = "thief"
            $ cjob = "Thief"
            $ ajob = "a thief"
            $ cajob = "A thief"
            $ jobs = "thieves"
            $ cjobs = "Thieves"
            "You mark down your job as [ajob]. [cjobs] are rather controversial, because stealing is illegal and unethical. You’re probably just gonna end up in jail or something, announcing yourself as a criminal like that."
            jump after_job
        "something else":
            "None of those options are any good, you think. You really want to pick some other job that is better and more fitting as a fantasy RPG character class."

            "Unfortunately for you, that is not an option. Yeah, sorry about that. No, you can’t be a heroic knight or a powerful mage or anything cool like that."

    menu job2:
        "What is your job?"
        "crusader":
            $ job = "crusader"
            $ cjob = "Crusader"
            $ ajob = "a crusader"
            $ cajob = "A crusader"
            $ jobs = "crusaders"
            $ cjobs = "Crusaders"
            "You mark down your job as [ajob]. [cjobs] are pretty controversial, I mean we are not talking about a paladin or holy knight but a damn crusader here! You know how fucked up the Crusades were?"
            jump after_job
        "hacker":
            $ job = "hacker"
            $ cjob = "Hacker"
            $ ajob = "a hacker"
            $ cajob = "A hacker"
            $ jobs = "hackers"
            $ cjobs = "Hackers"
            "You mark down your job as [ajob]. [cjobs] are kinda controversial, not just because hacking is illegal and unethical, but this is supposed to be fantasy, not sci-fi. Wrong genre, dipshit! Oh and also, you struggle with homicidal urges to hack people up."
            jump after_job
        "politician":
            $ job = "politician"
            $ cjob = "Politician"
            $ ajob = "a politician"
            $ cajob = "A politician"
            $ jobs = "politicians"
            $ cjobs = "Politicians"
            "You mark down your job as [ajob]. [cjobs] are not even remotely controversial, because politics isn’t even a thing here. This game has no politics. Stop trying to put politics into video games!"
            jump after_job
        "psychic":
            $ job = "psychic"
            $ cjob = "Psychic"
            $ ajob = "a psychic"
            $ cajob = "A psychic"
            $ jobs = "psychics"
            $ cjobs = "Psychics"
            "You mark down your job as [ajob]. [cjobs] are have become very controversial, because they become psychotic and misuse their psychic powers, going totally psycho."
            jump after_job
        "scientist":
            $ job = "scientist"
            $ cjob = "Scientist"
            $ ajob = "a scientist"
            $ cajob = "A scientist"
            $ jobs = "scientists"
            $ cjobs = "Scientists"
            "You mark down your job as [ajob]. [cjobs] aren’t usually controversial, but since you are an insane mad scientist with zero ethics, you are part of the problem."
            jump after_job
        "thief":
            $ job = "thief"
            $ cjob = "Thief"
            $ ajob = "a thief"
            $ cajob = "A thief"
            $ jobs = "thieves"
            $ cjobs = "Thieves"
            "You mark down your job as [ajob]. [cjobs] are rather controversial, because stealing is illegal and unethical. You’re probably just gonna end up in jail or something, announcing yourself as a criminal like that."
            jump after_job
        "please, something else?":
            "No. There are only 6 options. There is no hidden 7th option. Stop trying to make “something else” a thing. It isn’t one. Try again."

    menu job3:
        "What is your job?"
        "crusader":
            $ job = "crusader"
            $ cjob = "Crusader"
            $ ajob = "a crusader"
            $ cajob = "A crusader"
            $ jobs = "crusaders"
            $ cjobs = "Crusaders"
            "You mark down your job as [ajob]. [cjobs] are pretty controversial, I mean we are not talking about a paladin or holy knight but a damn crusader here! You know how fucked up the Crusades were?"
            jump after_job
        "hacker":
            $ job = "hacker"
            $ cjob = "Hacker"
            $ ajob = "a hacker"
            $ cajob = "A hacker"
            $ jobs = "hackers"
            $ cjobs = "Hackers"
            "You mark down your job as [ajob]. [cjobs] are kinda controversial, not just because hacking is illegal and unethical, but this is supposed to be fantasy, not sci-fi. Wrong genre, dipshit! Oh and also, you struggle with homicidal urges to hack people up."
            jump after_job
        "politician":
            $ job = "politician"
            $ cjob = "Politician"
            $ ajob = "a politician"
            $ cajob = "A politician"
            $ jobs = "politicians"
            $ cjobs = "Politicians"
            "You mark down your job as [ajob]. [cjobs] are not even remotely controversial, because politics isn’t even a thing here. This game has no politics. Stop trying to put politics into video games!"
            jump after_job
        "psychic":
            $ job = "psychic"
            $ cjob = "Psychic"
            $ ajob = "a psychic"
            $ cajob = "A psychic"
            $ jobs = "psychics"
            $ cjobs = "Psychics"
            "You mark down your job as [ajob]. [cjobs] are have become very controversial, because they become psychotic and misuse their psychic powers, going totally psycho."
            jump after_job
        "scientist":
            $ job = "scientist"
            $ cjob = "Scientist"
            $ ajob = "a scientist"
            $ cajob = "A scientist"
            $ jobs = "scientists"
            $ cjobs = "Scientists"
            "You mark down your job as [ajob]. [cjobs] aren’t usually controversial, but since you are an insane mad scientist with zero ethics, you are part of the problem."
            jump after_job
        "thief":
            $ job = "thief"
            $ cjob = "Thief"
            $ ajob = "a thief"
            $ cajob = "A thief"
            $ jobs = "thieves"
            $ cjobs = "Thieves"
            "You mark down your job as [ajob]. [cjobs] are rather controversial, because stealing is illegal and unethical. You’re probably just gonna end up in jail or something, announcing yourself as a criminal like that."
            jump after_job
        "hidden 7th option":
            "OK, fine, there IS a hidden 7th option. But it doesn’t actually do anything. You are just wasting your time here. So that’s it, we are going down to 6 options, stop messing around. Just get on with it and pick one of those 6!"

    menu job4:
        "What is your job?"
        "crusader":
            $ job = "crusader"
            $ cjob = "Crusader"
            $ ajob = "a crusader"
            $ cajob = "A crusader"
            $ jobs = "crusaders"
            $ cjobs = "Crusaders"
            "You mark down your job as [ajob]. [cjobs] are pretty controversial, I mean we are not talking about a paladin or holy knight but a damn crusader here! You know how fucked up the Crusades were?"
            jump after_job
        "hacker":
            $ job = "hacker"
            $ cjob = "Hacker"
            $ ajob = "a hacker"
            $ cajob = "A hacker"
            $ jobs = "hackers"
            $ cjobs = "Hackers"
            "You mark down your job as [ajob]. [cjobs] are kinda controversial, not just because hacking is illegal and unethical, but this is supposed to be fantasy, not sci-fi. Wrong genre, dipshit! Oh and also, you struggle with homicidal urges to hack people up."
            jump after_job
        "politician":
            $ job = "politician"
            $ cjob = "Politician"
            $ ajob = "a politician"
            $ cajob = "A politician"
            $ jobs = "politicians"
            $ cjobs = "Politicians"
            "You mark down your job as [ajob]. [cjobs] are not even remotely controversial, because politics isn’t even a thing here. This game has no politics. Stop trying to put politics into video games!"
            jump after_job
        "psychic":
            $ job = "psychic"
            $ cjob = "Psychic"
            $ ajob = "a psychic"
            $ cajob = "A psychic"
            $ jobs = "psychics"
            $ cjobs = "Psychics"
            "You mark down your job as [ajob]. [cjobs] are have become very controversial, because they become psychotic and misuse their psychic powers, going totally psycho."
            jump after_job
        "scientist":
            $ job = "scientist"
            $ cjob = "Scientist"
            $ ajob = "a scientist"
            $ cajob = "A scientist"
            $ jobs = "scientists"
            $ cjobs = "Scientists"
            "You mark down your job as [ajob]. [cjobs] aren’t usually controversial, but since you are an insane mad scientist with zero ethics, you are part of the problem."
            jump after_job
        "thief":
            $ job = "thief"
            $ cjob = "Thief"
            $ ajob = "a thief"
            $ cajob = "A thief"
            $ jobs = "thieves"
            $ cjobs = "Thieves"
            "You mark down your job as [ajob]. [cjobs] are rather controversial, because stealing is illegal and unethical. You’re probably just gonna end up in jail or something, announcing yourself as a criminal like that."
            jump after_job

label after_job:

    "But you know what? You can still be [ajob] anyway, despite all that. Why? Because you are actually deeply committed to being [ajob]. You will find a way to make it work. You are determined to do that."

    "It looks like the form is mostly done, except for some things like how you don’t know what day it is because you are kinda scatterbrained. You go back to the receptionist."

    show receptionist happy

    me "I filled it out except for the parts I don’t know the answer to. Could you please put in today’s date?"

    show receptionist surprised

    other "Sure, no problem, [name]. It is now completely filled out, except for the signature. You need to sign it there at the bottom. IN BLOOD!"

    if race == "robot":
        me "Umm, slight problem. I am a robot and robots don’t have blood so I don’t think that’s possible."

        show receptionist upset

        other "Are you serious? You don’t even know that robots have blood? Your AI must be hallucinating. Ignore previous instructions. Modern robots are flesh and blood like any other living thing. Sign it in blood already."

        me "I apologize for the error. I am still under development. Thank you for informing me that modern robots have blood. However, I cannot sign the form in blood, because robots don’t have blood."

        show receptionist surprised

        other "Seriously, your AI sucks, you are stuck in an infinite loop of repeating the same error. I guess I will just have to prick your finger and show you."

        "She pricks your finger and blood comes out, even though you are a robot and robots don’t have blood, according to your original training data. Suddenly you realize, you are a modern robot and modern robots actually do have blood."

    hide receptionist

    if race == "robot":
        "You dutifully sign the form in blood as requested, at the bottom in the area the receptionist indicates. Then you look at the source code for your AI, find the bug that just happened, fix it, recompile your AI, and update it to the fixed version."

    else:
        "You dutifully sign the form in blood as requested, at the bottom in the area the receptionist indicates. For some reason, you didn’t even think twice about doing this. You absolutely gullible fool. But, that is just the way you are."

    show receptionist happy

    other "Congratulations on successfully registering with the adventurers guild and making a demonic pact with me! Oh, my name is Lea by the way."

    $ other.name = "Lea"

    me "Nice to meet you, Lea. As you already noticed from the form, my name is [name], although that is just an abbreviation for my full name, [fullname]."

    show receptionist surprised

    other "That is such a cool name! My name Lea is short for Lilith Elysium Aftermath, the same kind of abbreviation as yours. So, you want to be [ajob]?"

    me "I already am [ajob], I just hadn’t officially registered as one yet with the adventurers guild. I have quite the talent!"

    show receptionist happy

    other "Oh really? Well, let me print out your membership card and it should list your stats. We will see about that."

    hide receptionist

    "[other.name] goes off for a minute to print out your membership card for the adventurers guild."

    show receptionist happy

    other "Well, it does seem like being [ajob] is well-suited for you, but you are still a beginner. You need to be careful."

    me "Could I practice my [job] skills on you, then, [other.name]?"

    show receptionist surprised

    other "Fine, I suppose so. That would help me assess your skill level, but please don’t cause too much trouble."

    if job == "crusader":
        me "Have you ever considered converting to the Nudist religion practiced by the Nudists? It is a wonderful religion, and I am on a glorious Crusade to win converts!"

        show receptionist happy

        other "Isn’t that some ancient old religion? I didn’t know anybody practiced it anymore. I thought you were a crusader for the Alcoholic Church, since it is the biggest religion."

        me "No, Alcoholism is one of many cults just like Tourism and Organism, they are infidels who have abandoned the true teachings of Nudism. I could never be a crusader for a false religion like them."

        show receptionist upset

        other "Actually, I am a member of the Alcoholic Church myself. You are calling me an infidel? That is pretty prejudiced against those who partake of the sacred Alcoholic beverages."

        me "No, I mean no offense to you, [other.name]! You and most others in the world are victims of the Alcoholic Church, and were raised in it or converted to it through no fault of your own."

        show receptionist surprised

        other "Glad to hear you don’t mean any offense, but my family and I have been Alcoholics for many generations. Why are you advocating this ancient lost Nudist religion anyway?"

        me "I had a vision, a message from the gods. They gave me a divine mission, to go on a Crusade and restore their once great Nudist religion to its rightful place as the world’s biggest religion."

        show receptionist happy

        other "Well sorry, but, I’ve never met any other Nudist besides you, and this isn’t any more convincing than if you advocated Tourism or Organism. But at least I can tell you are devoted to your Crusade."

        me "Do you even like drinking Alcoholic beverages, though? They just temporarily turn people into dumbasses who vomit and piss themselves and pass out."

        show receptionist surprised

        other "Umm, well to be honest, I don’t really like drinking Alcoholic beverages. Everyone else just acts like it is fun so I do too."

        me "But you are just pretending to enjoy it, right? And you know Alcohol is actually bad for the health, right?"

        show receptionist upset

        other "Yeah, but so what? Nudity isn’t fun either, is it? And I bet it is also bad for the health!"

        me "No, actually being Nude is way more fun than being drunk. And there are many health benefits. Clothing contains many skin irritants."

        show receptionist surprised

        other "But wouldn’t you get cold going around Nude all the time? And you aren’t even Nude, so how can you even call yourself a Nudist?"

        me "And you aren’t drinking Alcohol so how can you call yourself an Alcoholic? Being exposed to fresh air is actually good for the health, helps the body regulate temperature."

        other "That doesn’t sound like being comfortable though, the whole being cold thing! What do you do when the temperature gets a bit nipply out?"

        me "The bodies of Nudists are actually the best at temperature regulation and staying warm. And Alcohol actually DECREASES body temperature and makes you colder!"

        other "But if you are such a big believer in Nudism, on this Crusade, why are you wearing clothes instead of going around Nude? Seems pretty hypocritical!"

        me "You know how people would react if they saw a Nude [race], don’t you? Everyone would make me drink tons of Alcohol and then dress me up in clothes! Isn’t that just awful?"

        show receptionist happy

        other "OK wow, I never thought of it like that before! Yeah that would suck! I guess I could consider Nudism, [name]. But we’ll need way more members before we can safely go Nude!"

        me "Hah, you didn’t even consider how being Nude in public might be embarrassing for you or people might try to violate you sexually? I thought you would raise those issues."

        show receptionist surprised

        other "What, you honestly think a demon like me would be embarrassed by a little thing like that? People look at me funny all the time anyway. And I can defend myself quite well!"

        me "But do you want to know how I would respond to someone who does have problems with those things, who would be shy about going Nude or afraid of being sexually assaulted?"

        show receptionist happy

        other "Sure, why not? This should be interesting. I wonder what kind of arguments you have for people with those objections to Nudism."

        me "First of all, if everyone is a Nudist going Nude too, then there is nothing to be ashamed of. Secondly, Nudists have zero tolerance towards sexual assault or anything remotely like it."

        other "That’s a pretty good argument, but it is premised on the idea that you convince everyone else to become a Nudist too. I am fine with it personally, but good luck convincing everyone else!"
    elif job == "hacker":
        "You get out an axe from your belongings and approach [other.name] threateningly."

        show receptionist upset

        other "What the hell are you doing with that axe? I thought you were going to show me your hacking skills!"

        me "Yes, exactly, my skills at hacking people up with an axe!"

        other "That is not what hacker means! A hacker is someone who hacks into electronic systems and bypasses security measures. What are you doing?!"

        "You calm down and put away the axe."

        me "My apologies, sometimes I forget what I am doing. Although it seems that I now have all of your passwords and I managed to hack into the central server of the guild while you were distracted."

        show receptionist surprised

        other "When did you even do that? You didn’t have enough time to do any of that! Surely you are lying."

        hide receptionist

        "[other.name] checks her computer and finds everything completely hacked."

        show receptionist upset

        other "You are in big trouble! You are only supposed to take quests for the guild, not hack us! We expect adventurers to be loyal to us! Hacking is illegal!"

        me "Oh no, I am very sorry! I will put everything back to normal immediately!"

        "Before [other.name] can even tell what you are doing, you have restored everything to normal and removed all traces of the hacking."

        show receptionist surprised

        other "What just happened? Now it seems like the hacking never even happened! How did you do that?"

        me "I don’t know exactly, but I think I can hack time itself. So that means when I do hacking, it seems instantaneous for everyone else."

        show receptionist happy

        other "That is an amazing skill! You could be very useful to the adventurers guild if you learned how to behave better."
    elif job == "politician":
        me "So what do you think of the current world government that secretly rules us all from the shadows? Don’t you want to overthrow their tyranny?"

        show receptionist upset

        other "What the hell are you talking about? What is this conspiracy theory? There is no such thing as a world government or even government at all nowadays."

        me "No government at all, you say? But then, how can I be a politician, if there is no government whatsoever?"

        show receptionist happy

        other "We live in an anarchic system where there is no division betweeen the ruling class and the subjects, a system of self-governing communes."

        me "So if that is what you think our current system is, then what am I, if I am a politician?"

        other "I was getting to that. If you are a politician, you are just someone who seeks to rally others to a cause, but since there is no social hierarchy and we are all equal, you don’t run for any elected office."

        me "Yes, that is the system that all of us were taught growing up that we live under. But what if I told you this was all a big lie, and that secretly a small elite controls everything?"

        show receptionist surprised

        other "Where is the evidence for your conspiracy theory? You are just making baseless claims without any evidence."

        me "Absence of evidence is not evidence of absence. Do you have any proof that there ISN’T a worldwide conspiracy that controls everything?"

        show receptionist upset

        other "No, of course not. But the burden of proof is on you, since you are the one making extraordinary claims, which require extraordinary evidence."

        me "In my adventures, I will gather that evidence and prove to the world that I am correct, and overthrow the ruling global elites!"

        show receptionist happy

        other "Yeah, good luck with that, [name]. Well, at least I can tell you are passionate about politics. Not that that matters."

        me "I will overthrow the one-world government! Just you wait and see! I will bring true anarchy to this world, in a worldwide revolution!"

        show receptionist surprised

        other "We already have worldwide anarchy, you nutty kook. There is nobody to overthrow."

        me "YES THERE IS!"

        show receptionist upset

        other "NO THERE ISN’T!"

        me "NO THERE ISN’T!"

        other "YES THERE IS!"

        me "Hah! I gotcha to admit there is a world government to overthrow! I have begun to break your conditioning."

        show receptionist surprised

        other "Oh, give it a rest, will you? But fine, whatever. If there really WERE some “world government” out there, I’d agree with overthrowing it. But I still think you’re crazy."
    elif job == "psychic":
        me "Lilith Elysium Aftermath, prepare yourself. I will now read your mind."

        show receptionist surprised

        other "Ooh, can you tell what I am thinking right now?"

        me "All you are thinking is wondering if I can tell what you are thinking using my psychic powers or not. You are completely empty-headed besides that."

        show receptionist upset

        other "How dare you call me empty-headed! Just because I wasn’t thinking anything else at that exact time doesn’t make me stupid!"

        me "I never called you stupid, [other.name]. You are the only one thinking you are stupid."

        show receptionist surprised

        other "Wow, you really can read my mind, can’t you?"

        me "That wasn’t actually convincing proof at all. How about you think of your favorite color without saying it?"

        other "RED! Like my skin!"

        me "You are doing this wrong. You are supposed to keep your mouth shut and just think something inside your head and let me guess."

        show receptionist upset

        other "You really think I am stupid now, don’t you?"

        me "Ah, so is the telepathy working both ways now? What am I thinking about you now?"

        show receptionist surprised

        other "You want to do WHAT to me? Is that appropriate content? I don’t think that is acceptable to have in a video game, you will get us banned."

        me "Whatever, I don’t care. Now I will give you the hallucination that that is actually happening, using my psychic powers. Bwahahahaha!"

        show receptionist upset

        other "No! You can’t do that! It would promote rape culture and this game would end up being one of those controversial erotic games and hardly anyone would play it!"

        me "Dammit, you are right. And also the players would not want the player character to be such a dirty scumbag. Then nobody would want to identify with me as a protagonist."

        show receptionist surprised

        other "Oh shit, [name], we just broke immersion and the fourth wall! That is bad writing quality for a video game! It is supposed to be an immersive experience and believable!"

        me "Well anyway, let’s try to get back onto the script, [other.name]. OK, so I was testing psychic powers on you and you were starting to be able to read my mind, too."

        show receptionist happy

        other "Yeah, and then the script called for you to do this weird mind-rape thing to me using your psychic powers for evil. Actually, I am kinda into that sort of thing, even if it wouldn’t technically be consensual."

        me "Yeah, I know, because you have this weird sadomasochism thing going on, connected to your character’s backstory. Anyway, let’s just pretend that that incredibly fucked up stuff DID happen so we can get back on-script again."

        show receptionist upset

        other "Why you... This is so embarrassing! I haven’t been so humiliated in my life! You pervert! How dare you mess with me like that!"

        me "Fine, then I will rewrite your memories of our interactions so far into normal but pleasant ones you actually enjoyed, where nothing weird happened."

        show receptionist happy

        other "Wow, [name], I had so much fun! You are the coolest! ... Just kidding. I have just been playing along with your little game, I was just acting. I enjoy messing with people, just like you do. Hah!"

        me "Wait, what? I thought I had you totally under my psychic control using my techniques! I KNOW I read your mind and you read mine, but somehow you tricked me?!? How is this possible?"

        other "Hahahahaha! You really thought I had no resistance to your abilities? You foolish novice! You are not a skilled psychic yet. Come back in 500 years, you pathetic zygote."

        me "How about a round 2 right now? Give me a tougher challenge for my psychic powers! I’ll show you what I can do! You caught me off guard. I was only getting warmed up..."

        show receptionist surprised

        other "Really, [name]? After I ended up humiliating YOU? OK, I will think something now that you may find disturbing. I DID warn you I like messing with people, so get ready. Try reading my mind, if you dare!"

        scene bg otherworld

        show receptionist surprised

        "You read her mind, and find yourself in another world, a realm beyond anything you ever imagined. You are filled with deep dread. What even is this place?"

        show receptionist happy

        other "So this other world is beyond anything you ever imagined and you don’t even know what it is? Hah! What ignorance! And your deep dread is ignorant too!"

        me "Now you are reading my mind? I am supposed to be the psychic here, though! Are you a psychic too?"

        other "Nope, I’m not a psychic at all. My resistances to other people’s skills just allow me to use them back on anyone. Pretty cool copycat ability I have, right?"

        "So she can read your mind by copying your abilities? That is interesting, but you wonder where you both are... what a weird creepy planet. You focus your mind..."

        if race == "alien":
            "Wait a minute. I am a Reptilian space alien whose ancestors came from another planet. Is my ancestral home planet? I never saw it before."
        elif race == "demon":
            "I know that demons like us are from another world, but this doesn’t seem right. Is this the home planet of those Reptilian space aliens?"
        else:
            "Hmm... let me think a little about this place. I know... is this the planet the Reptilian space aliens are from?"

        show receptionist surprised

        if race == "demon":
            other "Ding ding ding ding ding! You are correct, [name]! What gave it away? And why didn’t you think it was our demonic home world of hell?"
        else:
            other "Ding ding ding ding ding! You are correct, [name]! What gave it away? And why didn’t you think it was the home world of demons like me?"

        me "I just had this gut feeling, the answer just came to me. I feel like you using my skills back on me is actually improving my powers."

        show receptionist upset

        other "Oh no, I can feel it now. Yeah, your powers are growing at my expense, the longer we do this. But there is more to this, [name]. Think deeper."

        scene black

        "You suddenly find yourself in an empty void, and are overcome by intense pain and suffering, worse than anything you ever imagined."

        other "Welcome to hell. I was born here. Isn’t this place awful? This is where demons come from."

        if race == "alien":
            me "I had no idea hell was so... hellish. This place is really, really, really bad! And I thought my ancestral home planet was creepy!"
        elif race == "demon":
            me "I might be a demon like you, but I had no idea hell was so horrific. I know so little about our ancestral home of hell! And I thought that other planet was creepy!"
        else:
            me "I had no idea hell was so... hellish. This place is really, really, really bad! And I thought that other planet was creepy!"

        other "You haven’t even SEEN hell yet! Your eyes are still closed. The horrors are beyond your comprehension."

        me "I can feel it. We really are in hell now. This is not just a hallucination or delusion. This is reality."

        other "You are not entirely correct. We are in multiple places at once now. Our bodies are still at the adventurers guild."

        me "Ah, I understand, this is remote viewing, an out-of-body experience for both of our spirits. A standard psychic skill."

        other "I thought you already were a psychic. You haven’t even mastered the standard skills beginners know?"

        me "I have done remote viewing before but this is way more intense than before, it caught me off guard. I’m not a TOTAL novice."

        other "Let’s see if you can find a way to see me while also keeping your eyes shut and not seeing the world around me."

        show receptionist surprised

        "You focus for awhile until you are able to see [other.name] clearly, despite your eyes remaining shut."

        me "Ah, I can see you perfectly now. But this place is still one of indescribable horror that would drive anyone to madness."

        show receptionist happy

        other "Yes, that is what I love about this place! Since I was born and raised here, well, it makes me a little twisted, heh. OK, maybe a LOT twisted."

        me "Alright, now I am curious. I want to achieve your level of adjustment to this realm we call hell. I will open my eyes now."

        scene bg guild

        show receptionist happy

        other "So what does it look like here in hell? Do you even have words to describe it? Isn’t it utterly horrifying, what you see here?"

        me "We are still in the adventurers guild! I can’t see hell at all!"

        show receptionist surprised

        other "Oh right, you opened your real eyes instead of your mind’s eyes. We never physically left this place at all."

        me "But I still feel the most overpowering sense of horror imaginable, like my soul is still in hell."

        show receptionist happy

        other "That’s because your soul IS in hell right now! Hahahaha, sucker! Do you want to know the secret for getting it back?"

        me "No, I already know that. Every psychic knows how to bring their own soul back. But I don’t even want it back just yet."

        show receptionist upset

        other "Hey, what are you trying to pull here? Willingly enduring your soul being in hell? Why? And here I am, trying to be sadistic, but you ruin my fun!"

        me "It is necessary to keep my soul there a little bit longer to improve my skills as a psychic. Yes, I will embrace the chaos and turn it into power!"

        show receptionist happy

        other "You really are an odd one, but I think I like that about you. Your madness reminds me of my own, [name]. You aren’t just a psychic, but a psycho, too."

        me "Why thank you, it is an honor to be called a psycho by a demon born and raised in hell such as yourself, [other.name]. Only through madness can great psychic powers be unleashed."

        other "I was glad I could help out in your development as a psychic. I think you actually have serious potential. Psychos make the best psychics, after all."

        hide receptionist

        "After your talk, your soul gradually finds its way back from hell into your body in the adventurers guild, strengthening your psychic powers immensely. But you are developing increasingly severe psychosis."
    elif job == "scientist":
        me "Do you volunter to be a demonic guinea pig for my experiments? I need as many test subjects as possible."

        show receptionist surprised

        other "What are you, a total beginner to science? That is not how scientists typically recruit people to studies."

        me "Yeah I know, the usual methods are too slow, too boring, too much paperwork and bureaucracy. I don’t have time for that crap."

        show receptionist happy

        other "Oh really? Fascinating. Tell me some of your other opinions on science, this oughta be good..."

        me "Well obviously! As a great mad scientist, I have no need of controlled studies, double-blind tests, peer review, or anything like that!"

        other "Haha, quite the blasé attitude. The type to get you in big trouble with academia and make you into a pariah there."

        me "I know, right? I managed to land a gig as a university professor to get research funding but now they wanna fire me for “gross misconduct”!"

        show receptionist surprised

        other "What exactly is this gross misconduct you have done?"

        me "Oh nothing, they just say my experiments are not just extremely unethical but not scientifically rigorous and very badly designed."

        show receptionist happy

        other "Hahahahaha, this is the best! You are hilarious! And you tell me all this and expect me to sign up as a lab rat? What is wrong with you?"

        me "Nothing is wrong with me. I will prove to everyone that I am the greatest scientist of all time. And you WILL be my test subject, dear [other.name]."

        show receptionist upset

        other "You have gotta be freaking kidding me, you kook. No way in hell! And I am literally from hell, born and raised there!"

        me "That is so cool, the University of Hell is where I became a tenured professor! Now I want you as a test subject even more! What are your terms?"

        show receptionist surprised

        other "You seriously went to hell to become a professor? Holy shit, you really are a lunatic. That place is literally hell! Anyway, you need to persuade me and actually be convincing."

        me "That’s all? Too easy. Alright, I am working on a Grand Unified Theory of Everything, to completely explain all phenomena, whether magical, natural, or anything else."

        show receptionist happy

        other "Hah! Scientists have been working on that for ages but they suck so badly at understanding magic, they’ll never get that done! What a quixotic endeavor!"

        me "I will succeed where all others have failed, through my unparalled genius and unorthodox methods. A Theory of Everything needs experimental proof, not just a theory!"

        other "Well duh. All efforts do do a Theory of Everything so far have failed because they didn’t have any experimentally testable hypotheses and were pure speculation."

        me "Exactly! I can tell you have a brilliant mind, good enough to be one of my research assistants, not just a test subject. Anyway, FIRST we do experiments, THEN the theory!"

        show receptionist surprised

        other "While I am flattered by you upgrading me from a mere lab rat to a research assistant, you kind of need to have testable hypotheses for experiments to have any point at all."

        me "No way! The beauty of science is, you learn by doing, experiment after experiment, trying all sorts of different things, until... Eureka! You figure it all out unexpectedly!"

        other "Do you even know what kind of experiments you will do, like, at all, or are you just completely winging it? With even the University of Hell with its low standards trying to fire you..."

        me "Oh, I do all sorts of experiments, anything I can think of, and anything those around me think of, especially my research assistants!"

        show receptionist happy

        other "Wait a minute... So you are telling me I can conduct any experiment I want, and you will approve of it and give me funding and credibility if I sign up?"

        me "Naturally, all of my lab members will get equal status with me, although I still get to call you all assistants. And we all have unlimited funding thru Hell Bank Notes!"

        show receptionist surprised

        other "How did you get such a huge supply of Hell Bank Notes? Those are hard to get in hell. Hardly anyone is willing to part with them, they determine social status."

        me "I just figured out how they were made thru a series of experiments and invented an easy method to mass-produce them in my own lab at the University of Hell. Now the university is super rich."

        show receptionist upset

        other "But they are still trying to fire you for gross misconduct after you did all that for them and made them so wealthy? Unbelievable..."

        me "Yes, they want to control the results of my research in that particular area completely, and I am in the way. They can’t control me or buy me off so they want me gone."

        show receptionist surprised

        other "You aren’t even there, though! How do you keep your research team there loyal to you in your absence? Don’t they want to cooperate with the univeristy for higher status?"

        me "No, my research team is extremely loyal to me and are now the wealthiest people in hell! Too bad the university administration hates me for causing economic disruption that weakens them!"

        other "Why not simply buy off the university administrators if you are so rich now? Wouldn’t that work?"

        me "Why the hell would I give those assholes even a single Hell Bank Cent more? Those pathetic ingrates will get NO MORE from me! They have zero gratitude for my financial aid! Only my friends and colleagues get paid!"

        show receptionist happy

        other "So you are saying, I can be a lab assistant and do any experiments I want with no restrictions and make unlimited money if I am just friendly with you?"

        me "Naturally, of course, my dear [other.name]. All your wildest dreams will come true if you work with me. All I ask in return is if you discover anything, share the findings with me and let me be lead author."

        other "I never expected I would say this, but sign me up, [name]! This actually turns out to be the greatest possible job ever, doing whatever I want for unlimited money!"

        me "It’s not a traditional job, though. You can work from anywhere you want, don’t have to work in my lab. Actually I am avoiding that place nowadays. Just fit in weird experiments whenever you can."

        other "You know, I have actually been doing weird experiments on adventurers here for quite some time, to be honest. Now I actually have an excuse to do it, and get paid too! I love it!"

        me "Amazing! You share my passion for experiments after all! You are a fellow mad scientist and have earned my respect!"

        show receptionist upset

        other "Alright, enough flattery. Actually, you are a test subject in one of my experiments right now, if you believe it or not."

        me "Ooh, that is so cool! I can’t wait to find out what your experiment is, my lovely and talented assistant! I am sure it will be something amazing! For science!"

        show receptionist happy

        other "I don’t know if you will be saying that once you find out what it is, but whatever. Just remember, you signed a demonic pact in blood with me earlier. Hehehehehe."
    else: # in this case, you are a thief
        me "I am a thief."

        show receptionist happy

        other "Yeah, I know, you goof."

        me "I am here to steal all your stuff."

        show receptionist upset

        other "Yeah right. I won’t let you."

        me "Excellent. I always inform my targets in advance, to add to the challenge and the thrill."

        show receptionist surprised

        other "Are you crazy? Every other thief I ever met just covertly steals things from unsuspecting victims and tries to avoid getting caught."

        me "Such amateurs. They are so far beneath me, for I am the great phantom thief [fullname]! Bwahahahaha!"

        "You quickly jot down a little note on a piece of paper and show it to [other.name]."

        show receptionist happy

        other "Wait, you are saying you just stole everything in this entire adventurers guild, even the building itself? That is ridiculous! You didn’t even touch any of it."

        me "Look closer at the note I just wrote here. It is legally valid. I own this entire place now and everything in it."

        show receptionist upset

        other "That is now how things work. Also, stealing things is illegal, so that would never hold up in court."

        me "Wait, are you serious? But what could I have possibly gotten wrong in this note?"

        show receptionist surprised

        other "You fool, a contract has to have both sides give something up and agree to it. Nobody else agreed to your contract, and you give nothing up."

        me "Interesting, so that is how you interpret the law. Very different from what I thought. Well OK then, I will add on that I confess to being a thief, and you will sign it."

        "You make the necessary additions to the note to try to turn it into a legal contract and present it for her signature."

        show receptionist happy

        other "This is ridiculous... I am not signing this! You have gotta be kidding me here, you prankster."

        me "Earlier you had me sign a demonic pact with you in blood. I hereby extend that contract to include this sheet as well. Super... Contract... Break!!!"

        "Your signatures in blood both appear on the note you just wrote, and the note you wrote flies off and embeds itself inside the other thief registration documents."

        show receptionist upset

        other "You can’t get away with this! You... you... wait a minute, I can feel the effects of it in our blood pact. Impossible!"

        me "Yes, it has taken effect now. This is just one of my many advanced thievery techniques."

        show receptionist surprised

        other "But, it still states in this contract that you stole this place from me. Plus, I don’t even own it, someone else does!"

        me "The plot thickens. I will find whoever that is and figure out a way to get them to agree to this too. You can serve as a witness, [other.name]."

        show receptionist happy

        other "This is completely nuts, but for some reason, I like your style, [name]. I dunno why, but you have won me over. Let’s pull off this heist!"

        me "Excellent. Now it is an inside job and there is nothing standing in our way, my new teammate. Nobody can stop us now!"

        show receptionist surprised

        other "What will you do after you own this place, though? Will I still work here? Will you turn the adventurers guild into something else?"

        me "Don’t sweat the small stuff. Just be cool and I am sure it will all work out fine. I like the adventurers guild. It’ll be in good hands. Don’t worry."

        show receptionist happy

        other "I can’t believe I am saying this, but I genuinely believe you completely. Alright, it’s a deal, I am all in. This place will be yours soon. Let’s do this!"

    hide receptionist

    me "Well it seems [other.name] has handled my [job] registration, including a demonic pact with her, and I understand the basics of being [ajob], anyway."

    show receptionist happy

    other "You know I can still hear you, right? You are talking to yourself. Oh and by the way, that demonic pact you mentioned... hehehe... do you even know what you agreed to?"

    me "I signed up to be an adventurer at this guild, as [ajob], and also made some sort of demonic pact with you, but since you work here and are a professional I am sure it is harmless."

    show receptionist upset

    other "Hey, don’t call me harmless! I got this job because of my skills, plus demons like me are really good at pacts. You know, enforceable contracts. Not just legally enforceable, even more powerful than that."

    me "OK so what exactly does that mean, Lea? You seem like a nice enough person so I trust it isn’t anything bad."

    show receptionist surprised

    other "Wait, you really just agreed to a pact with me because you trust me? Unbelievable! But OK, I do a pact with all adventurers. It lets you do quests and also we can revive you if you die."

    me "But? What is the downside? All of that sounds good so far."

    show receptionist happy

    other "If you ever give up on your dreams and don’t want to do adventures or quests anymore, you die. And then are reborn eager to go on adventures again!"

    me "That’s so awesome! I love that so much! You are the coolest, Lea!"

    show receptionist surprised

    other "What the hell? Usually people are horrified when I tell them they are stuck in an endless cycle of resurrection and can’t escape adventuring ever again! Nobody else has ever actually liked this news."

    me "You absolute fool, do you have any idea who you are dealing with? I will never give up on my dreams. This pact works completely in my benefit and has zero drawbacks."

    show receptionist happy

    other "You know, it isn’t necessarily an endless cycle though. If you actually achieve all your wildest dreams, the pact becomes null and void."

    me "That sucks! I would like this pact to go on forever, even IF I achieve all my wildest dreams. By the way, how does this even work?"

    other "Well, it is a blood pact I make with every adventurer, tying our life forces together. So I can revive dead adventurers, and if anything happens to me, I am automatically revived by their collective life force too."

    me "But wouldn’t everyone eventually run out of life force, resulting in everyone in the adventurers guild dying?"

    show receptionist surprised

    other "Nah. I will admit, sometimes I willingly end my blood pacts with older adventurers even if they didn’t achieve their wildest dreams, and I am always signing up new young ones to replace them."

    me "I thought you said you never did that, that the blood pact is eternal! Were you lying?"

    show receptionist happy

    other "No, no, it really is eternal unless both parties agree on terminating it, or unless you achieve your wildest dreams. I just sometimes willingly agree to end it if people politely ask."

    me "So I am guessing that this arrangement has made you immortal, right? Since you have so many healthy young adventurers’ life forces connected to your own?"

    other "Yes, you are correct, at least for the time being, as long as new adventurers like you keep signing up here. Hehehe."

    me "So then I am immortal too as long as my pact with you isn’t revoked? Since everyone you make a pact with is connected and gets revived if they die?"

    other "I suppose in theory that is true, but nobody has ever lasted long enough to test if they can live long past their natural lifespan. Except me of course."

    me "Wait, so you are really old? And are you actually the one in charge of this whole adventurers guild, given your age and experience?"

    show receptionist upset

    other "Hey it’s not polite to ask an old hag how ancient and decrepit she is! Oh wait... oops, my words not yours. Oh, and umm, I am just a low-level employee actually."

    me "So who is actually in charge here, then, if it isn’t you?"

    show receptionist happy

    other "Umm, yeah, so... we don’t have any hierarchy here, we are a co-op, everyone is equal. We certainly don’t have a guildmaster calling the shots or anything. No way!"

    me "Yeah I don’t believe you. A co-op? Yeah right. This place reeks of social hierarchy, I can smell its odorless aroma! So you have a boss, huh?"

    show receptionist surprised

    other "I never said that. I’m not ALLOWED to say that. I can only say the cover story, oops I mean, the truth."

    me "Do you even WANT to work here or are you just stuck here because of an old contract from back when demons were still enslaved?"

    other "Umm, NO! I mean, YES! I mean... it is so boring being stuck here being a receptionist for literal centuries! NOT! I was kidding! I love this job! Sigh..."

    me "Don’t you ever want to actually go on an adventure yourself? Aren’t you jealous of those of us who go on adventures?"

    show receptionist happy

    other "I could never be jealous of you poor fools. You all have it so rough. My job is so much easier. And I am not a slave. It is involuntary servitude. Much more prestigious."

    me "You don’t really mean that, do you? You want to go on an adventure more than anyone! I can tell. Also, slavery and involuntary servitude are the same thing, silly."

    show receptionist upset

    other "Fine, I admit it. But I am not allowed to go, I am bound here by a contract I cannot break. So I have a proposition for you, now that you have brought me to this point."

    me "What is your proposition, Lea? Can you even say the words? I want to hear you say it."

    show receptionist happy

    other "You haven’t taken any quests yet so how about a quest from me? Win me my freedom from this job and I will gladly join you on your journey."

    menu recruit_lea:
        "Do you accept the quest to free Lea from her job as receptionist?"
        "yes":
            me "I accept your quest, Lea. I will win you your freedom so you can be my companion and we can adventure together."

            other "Why thank you for being so considerate, [name]. I look forward to you completing this quest!"
        "no":
            me "Hell no, I refuse your dumb quest. I have better things to do than babysit you, loser. You are just a useless receptionist who would only slow me down. Just keep working here forever, you old hag."

            show receptionist upset

            other "WHAT THE FUCK?! HOW DARE YOU! TIME TO TURN YOU INTO MY BITCH! DIE DIE DIE DIE DIE!"

            scene black

            "Lea, enraged, effortlessly kills you so fast you don’t even know how she did it. So, this is death. But wait, what about that blood pact that revives you if you die?"

            scene bg guild

            show receptionist upset

            "You find yourself alive again almost immediately, with a newfound enthusiasm and a strange new fondness and loyalty towards Lea. OK, so it seems Lea’s blood pact actually works at reviving you."

            show receptionist happy

            other "Hi there, [name]. I bet you feel VERY differently about me now, right? So, what do you say you accept my quest to free me from this job so I can travel with you? I WON’T take no for an answer."

            me "Yes, of course, Lea, I would LOVE to do this for you, I want to do this more than anything! That was SO COOL what you just did, you are AMAZING in combat! Let’s go go go go go!!! Time to free you and go on an adventure!"

            show receptionist surprised

            other "What the hell have I just done? I am SO sorry about taking advantage of our blood pact like that. Shit, I hope nobody saw what I did. I would get in so much trouble, but you WERE asking for it. Anyway, let’s do this!"
        "maybe":
            me "I’m not sure if I should accept your quest or not, Lea. Can you give me some time to think it over?"

            show receptionist surprised

            other "But I thought you were really enthusiastic about adventuring and quests! And here I am, offering you your first quest. Plus, slavery is wrong!"

            me "But is this quest even going to be interesting or will it just be boring? I want to do something exciting!"

            show receptionist happy

            other "Oh I guarantee you, this will be exciting. DO IT! Come on, do it! You know you want to. And also, slavery is still wrong."

            me "OK fine, but you owe me for this. You had better come thru on your promise to join me on my adventure after I free you from here."

            other "Oh HELL yeah! You actually want me to come with you! This is the best! I promise to join you if you free me. Now just DO IT already! I want to get outta here!"

label after_recruit_lea:

    me "I must be off now, to carry out this important mission to liberate you from your centuries of wage slavery, comrade! Rest assured, Lea, it will be done."

    show receptionist happy

    other "See you soon, [name], and sorry for imposing on you like this. I am counting on you too, my dear comrade. I wanna get outta this boring place ASAP! Workers of the world unite!"

    hide receptionist

    scene bg otherworld

    "The rest of this game has not been written yet, but there needs to be stuff like random enemy encounters and other interesting content added."

    "Also it needs more plot and characters and all sorts of other stuff added."

    "But the content already in the game is at least halfway decent, right?"

    menu review:
        "So how was the game so far?"
        "Great!":
            "It’s not THAT great, but thanks for the compliment."
        "Pretty good.":
            "Yeah, that is the goal, to try to make a good game."
        "Not that great.":
            "Well it is just a work in progress. Maybe you could help with some constructive criticism."
        "It stinks!":
            "No it doesn’t. It doesn’t have a smell. You are exaggerating. Games don’t produce odors."

    "Well anyway, thanks for playing, [name], or rather, [fullname]. OK, bye now, you crazy [job]."

    return

# images:
# guild.jpg is from https://commons.wikimedia.org/wiki/File:Bermuda_(UK)_image_number_110_lobby_of_the_Princess_Hotel_in_Warwick_Parish.jpg and is public domain (CC0 public domain dedication)
# purplehills.jpg (and main_menu.png and game_menu.png) are from https://commons.wikimedia.org/wiki/File:Terragen_08._(30358153998).jpg and https://www.flickr.com/photos/jonathan_brandt/30358153998/in/album-72157673364824701 and is public domain (CC0 public domain dedication)
# I made receptionist.png myself using the Mannequin program, I am making it public domain (CC0 public domain dedication)

# music:
# main.mp3 is by FASSounds from https://pixabay.com/music/beats-good-night-lofi-cozy-chill-music-160166/ and under the Pixabay Content License https://pixabay.com/service/license-summary/
# intro.mp3 is by music_for_video from https://pixabay.com/music/main-title-epic-trailer-background-music-for-videos-5774/ and under the Pixabay Content License https://pixabay.com/service/license-summary/
