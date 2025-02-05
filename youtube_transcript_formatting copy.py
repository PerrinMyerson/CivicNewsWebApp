import re

# Function to remove timestamps and print sentences one by one
def convert_transcript(transcript):
    # Remove timestamps using regex
    cleaned_transcript = re.sub(r"\d+:\d+", "", transcript).strip()
    cleaned_transcript = re.sub(r":\d+", "", cleaned_transcript).strip()
    # Replace multiple spaces and newlines with a single space
    cleaned_text = re.sub(r'\s+', ' ', cleaned_transcript)
    
    # Split cleaned text into chunks of 100 words
    words = cleaned_text.split()
    for i in range(0, len(words), 150):
        chunk = ' '.join(words[i:i + 150])
        print(chunk)
        print("\n")  # Add a newline for readability

text  = """""
3:09
24th 2024 board business meeting at Memphis Shelby County Schools Miss Clark
3:17
please call the RO commissioner mckisic here
3:23
commissioner Garcia here commissioner Porter here
3:28
commissioner Murphy here commissioner love here commissioner mckenny present
3:37
commissioner OT here commissioner Williams pres Vice chair Coleman here
3:44
you have nine present we do have a quorum thank
3:53
you will you please stand for the Pledge of Allegiance and posting of colors tonight's posting of
4:00
colors is presented by Kirby High
4:22
School the United States of America to the Republic for which it stand na
4:37
please remain standing for a moment of
4:43
silence thank you you may be seated
5:06
the the question is now on the approval of the agenda are there any amendments
5:11
superintendent fagin Madame chair we would like to remove item 12.1 for further legal
5:19
review board
5:25
members commissioner McKenna thank you
5:30
yes I'd like to um pull the ad hoc
5:37
committee and I'd like to pull that noting for my fellow board members that
5:42
I asking for that to go to committee once we do our um annual board
5:49
committees
6:10
okay all right and I'd also like to add um the
6:16
policy Board General Counsel
6:23
policy okay Board District General Council it's not numbered at this point but the title of it is board District
6:30
general
6:35
counsel it will come under policy's first reading there being no further
6:41
amendments to the agenda is there a motion for the approval of the agenda of agenda I'm
6:49
sorry motion by commissioner love second by commissioner McKenna roll call vote
7:02
commissioner mckisic I commissioner Garcia I commissioner Porter I
7:08
commissioner Murphy I commissioner love I commissioner
7:14
mcken I'm sorry yes commissioner OT hi
7:20
commissioner Williams Vice chair ceman I you have nine in the affirmative thank you the
7:27
agenda is approved we are now on to public comment in
7:33
accordance with State Statute the board shall reserve a period for public
7:39
comments excuse me during business and special call meetings only those members
7:44
of the public who submit public comment cards to the board chairman prior to the
7:49
commencement of this meeting shall be permitted to address the board public comments shall be taken in the order in
7:56
which the public comment cards are received a signup sheet for public comment will be a will become available
8:03
30 minutes prior to each applicable meeting and will be closed at the start of the meeting this sign up is located
8:10
at the entryway table just past the security checkpoint speakers must State their
8:17
name organization he or she is representing if any and subject of their
8:23
comment before they are permitted to proceed speakers may offer objective comments about school operations and
8:30
programs that concern them speakers are asked to refrain from using name of
8:36
personnel or name of names of persons connected with the school system particularly when lodging a complaint
8:44
speakers will not be permitted to engage in Gossip make def flammatory comments
8:49
or use abusive or B vulgar language the chairman shall have the authority to
8:55
terminate the remarks of any individual who is D disruptive and does not
9:01
adhere to board rules Dr Schultz please announce the number of speakers and time allotted per
9:07
speaker there are five speakers this evening 3 minutes each your time is projected on the screen to your right
9:14
and directly behind the board when you hear a bail your time has
9:21
expired our speakers this evening are Dr Trenton Watson Jarvis cook Samantha hunt
9:30
Le marable and Marilyn
9:39
glass Dr Trent
10:03
mic again good evening my name is Dr Trenton Watson principal of Westwood High School 4480 Westmont Memphis
10:10
Tennessee 38109 uh I have been asked to come here this evening to speak
10:17
about how the district has supported me as a principal and I want to be specific
10:24
now I know Vice chair Coleman and I can't say name specifically but I'm not complaining so I I need to be able to
10:30
say a couple of names maybe two three four five um to talk about the support
10:37
uh I'll start with uh Dr Richmond uh who has long supported me uh as an educator
10:43
even before becoming a principal has always poured into me uh as an educator giving me tidbits of advice on how to
10:50
move knowing that one day I aspired to be a leader and then once becoming even before he got the position that he's in
10:57
now has supported me at West would and I'm very thankful uh for him uh to
11:03
Alicia ker who keeps her foot on my neck um about the things that we're doing in
11:08
the school she not only coaches and she doesn't look at challenges but she coaches and pinpoints opportunities for
11:15
growth uh in in our school and I'm very thankful to her and she's a constant uh
11:20
mentor and I'm very appreciative of her uh to everyone uh that has been involved
11:26
in the process at Westwood we're moving forward and we are growing specifically
11:32
in terms of our student population and the things that we're doing at Westwood uh brother Jenkins I'm thankful to him
11:39
for his presence at Westwood uh coming out to support us uh brother Langston
11:44
for asking me to be involved in the New Movement uh that's going on in the
11:50
district uh we spent an exuberant amount of time talking about the challenges instead of focusing on the opportunities
11:56
and we have to start focusing on the opportunities that we have in this District Dr fagins we are appreciative
12:03
of all of the things that are coming down the pike and and we're going to work through all of that so that we can
12:10
uh raise to the level of expectations that we all should have in terms of our children I promise you that if you just
12:17
keep watching there are some great things that's going to happen in 38109 especially at Westwood High School uh I
12:23
am pushing the agenda every day to make sure that we are A Cut Above All the
12:28
Rest uh I'm I'm looking for my Athletic Complex I know it's coming uh I'm gonna push until I get it uh we're going to do
12:36
those things because I promise you the alumni is behind all of this because they want to see uh Westwood uh be a
12:43
rising star once again in our district thank
12:57
you good evening to each and every one of you my name is Jarvis cook uh when I stood here on June 11th I
13:07
was an employee with the district serving as human resources employee Enterprise analyst I was here advocating
13:13
for my uh colleagues here at the central office just three days after my speech received media attention my team and I
13:19
were informed by an unqualified individual someone who should have never delivered such news that our team was
13:26
being eliminated the chief of human resources at that that time was not informed of this decision and our former
13:32
Total Rewards director also confirmed that he had no prior knowledge of this action as our team consistently
13:38
performed high level work for this District we were told that June 28 would be our last day in office however a
13:44
member of the superintendent staff which is present today indicated that we were to report back to work that Monday yet
13:51
that Friday evening all our access was abruptly revoked without any rationale for our termination we reached out to
13:58
the superintendent requesting a meeting to discuss our roles and uh request our
14:04
roles and contributions but these requests were unanswered only two board members responded to our emails on
14:11
August 19th we filed a formal complaint with the general council's office and here we are a month later we have yet to
14:17
receive any updates on the investigation this situation is highly unprofessional and shown a lack of integrity and we
14:25
deserve answers someone needs to explain to me why our jobs are listed in the
14:31
approved Budget on page 588 but we were still terminated also we apply for other
14:38
HR positions and school support positions just to remain employed with the district however no updates I was
14:45
good enough to hire last November but I'm not good enough to hire right now we assume that the positions which were
14:51
created and available to help impact the staff um but we have learned that staff
14:56
members who were not impacted were moved into the those positions they don't have the qualifications or the skill set we
15:04
uh was contacted August 14th after 700 p.m. to come in and interview the next
15:09
day uh for a position at 11:00 a.m. and no feedback whatsoever the job postings
15:14
have been put up and taken down at least four times all of this leads me to
15:20
believe that this is a result of retaliation and I am waiting to be proved wrong I urge each of you to not
15:28
play the game of politics and do the right thing because you are playing with
15:34
people lives we had people on our team that dedicated 20 plus years to this
15:40
District good talent that could still be here supporting and helping but you sent them home you sent them home we didn't
15:47
get a thank you for your service we didn't get an appreciation all we got was to be dismissed from this district
15:54
and it is embarrassing it is humiliating and it's not right and if anyone is okay
15:59
with this and feel that this is right God have mercy on your
16:18
soul all right well um good afternoon greetings to each and every one of you I
16:23
am Samantha hunt wait can
16:29
I am Samantha hunt and I came tonight just to um um acknowledge that a ratio
16:36
exists um between how teachers teach and how students learn and that is a
16:42
statistic that is seemingly ignored here in mempis in Shelby County fortunately I
16:48
am equipped with the latest um instructional strategies and as well as
16:55
scientific um scientific ific research that
17:03
informs instructional practices um and just shapes academics
17:09
overall recently the superintendent incentivized an incoming cohort and I
17:15
believe at the time the incentive was a monetary incentive about $5,000 when I signed on my incentive was a five-year
17:23
placement agreement well back in 2022 upon completing a nearly $30,000
17:28
teaching credential I was formerly inducted here um at the Board of Education as an MCA MCS teacher and I'm
17:36
stunned and embarrassed by this extended delay for a report date back to work I'm
17:44
part of the working class I am not stay-at-home and I can confidently speak
17:50
um not just as a University graduate of the University of Tennessee but on
17:55
behalf of as a stakeholder of the Tennessee Board of Regents um on behalf of the national
18:02
accreditation for University and standards and education practices everywhere not just the state of
18:08
Tennessee I can say that it's important that we um as graduating employees when
18:17
we're hired if you guys offer us offer us incentives we would like for you guys to follow through with those and it's
18:24
important for us to be where we should be um my star date is delayed but what
18:29
is rapid what continues to grow is email hacking in crime gender-based um
18:36
self-proclaimed dominance and intimidation and payroll schemes and scams and I just came to say that I
18:43
don't want to become a victim of that and um those are all things that are dangerous but we can't afford to ignore
18:49
them thank you
19:03
good afternoon good afternoon I am Marilyn glaz I am hold on Miss glad miss marble
19:11
goes before you hold up one before you hold on I'm sorry excuse me you fine I
19:18
thought I counted right that was okay um yes I'm Liz
19:26
marble president of United education Association uh 6263 pop Avenue Memphis
19:33
Tennessee 38119 the United Education Association has initiated the
19:38
collaborative conferencing process for educators the professional Educators collaborative conferencing act known as
19:46
Pekka is how local Boards of education and their professional employees are empowered by law to meet and
19:53
collaboratively discuss and agree to matters of salaries working conditions
19:58
benefits and other issues important to Educators and students the Pekka Law
20:03
requires us to obtain 15% of eligible employee signatures on a petition and
20:09
once we have obtained those we will submit the signatures to this board the peti this petition will request that a
20:16
vote be held for all eligible staff asking whether they want to have
20:21
collaborative conferencing UA is currently Gathering signatures and we
20:27
know that educators are excited to continue to collaborate with the district Memphis Shelby County Schools
20:34
works best when we all work together and Educators have a voice we look forward
20:39
to working with you to ensure a smooth Pekka process on another note we would like to
20:46
thank you the board our superintendent Dr Marie fagin School
20:52
Board uh staff Educators and all staff
20:57
support staff in schools we'd also like to thank community members but most importantly our students and parents for
21:05
assisting us with the very smooth smooth School opening for this 2425 school year
21:11
your tremendous service to our children our district and our communities is going to bring great results when we all
21:19
work together we truly believe as Educators our students win UEA the
21:25
United Education Association appreciates the Bold vision of the district to make
21:30
proactive steps to improve literacy decrease chronic treny and other
21:35
supports in schools were needed we are pleased with the early results and we
21:40
too look forward to that Day of Reckoning when the scores and the results come in and we hope to have a
21:47
huge celebration now we know that we've had a few bumps in the road recently but we
21:53
also appreciate the fact that we take ownership of those bumps and we seek ways to improve and be better and at the
22:00
end of the day all 111,000 children reached home safely and so did all of
22:07
our employees thank you for your tremendous work and for your heartfelt
22:12
work to the children of this
22:24
District once again thank you good afternoon and and thank you uh Dr pagin
22:30
and the entire staff uh for your support of our students and the teachers in
22:35
Shelby County Schools I am Memphis I am U Marilyn
22:41
glass and I am a 31st I am in my 31st year of teaching with Memphis Shelby
22:46
County Schools I did my student teaching here I'm sorry thank you okay there we go I am
22:53
Marilyn glass and I am in my 31st year of teaching at Memphis Chevy County Schools I did my student teaching in
23:00
this district and I've been with this District ever since I am a nationally board certified teacher and I tell you
23:06
I'm so excited about the teaching and learning that's going on in the schools this year to everything there's a season
23:13
and a time to every purpose under the heavens Ecclesiastes 3:1 I come to you
23:18
in this season at this time for the purpose to humbly ask for a rewarding
23:24
resolution to the teachers evaluation process and implore you to take action
23:31
with wisdom since the Inception of using the Tim rubric as the tool to evaluate
23:37
teaching and learning with Memphis sh Shelby County Schools teachers have thought that we were being evaluated
23:44
objectively and that as there are clear indicators stating the data that reflects what should be seen said and
23:51
heard to substantiate evaluation results policy 4046 provides guidelines for
23:58
evaluating teachers it states that the evaluation of teachers should reflect a
24:03
fair meaningful and accurate depiction of a teacher's development growth and
24:09
performance and it lets us know that results from a teacher's evaluation are
24:14
used to inform Personnel decisions including rewards and Leadership
24:19
opportunities it states that the evaluation should be conducted with Fidelity moreover there are Provisions
24:27
so that the Integrity of the evaluation results is not compromised and that
24:32
there are procedures to ensure that the evaluations are fundamentally Fair policy 4020 states that the
24:40
supervisors are responsible for adhering to the evaluation process using the Tim rubric and having
24:48
the strength of these policies seem to paint the picture of an objective and
24:54
fair process however this process is flawed
25:00
it is flawed because evaluators do not have to provide data nor evidence to
25:07
reflect What was seen said and heard during observation they can arbitrarily decide
25:13
what the evaluation results are and going to be regardless what happened during the observation I am here to ask
25:20
you to consider to reconsider the policy regarding teacher observations and make
25:26
it so that the words recommended but not required are no longer part of the
25:31
process teachers deserve to be evaluated to be um evaluated with evidence with
25:39
data and data should be required in that evaluation no administrator should have
25:44
the power or the ability to say to arbitrarily score a teacher they shall
25:50
have to provide evidence thank you and I hope this policy is addressed
26:00
thank you we are now on to special order of business the election of the Shelby
26:05
County Board of Education chair and vice chair for 2024 2025 Dr Schultz wearing
26:11
your hands well it's not too heavy a
26:17
load all right ladies and gentlemen of the board um our parliamentary authorities Roberts Rules of Order 12th
26:24
edition the procedure for election in that uh volume is actually comes out of
26:29
the 19th century and doesn't serve us particularly well however Roberts does allow you to choose a different method
26:35
and I'm going to suggest one to you and if there's no objection we will use that method it looks this will look a lot
26:40
more like what we're used to with elections nominations will be opened you
26:46
may nominate Yourself by the way absolutely that is your right um a rooll
26:52
call vote is required in our policies you may vote for one nominee
26:59
when When the Roll Call is called there are three things you can say first provide the name of the person you're
27:05
voting for second you may pass which says that you're not ready to vote yet please come back around and ask me again
27:13
you may vote present which means that you are not going to vote but you would like to be marked as present in the in
27:21
the minutes at the time the vote was taken uh it will take five votes to win
27:30
is there any objection to using this method everybody understand it roll call
27:36
when they come around to you just say a name or one of the other options we'll
27:41
see if we can get five votes somehow uh you may nominate yourself you
27:46
may also vote for yourself nothing wrong with that your vote is legitimate uh you may nominate as many
27:53
people as you like but only one at a time to give other people the ability to also nominate
27:59
that's it the floor is now open for nominations
28:08
commissioner love nominations for for chair chair I'm sorry for chair
28:14
commissioner love and then commissioner huy Garcia I'm going to nominate you Joyce
28:20
Heman thank you I had the same nomination thank you
28:26
I move to close nominations don't have to if nobody else has
28:32
nominations they Clos roll call vote roll call
28:41
vote commissioner mckisic Joyce D
28:47
Coleman commissioner Garcia Joyce Coleman commissioner Porter George
28:55
koven commissioner Murphy Joyce Coleman commissioner love Joyce Coleman
29:02
commissioner mckenny Joyce Coleman commissioner
29:08
OT Joyce Coleman commissioner Williams joce
29:15
Coleman Vice Coleman Joyce D
29:20
Coleman you have nine in the affirmative for commissioner Coleman congratulations
29:33
Joyce D Coman Shall Serve as the chair for the 2024 2025 school year thank you
29:40
all much congratulations it was
29:51
a now we're on to Vice chair commissioner
29:56
mik I'm I'm entering amember hu Garcia's name into a nomination for vice
30:03
chair commissioner Murphy I nominate Stephanie love for vice
30:13
chair no other nominations nominations are closed roll call V excuse me um is
30:20
it possible for us to hear from our nominees on why they want to
30:25
serve is that something that's permissible I know it's happened in the past but I don't know if that's there's
30:30
no rule against it okay we can do it all right both you
30:36
want
30:41
yes okay sure miss Garcia was nominated first so our parliamentarian say she go
30:47
first okay great well thank you for the nomination bber mckisic and I'm running
30:52
for vice chair of Memphis Shelby County School's colleagues because I'm ready to elevate my leadership ship just as we
30:59
had four recent additions to the board um throwing my hat in the ring is not
31:05
about my opponent it is believing that I am the Right leader in the right moment uh to move the district
31:11
forward my personal and professional experiences have brought me to this moment with a deep experience in
31:19
advocacy nonprofit and government I believe we're entering a time where we can go better faster
31:28
and use the data and listen to stories and I believe that I'm the right leader for
31:34
this I have a track record of clear
31:40
communication I am committed to using my
31:46
strengths to help us set ambitious and feasible goals for our
31:52
students and not in this role nor any role I've ever had
31:58
have I been successful alone and so I'm committed to building deep relationships
32:04
with each of you so we get the work done and we get our resources to our students
32:09
family staff who need it the most I am ready to serve and I ask you to deeply
32:16
consider a vote for me tonight thank
32:23
you I didn't prepare a speech
32:28
but I am a board member a parent and a community advocate my work speaks for
32:36
itself you may not always agree with me but I have the
32:42
district best in mind I have the teachers students best in mind I have
32:48
the students best in mind I com um am committed to this work
32:56
I show up every day ready to work
33:04
um you vote for who you want
33:11
to but like Amber said um I can't do this work
33:17
alone and it's going to take each of us to do the heavy listing along with the
33:25
superintendent and the board chair here thank
33:32
you roll call
33:38
vote commissioner mckisic board member
33:43
Garcia commissioner Garcia Amber Huck Garcia commissioner Porter a
33:53
pass commissioner Murphy Stephanie love
33:59
commissioner love Stephanie love commissioner mcken Stephanie
34:06
love commissioner OT Stephanie
34:11
love commissioner Williams
34:17
gcia Vice chair colan Stephanie
34:26
love Comm commissioner Porter Stephanie
34:33
love got six in affirmative for love and three for
34:41
Garcia sherff Coleman if I may uh in the spirit of unity and working together as
34:47
a board to um change my vote to miss Stephanie love thank you
34:59
we have seven in the affirmative for love and two for Garcia we're proud to
35:05
announce that Miss Stephanie love will serve as the vice chair for the 24 2024
35:11
2025 school year thank
35:16
you at this time I ask all my colleagues if we could take a group photo we just
35:22
come and take a picture and I'm also very hon that my
35:28
daughter left her job to come be with her mama on
35:34
today thank you myisha I love you
36:24
to
36:56
two few
37:26
more one two three
38:00
think
38:32
the question is now on the approval of the minutes for the following meetings approval of the minutes of the August 27
38:39
2024 business meeting approval of the minutes of the August 2024 work session
38:45
are there any corrections there being no Corrections do we have a motion to approve these
38:51
minutes and a second motion by commissioner love
38:58
second by commissioner McKenna roll call vote
39:09
please commissioner mckisic I commissioner Garcia I
39:16
commissioner Porter I commissioner Murphy I commissioner love hi commissioner
39:24
mcken I commissioner oang I commissioner Williams
39:32
I chair Coleman I you have nine in the
39:40
affirmative thank you the minutes are listed the minutes as listed are
39:47
approved superintendent recognition of Grants gifts and
39:53
donations we are now we are now on to committee reports at this time we have a special
40:00
presentation we would like to do from the
40:16
board hey
40:22
Amber hey Amber this is Michelle your seatmate on the day of is representing
40:28
District 1 I just want to wish you a very happy birthday I so enjoy our time
40:33
together and I know just how much fun you are when the cameras aren't rolling at Schoolboard meetings but I look
40:39
forward to continuing to serve with you on the Memphis Shelby County School Board happy birthday to you happy
40:46
birthday Amber happy birthday Amber wishing you many more years to come
40:53
happy birthday board M Garcia wishing you all the best your heart work and dedication is truly appreciated happy
41:03
birthday happy birthday Amber I hope you had a great day happy birthday Amber many more enjoy
41:11
serving with you on the on the board of education and do be well and this is the birthday song now I need
41:18
to know it when you sing it sing it when you know it this is
41:25
a birthday song wait keep this I got to tell this
41:33
is this is a birthday so it doesn't last that long happy birthday happy birthday
41:41
Amber I hope that your month has been just absolutely wonderful I wish you
41:48
many many more happy birthday
41:55
enjoy there you have special you are to this board and we wish you a happy
42:00
birthday very happy birthday thank you so much that was uh that was beautiful
42:07
and I I I really I honestly uh I think it's wonderful to see our personalities
42:13
come out a little bit here so um thank you for being good supports putting it together so I think I probably get to
42:19
contribute to some birthday videos now right this is a little tradition we're starting so thank you all thank you
42:26
Amber was the first we don't know what's going to be next I was in the doctor's office when I recorded that video from
42:33
here right I was done I was eating
42:39
um for the board board chairs report tonight I would just like to do a couple
42:44
of special recognitions and this is something that we're going to do every month for our district because we have
42:51
such greatness going on in our district and we want we're going to start spotlighting more of it and the first
42:58
one is District Two and Three they always going to work together
43:04
District Two and Three Craig M and Riley Egypt they played a game on Saturday the
43:10
21st the the Egypt the Ry Egypt Craigmont High School classic who
43:19
won Raleigh Egypt okay we're going to leave it alone congratulations to Riley
43:24
Egypt on the on their win and congratulations to craigm marching band
43:30
on winning the southern harage classic Battle of the band but the principal for
43:36
Riley Egypt is Dr Jamie green and the principal for craigm is Dr Derek King
43:43
and Devonte Kennedy is is the band director see it ain't by meos I get all
43:49
choked up he has grown this um this band from 60 members to over a hundred people
43:57
100 students we also would like to say the tsba fall district meeting was recently
44:05
held and they wanted to send a special thank you for Memphis because we hosted the the tsba fall uh district meeting
44:14
here District 8 White Station High School congratulations on their student
44:20
directed student Le run of Alice in Wonderland Alice in Wonderland Jr it was
44:26
a great job uh commissioner hu Garcia got a chance to go see it and she's been
44:32
smiling ever since talking about how wonderful it was and we just want to recognize and thank everyone for
44:40
participating academic perform performance committee meeting everything from the academic committee is on the
44:46
agenda tonight budget audit and finance committee
44:52
report all items are on the agenda tonight
44:57
Charter Schools committee report thank you chair Coleman um we actually had our
45:04
very first meeting today uh with the charter part partnership Council and it was a lot of just mostly you know meet
45:11
and greet and welcomes and laying out the template of how they're going to move forward and how they will come back and report back to the board so it's
45:17
going to be a monthlong process but um I will keep you posted thank you thank you
45:23
commun community outreach and engagement committee report rep no
45:28
report evaluation committee report we do have a meeting schedule for
45:34
this Thursday and this is not to evaluate our superintendent this meeting
45:40
this Thursday is to come up with the tools that we need in order to start the
45:45
evaluation process we have to have something done by October the end of
45:50
October so on this Thursday it would just be to discuss the tools that takes
45:56
to for the evaluation somebody got it misc confused saying we're evaluating our superintendent we will not
46:02
disrespect her by an evaluation without having the tools and everything in proper
46:10
place policy governance and legislation committee report um R Ria Stewart would
46:17
you come up and give the
46:25
update thank you than you do you want me to address the the
46:31
policy that was added to the agenda at this
46:38
point no no just give an update on the uh committee meeting okay so we had
46:47
um the are you referring to the meeting on
46:53
yesterday no the committee meeting which was held on September the
47:08
10th the the policy committee meeting that was held on September the 10th we just reviewed um we didn't review any
47:15
policies on September the 10th but we did discuss the ongoing legislative agenda process that's what it was okay
47:22
so we did discuss um proposed legislative agenda items and we sent out
47:29
um an email to the board members to solicit any um particular ideas that you
47:35
may have around the agenda what is the timeline for all board members to submit
47:40
their proposals we ask for those um proposals to be submitted by the 30th of
47:45
this month thank you thank
47:51
youur procurement committee report um the items are on the agenda for for
47:57
tonight general counsel report thank you madam chair no
48:03
report before I bring the superintendent's rep up for her report I want to recognize the Tennessee Valley
48:09
Authority on today they had commissioner Otay out in her
48:15
schools donating school supplies to the students in the district five District 5
48:22
they were out today donating and we just want to thank them for their partnership with Memphis Shelby County
48:28
Schools superintendent's report thank you madam chair i' like to start off I know we removed item 12.1 it
48:35
was for Prodigy uh but we did ask the the student to be here tonight the Legacy Builder who actually lifted uh
48:43
this as an opportunity to be spread across the district so while it will be under additional legal review it did want to start out by acknowledging
48:49
Andrew Ellis and I think his mom is in the audience If You're Here Andrew did he
48:54
leave there he is come on up
49:00
Andrew come on up so when we think about bringing to the board the best decisions uh many of
49:07
those are certainly uh brought by led directly by our students but all of them are informed uh by our students and so
49:14
Andrew led the conversation rallied and galvanized the the energy and the spirit of the other 49 Legacy Builders who uh
49:23
were in the space had robust conversations about the impact of the same and so we want to shine the light
49:29
on you young sir um thank you Dr fagin for inviting me to the board meeting and recognizing
49:35
me for my service to the district and I just want want yall to know that I truly
49:42
think pry can work and of course it is doesn't it's not without its cons and Pros uh just raise it there you go um
49:51
but I do think Prodigy is amazing I just had a interview with some other students from across the district and they were
49:56
talking about I ready versus Prodigy and when I mentioned I Prodigy their their face is lit up and so I truly think
50:03
Prodigy can work um they have amazing statistics on their um amazing statistics on the website about how
50:09
they've implemented it and how there also even research published by California schools and reviewing how the
50:16
effects of pry have have affected their students math scores and so um please
50:22
bear with me and that just thank you again Andrew is a senior correct
50:27
M College High School there we go thank you
50:46
Andrew I think we heard Dr Watson at Westwood mention a smooth start which
50:52
has been shared by many of our principles and leaders and so much of that smooth start could not take take place without our one of our first
50:58
spaces uh which is generally our general office secretaries and so did invite them to be here this evening as well if
51:04
you are here a general office secretary we are full fully staffed uh across the
51:11
district in that area we had several vacancies before uh I think the increase in compensation certainly helped but
51:17
your invaluable service to the district and specifically to your schools as we
51:23
have experienced an increase in enrollment and overall all uh trending upward we thank you and tonight we shine
51:30
the light on you as well if you will come
51:40
forward general office secretaries come on
51:48
forward I know they're out there come on forward they're coming forward
51:56
if you will come forward please so that we can get your picture with the
52:19
staff oh a lot of
52:55
even e
53:51
not
54:24
than
54:29
than
55:25
okay for
56:23
you she
56:33
all right so to the superintendent report board members this evening uh we'll
56:44
begin uh as we approach the quarter uh we made the commitment to deliver quarterly impact reports and so just
56:51
sharing when we will share those particular reports our first one is slated to be provided to you October the
56:56
25th again this is our commitment to um monitor each of our measurable contracts
57:02
and so that's about 300 plus active contracts uh and we commit to providing that to you October the 25th just to
57:09
take a look at the assessment criteria that the team uses uh when evaluating contracts uh is is the screened here uh
57:18
key areas timeline budget quality of deliverables stakeholder communication and then there's a risk management and
57:24
then an overall contract status uh looking at at risk on track and off track uh will be how these contracts are
57:31
rated as we arrive at uh the points earned and then certainly the points possible uh to stand up uh just the
57:39
contributions that we've made commitments to Via writing just sharing how those are showing up in our schools
57:46
or the respective spaces where results are
57:51
anticipated 75 nutrition staff uh School support staff have been hired uh as a
57:56
recruitment update since July 1st uh our new high food service training there's some numbers there we have another one
58:03
coming up September 30th our part-time job information sessions as we continue to uh stand up ways uh to fill the many
58:10
positions that remain we have upcoming recruitment activities for this particular position with one tomorrow uh
58:16
a virtual hiring or VA hiring event our daily teacher
58:24
vacancy Elementary has the highest number of vacancies at 75 four of those are under HR review meaning we're moving
58:31
four individuals forward uh special education continues to show a large number of vacancies we're now at 85 we
58:37
last reported 86 uh with no HR reviews pending mathematics remains certainly a
58:43
critical area with 44 vacancies and 11 of those are under review uh our English
58:50
uh speakers other their languages and foreign language have notable vacancies with 20 and3
58:58
respectively our enrollment updates uh some 110,000 396 and so there appear to
59:06
be some double counting uh in our prek space and at the CDC the Child
59:11
Development Center uh we're looking at
59:26
uh as of yesterday as we look at the projected numbers uh for fiscal year
59:32
2025 in comparison to 20124 we're certainly higher with 108 610 uh in
59:38
week8 of last year and we're at 110 356 this
59:47
year so a lot of metrics here on this slide uh what we've attempted to do is
59:52
just return uh our last presentation of this was in end of year and so as we
59:57
have entered the year uh just breaking down our metrics what you're looking at here's K12 metrics for September
1:00:05
highlighting decreases in teacher vacancies unlicensed teachers absenteeism and small changes in
1:00:10
enrollment as we take a look at the teacher vacancies uh there's been
1:00:16
6.2% of our teacher positions are currently vacant uh 7.9% is where we
1:00:21
entered or finished last year in our non-charter schools uh as we look at unlicensed teachers in our non-charter
1:00:28
schools uh these are or District Le schools this is 19.1% of Educators
1:00:35
currently hold teaching permits and limited licenses current enrollment of all
1:00:42
schools 106 317 and so you see the breakdown there prek enrollment 4616 for
1:00:50
all schools and you see the breakdown across uh charter schools and then district schools
1:00:56
absence rate all schools 6. 6.6% is the average percent of students who are not
1:01:03
in attendance certainly we're down about 2% here in terms of the change uh our
1:01:09
chronic absenteeism is down overall uh it's down at district schools and certainly down uh at Charter Schools so
1:01:16
we're trending in the right direction if we keep this pace and certainly uh we can stand a few improvements there and
1:01:21
we have some initiatives and some work going into that
1:01:28
looking at K5 space only this shows a drop in our K5 enrollment absenteeism
1:01:34
and chronic absenteeism in the month of September with Charter Schools seeing increase enrollment and lower absentee
1:01:40
rates if you're looking at the current number of enrolled students at all schools per K5 you see
1:01:46
51,27386 per
1:01:56
is the average of students who are not in attendance at all schools and you see the breakdown here district schools and
1:02:01
Charter Schools chronic absenteeism this is the percent of students missing 10% of
1:02:07
school days for any reason and who were enrolled at least 50% of the year so far
1:02:14
21.5% of district schools and 18.3% uh of charter schools and overall
1:02:20
20.9% of students have missed 10% uh or more of school days so
1:02:27
far in K5 in our Middle grades 6 through eight
1:02:33
current enrollment overall 23,9 66 students you see that an increase of
1:02:39
603 in our district schools
1:02:48
18,1918 an absence rate of 5.6% in all schools district schools 5.6% and and
1:02:55
certainly Charter Schools across the board it's 5.6% in comparison to last year's just right at
1:03:02
8% chronic absenteeism in Middle grades 18.8% of students have missed already
1:03:08
10% of school days for any reason and they've been enrolled at least 50% of the year so far our district schools are
1:03:16
seated at about 18.9% so far and 18.4% at our charter
1:03:24
schools for grades and 9 through 12 enrollment increased absenteeism decreased and chronic absenteeism saw a
1:03:31
sharp drop in charter schools looking at current enrollment in all schools for high school grades 9 through 12
1:03:40
31,700 students or more in our district schools that's 26356 students where the greatest gains
1:03:47
have been made and our charter schools have also increased at nearly 260 the absence rate 8.4% is the average
1:03:55
percentage students who are not in attendance at all schools 8.8% at district schools 6.2% at Charter Schools
1:04:04
looking at Chronic absenteeism again this is the percent of students or high school students who have missed 10% or
1:04:09
more of school days for any reason and they've been enrolled at least 50% of the school year so far we're at 29%
1:04:17
overall with 30% in our district schools 21.8% in charter schools certainly our
1:04:24
greatest work in this area area is in our high schools or in our grades 9 through 12 looking at and we've added
1:04:31
off track in terms of graduation rate so that we start our tracking in ninth grade and track grades 9 10 and 11 so
1:04:38
that we have a deeper understanding of what our graduation rate uh could look like at all schools right now 27.3% of
1:04:45
students are off track for graduation at our district schools that's 29% and our
1:04:51
Charter Schools that's 14.8% grade 12 our senior
1:04:57
42% across all schools of seniors are projected to be off track for graduation
1:05:04
that's nearly half of our senior class and so our greatest efforts are there
1:05:09
41% or 41.4% in district schools and nearly 50% in our Charter Schools
1:05:15
sitting at 48.7% and again this is the current cohort
1:05:20
2025 uh and grades 9 through 12 those are our metrics
1:05:28
all right Madame chair this concludes my
1:05:34
report thank you commissioner love um I would be interested to know
1:05:42
what percentage of the aism in contribute to uh suspensions and is
1:05:51
soltions we'll get that data
1:06:03
commissioner mckenny thank you thank you for that report superintendent fagin can you
1:06:10
explain because I think for the listening public and for the public why we include Charter School data in this
1:06:17
these reports sure so charter schools in many areas count in our data and so uh as a
1:06:25
district authorizer uh we are responsible in many regards or at least uh the responsibility for sharing out
1:06:32
providing resources maintaining collaboration although the autonomy exists uh for our charter schools in
1:06:38
many spaces like enrollment attendance um there are still the data is still shared um graduation rates as well uh in
1:06:47
other areas uh that particular information is Standalone but we still share it out because the money passes
1:06:53
through in terms of the funding through the district I have one followup thing um so
1:07:01
I appreciate that we are now doing the charter advisory Council so that that's
1:07:06
some of the things that we can we can talk about how we can leverage possibly resources and possibly programming or we
1:07:14
can do some thoughts around how we can work on these things
1:07:21
together commissioner love second time
1:07:27
I'm following Direction um the number of
1:07:33
students um that aren't on grade level um I would be interested to
1:07:43
know how daily attendance attributes to the number two years ago I was in tresmond
1:07:53
high school and there was a a a high number of ninth
1:07:59
graders um um who haven't been to school in two
1:08:06
years yes thank you for that question board member love when we think about uh off track rate which is why we started
1:08:12
to track it here so graduation rate for lack of better words is a lagging indicator that's just what happens after
1:08:18
the fact uh what we have to do is what we're doing now is tracking it on the front end so as an individual a student
1:08:24
enters GR 9 which is what you're lifting here we're monitoring closely uh how they Faire at the end of a quarter how
1:08:31
they end at the end of the semester so that we can ensure that they remain on track meaning if a student lacks success
1:08:37
in a course we either reenroll them or we stand up an additional action plan to ensure that they obtain that credit so
1:08:44
that they when they transition to the next grade level they have the number of credit certainly that is necessary for
1:08:49
matriculation meaning to move to the next grade but more importantly they have the number of credits that are NE
1:08:55
necessary to keep them on track so ideally if a student is taking eight courses in high school or seven courses
1:09:01
in high school you at least want them to obtain or attain five of those seven credits all of them is the goal and the
1:09:07
expectation but at least five keeps you on track as you matriculate to the next level it it doubles and it adds up and
1:09:14
so if we know where a student is semester by semester and certainly year by year we're more likely to decrease
1:09:21
the dropout rate because we can step in with students who aren't showing up as early as their freshman year but
1:09:27
certainly we can make summer school more substantive and any additional credit recovery programs that are necessary
1:09:33
that a student needs to reenroll in a class or expand our Master scheduling efforts so that students retake a course
1:09:40
that they failed uh don't want to pour too much information tonight but did want to share why it was important to
1:09:46
add the off trck uh monitoring uh to our metrics so that we know uh by student
1:09:52
and by School uh how our students are doing attendance to your specific question in the contribution it is
1:09:58
absolutely attendance the more days that a student misses the more class that
1:10:04
they miss which is why our come to win initiative is so important where we've shared and will continue to share the
1:10:09
impact of one minute 10 minutes one day one week uh the impact on learning and
1:10:15
instruction but certainly when we think about off track that's the direct or certainly one of the direct contributing
1:10:22
factors commissioner Murphy I think um Madam chair Madame
1:10:29
Vice chair superintendent um I think you answered a little bit of my question but we still have a lot of students that
1:10:36
still is not registered in school at this time what are we doing are we communicating with the families I just
1:10:42
want to know what how we're going to move from here to get them enrolled in
1:10:47
class uh through the chair thank you um boy commissioner Murphy for the question
1:10:53
as we think about the number of students who are already missing classes uh we took a look at the number of students in
1:10:59
terms of overlap that ended the year having missed classes as as well and so certainly those students that ended the
1:11:06
year uh quinic absenteeism treny they started the year as well and so uh our
1:11:13
efforts are with the community with our families uh to stand up a a massive meeting we have about 1538 students
1:11:21
right now who have 8 to 23 or more absences already ready we plan to have
1:11:26
the conversations with them about what they need for sure educating them about what it means to be chronically absent
1:11:32
or Trent but also more importantly if there are resources that are needed being able to partner them directly with
1:11:38
our partners and vendors in the community while understanding that there are legal ramifications uh and
1:11:44
consequences and outcomes uh with consideration of compulsory law as you think about directly enrolling uh we do
1:11:51
have some students who have not enrolled uh for various reason reasons uh some families are experiencing houselessness
1:11:58
as we know others are still choosing a district uh others we have not been able to get in contact so by District we plan
1:12:05
to share that information with you so that you can look at it by District the efforts that our student excuse me that
1:12:10
our schools have been carrying out so far with making the phone calls uh we have several who have gone out knocked
1:12:16
on doors uh to check and see if addresses are accurate and so we'll be able to share that comprehensive review
1:12:23
uh of the more just over at th000 students that have yet to enroll this is a broad um district and
1:12:32
we need more hands on deck in order to reach the rest of the families that have children that is not registered how are
1:12:38
we going to do that when we don't have enough
1:12:47
staff through the chair board member Murphy in terms of not having enough staff i' have to seek Clarity are you
1:12:54
sharing at our schools or if you can provide a little more context for me when we had seed they were there to um
1:13:04
help out with absenteeism they were there with treny they were reaching out to the families that were homeless and
1:13:11
we have we don't have that many hands on deck right now but we have too many children still out of school and so we
1:13:18
need more hands on deck to reach these families to see what's going on with these families and why their children
1:13:23
are not in school and and so we need more help so we have family engagement Liaisons treny Liaisons and attendance
1:13:30
liaison have been leading this work and they're in the schools and so they've been making the calls uh in tendem with
1:13:37
the the team uh either problem solving team or the school support team uh in making these calls and efforts uh some
1:13:43
of the students were still trying to track because there is um a gap if you will in understanding who is enrolled in
1:13:50
charter schools I think that is where the question that is lifted earlier that's where that dichotomy exists in
1:13:57
terms of the sharing of data and so some of the students could be enrolled elsewhere uh some of them could have
1:14:02
moved out of state uh there are many Dynamic factors as we consider the students who have not enrolled yet again
1:14:09
this is standing it up against projected enrollment uh and several of these numbers were for our prek students and
1:14:16
so we've lifted in previous conversations uh about my why many of our families have either left or not
1:14:21
chosen to enroll or generally speaking the funding that is required for prek which makes our numbers the gaps there
1:14:28
if we're looking at the numbers specifically about where enrollment is greatest just want to go back to that
1:14:34
slide for a second we anticipated
1:14:40
5,80 prek students and we're at 4633 uh as we look across the board our
1:14:47
CDC uh we're exceeding enrollment there uh as we look at Al alternative
1:14:52
enrollment certainly um we we don't want as many students there as we look at Charter enrollment you see that it is
1:14:58
down as well as we look at Excel Memphis virtual meaning our schools Memphis
1:15:04
virtual adult high school looking at the projected numbers all of those uh have exceeded or right where we projected it
1:15:11
uh so it's really in our prek numbers where we're missing most of the students that we expected or projected to be
1:15:17
enrolled we also anticipated many of the ASD mergers uh or from the mergers uh
1:15:25
return of those schools if you will we anticipated many of those students coming back to us and they did not and
1:15:30
so enrollment here uh pretty fluid um but not necessarily because these
1:15:36
students are in our schools or supposed to be in our schools right because we we still have a lot of students that's out
1:15:43
and and we have to get them in class and you say you have somebody in in each school but something is not working
1:15:49
because we still missing thousands of kids something is not working because we have that many you you have a liaison in
1:15:56
each school from from my understanding and if we have a liaison in each school but we're still missing thousands of
1:16:03
kids then something they're doing is not
1:16:11
right commissioner Williams can you tell me today how many classrooms are without a
1:16:21
teacher so we have 358 vacancies uh these are instructional
1:16:27
vacancies and on the screen is the the identification of those vacancies
1:16:34
seven in art I don't want to read them all but that that's where the vacancies exist uh with the few under HR review
1:16:41
the 21 meaning there's someone that is uh in the pipeline and moving forward in the onboarding process uh so that 358
1:16:48
the true vacancy number is 336 uh as we think about who's moving uh
1:16:53
but today there are 3 58 across these particular uh classes so that means
1:16:59
we've had about um 50 or 60 classrooms without instruction or prop or certified
1:17:05
instruction with that number we still have a large number of people who are teach teaching without credentials
1:17:10
that's correct so I am curious to know in your thinking what impact will that have on the outcome of achievement this
1:17:18
year we have too many vacant classrooms I know it's a big lift it's across the
1:17:23
nation but something has to happen to fill the classrooms with teachers who know what they're doing and who can
1:17:30
teach children and those who are there you got to wear them out because they're try to cover the whole school and
1:17:36
they're probably start dropping out sooner or later but I don't know how it's going to impact and how it will be
1:17:42
positive without teachers standing before children who can deliver instruction I don't see anything in that
1:17:48
but failure board member Williams of course we've had multiple conversations about
1:17:54
this and so we certainly align and are thinking about the the impact uh of not
1:18:00
having a teacher one certainly the impact of not having a certified teacher too uh and then as you've asked about
1:18:07
you know what is the impact and do we know the correlation if you will between those who are not certified but on the
1:18:13
permit uh and those who are still moving through the pipeline uh I won't speak
1:18:19
directly to that because I'd like to get the official um data for it um because I
1:18:24
do know that there are several teachers who are operating with a permit who have Prov proven quite effective and so want
1:18:30
to make sure that I share uh the right and accurate information uh because we do appreciate those who are aspiring uh
1:18:36
to become fully licensed while we think about the greater question and ask which is Recruitment and you are certainly
1:18:42
aware of our efforts because you've participated and supported many of our hiring blitzes and so it is not because
1:18:48
of lack of effort uh but certainly as you've lifted as well Across the Nation this is a challenge uh losing some
1:18:54
300,000 teachers in the pandemic uh that is not something that we will recoup uh
1:19:00
in in anytime soon uh as we work to make the field more attractive uh to the
1:19:05
degree possible that we can as a district Memphis Shelby County Schools I think we are doing that uh as we work to
1:19:11
continue strengthen compensation uh to attract the most qualified individuals I think we are doing that as we continue
1:19:18
to stand up the types of recruitment efforts through our move Memphis our Partnerships with our residential uh
1:19:24
facilities to to provide uh housing uh and certainly additional ways that we
1:19:29
are thinking about um feeling these positions uh but certainly it is not
1:19:34
without being stated uh when it's brought to the board to have the real critical conversations about our
1:19:39
buildings the number of buildings that we have uh the enrollment in several of them and the the true decisions that
1:19:45
have to be made because if uh we had the same number today uh with fewer
1:19:51
buildings if you will um then we could feel more of our positions and so uh
1:19:56
there are a lot of decisions that are forthcoming uh that we would all be responsible for making uh as we keep the
1:20:03
question that you've centered here in mind how do we fill these positions uh in the best interest of kids and
1:20:08
certainly for the performance and outcomes but ensure they have the type of educational experience that we'd like
1:20:13
to afford them very clear to me that we will not move the needle without
1:20:20
teachers if we we cannot have as many teachers the percentage of of unfilled
1:20:25
classrooms and think that we're going to make advances it's impossible to do so that has to be a priority of getting
1:20:32
folk in front of children who can teach and will teach what they need to know to be
1:20:39
successful commission since we're on the topic of
1:20:46
uh absenteeism chair Vice chair superintendent uh as I was visiting the
1:20:52
schools today uh very grateful for TVA want to give them a shout out again for being one of our Community Partners I
1:20:58
emailed every teacher in my district and they all emailed back something that they wanted as far as supplies and we
1:21:03
went and we gave every school in our district supplies today and so as I I
1:21:08
was going through a couple people had some things that they wanted to mention regarding the
1:21:13
vaccinations um apparently um some of the kids were automatically re-enrolled um this summer and the
1:21:21
information was not updated and neither were CH records received I'm just kind of asking this is what was told to me so
1:21:28
a lot of the kids are out of compliance as far as having the vaccinations um I received a call so I
1:21:33
didn't even know that my son didn't have everything I thought everything was up to speed we have to send it over so I
1:21:38
sent my my documentation over but you have some parents that cannot are that quick on their feet to get that done so
1:21:47
I do think it's not a bad idea to have um I don't know the guidelines if those nurses can give uh the vaccinations or
1:21:54
if we and have the health department come in so that we don't have to withdraw those kids because they're going to have to be withdrawn CU they're going to be out of compliance and we're
1:22:00
going to be having even more students not at school so just wanted to bring that to you guys
1:22:11
attention commissioner McKenna second time and then commissioner Murphy thank
1:22:17
you through the chair one thing um can we get this loaded up to bardocks so
1:22:24
that our public can see this as well and we can share
1:22:35
it the PowerPoint yes superintendent it now it is it takes a
1:22:41
little while okay next thing that I would like to say um superintendent you raised something um while you were
1:22:47
talking about permitted teachers and you indicated that you have are starting the
1:22:53
process for looking at those permitted teachers cuz some of them have actually done some really good work and are level
1:22:59
four and fives and it is a state issue that we have that won't allow us to keep
1:23:05
those permit or to shift them into um permanent teacher positions so I think
1:23:10
this is when we have to put in our legislative agenda items this may be something that we can take to the state
1:23:16
as a legislative agenda item particularly since we need to be creative given the shortage not only in
1:23:21
Shelby County across the state but Across the Nation uh thank you board member McKenna and
1:23:27
just to be clear I think what we're we're emphasizing uh is that uh while three years is currently the state's uh
1:23:34
expectation and and requirement in terms of the amount of time that you have what
1:23:39
we'd like to underscore and emphasize for consideration is the consideration for those who may be level three and
1:23:46
four to have some level of EX exception if you will if they've proven to be effective uh for our students so just
1:23:53
wanted to be clear about what we would be advocating for I know we've had a little conversation about it so just for the record uh and certainly align with
1:24:00
the same um Madam chair Madam Vice chair superintendent I would like to picky
1:24:06
back off of what um commissioner Williams said because I um spoke with
1:24:11
some teachers that are in classrooms and they are English teachers but they're teaching trigonometry and they know
1:24:19
nothing about trigonometry I've also had some um teachers call me and say they
1:24:25
put in applications for a teaching position and they still never got a call
1:24:31
or they never got looked up they never did anything nobody never even called them back so I'm getting those calls as
1:24:37
well and this is coming from the students that's telling me that their teachers are not Math teachers they know
1:24:43
more than the math teacher so we have to do something because it's about our kids
1:24:48
and we need the right teachers teaching in the right classes versus putting a teacher in a class that don't notice
1:24:56
subject through the chair board member Murphy I appreciate you
1:25:01
elevating what I would share would be concerning so I want to say this delicately while we have a need as many
1:25:08
districts do across the country uh we're not desperate in such a way that we
1:25:13
would place an English certified teacher teaching math so I'd like to know
1:25:18
offline you know who who that offline I I will tell you offline uh so that we can write that
1:25:24
wrong um because that is more detrimental uh to to hello
1:25:32
there there that would be more detrimental to a student um if you will than than the
1:25:38
current status and so offline look forward to hearing that from while we talking offline I'm going tell you about that failing that's teaching
1:25:45
too' offine through the chair uh yes offline we will continue the conversation I I appreciate that but I
1:25:51
want to be clear that uh as as deeply committed as we are to filling the vacancies our commitment is deepest to
1:25:58
ensuring that we have qualified teachers and so we have certified substitute
1:26:03
teachers who are retired uh and and they serve us well and so I want to make sure
1:26:09
that we recognize them also while we have true vacancies uh our coverage has
1:26:14
averaged between 88% to 90% meaning that's how many of them we've had
1:26:19
covered from day to day so we appreciate it we've also had several retired teachers uh board Williams to reach out
1:26:25
and they want to return to do this work and so while I may or may not be asking you to do the same uh I am sharing with
1:26:32
you sharing with you that the interest Is On The Rise um because they
1:26:38
understand uh the urgency of now and so I appreciate all of board members um concerns certainly know that it is
1:26:44
shared but we will not um we will not um Place anyone before
1:26:50
our students uh that cannot contribute to their good thank
1:26:56
you commissioner OT you're second and commissioner Porter superintendent I feel to ask the
1:27:03
question of who we have that uh that can work across the district with the schools uh to provide the health
1:27:09
vaccinations I know the seed office was doing that at one point so who do we have in place so we can kind of get that
1:27:14
going sure we we do have our own health uh Center but we also partner with the Shelby County Health Department and I
1:27:20
think one of these items or at least one previous uh was about vaccinations and expanding our work there to ensure that
1:27:27
it's happening uh there is a deadline coming we haven't reached it just yet um but quite confident yeah we're we're
1:27:33
pushing it uh but certainly our efforts are there so are we going to Pro put any one white law overseas okay so Dr White
1:27:40
Law will be able to provide us with some information that's right okay we'll get um I think you're looking for and I
1:27:46
don't want to put words in your mouth but just for clarity you'd want to know just where we are right now in terms of the number of students who would be
1:27:52
missing uh those vaccinations we any required records as well and then certainly what our efforts are to ensure
1:27:58
that we contact and reach them is that accurate I want to know who who we would uh when we could put someone in place
1:28:05
right away because there's a lot of students and we're going to be approaching the deadline pretty quickly
1:28:10
I know one school had 90 students uh for one grade level so we need to put someone in in place quick and so I just
1:28:16
want to see do we have someone we can go ahead and put in place as soon as possible to start that because we do
1:28:22
have certified qualified nurses where I again I don't know the contract but they
1:28:27
could they could uh administer the um vaccinations right there commissioner let's talk about doing a a health fair
1:28:33
in that area to see about getting the vaccination like a One Stop Place perfect that answer my question and will
1:28:40
you share that specific school that you're highlighting with with 90 as well that's PL yeah there a lot of schools
1:28:46
that have whether rather not um but yeah it was shared with me uh
1:28:52
one school had night review the data again not sure that we saw that but we'll review it again um but overall
1:28:58
certainly understand your sentiment in terms of the focus commissioner
1:29:05
mckiss Porter is next oh I'm sorry commissioner Porter I apologize thanks chair um I may have
1:29:12
missed it in the presentation but was there a way to trct the students coming from the ASD schools back to um public
1:29:18
Shelby County Schools is that way um was it the day of that precise
1:29:24
so we uh thank you through the chair board member reporter for the question
1:29:30
so when we attempted to uh monitor this data a lot of gaps uh so we had the list
1:29:38
if you will but in terms of knowing where those students are it's a matter of looking at each roster seeing if they
1:29:43
showed up somewhere across our district uh in terms of tracking if Marie Fagan
1:29:48
based on leaving you know XYZ ASD school did she go directly to Craigmont as we
1:29:54
expected uh we only know that um if we had the record right so there's about
1:29:59
three we
1:30:04
projected 3,729 uh students to come to us from ASD
1:30:12
uh I will make sure we get do we have those numbers bill of how many
1:30:18
students Mr White
1:30:24
good evening superintendent and board members um that that number actually is
1:30:29
what's projected to be the ASD District's enrollment because the dollars actually come to us and then we
1:30:36
have to distribute those to the ASD but we can look into your question of the
1:30:42
students who um we were to receive from the ASD how many of those actually ended
1:30:48
up with us but we can do that yeah and I appreciate that yeah trying to see it
1:30:54
was the data that precise and then um another question is just curious on the the district efforts of trying to
1:31:00
recruit out of state just trying to see how many teachers was actually um you know chose to come to Tennessee and will
1:31:07
come to Memphis rather to teach so if yall had the information absolutely we'll give you the data of interest in terms of interviews and and applications
1:31:13
as well as those who actually chose
1:31:19
absolutely commissioner mcki thank you madam chair I just wanted to uh recommend if there any further
1:31:25
individual questions like this if we could maybe address them with the superintendent and move forward with the
1:31:31
balance of the meeting okay one more and then we'll be done
1:31:38
commissioner love I just want to give a shout out to
1:31:44
the resource officers in my district and all around last week was crazy and you guys
1:31:53
help it down that's
1:31:59
true that was worth the third
1:32:05
time that's aome
1:32:11
pleas yeah to the first reading of
1:32:21
policy 11.1 11.1 first reading proposed policies
1:32:27
first
1:32:34
reading Miss
1:32:45
Stewart superintendent Fagan's board members if you can recall um last month
1:32:52
the board passed a resolution requiring a policy to be drafted and presented to
1:32:57
the board regarding the position of the um Board District general counsel we
1:33:04
have this policy before you this afternoon and there are eight seven
1:33:10
components to the to the policy and I'll just give a high level overview the
1:33:15
first section deals with the established position of the Board District general counsel including his or her primary
1:33:23
respons abilities and general duties the policy next outlines the office of the
1:33:28
Board District general counsel and the Departments that will report to the
1:33:34
general Council um it also states that the general council is authorized to
1:33:39
hire employees within those departments as well as to set salaries the policy
1:33:45
also authorizes The General Counsel to enter into contracts as well as settled
1:33:51
disputes it also outlines a conflict of interest compensation and benefits for
1:33:58
the general Council an evaluation and performance um review that must be
1:34:04
conducted annually and we've also included a severability
1:34:17
clause Miss mckenny did you want to uh chair Vice chair superintendent
1:34:25
motion to suspend the
1:34:30
rules y we're going to suspend it for the Board District general counsel yeah
1:34:36
this is to suspend the rule uh for those of you who our new policies usually take
1:34:41
two readings there's a first reading where no action is taken and then the next month uh it comes up for adoption
1:34:49
uh this one it is possible to adopt if it's something that's important it needs to happen now if you suspend the policy
1:34:57
you may adopt this at this meeting so and that can be combined by the way to
1:35:02
suspend the policy and adopt that's what she's asking for so one vote will do both
1:35:12
second roll call Vote
1:35:19
Yes commissioner mckisic I commissioner gar IA I commissioner Porter I
1:35:28
commissioner Murphy I commissioner love I commissioner
1:35:33
McKenna I commissioner OT I commissioner William I chair Coleman I you have nine
1:35:43
in the affirmative that motion passes
1:35:54
Miss Stewart do we have a Tennessee school visitor schools School visitors
1:36:01
code for SEC for first reading first reading first reading yes that's
1:36:19
up sorry about that yes we do have the um TS is actually the toss model policy
1:36:28
for um visitors code of
1:36:34
conduct uh no action needs to be taken on this this evening it'll come up again at the next meeting for
1:36:51
adoption motion to susp bend the rules to adopt on first reading
1:37:00
second roll call
1:37:06
vote commissioner mckisic I commissioner Garcia I commissioner Porter I
1:37:14
commissioner Murphy I commissioner love I commissioner mckenny I commissioner OT
1:37:22
I commissioner Williams I chair Coleman I we have nine in the affirmative that
1:37:30
motion passes consent agenda we are now on to
1:37:35
the consent agenda are there any items to be removed from the consent agenda let me
1:37:42
speak uh you it is your right to remove something from the consent agenda if
1:37:47
there's anything you'd like to talk about or ask a question uh everything on the consent agenda is done with no more
1:37:53
debate so if there's something you'd like to move it will move down to request for
1:38:06
Action mckenny commissioner McKenna yes I'd like to move item 12.5 approval for
1:38:12
Head Start 2025 continuation application and recompetition application
1:38:29
commissioner love
1:38:39
9.20 yeah I was asking to move uh an item off
1:38:47
the consent agenda
1:39:00
um the one
1:39:05
rep yeah
1:39:21
yeah yeah yeah I just have a
1:39:30
question one question all right that's it I
1:39:36
think if you will read them then we can do the okay skip first
1:39:45
one 12.2 adoption thinking mathematically the eighth
1:39:51
edition I don't have amount there's nothing 12.3 contract approval RCM
1:39:59
Health Care Services
1:40:13
$35,790
1:40:18
12.6 approval Chevy County Health Department immunization event partnership
1:40:36
no this just isn't bold resol contract approval School lengths in the amount of
1:40:43
$433,500
1:40:53
you for the school based liazon program between juvenile court and Memphis
1:40:58
Shelby County Schools $225,000 12.9 contract renewal mou for
1:41:06
the Youth Court program between juvenile court and Memphis Shelby County
1:41:12
Schools no dollar amount 12.10 contract approve a signal health
1:41:18
and life insurance company for administrative Services only rates
1:41:25
$41,900 th000 12.11 contract approval Project
1:41:32
Lead the Way Grant acceptance acceptance of
1:41:40
$330,000 for Maxine Smith steam Academy 12.12 approval pure music and
1:41:47
Entertainment Group donation donation in am am in the amount of $100,000 to
1:41:53
Cummins K8 12.13 approval electric responsible
1:42:02
recyclers student desktops in amount of
1:42:09
$252,400 12.14 approval Thomas consultant student laptops in the amount
1:42:15
of 1,167
1:42:21
6987 12 15 contract approval 806 Technologies for title one
1:42:29
great webbased platform in the amount of $121,400
1:42:38
12.16 approval doto County mou no dollar
1:42:46
amount 12.17 approval Master service agreement cognia Incorporated
1:42:55
no dollar amount 12.18 contract approval en lighten Inc Sherwood Middle School in
1:43:03
the amount of $22,000 12.19 approval tcat dual
1:43:11
enrollment agreement no dollar amount
1:43:16
1220 contract approval project Bill phase one HVAC upgrades and the amount
1:43:22
of 2 24 million 71413
1:43:30
5.70 that one's removed moved that one's moved 12 22 approval former Vance midle land
1:43:42
lease in the amount of $5 12.23 contract approve of Holland and
1:43:49
night LLP in the meat of in the amount of
1:43:55
$108,000 12.24 contract approval project Bill roof replacement in the amount of
1:44:02
13 m729
1:44:08
41353 12.25 oh that's it I'm
1:44:14
sorry do I have a motion to approve the consent agenda in a
1:44:21
second motion by commissioner Porter second by commissioner hu
1:44:29
Garcia roll call vote
1:44:34
please commissioner mckisic hi commissioner Garcia I commissioner
1:44:41
Porter I commissioner Murphy I commissioner love commissioner mckenny I commissioner
1:44:49
OT I commissioner Williams I board chair Coleman I you have nine in the
1:44:56
affirmative thank you the consent agenda
1:45:06
passes request for Action 13.1 approval resolution to
1:45:13
disapprove of the proposed termination of the Memphis Area Transit Authority bus routes in support of Memphis city
1:45:19
council gun referendum was that read into the record at the
1:45:25
last meeting okay all you need is a motion in a second Matt can I get a
1:45:31
motion in a second uh motion to approve I think
1:45:36
everybody added their names on it and I see this one yeah make sure that everybody did great yeah
1:45:46
second roll call vote oh I'm sorry motion by commissioner hu Garcia second
1:45:51
by commissioner Murphy roll call vote
1:45:56
please commissioner mckisic hi commissioner gar I commissioner Porter I
1:46:04
commissioner Murphy I commissioner love commissioner mckenny I commissioner
1:46:11
OT I commissioner Williams I board chair Coleman I we have nine in the
1:46:16
affirmative that motion passes thank you 13.2 approval ad hoc committee on
1:46:23
strategic partnership initiatives
1:46:28
plan that was
1:46:35
removed and then there's two that came down 12.05 what's 12.05
1:46:54
yes I I merely took it off a consent agenda because I need Clarity on what we're being asked to approve so I would
1:47:02
like to um through chair as superintendent what are we being asked to
1:47:10
approve for the recompete not the comp for the recompete for the recompete part
1:47:19
okay through the chair uh board member Murphy the recompete application uh
1:47:25
opens on October 16th board member McKenna I've been called mcken McKinley
1:47:31
and now Murphy I'm still thinking about her last comment that's all uh but I'm focused uh
1:47:38
the the recompete application uh opens on October the 16th uh I think the reason the team was placing it on here
1:47:45
was to get ahead of it I think that what the board would probably want to consider is a special call so that you
1:47:50
review the actual application itself uh I think what was being asked here was
1:47:55
jumping probably a little ahead for the recompete uh in terms of seeking the approval because the approval comes
1:48:01
through the board uh so for the recompete which opens uh October the 16th it has a 60-day window to complet
1:48:09
it so that one I think we would be okay uh to to move uh and if necessary call a
1:48:15
special call unless there's some information that I haven't been made aware of I think in our conversations with headart uh as well as others there
1:48:23
hasn't been any information given to me specifically that would state that we need to have it on tonight's agenda um
1:48:28
but certainly provide additional details that would support uh Miss Miss
1:48:35
Gordon good evening superintendent and board Commissioners we're asking for the board to give us permission to apply
1:48:43
tonight this is what you're voting on you're allowing us permission to review the application and to apply for the
1:48:50
continuation that will complete the school year and then apply when the
1:48:55
grant opens on in October so tonight we're just asking for
1:49:00
permission from the board for us to
1:49:13
apply commissioner Murphy I didn't push that
1:49:19
button yeah commissioner
1:49:28
love pick it back in off what I spoke about last week um superintendent and um
1:49:37
Davin are y'all going to receive a consultant to draft this
1:49:47
grant so we have an internal consultant I I think that the the the the misbelief
1:49:54
if you will is that we're trying to complete this application by ourselves uh so there's certainly someone in the
1:50:00
finance department uh who has uh the Insight here uh We've certainly filled
1:50:06
out the application before where there is additional Insight that is necessary we certainly would not be you know
1:50:12
opposed to having a deeper review um but looking at the previous application for
1:50:17
me it's more about what we're able to State about how we've addressed the issues that are highlighted in the
1:50:24
deficiencies uh and and sustaining A Way Forward uh that does not have us in the
1:50:30
same space again uh but where there's additional support needed we would receive it uh where necessary thank
1:50:40
you commissioner mckenny um thank you through the
1:50:45
chair I understand that it's is this required by headart for you to get our
1:50:53
permission to apply for the recompete that the board or is it that
1:51:00
we're going to you're going to have to bring this because there's two things there's the permission to apply and then there's the permission to actually um
1:51:08
submit and so the question becomes is this coming back to us to yeah to Super
1:51:14
is this coming back to us um or because that's my understanding unless I I misunderstand how this works
1:51:25
through the chair uh board member mckenny as I have shared the language has not been provided to me that says
1:51:31
that we need to seek permission to apply what has been provided to me is that we
1:51:37
need permission to submit the application uh I did request a review uh
1:51:43
of the documentation in 2018 or so uh to to share the same thing U that was not
1:51:49
provided to me what was shared is that it existed that you approve the actual
1:51:55
application and so if there's something new which is what I've asked the team to provide to me in terms of any language
1:52:01
that has changed because there have been some changes uh with Head Start that is yet to come to me so I am in the same
1:52:07
space uh as I was when the last information was provided to me that's based on the information that I
1:52:15
have chair I would just again this is not to hold it up but again you're asking us to approve something we
1:52:21
haven't seen and I do since it hasn't been posted it's my understanding I'd like to suggest that we take that piece
1:52:29
off and wait until we actually have the application to approve and then let's go
1:52:34
ahead and um move on the continuation application
1:52:40
okay commissioner mckiss thank you madam chair so superintendent if I just can ask for
1:52:47
clarification from Miss Gordon because um Miss Gordon
1:52:55
um my apologies but I I know that I was a part of the process the last time
1:53:00
there was a very elaborate process for the application and uh as a board member
1:53:05
coming down to your offices can you maybe just to help provide more illumination for the board that when
1:53:11
you're asking for permission just to even get the process started is that what you're saying here because it required the last time I was a part of
1:53:18
this review process it was uh very elaborate and um they had to you know
1:53:23
pick board members to come and sit in on uh communication and interviews and that
1:53:28
people who traveled in from out of state so is that what we're um asking here asking for permission to get that whole
1:53:35
process started just to add Clarity to that please so it's it's two parts
1:53:41
commissioner um mckisic the first part is we are funded to December
1:53:47
2024 the second half the application is due October the 1 first so tonight
1:53:54
you're giving us permission to finish the continuation application and then on October the 21st
1:54:02
when the recompete application is po out on the street then we will apply for
1:54:08
that we have 60 days after it is posted we will come back to the board with the
1:54:14
completed continuation at the the recompete application but tonight you're
1:54:19
giving us permission to apply to finish the school school year and then when the application is
1:54:26
posted on the 21st for the recompete we will bring that application the full
1:54:33
recompete application back to the board superintendent reviews senior leaders
1:54:39
reviews and then the board will get the final review for the recompete okay so um thank you for
1:54:46
adding that level of clarity because and just to make sure for the listening public the reason why it is important to
1:54:53
get this process started now while you're asking for these two votes if you could just provide more information so
1:54:58
everyone's Crystal Clear uh the board and the listening public on on why it's important to why we can't wait until or
1:55:04
maybe even I guess we could have a special call meeting but if we can get it done tonight starting it can you speak to that
1:55:10
please because we have such a short time frame with the the continuation it is
1:55:16
due to the hit start regional office October the 1st so it's the same budget
1:55:22
that we have applied that you have approved it is just now saying what we will do with the monies for this school
1:55:30
year to finish out the school year so thank you so much so to our parliamentarian um can we do this this
1:55:37
two items with one vote if so that's what I'm moving for us to do your motion is to divide the question yes you can do
1:55:43
it if if there's no objection you can do it or you can do it by vote it would take a majority vote of those present in
1:55:49
voting to divide the question into two parts I'm I'm not asking to by the question just keep it as it is is what
1:55:54
I'm saying that's what I my motion is just to continue that's where we are right now no one has moveed to the move
1:56:01
yes so the motion there's a motion to adopt second did I hear second
1:56:09
yeah and this is adopting as it appears before you with both
1:56:14
parts we good go ahead roll call vote roll call
1:56:21
vote
1:56:26
commissioner mckisic I mck commissioner Garcia I commissioner Porter I
1:56:34
commissioner Murphy I commissioner love I commissioner mckeny
1:56:40
no commissioner OT I commissioner Williams
1:56:46
I board chair Coleman you have eight in the affirmative and one no
1:56:53
one in the one in the negative one negative I'm sorry motion is adopted the motion is
1:57:00
adopted now window replacement this was Miss
1:57:08
L we're now on to 12.21 approve a project Bild phase one
1:57:14
window replacements commissioner love Vice chair love I'm sorry um
1:57:23
Tito if it's all right with the superintendent um superintendent first
1:57:31
then she will hand it off to Tito um a
1:57:40
um several board members asked a question throughout this year when are
1:57:47
we going to see the updated um face two windows and roof
1:57:56
Replacements um the reason I asked that is because I've been receiving a
1:58:04
lot of calls from my schools scena Hills in particular they have been on the list
1:58:10
for 14
1:58:15
years through the chair thank you for the question uh Vice chair love uh Miss
1:58:21
Stuart if you will provide their response to to board member Love's question
1:58:29
please yes ma'am thank you Miss love um as you know we're finishing the facility
1:58:34
condition assessment the districtwide assessment um I believe we have 28 assessments left so that we have a
1:58:40
better way to prioritize all of the projects I will look back in previous um
1:58:47
administration's prioritization levels and see where scena Hills will is or was
1:58:54
um uh that was not on this this phase thank you yes
1:59:04
ma'am may I get a motion in second for adoption I'm sorry
1:59:10
commissioner second roll call
1:59:20
vote good commissioner mckisic I commissioner
1:59:27
Porter commissioner Garcia I commissioner Porter I commissioner
1:59:32
Murphy I commissioner love I commissioner mckenny I commissioner OT I commissioner
1:59:41
Williams I chair Coleman I you have n in the affirmative that motion
1:59:47
passes we are now on to our strategic allocation items I will now read the the resolution into record resolution
1:59:54
approving mscs board member strategic School fund allocation
2:00:00
September 2024 dollar amount $91,200 it is recommended that the sh County
2:00:07
Board of Education approves the the mscs board member strategic School fund
2:00:14
allocations for September 2024 is there a motion and a
2:00:19
second there you go you got motion to approve second motion by commissioner hu Garcia
2:00:27
second by commissioner Murphy roll call vote commissioner mckisic I commissioner
2:00:36
Garcia I commissioner Porter I commissioner Murphy I
2:00:41
commissioner love I commissioner McKenna I commissioner OT I commissioner
2:00:48
Williams I board chair Coleman I you have nine in the F to the motion passes
2:00:55
there being no further business this meeting is adjourned thank you
2:01:08
colleagues M Turner

Live chat replay was turned off for this video.


"""

converted_transcript = convert_transcript(text)
print(converted_transcript)