class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.path2 = ""

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
        self.get_path();
	
		
    def get_path(self):
		s = ""
		for path in self.paths.keys():
			s = s + "    " + path
		self.path2 = s
		
		
central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew.  You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an 
escape pod.

You're running down the central corridor to the Weapons Armory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate filled body.  He's blocking the door to the
Armory and about to pull a weapon to blast you.
""")


laser_weapon_armory = Room("Laser Weapon Armory",
"""
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
The Gothon stops, tries not to laugh, then busts out laughing and can't move.
While he's laughing you run up and shoot him square in the head
putting him down, then jump through the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan the room
for more Gothons that might be hiding.  It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the
neutron bomb in its container.  There's a keypad lock on the box
and you need the code to get the bomb out.  If you get the code
wrong 10 times then the lock closes forever and you can't
get the bomb.  The code is 3 digits.
""")


the_bridge = Room("The Bridge",
"""
The container clicks open and the seal breaks, letting gas out.
You grab the neutron bomb and run as fast as you can to the
bridge where you must place it in the right spot.

You burst onto the Bridge with the netron destruct bomb
under your arm and surprise 5 Gothons who are trying to
take control of the ship.  Each of them has an even uglier
clown costume than the last.  They haven't pulled their
weapons out yet, as they see the active bomb under your
arm and don't want to set it off.
""")


escape_pod = Room("Escape Pod",
"""
You point your blaster at the bomb under your arm
and the Gothons put their hands up and start to sweat.
You inch backward to the door, open it, and then carefully
place the bomb on the floor, pointing your blaster at it.
You then jump back through the door, punch the close button
and blast the lock so the Gothons can't get out.
Now that the bomb is placed you run to the escape pod to
get off this tin can.

You rush through the ship desperately trying to make it to
the escape pod before the whole ship explodes.  It seems like
hardly any Gothons are on the ship, so your run is clear of
interference.  You get to the chamber with the escape pods, and
now need to pick one to take.  Some of them could be damaged
but you don't have time to look.  There's 5 pods, which one
do you take?
""")

the_end_winner = Room("The End", 
"""
You jump into pod 2 and hit the eject button.
The pod easily slides out into space heading to
the planet below.  As it flies to the planet, you look
back and see your ship implode then explode like a
bright star, taking out the Gothon ship at the same
time.  You won!
"""
)

the_end_loser = Room("The End",
"""
You jump into a random pod and hit the eject button.
The pod escapes out into the void of space, then
implodes as the hull ruptures, crushing your body
into jam jelly.
"""
)

escape_pod.add_paths({
    '1': the_end_loser,
    '2': the_end_winner,
    '3': the_end_loser,
    '4': the_end_loser,
    '5': the_end_loser
})

generic_death = Room("death", "You died.")

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '132': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot': generic_death,
    'dodge': generic_death,
    'tell a joke': laser_weapon_armory
})

START = central_corridor



the_entrance = Room("Entrance of the Maze",
"""
You are Theseus, the son of King Aegeus, and you have 
been sent on a mission to kill the minotaur, a son of 
King Minos who lives in a maze. If you succeed, glory 
will befall upon you. If you fail, you will become 
another tribute to the hungry minotaur who has eaten 
thousands of befallen heroes in the past. You 
approach the entrance of the maze along with the King 
Minos and Princess Ariadne. They give you a map, and 
they offer you a ball of thread to keep track of your 
way through the maze. Will you take the thread?
"""
)

the_beam = Room("To Beam or Not to Beam",
"""
Now you are a little bit in the maze, but you can 
still see the entrance and the light of day behind 
you. You see multiple passages in front of you. In 
front of these passages, there is a huge beam that 
doesn’t look very sturdy. Before you proceed further, 
what do you decide to do with the beam in front of you? 
"""
)

the_fight = Room("The Setup",
"""
You are now in the maze. You go further and further 
inside and soon you are enveloped in complete darkness. 
You feel your way along the walls and around the twists 
and turns of the labyrinth. Somewhere deep inside, the 
bull was stamping and snorting, impatient to meet its 
latest sacrifice. At last, deep within, you could hear 
that the Minotaur is close by. You find a passageway 
that leads to a dead end, but discover a sudden turning 
just before the end. You have seen this passage on the 
map and realize it was just the place you are looking 
for. How do you decide to approach the Minotaur in the 
corridor?
"""
)

entrance_death = Room("Oh no! You have failed.", 
"""
You have failed to properly use the thread that 
would have allowed you to keep track of your way 
through the maze and come back safely whether 
you succeed or fail. You entered the maze and 
became enveloped in darkness. You end up wandering 
the maze forever, either dying from thirst and 
hunger or getting eaten by the minotaur.
"""
)

fight_death = Room("Oh no! You died.",
"""
Heading straight for the minotaur was not a good idea. 
You underestimated his strength and his agility. He 
quickly lifts you up and stuffs you in his mouth as a 
tasty treat. You now suffer the same fate as all the 
others who have gone into the maze. You are dead.
"""
)

fight_win = Room("You win! You have become the new glorious hero of Crete!", 
"""
You hide yourself around this final twist and call out 
to the Minotaur. It hears you and comes charging down 
the passage, but it could not slow down before the 
turning and charged straight into the wall. While it 
is still stunned from the impact you thrust your spear 
into the beast’s neck and kill it, though it does not 
give up its life before letting out a terrible bellow.

You now use your thread to go back to the entrance. 
King Minos, your father, and Princess are in shock 
that you made it out alive. The princess admires you 
greatly and falls in love with you. You propose to her 
and she agrees. You two live happily ever after.
"""
)

the_entrance.add_paths({
    'take it': the_beam,
    "don't take it": entrance_death
})

the_beam.add_paths({
    'tie the thread to the beam': the_fight,
    'ignore and proceed with caution': entrance_death
})

the_fight.add_paths({
    'rush towards him': fight_death,
    'slowly approach the minotaur': fight_death,
    'hide yourself around the twist and call out to him': fight_win
})

START2 = entrance_start
