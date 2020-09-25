label onto_school_day_1:

    scene road_to_school_day

    "As I walked out, I couldn't help but feel bad about the way I acted towards her.
    She must be going through as hard a time as I am."

    "She tried putting on a brave face for my sake, but I know just seeing me
    reminds her of it all."

    "But seeing her face brings back memories that are hard for me to remember.
    I know I should let go of the past, but it's still so fresh in my mind."

    "*BAAAAM!!!!!!*"

    scene bg white_transition

    "Everything goes white as I'm suddenly confronted with a bike colliding with me."

    scene bg collision

    "My vision begins to return as I find myself on the ground, in massive
    amounts of pain throughout my body."

    "In front of me is a totaled motor bike and off to the side, the perpatrator.
    A red headed, red eyed girl who is currently in shock over the state of the
    motorbike."

    menu:

        "Watch where you are going! What the fuck!?":
             $ rio_route -= 1
             jump what_the_fuck

        "Are you okay?":
             $ rio_route += 1
             jump are_you_okay

        "Get up and go.":
            jump leave

    label what_the_fuck:
        "Anger begins to boil over and seep out of me."

        mc "What the fuck are you doing?! Watch where you are going!"

        scene bg collision_tear

        "The girl looks startled by my outburst. She suddenly starts tearing
        up."

        scene bg collision_cry

        rio "WAHHHHHHHHH!"

        "She bursts out into tears. This girl is seriously annoying. Whatever, she's
        not my problem."

        style multiple3_say_window:
            xsize 640
            background "gui/halftextbox.png"

        style block1_multiple3_say_window:
            xalign 0.0

        style block2_multiple3_say_window:
            xalign 1.0

        style multiple3_namebox:
            xpos 70

        style multiple3_say_dialogue:
            xpos 90

        style block3_multiple3_say_window:
            background "gui/toptextbox.png"
            xalign 0.0
            yalign 0.0

        style block3_multiple3_say_dialogue:
            xpos 300
            xsize 640

        style block3_multiple3_namebox:
            xpos 280

        "Female Student 1" "\"What's happening over there?\"" (multiple=3)
        "Male Student 1" "\"I don't know, maybe we should check it out.\"" (multiple=3)
        "Female Student 2" "\"Wow, that looks like a serious mess.\"" (multiple=3)

        "A couple of other people are gathering around the scene happening
        before them. I really need to get going."

        jump end_choice_1

    label are_you_okay:
        mc "Ouch...."

        "My body is filled with pain everywhere, but I realize the girl in question
        is probably not doing too hot either."

        mc "Hey.... are you okay? Sorry, I wasn't paying attention to where I was
        going."

        "She looks up, finally noticing that you are also on the ground next to her.
        She seems to finally realize what happened. She lowers her head to the ground."

        scene bg collision_apology

        rio "I'm so sorry! I didn't see you at all!"

        mc "It's okay, I didn't see you either, it was most definitely my fault,
        but more importantly, are you okay?"

        jump end_choice_1

    label leave:
        "In the hurry I was, I sort my things together and move my way to school, not entirely sure waht transpired."

        jump end_choice_1

    label end_choice_1:
        "I get up, dust myself off and head on toward the school."
