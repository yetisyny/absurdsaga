[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# Absurd Saga

Absurd Saga is an experimental absurdist RPG developed by [Rich McGrew](https://github.com/yetisyny) and the rest of [the Absurd Saga DevTeam](https://github.com/absurdsaga), with a simple, intuitive user interface aimed at accessibility and ease of use for all types of players.

This game project aims to eliminate as many obstacles as possible to having fun, and be widely available for free on as many platforms as possible for everyone. Annoyances being avoided include microtransactions, ads, requiring a constant Internet connection, being pay to win, needing to create an account and password, being a buggy mess that crashes, excessive grinding, inventory management, timed events, a confusingly complicated user interface, and parts of the game where you get stuck and need a walkthrough.

It is a free and open-source cross-platform game, based on the excellent [Ren'Py game engine](https://www.renpy.org/) (whose GitHub page is [here](https://github.com/renpy/renpy)). Contributions, improvements, translations, and ports to other platforms are all very welcome on this Absurd Saga GitHub page, although it is a bit premature for some of those given the incomplete status of the game.

Code and text are under the [MIT License](https://github.com/absurdsaga/absurdsaga/tree/main?tab=License-1-ov-file), and images and music are under other free licenses (more details to be announced later once the game is more complete, as this could change over time depending on which images and music are added). Currently, all images are under the [CC0 public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/), and all music is under the [Pixabay Content License](https://pixabay.com/service/license-summary), but that could change at any time if other content under other licenses is added.

The game in its present very early pre-alpha state, is indeed a playable game that works and is interactive and has graphics and music, and has some attempts at humor that may or may not actually be funny. And it has some very basic character development and worldbuilding and storyline.

But it is currently FAR too short and incomplete to be putting out binary releases for people to directly install, or uploading into app stores, or anything like that. Most of the core game functionality is still missing, it is mostly just the charater creation and intro to an RPG but it doesn’t get to random encounters and it doesn’t have various stat, leveling, etc. systems implemented yet. It is meant, as the title suggests, to be an absurdist game and rather silly, a parody of more traditional RPGs. The game is written in English, and while the plan is to have translations into a wide variety of languages, currently there is only one translation, in German, which only really translates the basic user interface text and not the text in the game itself, so the game is still only really playable in English currently.

But the source code is all here, and anyone who wants to can install and play it by installing the latest version of Ren'Py, creating a new project called “Absurd Saga”, and then downloading all the files from this GitHub repository and putting them into the “game” directory of the Absurd Saga project. To download the code in its current state, I suggest going to the “Code” thingie near the upper right of this project page and choosing “Download ZIP”. Then you unzip that ZIP file into the game directory of a Ren'Py project, and then you can play the game from the Ren'Py launcher by clicking the “Launch Project” button.

It is highly recommended to use [Visual Studio Code](https://code.visualstudio.com/) for developing Ren'Py projects, currently, as that is the only Integrated Development Environment which has a Ren'Py plugin actively maintained by the official Ren'Py project, a plugin that the Ren'Py installer will install into Visual Studio Code if you already have it installed, and that is also available to download on the Ren'Py website. That is mostly just something you need to know if you are a developer, not if you just want to play the game. While Ren'Py is built on top of Python, Ren'Py is a different language from Python, so an editor using a Python extension (for the .py file extension) won’t work correctly on Ren'Py source code files (with the .rpy filee extension).

Porting the game Absurd Saga to other platforms and adding more translations ought to be pretty straightfoward in Ren'Py. It supports Windows, Mac, Linux, Android, iOS, HTML5 web apps, and even Google TV / Android TV and Apple TV, I think. And the Ren'Py Launcher has most of the tools people need for this. So, this choice of game engine ought to make it relatively easy to port this game to many platforms and translate it into other languages. While Ren'Py is mainly aimed at developing the visual novel genre of games, Absurd Saga, as an RPG, still has a visual novel-style interface, one that Ren'Py is ideal for, because it already comes with this interface built in as the default. And adding RPG functionality is not that difficult, given the ability to add inline Python code. And if you consider that it is a free and open source game engine that has been around for many years with an active community that is also regularly updated, Ren'Py looks like the perfect choice for a game like Absurd Saga to be based upon.

I encourage you to experiment with the Absurd Saga project in Ren'Py and give feedback on it, and new contributors to this project are welcome to join. Especially artists and translators, who will become more important later on as the game’s code and script get more complete but more art assets are needed and there is much more text to translate into other languages. Although in the case of translators, it would probably be best to hold off on doing most of the work until after the game is, at least, very near to completion, if not entirely complete, because the text in the game is being changed all the time currently. There is not much need for musicians, because there is such a wonderful wide array of royalty-free music available online. Unless of course, you are extremely talented at composing game music like legendary game music composer Nobuo Uematsu, in which case, your contributions would be greatly appreciated. As far as art / images / graphics, though, we could definitely use some artists for drawing the character sprites and screen backgrounds and possibly a cooler-looking GUI. But as this is a free and open source project, it is an all-volunteer operation, meaning unpaid. Still, a good place to showcase your talent and creativity. Especially if this game actually turns out to be a good game that, at least, achieves some niche level of popularity.

Also, as another part of the development process, feedback from players is greatly appreciated, about things you like or dislike in the game, because one goal is to make the game as fun as possible. And it ought to have a lot of replay value and not just be something you play and beat once and then consider done and never play again. This project aims to be the type of game that players come back to again and again and genuinely enjoy playing. With most commercial games, the number of players peaks soon after the game is launched but then gradually diminishes. But with games that have the right type of gameplay and communities, the number of players gradually increases over time, and even if it eventually hits a peak and then decreases, it still retains a relative level of popularity and people who have played it before go back to revisit it and play it again because they still enjoy it. And people might make mods or forks of the game or other games inspired by it, and in some cases, a game even inspires a new subgenre of games that are similar to it.

The most ambitious goal of Absurd Saga is to be that type of game, the one that will attract a dedicated community, lead to it being continually developed for years, have it serve as an inspiration for other games, and have the community enjoy making mods and forks of the game along with still enjoying the original base game, too. And for that to happen to such an extent that commercial game developers are inspired by it too, and that they note that the highly permissive MIT License allows them to copy things they like from this game, and then they also put out games inspired by Absurd Saga. This is the exact reason why this game is not under a copyleft license like the GNU GPL, because this game project has the ambition to be a game that the commercial game industry is inspired by, leading to them increasing the quality of their games and reversing some of the unfortunate trends in recent years with commercial games getting worse in a variety of different ways.

Ultimately the purpose of this project is to change the trajectory of the entire gaming industry in a more positive direction, against exploitative things that rip off players and make games less fun (e.g. pay to win gacha games full of microtransactions where you need a constant Internet connection), and moving games back in a more fun direction where game developers do the best to give players what they want without arbitrary annoyances (e.g. games you can play anytime, anywhere, including offline, as much or as little as you want, without anything getting in the way of you having fun). As well as to raise the profile of the wonderful Ren'Py game engine and the entire visual novel / VN genre, and help Ren'Py and visual novels gain in popularity by introducing more players to this style of video game interface in a compelling way. You can find a large database of amazing visual novel games at [vndb.org](https://vndb.org/). However, to be clear, this game Absurd Saga is not technically a visual novel, but an RPG (role-playing game), much more interactive than a visual novel (VN). It just has a lot of similarities to actual visual novels, and is sort of a hybrid between an RPG and a true visual novel. This hybrid RPG/VN game genre already exists, in fact most gacha MMORPGs nowadays have VN elements to them, but Absurd Saga aims to make a better version of this hybrid RPG/VN genre more popular, without any of that gacha/microtransaction garbage ruining things and actively making the games less fun while ripping off players.
