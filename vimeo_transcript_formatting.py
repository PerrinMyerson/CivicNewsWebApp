import re

def format_subtitles(subtitles, chunk_size=12, output_file='formatted_subtitles.txt'):
    import re
    import os

    # Check if the output file exists; if not, create it; if yes, it will be edited (appended to)
    if not os.path.exists(output_file):
        open(output_file, 'w').close()

    # Split the input text into lines
    lines = subtitles.split('\n')
    
    # Lists to store cleaned dialogue lines and their timestamps
    dialogue_lines = []
    timestamps = []

    # Regular expressions to identify timestamps
    timestamp_pattern = re.compile(r'^\d{2}:\d{2}:\d{2}[.,]\d{3} --> \d{2}:\d{2}:\d{2}[.,]\d{3}$')
    line_number_pattern = re.compile(r'^\d+$')

    start_time = ""
    end_time = ""

    # Open the file in append mode to edit or add new content
    with open(output_file, 'a') as file:
        # Process lines to separate dialogue and timestamps
        for line in lines:

            # Skip line numbers
            if line_number_pattern.match(line):
                continue

            # Handle timestamp lines
            if timestamp_pattern.match(line):
                current_start, current_end = line.split(' --> ')
                if not start_time:
                    start_time = current_start  # Set start time for the first line of a chunk
                end_time = current_end  # Continuously update the end time for the last line of the chunk
                timestamps.append((current_start, current_end))
                continue

            # Skip empty lines
            if not line.strip():
                continue

            # Add the dialogue line
            dialogue_lines.append(line.strip())

        # Merge lines into larger chunks with broader timestamp ranges
        for i in range(0, len(dialogue_lines), chunk_size):
            current_chunk = dialogue_lines[i:i + chunk_size]

            # Determine start and end times for each chunk
            if current_chunk:
                # Get start and end timestamps for the chunk range
                chunk_start_time = timestamps[i][0] if i < len(timestamps) else "00:00:00,000"
                chunk_end_time = timestamps[min(i + chunk_size - 1, len(timestamps) - 1)][1] if i + chunk_size - 1 < len(timestamps) else end_time
                
                # Format the merged chunk with the broader timestamp range
                formatted_chunk = f"{chunk_start_time} --> {chunk_end_time}\n{' '.join(current_chunk)}\n"
                
                # Print and write the formatted chunk to the file
                print(formatted_chunk)
                file.write(formatted_chunk)

text = '''WEBVTT

1
00:00:01.615 --> 00:00:01.905
Okay.

2
00:00:01.905 --> 00:00:04.145
With that being done, I'd like to, at this time, uh, uh,

3
00:00:04.145 --> 00:00:05.505
first of all, my name is Greg Faulkner.

4
00:00:05.505 --> 00:00:07.025
I'm chair of the Panel for Education Policy,

5
00:00:07.685 --> 00:00:10.985
and I'd like to, at this time, call our September 30, uh,

6
00:00:11.125 --> 00:00:13.265
um, October 30th meeting to order.

7
00:00:14.055 --> 00:00:16.475
And, uh, thank you all for being here this evening

8
00:00:16.655 --> 00:00:18.475
and welcome you and look forward to, uh,

9
00:00:18.745 --> 00:00:20.435
your participation in the meeting.

10
00:00:21.015 --> 00:00:24.155
Uh, just a few housekeeping, uh, things I'd like to discuss

11
00:00:24.155 --> 00:00:25.515
before we get, uh, started.

12
00:00:26.135 --> 00:00:28.875
If you signed up for public comment on an issue related

13
00:00:28.935 --> 00:00:33.475
to your students', uh, school, um, personnel, please speak

14
00:00:33.475 --> 00:00:36.355
with a member of the New York City Department of, uh, uh,

15
00:00:36.675 --> 00:00:38.595
a public school staff in the audience.

16
00:00:39.125 --> 00:00:40.515
These individuals will be able

17
00:00:40.515 --> 00:00:42.355
to take down detailed information

18
00:00:42.455 --> 00:00:45.595
and provide direct follow up if you wish to encourage,

19
00:00:45.895 --> 00:00:47.555
engage with the panel directly.

20
00:00:48.095 --> 00:00:50.155
You can also reach out to us, uh,

21
00:00:50.155 --> 00:00:52.275
through our email, um, site.

22
00:00:52.275 --> 00:00:53.315
We'll talk more about that later.

23
00:00:53.375 --> 00:00:55.075
We like to really engage with the public

24
00:00:55.095 --> 00:00:58.395
and hear your feedback on, on any number of issues.

25
00:00:58.665 --> 00:00:59.875
With that being said, I'd like to,

26
00:00:59.875 --> 00:01:01.555
at this time call ask our Secretary,

27
00:01:01.795 --> 00:01:03.075
secretary Nathan, to please call the role.

28
00:01:04.205 --> 00:01:05.435
Thank you, chair Hoffner.

29
00:01:08.825 --> 00:01:10.995
When I call your name members, please, um,

30
00:01:11.395 --> 00:01:12.635
indicate, um, that you're here.

31
00:01:13.175 --> 00:01:17.495
Um, Marielle Ali, uh, Adriana Ali

32
00:01:19.435 --> 00:01:20.395
tb, Shaday Arnold,

33
00:01:23.985 --> 00:01:25.165
uh, Shirley Alban,

34
00:01:27.265 --> 00:01:30.565
Master Jedi, Shirley Obert is present

35
00:01:31.105 --> 00:01:33.085
and may a four feet with all of you.

36
00:01:33.475 --> 00:01:34.475
Have fun tomorrow.

37
00:01:39.585 --> 00:01:43.095
Aaron Bogue, excuse me. Excused.

38
00:01:43.555 --> 00:01:45.735
Not coming. Uh, Camille Casre.

39
00:01:45.885 --> 00:01:48.655
Present, Marjorie Deans stag. Present.

40
00:01:49.435 --> 00:01:52.565
Amy Fair, present. Anita Garcia.

41
00:01:52.875 --> 00:01:55.645
Present, Anthony Giordano.

42
00:01:59.585 --> 00:02:04.425
Uh, Dr. Angela Green. Present. Navid Hassan. Here.

43
00:02:05.425 --> 00:02:08.855
Alice Ho. Present, Rema Ro

44
00:02:11.425 --> 00:02:12.445
Uh, Jess Lee.

45
00:02:12.445 --> 00:02:17.285
Present. Dr. Sharon Owin. Present. Alan Ong.

46
00:02:17.285 --> 00:02:21.845
Present. Maisha SAP. Present. Thomas Shepherd.

47
00:02:22.155 --> 00:02:24.475
Present. Ven Ang.

48
00:02:27.075 --> 00:02:31.765
Um, Manuel Vera and Chair Gregory Faulkner. Present.

49
00:02:32.255 --> 00:02:32.765
Thank you.

50
00:02:39.215 --> 00:02:41.375
17 members are present. We have a quorum.

51
00:02:41.515 --> 00:02:45.495
Um, and in addition to the members, um, is Lara Lai here

52
00:02:45.555 --> 00:02:46.975
for Controller Brad Lander?

53
00:02:48.455 --> 00:02:52.215
I am. Thank you. And Chancellor Melissa Avili Ramos.

54
00:02:53.125 --> 00:02:54.735
Good evening. Present. Great.

55
00:02:55.865 --> 00:03:00.345
So I see the forces with us. Okay.

56
00:03:00.965 --> 00:03:05.095
Um, our next order of business is the approval

57
00:03:05.115 --> 00:03:08.255
of the minutes from September 25th, 2024.

58
00:03:08.635 --> 00:03:10.415
Is there a motion for unanimous consent

59
00:03:10.875 --> 00:03:12.095
on the adoption of those minutes?

60
00:03:12.275 --> 00:03:14.775
Is there a second to the motion? Second. Second.

61
00:03:14.795 --> 00:03:17.455
Is there objection to unanimous consent on the approval

62
00:03:17.455 --> 00:03:21.475
of the minutes of September 25th, 2024, hearing?

63
00:03:21.495 --> 00:03:23.475
No objection. So what if the minutes are adopted?

64
00:03:23.725 --> 00:03:26.075
Those minutes are adopted? Yes. I see her hand.

65
00:03:26.435 --> 00:03:27.955
Question, panel member, member

66
00:03:29.045 --> 00:03:30.045
Caster Ready? Caster

67
00:03:30.045 --> 00:03:30.725
ready?

68
00:03:32.415 --> 00:03:34.015
I I had been reviewing the minutes

69
00:03:34.155 --> 00:03:35.295
and everything looks fine,

70
00:03:35.395 --> 00:03:36.735
but it was just something I wanted

71
00:03:36.735 --> 00:03:37.935
to suggest for the future.

72
00:03:38.635 --> 00:03:41.615
At the very bottom of the minutes, it, uh,

73
00:03:41.765 --> 00:03:43.775
says resolutions from this meeting are

74
00:03:43.775 --> 00:03:48.615
available@theschools.gov website for panel

75
00:03:48.635 --> 00:03:49.655
for education policy.

76
00:03:50.195 --> 00:03:55.055
But if you go there, it sort of is like a circular mishmash

77
00:03:55.055 --> 00:03:59.055
of how to ever find the things related to these minutes.

78
00:03:59.715 --> 00:04:03.535
So I was wondering if we could include the link

79
00:04:03.595 --> 00:04:07.055
to the contracts with the minutes so that

80
00:04:07.595 --> 00:04:10.335
if somebody was planning to go look this over,

81
00:04:10.405 --> 00:04:12.215
they actually would know what it means. So

82
00:04:12.215 --> 00:04:13.255
Currently there's a summary

83
00:04:13.255 --> 00:04:15.375
of the contracts that that's available.

84
00:04:15.475 --> 00:04:17.855
Are you asking for more than a summary

85
00:04:17.875 --> 00:04:19.735
or is a, what Would a summary be sufficient?

86
00:04:20.095 --> 00:04:21.455
I, I don't see a summary here.

87
00:04:21.685 --> 00:04:24.975
Well, I'm saying that currently we send out a summary

88
00:04:25.035 --> 00:04:28.685
of the contracts go is is sent out. Right?

89
00:04:29.105 --> 00:04:31.165
The same you're saying that's publicly posted. Okay.

90
00:04:31.385 --> 00:04:33.685
Should be attached here. And

91
00:04:33.985 --> 00:04:34.985
So you're just like, okay.

92
00:04:35.225 --> 00:04:37.085
So Right. Just, just for reference.

93
00:04:37.395 --> 00:04:38.845
Okay, fine. Thank you so much.

94
00:04:38.845 --> 00:04:39.845
So let me follow up on that

95
00:04:39.845 --> 00:04:42.205
and we'll see if we can have that, um, inclusion,

96
00:04:42.705 --> 00:04:43.725
um, added as well.

97
00:04:44.215 --> 00:04:46.165
Thank you. Any other comments?

98
00:04:46.375 --> 00:04:48.285
Thank you for your comment. Okay.

99
00:04:48.425 --> 00:04:51.405
So ladies and gentlemen, we're gonna begin, uh, uh, today

100
00:04:51.405 --> 00:04:54.605
and I'm, and I'm happy to welcome our new chancellor

101
00:04:54.745 --> 00:04:56.245
who has joined us on the stage.

102
00:04:56.865 --> 00:04:57.085
Um,

103
00:05:02.225 --> 00:05:04.705
I, I think this is really, we're beginning a new chapter

104
00:05:04.925 --> 00:05:06.825
for our, um, school system,

105
00:05:07.125 --> 00:05:08.745
and I think it's gonna be a great new chapter.

106
00:05:09.285 --> 00:05:11.825
Um, I'm happy to welcome you to the platform as well.

107
00:05:11.925 --> 00:05:14.505
And I think that, um, sends an important message

108
00:05:14.505 --> 00:05:16.825
that we have the chancellor here with us, um,

109
00:05:16.855 --> 00:05:18.545
join joining us on stage.

110
00:05:18.545 --> 00:05:19.905
And I really appreciate that.

111
00:05:20.445 --> 00:05:23.465
And, uh, that so far in, in, in your, uh,

112
00:05:23.465 --> 00:05:26.705
very new administration, the chancellor has really engaged

113
00:05:26.705 --> 00:05:28.985
with the panel and it's been available and accessible.

114
00:05:28.985 --> 00:05:31.665
And I think that really bodes for a great start for us

115
00:05:31.805 --> 00:05:34.865
and a great start for our, uh, uh, uh, new Year.

116
00:05:35.165 --> 00:05:36.665
So with that, I'd like to turn it over

117
00:05:36.685 --> 00:05:38.105
to our chancellor chair.

118
00:05:38.315 --> 00:05:39.345
Ramos floor is yours.

119
00:05:40.235 --> 00:05:41.465
Thank you so much, chair.

120
00:05:41.645 --> 00:05:43.225
And, uh, good evening to everyone.

121
00:05:43.355 --> 00:05:45.305
Wanna thank, uh, again, chair Faulkner,

122
00:05:45.305 --> 00:05:48.065
vice Chair Dr. Green, and all of our PEP members.

123
00:05:48.365 --> 00:05:50.385
Uh, and again, thank you for joining us, uh,

124
00:05:50.385 --> 00:05:52.585
earlier this week at our luncheon, uh,

125
00:05:52.725 --> 00:05:54.745
for taking time outta your schedule to be with us.

126
00:05:55.455 --> 00:05:59.005
Also, wanna acknowledge, uh, MS 1 31 Pace High School

127
00:05:59.005 --> 00:06:02.005
and Emma Lazarus High School, the principals here, uh,

128
00:06:02.005 --> 00:06:04.125
principal, uh, Gabel, gla,

129
00:06:04.225 --> 00:06:06.645
and Gini, as well as Superintendents,

130
00:06:06.645 --> 00:06:08.085
McGuire, Edleman, and Sullivan.

131
00:06:08.135 --> 00:06:09.565
Thank you so much for hosting us.

132
00:06:09.985 --> 00:06:14.685
So it's been a, a very busy first few weeks, very exciting.

133
00:06:14.685 --> 00:06:18.125
First few weeks I visited schools across the five boroughs,

134
00:06:18.125 --> 00:06:20.085
including a community school in the Bronx,

135
00:06:20.505 --> 00:06:24.525
an a SD program in Manhattan, a D 79 program in Queens,

136
00:06:25.005 --> 00:06:26.205
a New York City read school,

137
00:06:26.205 --> 00:06:28.325
and a New York City South School on Staten Island,

138
00:06:28.505 --> 00:06:30.245
an early childhood center in Brooklyn.

139
00:06:30.245 --> 00:06:31.445
And that's just to name a few.

140
00:06:32.105 --> 00:06:34.845
Amy, I also visited your daughter's school Renaissance,

141
00:06:34.895 --> 00:06:37.925
which happens to be, uh, in my old high school, uh,

142
00:06:37.945 --> 00:06:40.125
my old campus, uh, back at Lehman High School.

143
00:06:40.665 --> 00:06:42.325
Uh, so that was great to do that as well.

144
00:06:42.665 --> 00:06:44.245
As always, I'm amazed by the work

145
00:06:44.245 --> 00:06:46.405
that's happening in our schools every single day.

146
00:06:46.405 --> 00:06:48.445
There's something for everyone in New York City public

147
00:06:48.445 --> 00:06:50.085
schools, and we truly serve the entire

148
00:06:50.115 --> 00:06:51.405
city in all of its diversity.

149
00:06:51.945 --> 00:06:54.005
And I look forward to continuing our visits

150
00:06:54.105 --> 00:06:56.405
and continuing to meet all of you on our travels.

151
00:06:56.865 --> 00:06:58.725
Um, all in all, I've jumped right in

152
00:06:58.825 --> 00:07:00.845
and it's clear to me that our educators

153
00:07:00.845 --> 00:07:03.045
and school communities are building bright starts in bold

154
00:07:03.045 --> 00:07:04.205
futures across the city.

155
00:07:04.905 --> 00:07:06.725
As I've shared before, I'm committed

156
00:07:06.725 --> 00:07:09.085
to continuing priorities like New York City reads,

157
00:07:09.145 --> 00:07:11.365
New York City solves and our pathways work.

158
00:07:12.135 --> 00:07:14.625
Just last week, CUNY Chancellor Matos Rodriguez

159
00:07:14.625 --> 00:07:16.665
and I handed out welcome letters to signals

160
00:07:16.665 --> 00:07:17.865
to our graduating seniors.

161
00:07:17.865 --> 00:07:19.465
There is a place for you at CUNY

162
00:07:19.465 --> 00:07:20.665
as long as you finish strong.

163
00:07:21.505 --> 00:07:22.755
Also related to pathways,

164
00:07:22.835 --> 00:07:25.395
I attended the I Will Graduate event,

165
00:07:25.405 --> 00:07:26.755
which is a motivational event

166
00:07:26.755 --> 00:07:28.195
for hundreds of high school seniors.

167
00:07:28.375 --> 00:07:30.555
And the energy in the room was incredible.

168
00:07:31.345 --> 00:07:33.805
In addition to these priorities, there are a few other areas

169
00:07:33.805 --> 00:07:35.805
that I think we need to be laser focused on,

170
00:07:35.825 --> 00:07:38.525
and I have labeled them as my three commitments.

171
00:07:39.305 --> 00:07:43.525
So, in order school safety and overall sense of wellness

172
00:07:43.785 --> 00:07:45.045
and safety, both physical

173
00:07:45.045 --> 00:07:46.765
and emotional for our young people,

174
00:07:47.315 --> 00:07:49.045
that is a non-negotiable for me.

175
00:07:49.755 --> 00:07:52.895
And that's why last weekend we hosted a terrific community

176
00:07:52.895 --> 00:07:55.455
safety forum where agencies from across the city shared

177
00:07:55.775 --> 00:07:57.455
resources and listened to families.

178
00:07:57.455 --> 00:08:00.095
And I wanna give a special thanks to Chief of Safety

179
00:08:00.115 --> 00:08:02.375
and Prevention Partnerships, mark Rampant for pulling

180
00:08:02.375 --> 00:08:04.095
that together for New York City Public Schools.

181
00:08:04.815 --> 00:08:07.945
I believe change is only possible if we work together.

182
00:08:08.045 --> 00:08:10.185
And the forum was a great example of that.

183
00:08:11.305 --> 00:08:13.325
The other two commitments I plan

184
00:08:13.325 --> 00:08:15.445
to zoom in on are teacher support and family

185
00:08:15.545 --> 00:08:16.965
and community empowerment.

186
00:08:17.215 --> 00:08:18.485
Again, our families need

187
00:08:18.485 --> 00:08:19.845
to be at the table when we are

188
00:08:19.845 --> 00:08:21.205
making decisions for their children.

189
00:08:21.585 --> 00:08:23.445
As a mother, I understand this completely.

190
00:08:24.245 --> 00:08:27.385
I look forward to sharing more about my priorities

191
00:08:27.385 --> 00:08:28.705
with you all in the coming weeks.

192
00:08:29.695 --> 00:08:31.935
I also want to acknowledge some of the celebrations

193
00:08:31.935 --> 00:08:33.735
that have taken place since we last met.

194
00:08:34.195 --> 00:08:36.735
Our Jewish community celebrated the high holidays.

195
00:08:36.835 --> 00:08:38.375
We had Hispanic Heritage Month

196
00:08:38.375 --> 00:08:40.495
and Italian Heritage Month, both

197
00:08:40.495 --> 00:08:43.775
of which we celebrated at SW mm-Hmm, yep.

198
00:08:45.115 --> 00:08:47.575
We commemorated Indigenous People's Day,

199
00:08:47.595 --> 00:08:49.895
and we have both Halloween and Diwali this week.

200
00:08:50.905 --> 00:08:53.995
Apologies. It's our first year with a day off for Diwali.

201
00:08:54.015 --> 00:08:55.845
And I'm proud that in New York City public schools,

202
00:08:55.985 --> 00:08:57.005
our students, families

203
00:08:57.005 --> 00:08:58.725
and staff don't need to choose between school

204
00:08:58.745 --> 00:09:00.085
and faith or culture.

205
00:09:00.625 --> 00:09:02.925
On the topic of holidays, we also announced today

206
00:09:02.925 --> 00:09:05.365
that December 23rd will be part of our December break.

207
00:09:05.425 --> 00:09:07.525
We heard a lot of advocacy from family, staff,

208
00:09:07.525 --> 00:09:08.565
and students on the issues.

209
00:09:08.905 --> 00:09:10.405
And I'm committed to hearing from

210
00:09:10.405 --> 00:09:11.845
and responding to that feedback.

211
00:09:11.915 --> 00:09:14.445
Special thanks to Isaac, the young man who made sure

212
00:09:14.445 --> 00:09:15.925
that he sends a letter to the mayor

213
00:09:16.185 --> 00:09:17.725
and the Chancellor, uh,

214
00:09:17.945 --> 00:09:19.645
who is responsible for this great day.

215
00:09:20.345 --> 00:09:22.325
And of course, next week we have our election.

216
00:09:22.435 --> 00:09:23.605
It's more about important.

217
00:09:23.795 --> 00:09:25.525
It's more important now than ever

218
00:09:25.525 --> 00:09:27.125
that we teach our students about facts,

219
00:09:27.375 --> 00:09:28.405
about their civic duties

220
00:09:28.425 --> 00:09:30.965
and about how to engage with others on current events

221
00:09:30.985 --> 00:09:33.325
and contentious topics, especially when they disagree.

222
00:09:34.025 --> 00:09:35.965
I'm proud of all our civics team has done

223
00:09:35.965 --> 00:09:37.765
to support schools leading up to the election,

224
00:09:37.765 --> 00:09:38.885
including registering

225
00:09:38.885 --> 00:09:42.325
or pre-registered over 85,000 students to vote since 2019.

226
00:09:42.945 --> 00:09:44.525
As we head into this momentous chapter

227
00:09:44.545 --> 00:09:46.165
of our country's history, I'm confident

228
00:09:46.165 --> 00:09:47.605
that our students are prepared to be the leaders

229
00:09:47.605 --> 00:09:50.045
of tomorrow, no matter the elections outcome.

230
00:09:50.425 --> 00:09:52.525
And with that, I wanna turn it back to Chair Faulkner

231
00:09:52.525 --> 00:09:53.765
so we can proceed with the meetings.

232
00:09:55.095 --> 00:09:58.195
You know, um, this is really a lot of events, a lot

233
00:09:58.195 --> 00:10:00.155
of activity, um, hitting the ground running.

234
00:10:00.255 --> 00:10:03.795
But I I also wanted to reference, um, civics for all.

235
00:10:03.795 --> 00:10:05.755
You know, we've been expanding the Civics for All program,

236
00:10:06.335 --> 00:10:08.995
and you made reference to Isaac, the young man who

237
00:10:09.555 --> 00:10:13.915
I believe collected 23,000 signatures to really force

238
00:10:14.295 --> 00:10:16.275
and suggest a change in the, um,

239
00:10:16.935 --> 00:10:18.835
and, uh, uh, on December 23rd.

240
00:10:18.895 --> 00:10:21.355
So I think that that speaks very well for

241
00:10:21.355 --> 00:10:22.435
what we're doing in our schools.

242
00:10:22.435 --> 00:10:24.195
It speaks weirdly well about civic engagement.

243
00:10:24.655 --> 00:10:27.235
And, um, I'd love for this young man to come to a panel

244
00:10:27.255 --> 00:10:29.795
and let's have us officially say something.

245
00:10:29.955 --> 00:10:32.475
'cause I think that was an amazing, uh, thing to have

246
00:10:32.495 --> 00:10:34.395
to see, you know, an eighth grader.

247
00:10:34.895 --> 00:10:36.875
Um, really, you know, a lot

248
00:10:36.875 --> 00:10:39.915
of adults sometimes we're reluctant to, to, uh,

249
00:10:40.055 --> 00:10:42.515
accept the challenges of, of, of seeing what we can do

250
00:10:42.515 --> 00:10:44.795
with our, um, leadership and experience.

251
00:10:44.795 --> 00:10:47.475
And so to see this happen from a young one

252
00:10:47.475 --> 00:10:49.555
of our students is like, extremely impressive.

253
00:10:49.595 --> 00:10:51.635
I think that was one of the best parts of the story for me,

254
00:10:51.865 --> 00:10:54.555
that this was a young, uh, one of our students who was able

255
00:10:54.555 --> 00:10:56.755
to, to get policy change.

256
00:10:56.755 --> 00:10:57.915
And I think that's really important.

257
00:10:58.535 --> 00:11:00.075
So, again, thank you Chancellor and,

258
00:11:00.135 --> 00:11:02.155
and, uh, you know, I look forward to this, uh,

259
00:11:02.685 --> 00:11:04.035
continuing collaboration.

260
00:11:05.275 --> 00:11:06.725
Okay, as we move now,

261
00:11:06.725 --> 00:11:07.925
we're gonna move into the business

262
00:11:07.925 --> 00:11:09.085
portion of tonight's meeting.

263
00:11:09.745 --> 00:11:12.685
Um, you know, again, I always wanna recognize the panel

264
00:11:12.685 --> 00:11:14.165
for the work that has been.

265
00:11:14.165 --> 00:11:15.365
It's been a busy few weeks,

266
00:11:15.365 --> 00:11:17.285
and I want to thank always the panel for the work that,

267
00:11:17.625 --> 00:11:18.805
uh, they've been engaged in.

268
00:11:18.865 --> 00:11:20.885
And, um, the meetings and the briefings

269
00:11:20.905 --> 00:11:23.965
and other things that, uh, have taken place over the course

270
00:11:23.985 --> 00:11:27.445
of the last, uh, month, um, leading up to tonight's meeting.

271
00:11:27.545 --> 00:11:29.605
So I just, again, want to acknowledge the work of the,

272
00:11:29.605 --> 00:11:30.725
uh, of the panel.

273
00:11:31.455 --> 00:11:33.355
Uh, with those special notes outta the way I'd like to move,

274
00:11:33.445 --> 00:11:36.875
we'll move into, um, the voting portion of meeting.

275
00:11:37.615 --> 00:11:41.085
Um, as we move into the business portion tonight, I want

276
00:11:41.085 --> 00:11:44.525
to let you know that, um, we'll be calling

277
00:11:44.625 --> 00:11:46.165
how we'll be calling people up to speak

278
00:11:46.665 --> 00:11:48.245
and, uh, what the rules of engagement

279
00:11:48.245 --> 00:11:49.285
will be during that time.

280
00:11:50.145 --> 00:11:54.325
Um, during the public comment period, everyone

281
00:11:54.325 --> 00:11:57.645
who is signs up to speak on specific agenda items will be

282
00:11:57.645 --> 00:11:59.045
allotted up to two and a half minutes.

283
00:11:59.865 --> 00:12:01.765
I'm gonna ask our secretary, secretary, Nathan,

284
00:12:01.865 --> 00:12:04.725
to please call forward speakers from the signup sheets

285
00:12:04.825 --> 00:12:07.005
and keep an eye on the clock to ensure

286
00:12:07.005 --> 00:12:09.165
that speakers finish their comments within

287
00:12:09.165 --> 00:12:10.285
the allotted time period.

288
00:12:10.815 --> 00:12:12.205
Additional time will be

289
00:12:12.445 --> 00:12:15.005
provided as necessary to help facilitate comments

290
00:12:15.035 --> 00:12:16.885
that may require additional translation.

291
00:12:17.735 --> 00:12:19.755
We will call speakers up in groups of five.

292
00:12:20.255 --> 00:12:22.275
The clock will also indicate the amount

293
00:12:22.275 --> 00:12:23.755
of time remaining for each speaker.

294
00:12:24.255 --> 00:12:26.755
And a light will flash when there is one minute remaining,

295
00:12:27.055 --> 00:12:29.795
so that speakers know when their time is running low.

296
00:12:30.455 --> 00:12:32.235
At the conclusion of each speaker's time,

297
00:12:32.615 --> 00:12:34.235
we will move on to the next speaker.

298
00:12:35.135 --> 00:12:38.155
If the speaker is not present when their name is called,

299
00:12:38.175 --> 00:12:39.555
we will move on to the next speaker.

300
00:12:40.185 --> 00:12:42.755
Once we've done that, that speaker will not be able

301
00:12:42.755 --> 00:12:44.115
to redeem their place in the queue.

302
00:12:45.055 --> 00:12:48.145
This portion of the public comment is only

303
00:12:48.145 --> 00:12:50.985
for agenda items being voted on at tonight's meeting.

304
00:12:51.685 --> 00:12:54.065
If you accidentally signed up to comment

305
00:12:54.125 --> 00:12:55.145
during this section,

306
00:12:55.645 --> 00:12:58.745
but wish to comment on other matters, please see one

307
00:12:58.745 --> 00:13:00.905
of our staff members stationed at the microphone

308
00:13:01.525 --> 00:13:05.265
who will move you to the open, uh, comment section.

309
00:13:05.955 --> 00:13:09.705
Again, comments during this section, um, should only relate

310
00:13:09.705 --> 00:13:11.425
to proposals being voted on at

311
00:13:11.425 --> 00:13:12.945
tonight's, uh, this evening's meeting.

312
00:13:16.035 --> 00:13:17.135
Um, do we have,

313
00:13:17.515 --> 00:13:19.375
we do have one student signed off as a student.

314
00:13:19.565 --> 00:13:21.975
Yeah. Okay. So as we've changed in the past,

315
00:13:22.115 --> 00:13:24.055
we have moved the student comment section

316
00:13:24.645 --> 00:13:25.735
forward in the meeting.

317
00:13:26.035 --> 00:13:27.055
Um, so I don't know if there have,

318
00:13:27.255 --> 00:13:28.855
have there any students who might have signed up?

319
00:13:28.855 --> 00:13:30.215
Mm-Hmm. Yeah. Um, to speak,

320
00:13:31.005 --> 00:13:33.465
Uh, one student signed up for the public comment.

321
00:13:34.095 --> 00:13:38.705
Lila Torres, you make your way down to the microphone.

322
00:13:41.855 --> 00:13:45.355
Is she here? I don't know. We can call her later again.

323
00:13:49.675 --> 00:13:50.885
Okay. If she's not here now, we'll,

324
00:13:50.885 --> 00:13:52.045
uh, we'll call her again.

325
00:13:52.215 --> 00:13:53.445
We'll give her an opportunity to speak,

326
00:13:53.465 --> 00:13:54.565
uh, later on during the meeting.

327
00:13:54.675 --> 00:13:56.085
Yeah, I do wanna note that, um,

328
00:13:57.395 --> 00:13:58.725
Tang has arrived at the meeting.

329
00:13:59.565 --> 00:14:03.115
Okay, great. Thank you. Thanks. Okay.

330
00:14:03.115 --> 00:14:05.595
The first voting item on tonight's agenda, uh,

331
00:14:05.595 --> 00:14:07.595
this evening will be the consideration of contracts.

332
00:14:09.645 --> 00:14:11.325
Secretary Nation, could you please introduce the

333
00:14:11.485 --> 00:14:12.565
resolution to the panel

334
00:14:14.285 --> 00:14:15.285
Panel? Uh, yes. The

335
00:14:15.285 --> 00:14:16.075
resolution up

336
00:14:16.075 --> 00:14:17.995
for approval is entitled Resolution

337
00:14:18.055 --> 00:14:21.475
to Authorize Entry into Contracts, which Consists

338
00:14:21.475 --> 00:14:24.235
of Contract Agenda Items two through 18.

339
00:14:26.065 --> 00:14:28.795
Okay. Is there a motion to consider resolution

340
00:14:28.815 --> 00:14:30.715
to authorize entry into contracts?

341
00:14:30.935 --> 00:14:34.135
Is there a motion? Is there a second?

342
00:14:35.095 --> 00:14:36.135
I, okay.

343
00:14:36.135 --> 00:14:37.895
We will now move into public comment

344
00:14:38.005 --> 00:14:40.095
regarding the post, uh, resolution.

345
00:14:40.635 --> 00:14:43.455
Please note that this portion of the public comment is only

346
00:14:43.835 --> 00:14:45.775
for contract items being voted on at

347
00:14:45.775 --> 00:14:46.935
tonight's panel meeting.

348
00:14:47.595 --> 00:14:49.015
If you, again, accidentally signed up

349
00:14:49.015 --> 00:14:52.325
to speak on something else, uh, we be able to move you

350
00:14:52.325 --> 00:14:54.165
to a later, uh, section of the meeting.

351
00:14:54.905 --> 00:14:56.325
Um, so Secretary Nathan?

352
00:14:56.745 --> 00:14:58.845
Yes. I'll call five speakers at a time.

353
00:14:59.585 --> 00:15:01.965
Uh, David d Gamma,

354
00:15:02.145 --> 00:15:04.045
and excuse me if I mispronounce your name.

355
00:15:04.895 --> 00:15:08.395
Emily Haynes. Elona Nae,

356
00:15:10.085 --> 00:15:13.745
Kamala Carmen and Ra Salas.

357
00:15:15.345 --> 00:15:16.485
And when you get to the microphone,

358
00:15:16.485 --> 00:15:18.885
just also state your name since I've called a number

359
00:15:18.885 --> 00:15:20.445
of speakers at a time. Yeah. Sorry,

360
00:15:20.445 --> 00:15:21.445
David. Uh, but

361
00:15:21.445 --> 00:15:22.525
I was wondering if I could skip,

362
00:15:22.665 --> 00:15:24.085
can you bump yourself down or

363
00:15:24.085 --> 00:15:25.085
No? Do you wanna just

364
00:15:25.085 --> 00:15:26.245
talk into the public comment?

365
00:15:26.425 --> 00:15:29.605
Not on the contract? Yeah. Okay. Thank you.

366
00:15:34.575 --> 00:15:37.365
Hello. Um, I'll take off my mask to

367
00:15:37.365 --> 00:15:38.205
Speak. Thank you.

368
00:15:38.705 --> 00:15:41.615
Um, my name's Kamala Carmen.

369
00:15:42.215 --> 00:15:43.495
I am a co-founder

370
00:15:43.715 --> 00:15:46.455
and a steering committee member of NYC optout.

371
00:15:46.955 --> 00:15:50.265
Um, and, um, when the

372
00:15:51.355 --> 00:15:56.195
periodic assessments were, um, introduced at the tail end

373
00:15:56.195 --> 00:16:00.275
of the de Blassio administration, um, we, um,

374
00:16:00.785 --> 00:16:04.635
were skeptical of these from, from having heard about MAP

375
00:16:04.695 --> 00:16:07.035
and, and, and the other assessments, um,

376
00:16:07.625 --> 00:16:11.295
that were already being administered around the country, um,

377
00:16:11.295 --> 00:16:13.735
country, and did not have, uh, good reception.

378
00:16:14.515 --> 00:16:15.535
Um, so shortly

379
00:16:15.585 --> 00:16:19.415
after they were administered for the first time, we, uh,

380
00:16:19.415 --> 00:16:24.255
created a, a educator survey, um, where over a hundred,

381
00:16:24.955 --> 00:16:27.375
uh, educators responded to this survey

382
00:16:28.105 --> 00:16:29.855
about the periodic assessments.

383
00:16:30.055 --> 00:16:32.415
And I'm just gonna read to you some of the findings of

384
00:16:32.415 --> 00:16:37.295
that survey to show that spending $15 million

385
00:16:37.995 --> 00:16:41.665
on these periodic assessments is insanity.

386
00:16:42.205 --> 00:16:44.785
And it's, um, I, I really urge you

387
00:16:44.785 --> 00:16:45.865
to spend our money better.

388
00:16:46.645 --> 00:16:50.415
Um, so here's, here's some, uh, some

389
00:16:50.415 --> 00:16:53.935
of the things the assessments are no better at identifying

390
00:16:54.135 --> 00:16:55.695
students who need support than

391
00:16:55.695 --> 00:16:57.775
where the methods teachers were already using.

392
00:16:58.515 --> 00:17:00.535
As this was purportedly a major reason

393
00:17:00.595 --> 00:17:01.615
for purchasing the test.

394
00:17:01.715 --> 00:17:03.775
It points to a major failure of purpose.

395
00:17:04.795 --> 00:17:07.505
Among, um, 109 survey respondents.

396
00:17:07.505 --> 00:17:10.665
Only 2% agreed with the statement quote,

397
00:17:10.885 --> 00:17:13.705
the assessment data recently collected identified students

398
00:17:13.725 --> 00:17:15.585
who need support, who had not been

399
00:17:15.865 --> 00:17:17.025
identified through other means.

400
00:17:17.985 --> 00:17:20.225
A literacy coach, um, said, quote,

401
00:17:20.225 --> 00:17:22.305
these screeners are insanely time consuming

402
00:17:22.445 --> 00:17:24.785
and did not identify any students who were struggling,

403
00:17:24.785 --> 00:17:27.705
who had not already been identified using school-based data.

404
00:17:28.175 --> 00:17:30.425
This educator had spent more than 14 hours

405
00:17:30.945 --> 00:17:33.185
training administrating and re administering

406
00:17:33.185 --> 00:17:34.865
and reading reports from the screeners.

407
00:17:35.375 --> 00:17:36.425
So-called screeners,

408
00:17:36.465 --> 00:17:38.145
I would say they're just standardized tests, really.

409
00:17:38.725 --> 00:17:41.025
Um, a high school teacher at a school for new immigrants.

410
00:17:41.325 --> 00:17:43.265
The majority, our students are ls,

411
00:17:43.265 --> 00:17:44.665
both in English and math test.

412
00:17:44.665 --> 00:17:46.905
Were administered in English way above their English level.

413
00:17:47.245 --> 00:17:49.925
I'm not sure how useful the data is since the language

414
00:17:49.925 --> 00:17:52.205
barrier means the test may not have actually been measuring

415
00:17:52.205 --> 00:17:55.465
the skills they were designed to measure another teacher.

416
00:17:55.605 --> 00:17:56.945
The question, the test questions

417
00:17:56.945 --> 00:17:58.865
that I saw were too narrow in scope

418
00:17:59.085 --> 00:18:00.745
and did not represent skills that are

419
00:18:00.745 --> 00:18:02.145
of value in measuring a student's

420
00:18:02.145 --> 00:18:03.265
reading and writing potential.

421
00:18:03.445 --> 00:18:06.065
The subsequent results provided zero resources

422
00:18:06.065 --> 00:18:07.225
for improving student skills,

423
00:18:07.485 --> 00:18:10.225
and the lexel reading scores seem wildly off based on

424
00:18:10.465 --> 00:18:12.225
demonstrations of skills that I have seen from students

425
00:18:12.225 --> 00:18:14.265
outside of the testing experience. Thank

426
00:18:14.265 --> 00:18:15.265
You.

427
00:18:19.425 --> 00:18:21.715
Good evening. I'm Emily Haynes, uh,

428
00:18:21.855 --> 00:18:23.115
New York City Public School teacher.

429
00:18:23.185 --> 00:18:25.915
I've been teaching in public schools for the last 27 years,

430
00:18:26.055 --> 00:18:28.715
and I believe that New York City teachers are New York

431
00:18:28.735 --> 00:18:30.035
City's most passionate.

432
00:18:30.475 --> 00:18:32.275
I became a teacher because I grew up in the

433
00:18:32.275 --> 00:18:33.475
Bronx in public schools.

434
00:18:33.855 --> 00:18:35.595
And my life's work is to make sure

435
00:18:35.595 --> 00:18:37.555
that we meet every student where they are

436
00:18:37.855 --> 00:18:39.875
and help them achieve their highest goals

437
00:18:39.975 --> 00:18:41.115
and biggest dreams.

438
00:18:41.655 --> 00:18:44.355
And in doing that, over the last 27 years, I've learned

439
00:18:44.355 --> 00:18:46.995
that there is no contracts, no app, no curriculum,

440
00:18:47.215 --> 00:18:49.355
no assessment that can do this work,

441
00:18:49.655 --> 00:18:52.195
but the most passionate, dedicated teachers can.

442
00:18:52.575 --> 00:18:55.795
The amount of teaching time we are losing to assessments

443
00:18:56.335 --> 00:18:59.395
is another injustice that is being done to our students.

444
00:18:59.935 --> 00:19:02.355
Our students are snowflakes.

445
00:19:02.575 --> 00:19:05.555
And the only people that can measure and love

446
00:19:05.655 --> 00:19:07.555
and identify the strengths

447
00:19:07.555 --> 00:19:09.995
and needs of those students are the teachers.

448
00:19:10.515 --> 00:19:14.635
I can tell you that we now spend three class periods three

449
00:19:14.635 --> 00:19:19.155
times a year on these, uh, uh, assessments.

450
00:19:19.295 --> 00:19:22.355
The periodic assessments, plus eight entire school days,

451
00:19:22.445 --> 00:19:25.915
eight entire school days on mock state exams,

452
00:19:26.385 --> 00:19:29.595
plus the four days on the actual state exams.

453
00:19:29.785 --> 00:19:33.315
Plus, with the new imposed mandated curriculum from

454
00:19:33.325 --> 00:19:35.555
above every single unit, we have

455
00:19:35.555 --> 00:19:38.835
to spend three class periods on mid-unit assessments

456
00:19:39.015 --> 00:19:40.915
and three on end of unit assessments.

457
00:19:40.915 --> 00:19:45.555
Which means that in some units, 40% of class time is going

458
00:19:45.615 --> 00:19:47.115
to assessing our students.

459
00:19:47.375 --> 00:19:49.275
Please let us teach our students.

460
00:19:49.895 --> 00:19:52.395
We know our students, we love our students,

461
00:19:52.735 --> 00:19:53.955
we believe in our students.

462
00:19:54.575 --> 00:19:57.915
But when we have to assess our students constantly, I agree

463
00:19:57.915 --> 00:19:59.555
with you a hundred percent chancellor.

464
00:19:59.775 --> 00:20:01.555
We want students, we want schools

465
00:20:01.905 --> 00:20:05.155
that are every single parent's first choice.

466
00:20:05.895 --> 00:20:07.275
And we want safe schools.

467
00:20:07.455 --> 00:20:10.595
Our students don't feel safe when we are putting something

468
00:20:10.595 --> 00:20:13.675
in front of them and making them sit still for hours

469
00:20:14.065 --> 00:20:17.515
that we did not create and is not going to help us.

470
00:20:17.745 --> 00:20:19.875
That does not make our students wanna come to school.

471
00:20:19.935 --> 00:20:22.315
It does not make us as teachers come to school.

472
00:20:22.995 --> 00:20:26.075
I am coaching teachers who are now telling me that

473
00:20:26.075 --> 00:20:28.755
after years in the classroom, they are miserable.

474
00:20:28.815 --> 00:20:31.275
Coming to school, they're miserable.

475
00:20:31.395 --> 00:20:34.035
I had a teacher, a first year teacher, who was a para

476
00:20:34.135 --> 00:20:37.835
for 20 years, an excellent expert educator

477
00:20:37.975 --> 00:20:40.795
who can teach any kid you put in front of him

478
00:20:41.095 --> 00:20:43.195
who can diagnose and assess and teach.

479
00:20:43.455 --> 00:20:46.035
Any single kid tell me he was gonna become a school

480
00:20:46.395 --> 00:20:47.925
custodian today

481
00:20:48.945 --> 00:20:52.355
because he can't deal with these impositions.

482
00:20:52.935 --> 00:20:54.765
Thank you. Thank you.

483
00:21:00.265 --> 00:21:03.435
Good evening everyone. Dr. kli Sala Ramirez.

484
00:21:03.735 --> 00:21:06.315
I'm a parent in both District four and the consortium.

485
00:21:06.895 --> 00:21:09.795
Um, I also wanna talk a little bit about these assessments.

486
00:21:10.095 --> 00:21:12.555
Um, when I was your colleague at that table,

487
00:21:13.115 --> 00:21:15.275
I spoke a lot about the importance

488
00:21:15.275 --> 00:21:17.915
of having culturally responsive education as well

489
00:21:17.915 --> 00:21:20.315
as appropriate assessments for our students.

490
00:21:20.805 --> 00:21:24.115
These are $15 million that we're going to be committing

491
00:21:24.335 --> 00:21:26.955
to assessments that when I go visit schools in Manhattan,

492
00:21:27.505 --> 00:21:28.515
they tell me

493
00:21:28.545 --> 00:21:31.675
that teachers aren't really using the assessments

494
00:21:31.675 --> 00:21:33.475
and that it does not align

495
00:21:33.475 --> 00:21:35.395
with the curriculum that they are using.

496
00:21:36.175 --> 00:21:40.555
And so why are we investing this much money when we have

497
00:21:41.015 --> 00:21:44.235
the opportunity to put that money towards teacher training

498
00:21:44.255 --> 00:21:45.395
and teacher investment?

499
00:21:45.975 --> 00:21:48.555
And that's what we need to do right now, particularly

500
00:21:48.895 --> 00:21:51.315
as we have these rollouts of initiatives

501
00:21:51.585 --> 00:21:54.195
that are addressing some of the things that we needed

502
00:21:54.215 --> 00:21:57.155
to address historically, which again, is to support

503
00:21:57.745 --> 00:22:00.235
pedagogical practices that support student learning,

504
00:22:00.345 --> 00:22:02.635
like problem-based learning and inquiry-based learning.

505
00:22:02.895 --> 00:22:05.355
That's where we need to make our investments.

506
00:22:05.895 --> 00:22:07.715
We have professionals on the ground

507
00:22:08.105 --> 00:22:10.155
that have the ability to provide that.

508
00:22:10.535 --> 00:22:13.195
We don't have to pay for outside PD

509
00:22:13.305 --> 00:22:15.795
because we have our experts in our classrooms

510
00:22:16.295 --> 00:22:17.475
and we have the ability

511
00:22:17.535 --> 00:22:19.835
to engage our students in a comprehensive way.

512
00:22:20.015 --> 00:22:22.715
And if that weren't true, there wouldn't be an ability

513
00:22:22.855 --> 00:22:24.835
or a proposal that's moving forward

514
00:22:25.295 --> 00:22:27.995
to actually perform performance based assessments on our

515
00:22:27.995 --> 00:22:30.595
high school students for graduation requirements.

516
00:22:30.935 --> 00:22:33.875
So we continue to rely on standardized curriculum,

517
00:22:34.195 --> 00:22:36.115
standardized assessments when children

518
00:22:36.335 --> 00:22:38.075
and brains are not standardized.

519
00:22:38.935 --> 00:22:41.275
Um, so I wanna continue to lift that.

520
00:22:41.415 --> 00:22:45.275
We already spent $23 million on iReady.

521
00:22:45.605 --> 00:22:49.035
We're gonna go ahead and spend another $15 million on map

522
00:22:49.055 --> 00:22:51.195
and HMHI think we really need

523
00:22:51.195 --> 00:22:53.075
to question exactly what we're doing with this.

524
00:22:53.135 --> 00:22:56.155
And once again, I didn't see any data connected

525
00:22:56.175 --> 00:22:57.875
to the use of these instruments.

526
00:22:58.255 --> 00:23:01.635
Um, I I beg you to continue to ask for that data

527
00:23:01.735 --> 00:23:03.315
and that validity, um,

528
00:23:03.375 --> 00:23:05.515
to figure out which schools are the ones

529
00:23:05.515 --> 00:23:08.955
that are using these instruments effectively, if at all.

530
00:23:09.335 --> 00:23:11.475
Um, because a lot of the people on the ground,

531
00:23:11.475 --> 00:23:13.395
including principals, are saying

532
00:23:13.395 --> 00:23:15.755
that they already have authentic assessments

533
00:23:15.755 --> 00:23:17.835
that help them understand where children need to go.

534
00:23:18.415 --> 00:23:22.155
Um, I do also support the special education enhancement,

535
00:23:22.155 --> 00:23:24.515
particularly in, in early childhood education.

536
00:23:24.515 --> 00:23:25.515
And we need to continue

537
00:23:25.515 --> 00:23:28.235
to support our early childhood learners, um,

538
00:23:28.255 --> 00:23:30.075
and stop piecemealing these contracts.

539
00:23:30.075 --> 00:23:31.075
Thank you.

540
00:23:36.345 --> 00:23:39.695
Thank you. Uh, Alona a high school teacher in the Bronx.

541
00:23:39.995 --> 00:23:43.845
Um, It is incredibly frustrating

542
00:23:43.845 --> 00:23:46.765
to see a $15 million contract at the same time

543
00:23:46.765 --> 00:23:48.405
that schools budgets are being cut

544
00:23:48.425 --> 00:23:50.165
and schools can't afford copies.

545
00:23:50.545 --> 00:23:51.805
And long-term subs

546
00:23:51.825 --> 00:23:54.285
or paraprofessionals an assessment

547
00:23:54.675 --> 00:23:57.165
that does not actually assess the things

548
00:23:57.165 --> 00:24:00.725
that we state is assess the things that we state it assesses

549
00:24:01.705 --> 00:24:04.045
is make and make sense.

550
00:24:04.045 --> 00:24:05.365
These are supposed to be screeners.

551
00:24:05.395 --> 00:24:07.605
Screeners should take no more than 20 minutes.

552
00:24:07.785 --> 00:24:10.205
The fact that we're forcing kids to sit eight hours

553
00:24:10.305 --> 00:24:12.445
to take this exam, that then tries

554
00:24:12.445 --> 00:24:15.005
to group them into lifestyle and grade bands.

555
00:24:15.275 --> 00:24:17.605
When if we're trying to screen for reading comprehension,

556
00:24:17.635 --> 00:24:20.245
what would be much more helpful is if it actually broke down

557
00:24:20.245 --> 00:24:22.325
the reading skills that these students need.

558
00:24:22.705 --> 00:24:24.485
But the screener is, this screener in

559
00:24:24.485 --> 00:24:26.045
particular does not do that.

560
00:24:26.145 --> 00:24:28.325
It was not designed to screen students for this.

561
00:24:28.665 --> 00:24:32.085
So then you have to test kids with two additional tests

562
00:24:32.225 --> 00:24:35.165
to try and diagnose exactly what their reading needs are.

563
00:24:35.505 --> 00:24:37.765
So now all you're doing is testing, testing, testing,

564
00:24:37.985 --> 00:24:39.405
and kids don't actually have time

565
00:24:39.745 --> 00:24:41.365
to get the supports that they need.

566
00:24:42.245 --> 00:24:43.285
Additionally, as teachers,

567
00:24:43.425 --> 00:24:45.245
we don't get access to their test scores.

568
00:24:45.625 --> 00:24:46.965
So you're having these screeners

569
00:24:47.065 --> 00:24:48.605
and the teachers don't ever get

570
00:24:48.605 --> 00:24:50.605
to see the data from these screeners.

571
00:24:50.865 --> 00:24:53.485
So we can't use it to actually inform our lesson

572
00:24:53.545 --> 00:24:54.645
and our curriculum planning.

573
00:24:55.025 --> 00:24:57.165
And then lastly, it is really frightening

574
00:24:57.165 --> 00:24:59.005
that this is the screener we're purchasing.

575
00:24:59.425 --> 00:25:01.725
Uh, at the same time as we're giving millions of dollars

576
00:25:01.785 --> 00:25:04.965
to H-M-H-H-M-H has now purchased this screener.

577
00:25:04.985 --> 00:25:06.885
And it, I can't help

578
00:25:06.905 --> 00:25:09.845
but think this is one way that we're really contributing

579
00:25:09.845 --> 00:25:12.085
to the privatization of public education.

580
00:25:12.505 --> 00:25:14.525
We continue to seek and look outwards

581
00:25:14.525 --> 00:25:16.445
and pay these venture capitalists.

582
00:25:16.965 --> 00:25:20.285
Veritas Capital has bought up HMH and NWEA

583
00:25:20.545 --> 00:25:23.125
and now is bundling it into this one contract.

584
00:25:23.465 --> 00:25:25.885
Um, and we continue giving these mon people money

585
00:25:26.345 --> 00:25:28.285
to profit off of our children, um,

586
00:25:28.285 --> 00:25:30.125
when we have the expertise in-house.

587
00:25:30.305 --> 00:25:33.645
Um, so I really urge you all not to pass this contract.

588
00:25:33.825 --> 00:25:37.365
Um, and instead to give schools that $15 million so

589
00:25:37.365 --> 00:25:39.165
that they can pay for their copies

590
00:25:39.665 --> 00:25:42.605
and pay for long-term subs, pay for paraprofessionals,

591
00:25:42.705 --> 00:25:43.845
and hire more staff.

592
00:25:43.975 --> 00:25:44.975
Thank you.

593
00:25:46.005 --> 00:25:50.625
Thank you. Um, uh, chancellor Ram would like to comment.

594
00:25:51.625 --> 00:25:53.295
Thank you. I'll, I'll start.

595
00:25:53.355 --> 00:25:56.855
And then, uh, I'm going to ask, uh, my colleague to jump in

596
00:25:56.995 --> 00:25:59.495
and, uh, speak to school budget cuts.

597
00:25:59.835 --> 00:26:02.015
So first of all, I wanna thank you so much

598
00:26:02.115 --> 00:26:04.935
for your comments, um, on assessment, your insight,

599
00:26:04.935 --> 00:26:05.935
deeply appreciated.

600
00:26:06.475 --> 00:26:09.615
And we are going to set up opportunities

601
00:26:09.795 --> 00:26:12.415
to hear directly from teachers and administrators

602
00:26:12.415 --> 00:26:15.935
and parents regarding assessment practices, particularly,

603
00:26:16.395 --> 00:26:18.215
uh, what we do with data.

604
00:26:18.395 --> 00:26:20.655
So I would just wanna thank you and say that you were heard

605
00:26:20.875 --> 00:26:22.135
and we appreciate your comment

606
00:26:22.965 --> 00:26:26.025
and, uh, if we can have the school budget cuts addressed.

607
00:26:30.335 --> 00:26:30.765
Thank you.

608
00:26:35.645 --> 00:26:38.605
I know chancellor's working.

609
00:26:38.815 --> 00:26:40.365
Thank you, chancellor. Thank you panel.

610
00:26:40.535 --> 00:26:44.415
Thank you very much for the, for the comment as well.

611
00:26:44.715 --> 00:26:48.855
Um, appreciate it and appreciate the intent.

612
00:26:49.035 --> 00:26:52.655
So, um, look, we always wanna be putting as much

613
00:26:52.655 --> 00:26:55.055
of our money as we can into our schools.

614
00:26:55.675 --> 00:26:58.215
Um, even as the city's gone through a couple of rounds

615
00:26:58.275 --> 00:26:59.335
of tight budgets,

616
00:26:59.335 --> 00:27:00.855
and we've had to look at ways to

617
00:27:01.595 --> 00:27:04.855
reduce our budget overall at New York City Public Schools,

618
00:27:05.545 --> 00:27:08.055
we've actually increased our spending in schools

619
00:27:08.085 --> 00:27:09.215
over the past few years.

620
00:27:09.495 --> 00:27:12.095
I realize at the school level there's always more needs

621
00:27:12.155 --> 00:27:14.175
and always more we wanna do for our kids.

622
00:27:14.635 --> 00:27:16.495
But actually as we look over the past few years,

623
00:27:16.785 --> 00:27:20.015
we've increased spending across New York City public schools

624
00:27:20.675 --> 00:27:22.055
by over a billion dollars.

625
00:27:22.515 --> 00:27:24.975
We put in additional money through fair student funding,

626
00:27:25.415 --> 00:27:27.455
specifically for students in temporary housing,

627
00:27:27.765 --> 00:27:29.855
including all of our asylum seeking students.

628
00:27:30.355 --> 00:27:33.695
We put in additional dollars for class size in particular,

629
00:27:34.185 --> 00:27:36.655
we've put in additional dollars for teachers

630
00:27:36.675 --> 00:27:39.255
and principals as we've reached new collective bargaining

631
00:27:39.255 --> 00:27:41.095
agreements and the salaries they need

632
00:27:41.095 --> 00:27:42.575
and deserve so they can continue

633
00:27:42.575 --> 00:27:44.095
to live here and support our students.

634
00:27:44.795 --> 00:27:47.655
Um, and we've also been able to put in additional dollars

635
00:27:47.875 --> 00:27:49.695
to backstop a number

636
00:27:49.695 --> 00:27:52.175
of those stimulus programs like community schools,

637
00:27:52.325 --> 00:27:54.615
like Summer Rising, all of these programs

638
00:27:54.615 --> 00:27:57.775
that were really built on disappearing money that we thought

639
00:27:57.875 --> 00:27:59.095
as we as a city and

640
00:27:59.095 --> 00:28:01.215
with the council thought were really important to maintain.

641
00:28:01.675 --> 00:28:03.975
So over the past few years, I know it's always tough,

642
00:28:03.975 --> 00:28:05.215
but we have actually managed

643
00:28:05.215 --> 00:28:07.175
to increase funding into school budgets.

644
00:28:07.595 --> 00:28:09.455
Um, we also held schools harmless

645
00:28:09.455 --> 00:28:10.575
at the beginning of this year.

646
00:28:10.665 --> 00:28:11.935
We'll continue to fight for more.

647
00:28:12.245 --> 00:28:14.975
I'll also chancellor, if it's okay, just use this as

648
00:28:15.495 --> 00:28:16.895
a moment to, to note.

649
00:28:16.955 --> 00:28:20.055
As some of you know, there's a way bigger conversation going

650
00:28:20.155 --> 00:28:23.895
on about funding for schools in New York State right now.

651
00:28:24.395 --> 00:28:27.615
Um, the state, which is a big contributor to our budget,

652
00:28:27.615 --> 00:28:29.175
gives us about $10 billion.

653
00:28:29.715 --> 00:28:33.695
Um, just in one formula, the state is considering how

654
00:28:33.695 --> 00:28:36.775
to change how it funds all the schools in New York State.

655
00:28:37.115 --> 00:28:38.935
That's something the state hasn't actually

656
00:28:39.005 --> 00:28:40.295
done in a couple of decades.

657
00:28:40.955 --> 00:28:43.015
And the formula is way out of date

658
00:28:43.075 --> 00:28:46.455
and frankly doesn't take into account the needs of our kids.

659
00:28:46.595 --> 00:28:48.615
It doesn't fund our students in temporary housing,

660
00:28:48.925 --> 00:28:51.575
doesn't adequately fund our students with disabilities,

661
00:28:51.575 --> 00:28:54.415
or our English learners doesn't differentiate funding

662
00:28:54.475 --> 00:28:57.415
for those students based on their specific needs.

663
00:28:58.075 --> 00:29:00.175
Um, doesn't adequately look at the fact

664
00:29:00.175 --> 00:29:02.295
that things cost more in New York City

665
00:29:02.715 --> 00:29:04.575
as it looks at the dollars we get

666
00:29:04.875 --> 00:29:07.055
and doesn't provide additional money for the class size law.

667
00:29:07.055 --> 00:29:08.695
So, um, I'm happy to talk more about this,

668
00:29:08.695 --> 00:29:10.535
but I say this in part to say this is a fight

669
00:29:10.535 --> 00:29:12.415
that's gonna be going on in Albany.

670
00:29:12.565 --> 00:29:14.055
It's already going on in Albany.

671
00:29:14.075 --> 00:29:16.375
We expect the governor to put some changes in her

672
00:29:16.375 --> 00:29:17.575
budget early next year.

673
00:29:18.075 --> 00:29:20.175
Um, and we really hope we can all work together

674
00:29:20.275 --> 00:29:21.615
as a city, as a community.

675
00:29:21.615 --> 00:29:24.415
We've been working with advocates in the unions to continue

676
00:29:24.415 --> 00:29:26.455
to fight for more funding for New York City schools at this

677
00:29:26.455 --> 00:29:29.015
state level as well, uh, to support some of these programs.

678
00:29:29.225 --> 00:29:30.225
Thank you.

679
00:29:33.345 --> 00:29:34.255
Thank you. Is anyone,

680
00:29:34.615 --> 00:29:35.695
I have additional, additional comments.

681
00:29:35.695 --> 00:29:36.655
This is comments. Okay.

682
00:29:41.385 --> 00:29:42.325
No. Okay. No, we

683
00:29:42.325 --> 00:29:43.325
Can. Okay. I

684
00:29:43.325 --> 00:29:45.725
will call the, um, next group of speakers, um,

685
00:29:45.875 --> 00:29:50.045
that is Martina Meyer, Johanna Bjork

686
00:29:50.545 --> 00:29:52.125
and Lupe Hernandez.

687
00:29:52.705 --> 00:29:54.565
And while they're working their way down,

688
00:29:54.725 --> 00:29:55.885
I do wanna note we're joined

689
00:29:55.885 --> 00:29:57.645
by two more members of the panel.

690
00:29:58.025 --> 00:30:00.205
Um, Tony Giordano

691
00:30:00.745 --> 00:30:04.005
and Rema G***o are present at this time.

692
00:30:10.335 --> 00:30:12.835
You can begin. Okay. Thank, can you hear me? Yeah.

693
00:30:13.085 --> 00:30:15.795
Thank you. Hi, my name is Martina Meyer

694
00:30:15.935 --> 00:30:18.475
and I am an employee of the Department of Education.

695
00:30:18.475 --> 00:30:21.035
But in speaking right now, as a member of the public,

696
00:30:21.195 --> 00:30:23.275
a taxpayer and a person who's concerned,

697
00:30:23.315 --> 00:30:24.955
I hope you can see our graveyard.

698
00:30:25.225 --> 00:30:27.075
This has to do with our concerns related

699
00:30:27.135 --> 00:30:28.715
to the ongoing assessments

700
00:30:28.715 --> 00:30:31.635
and the impacts of these, um, mandated curricula.

701
00:30:31.795 --> 00:30:34.555
I wanna speak first and foremost though, about the, um,

702
00:30:34.625 --> 00:30:37.635
desktop and mobile computers, uh, contract item.

703
00:30:38.675 --> 00:30:40.535
I'm a former Walder teacher.

704
00:30:40.855 --> 00:30:42.375
I hope we know what Waldorf education is

705
00:30:42.375 --> 00:30:43.735
and Montessori education and not

706
00:30:43.735 --> 00:30:45.215
different philosophies of education.

707
00:30:45.275 --> 00:30:47.375
So I'm a former welder teacher, welder trained,

708
00:30:47.395 --> 00:30:49.415
and I'm also a graduate of welder schools.

709
00:30:49.875 --> 00:30:51.575
And, um, for those of you who don't know,

710
00:30:51.575 --> 00:30:53.695
there's not an obsession with technology at those schools.

711
00:30:53.875 --> 00:30:55.335
And those kids learn how to read.

712
00:30:55.795 --> 00:30:57.895
Um, the obsession with technology is a sad

713
00:30:57.895 --> 00:31:00.015
and dangerous trend that I see across public schools.

714
00:31:00.345 --> 00:31:02.375
We've gotten rid of our technology teachers,

715
00:31:02.375 --> 00:31:04.535
nobody's teaching children how to use these devices,

716
00:31:04.875 --> 00:31:06.975
but it's just being expected that they know how to type,

717
00:31:06.975 --> 00:31:08.015
they know how to double click.

718
00:31:08.045 --> 00:31:09.175
They know how to right click.

719
00:31:09.305 --> 00:31:10.815
There is no computer literacy

720
00:31:10.815 --> 00:31:12.975
that's being like, uh, examined.

721
00:31:13.235 --> 00:31:15.295
But also, I hope this body doesn't think

722
00:31:15.295 --> 00:31:18.175
that we should be like, progressing toward a room

723
00:31:18.195 --> 00:31:19.895
of children learning on laptops.

724
00:31:19.965 --> 00:31:21.735
Like that's not what great education is.

725
00:31:22.275 --> 00:31:24.015
We have the largest school system in the country,

726
00:31:24.195 --> 00:31:27.215
and these contracts that we're making have global impact

727
00:31:27.565 --> 00:31:29.175
through purchasing these cheap,

728
00:31:29.555 --> 00:31:32.135
low quality disposable Chromebook devices.

729
00:31:32.285 --> 00:31:35.415
Year after year indefinitely, we are

730
00:31:36.295 --> 00:31:38.575
directly perpetuating the ongoing genocide

731
00:31:38.635 --> 00:31:41.295
and forced child labor in cobalt mines in the Congo.

732
00:31:41.875 --> 00:31:44.095
Our purchases have direct impacts.

733
00:31:44.195 --> 00:31:47.375
And I think this outfit is not an exaggeration.

734
00:31:47.375 --> 00:31:50.135
Like we are directly responsible for the continued death

735
00:31:50.515 --> 00:31:54.815
and genocide of children, of, of human beings inside

736
00:31:54.875 --> 00:31:56.015
of cobalt minds.

737
00:31:56.315 --> 00:31:58.255
And it's all because we wanna have, make sure

738
00:31:58.255 --> 00:31:59.375
that we have these really cheap

739
00:31:59.485 --> 00:32:00.655
laptops in everybody's hands.

740
00:32:02.755 --> 00:32:04.055
I'm taking a moment to just honor

741
00:32:04.115 --> 00:32:05.295
the, the lives of those children.

742
00:32:06.405 --> 00:32:08.585
How can we in good conscious spend our money this way?

743
00:32:09.125 --> 00:32:12.065
Why are these devices designed with built in death dates?

744
00:32:12.655 --> 00:32:14.825
This is incredibly wasteful and irresponsible.

745
00:32:15.205 --> 00:32:18.225
We should be using the weight of these contracts, the weight

746
00:32:18.245 --> 00:32:21.385
of our power as the largest school system in the country,

747
00:32:21.725 --> 00:32:23.945
to demand longer lifespan for each device,

748
00:32:24.165 --> 00:32:25.265
and a more comprehensive

749
00:32:25.445 --> 00:32:27.705
and internalized plan for maintaining

750
00:32:27.705 --> 00:32:28.785
and supporting these devices.

751
00:32:29.205 --> 00:32:31.465
It pains me to see that we are continuing

752
00:32:31.465 --> 00:32:34.225
to purchase ad nausea, these replacement

753
00:32:34.405 --> 00:32:35.945
and very disposable devices.

754
00:32:36.665 --> 00:32:38.545
I agree with everything that was previously stated about

755
00:32:38.545 --> 00:32:39.580
the periodic assessment.

756
00:32:40.005 --> 00:32:42.085
I teach students who are dual language learners.

757
00:32:42.245 --> 00:32:43.445
I have a lot of newcomers

758
00:32:43.665 --> 00:32:45.845
and they had to take a lot of assessments in English.

759
00:32:46.445 --> 00:32:49.085
I don't understand why we are assessing children in

760
00:32:49.085 --> 00:32:50.245
a language that they don't speak.

761
00:32:50.425 --> 00:32:51.965
It doesn't gimme any additional information,

762
00:32:51.965 --> 00:32:53.205
and it takes away from my ability

763
00:32:53.205 --> 00:32:54.525
to give them the instruction that they need.

764
00:32:55.335 --> 00:32:55.765
Thank you.

765
00:33:03.005 --> 00:33:05.085
I, uh, my name is Johanna Bjork.

766
00:33:05.725 --> 00:33:09.805
I am the parent of a 10th grader at, uh,

767
00:33:10.585 --> 00:33:12.765
uh, high school, just down the street from here

768
00:33:12.865 --> 00:33:14.045
in the Murray Bergstrom building.

769
00:33:14.705 --> 00:33:17.125
Um, and I really hope chancellor, that when you say

770
00:33:17.125 --> 00:33:18.365
that you wanna hear from parents that,

771
00:33:18.365 --> 00:33:21.925
you mean parents like me, parents who elected

772
00:33:21.985 --> 00:33:25.725
to send their child to a school that is not screened, um,

773
00:33:26.145 --> 00:33:29.845
who want their child to have a, an educational experience

774
00:33:29.845 --> 00:33:32.565
with students of diverse types of academic learners.

775
00:33:32.755 --> 00:33:36.645
Because I feel like in the past few, few years,

776
00:33:36.905 --> 00:33:38.525
the emphasis has gone the other direction.

777
00:33:38.585 --> 00:33:40.605
But this is, is about contracts

778
00:33:40.865 --> 00:33:42.525
and it is about the assessments.

779
00:33:43.165 --> 00:33:47.485
I, as a parent, I have received the scores.

780
00:33:47.675 --> 00:33:49.725
I've been looked to see what the assessments are

781
00:33:49.725 --> 00:33:50.845
and how my child did.

782
00:33:51.075 --> 00:33:53.525
It's meaningless. It gives me no information.

783
00:33:53.845 --> 00:33:55.285
I wanna know if my child is doing well

784
00:33:55.285 --> 00:33:56.965
and I only see a score that says he's,

785
00:33:57.345 --> 00:33:59.325
his math is at a 12th grade level.

786
00:33:59.395 --> 00:34:00.405
Well, what does that mean?

787
00:34:01.005 --> 00:34:03.365
I have to talk to the teacher to understand what he,

788
00:34:03.365 --> 00:34:05.285
where he struggles, where he doesn't,

789
00:34:05.285 --> 00:34:07.605
and then learn, well, actually this is really not very

790
00:34:07.605 --> 00:34:09.485
meaningful because it, it isn't measuring

791
00:34:09.485 --> 00:34:11.085
or aligned with the curriculum whatsoever.

792
00:34:11.505 --> 00:34:13.525
And we're spending so much money on it.

793
00:34:13.785 --> 00:34:15.405
And yet it ends up being used

794
00:34:15.405 --> 00:34:19.405
to shame Schools like the school, my school child attends

795
00:34:19.665 --> 00:34:22.125
and elevate for reasons that have nothing to do

796
00:34:22.125 --> 00:34:23.525
with the instructional practices,

797
00:34:23.525 --> 00:34:25.765
but only have the re the, to do with the fact

798
00:34:25.765 --> 00:34:27.325
that schools handpick their students.

799
00:34:27.665 --> 00:34:29.685
The schools that do well on these assessments.

800
00:34:30.825 --> 00:34:33.825
I re I can't, I am a data person.

801
00:34:34.305 --> 00:34:37.505
I love spreadsheets more than probably anybody in this room.

802
00:34:38.125 --> 00:34:41.105
Um, I adore looking at data.

803
00:34:41.605 --> 00:34:44.625
Um, and I also work for the DOE.

804
00:34:44.625 --> 00:34:47.225
So I, I say this knowing I'm here as a parent,

805
00:34:47.325 --> 00:34:48.785
but I, I use this data.

806
00:34:48.965 --> 00:34:50.385
I'm, uh, one of my things I try

807
00:34:50.385 --> 00:34:53.025
to do is get this information to be useful to teachers

808
00:34:53.325 --> 00:34:54.745
and over and over

809
00:34:54.805 --> 00:34:57.985
and over again, it's banging my head against the wall

810
00:34:57.985 --> 00:34:59.105
because it doesn't tell them

811
00:34:59.545 --> 00:35:00.625
anything they don't already know.

812
00:35:01.005 --> 00:35:03.225
It doesn't come to them in a format that they can.

813
00:35:03.945 --> 00:35:05.545
Teaching is one of the few professions

814
00:35:05.795 --> 00:35:08.065
where you don't sit in front of a computer all day.

815
00:35:08.445 --> 00:35:10.385
And yet we're asking our teachers to try

816
00:35:10.385 --> 00:35:13.305
to digest this information, which doesn't come

817
00:35:13.465 --> 00:35:15.985
to them in any sort of way that relates whatsoever to

818
00:35:15.985 --> 00:35:17.105
what they're doing in the classroom.

819
00:35:17.365 --> 00:35:20.785
And we're gonna spend $50 million on it. It's crazy.

820
00:35:21.375 --> 00:35:25.225
It's meaningless. There's a saying, garbage in, garbage out.

821
00:35:25.485 --> 00:35:28.585
And that is 100% what I see with the map and acas.

822
00:35:31.515 --> 00:35:31.945
Thank you.

823
00:35:39.095 --> 00:35:41.305
Good evening. My name is Lupe Hernandez

824
00:35:41.325 --> 00:35:44.225
and I'm speaking this evening in my own personal capacity

825
00:35:44.225 --> 00:35:45.985
as a New York City public school parent.

826
00:35:47.165 --> 00:35:50.105
Um, I'll start off with just a couple favors

827
00:35:50.105 --> 00:35:52.545
of agenda items eight and five.

828
00:35:52.725 --> 00:35:57.025
That's the extension of, uh, multifunctional devices, um,

829
00:35:57.665 --> 00:35:59.985
notebooks and mobile computers for our students, as well

830
00:35:59.985 --> 00:36:02.585
as the enhancement of special education for early childhood.

831
00:36:03.645 --> 00:36:07.865
Um, also, yes, on agenda item number three, I wanna raise

832
00:36:08.125 --> 00:36:10.585
and highlight to you guys that older students

833
00:36:10.685 --> 00:36:12.265
who are not immediately college bound

834
00:36:12.265 --> 00:36:13.345
are not less important.

835
00:36:13.975 --> 00:36:17.665
They may be the ones to save us from staffing shortages

836
00:36:17.665 --> 00:36:19.265
that harm our younger students.

837
00:36:19.765 --> 00:36:22.305
In particular, these are high vacancies

838
00:36:22.305 --> 00:36:25.265
of school bus drivers, monitors, mechanics,

839
00:36:25.285 --> 00:36:26.665
paraprofessionals, positions

840
00:36:26.665 --> 00:36:28.745
that do not require a college degree,

841
00:36:29.085 --> 00:36:30.465
but are something to be proud of.

842
00:36:30.845 --> 00:36:33.985
The unstaffed bus routes are causing to absences

843
00:36:34.045 --> 00:36:35.345
for students from classes

844
00:36:35.965 --> 00:36:37.665
and therapies, related services,

845
00:36:37.945 --> 00:36:40.065
absences from parents that go to work.

846
00:36:40.255 --> 00:36:41.705
Many parents have lost their jobs.

847
00:36:42.845 --> 00:36:47.065
Um, in regard to item agenda number three, we would like

848
00:36:47.085 --> 00:36:48.865
to implore for DOE

849
00:36:48.885 --> 00:36:53.105
to actually look into PD involving helping CTE programs

850
00:36:53.105 --> 00:36:56.665
leaders and approach entities that hire for such positions

851
00:36:56.725 --> 00:36:58.905
and or with the state run and

852
00:36:58.925 --> 00:37:01.065
or union run apprenticeship programs.

853
00:37:01.485 --> 00:37:03.305
So maybe a CTE co-op Tech

854
00:37:03.305 --> 00:37:04.545
and Pathways are used

855
00:37:04.685 --> 00:37:07.225
to strategically make a pipeline into service jobs

856
00:37:07.495 --> 00:37:09.585
that support better attendance and safety.

857
00:37:09.685 --> 00:37:10.905
And it's a win-win for all.

858
00:37:12.345 --> 00:37:16.115
Know no on a agenda item number two, I'll see, try

859
00:37:16.115 --> 00:37:17.715
to do this as quickly as possible

860
00:37:18.535 --> 00:37:20.315
at a time when schools are experiencing

861
00:37:20.315 --> 00:37:21.595
serious of staffing issues.

862
00:37:21.595 --> 00:37:25.475
Pulling educators away from to train or administer

863
00:37:25.575 --> 00:37:28.995
and interpret tests for dubious utility is unacceptable

864
00:37:29.455 --> 00:37:31.115
and unconscionable.

865
00:37:31.345 --> 00:37:33.635
This amount of money is truly a waste.

866
00:37:33.735 --> 00:37:35.955
And I will tell you, as a parent who opts out

867
00:37:35.955 --> 00:37:36.955
of all assessments

868
00:37:37.095 --> 00:37:40.595
and state tests, I speak with my son's teachers regularly

869
00:37:40.975 --> 00:37:42.315
and they assure me, and they,

870
00:37:42.495 --> 00:37:45.595
I'm very confident in their ability to be able to assess

871
00:37:45.595 --> 00:37:49.235
where my son is at and meet him where he needs to be.

872
00:37:50.045 --> 00:37:53.835
59% of survey respondents that was taken showed

873
00:37:53.835 --> 00:37:55.595
that students showed a sign of stress

874
00:37:55.595 --> 00:37:59.235
because they were being tested on end of year benchmarks.

875
00:37:59.525 --> 00:38:02.115
65% of a survey from respondents reported

876
00:38:02.115 --> 00:38:04.235
that administering these assessments interfered

877
00:38:04.235 --> 00:38:07.435
with our ability to actually assess

878
00:38:07.735 --> 00:38:09.395
trauma-informed practices.

879
00:38:09.935 --> 00:38:13.715
The third grade teacher ICT from Brooklyn spent quoted,

880
00:38:13.795 --> 00:38:15.675
I spent much time building back kids

881
00:38:16.695 --> 00:38:17.805
after taking these tests

882
00:38:17.805 --> 00:38:20.045
because they felt so badly taking the test

883
00:38:20.145 --> 00:38:21.165
and didn't understand.

884
00:38:21.915 --> 00:38:23.245
It's unclear whether schools

885
00:38:23.245 --> 00:38:24.685
have actually been able to use this.

886
00:38:24.685 --> 00:38:26.445
As we've heard from educators tonight,

887
00:38:26.795 --> 00:38:29.285
they don't actually get to see this data.

888
00:38:29.595 --> 00:38:31.405
It's useless. Please put this money

889
00:38:31.415 --> 00:38:33.125
where we can really support our students.

890
00:38:33.125 --> 00:38:34.125
Thank you.

891
00:38:40.755 --> 00:38:43.705
That is the end of the public comment. Okay.

892
00:38:43.705 --> 00:38:45.745
Uh, contract items. Great. Thank you.

893
00:38:45.765 --> 00:38:47.905
And I wanna thank members of the public who came out

894
00:38:47.905 --> 00:38:49.625
and thank you for your, uh, for your comments.

895
00:38:50.245 --> 00:38:52.585
We will now transition to panel member comments.

896
00:38:52.805 --> 00:38:54.025
And I'm looking at Tom Shepherd

897
00:38:54.265 --> 00:38:57.995
'cause I guess correctly

898
00:38:57.995 --> 00:38:59.595
that you would have your hand raised.

899
00:38:59.935 --> 00:39:01.115
So Panel Member Shepherd.

900
00:39:02.045 --> 00:39:05.565
Thank you. Um, I wanna start

901
00:39:05.705 --> 00:39:09.525
by saying thank you to the public

902
00:39:09.905 --> 00:39:11.485
who comes out month after month

903
00:39:12.145 --> 00:39:16.725
and speaks on these contracts and how they work

904
00:39:16.905 --> 00:39:19.685
or don't work for our school system

905
00:39:20.025 --> 00:39:21.645
and our students in particular.

906
00:39:22.905 --> 00:39:25.125
I'm sitting here this month and I'm looking at these numbers

907
00:39:25.585 --> 00:39:28.965
and it's not lost on me that

908
00:39:29.655 --> 00:39:33.525
we're spending almost as much to repair the sidewalks

909
00:39:33.905 --> 00:39:35.405
as we are in special education.

910
00:39:36.995 --> 00:39:40.975
And I got a problem with that, right?

911
00:39:41.045 --> 00:39:43.335
Like million and a half dollars for repair

912
00:39:43.335 --> 00:39:44.495
of asphalt pavement

913
00:39:45.235 --> 00:39:49.815
and $1.57 million in, um,

914
00:39:50.555 --> 00:39:52.415
um, one point, uh, 1.7 million

915
00:39:52.595 --> 00:39:54.095
for special education enhancements.

916
00:39:54.125 --> 00:39:57.895
Something just doesn't sound or feel right about that.

917
00:39:58.905 --> 00:40:02.125
And I've been sitting here for almost four

918
00:40:02.125 --> 00:40:05.365
and a half years across four chancellors

919
00:40:06.425 --> 00:40:10.485
and, you know, dozens

920
00:40:10.985 --> 00:40:14.515
of assessments that we've approved, you know, to the tune

921
00:40:14.815 --> 00:40:19.125
of, you know, dozens if not close

922
00:40:19.145 --> 00:40:20.605
to a hundred million dollars.

923
00:40:21.505 --> 00:40:24.525
And, you know, dozens of assessments that

924
00:40:25.045 --> 00:40:27.205
I couldn't tell you if they work or not,

925
00:40:27.595 --> 00:40:30.645
because nobody's ever come back and told us how they work

926
00:40:30.905 --> 00:40:33.295
or whether they work, right?

927
00:40:33.955 --> 00:40:38.005
And, you know, the community has a problem with that.

928
00:40:38.005 --> 00:40:41.315
And so do I, you know, when we look at

929
00:40:42.025 --> 00:40:46.755
this month when we're spending, you know, $85 million for,

930
00:40:47.535 --> 00:40:50.195
you know, notebooks and mobile computers,

931
00:40:50.335 --> 00:40:52.635
and you couple that with, you know,

932
00:40:55.605 --> 00:40:56.845
I mean, where do you go from here?

933
00:40:56.845 --> 00:40:59.685
Like $28 million on copy machines

934
00:40:59.905 --> 00:41:02.685
and, you know, all kinds of stuff.

935
00:41:03.025 --> 00:41:06.565
But then at the, at the same time, you know, we have schools

936
00:41:06.595 --> 00:41:08.485
that still don't have enough teachers.

937
00:41:09.145 --> 00:41:13.285
We have schools where, you know, our kids are, you know,

938
00:41:13.385 --> 00:41:16.405
placed in a position of spending more time in front

939
00:41:16.405 --> 00:41:19.125
of a computer and less time in front of a teacher.

940
00:41:20.105 --> 00:41:23.365
And that doesn't make any of us feel good.

941
00:41:24.455 --> 00:41:26.995
And you know, I've said before,

942
00:41:27.455 --> 00:41:29.195
and I'll say it again, at

943
00:41:29.195 --> 00:41:31.835
what point when we look at assessments, do we say

944
00:41:31.835 --> 00:41:34.785
to ourselves that enough is, is enough, right?

945
00:41:35.255 --> 00:41:37.265
When we are talking about assessments

946
00:41:37.335 --> 00:41:40.025
that assess the assessments that assess the assessments,

947
00:41:40.025 --> 00:41:42.465
that assess the assessments, we, we have

948
00:41:42.465 --> 00:41:45.145
to start asking ourselves at what point, like,

949
00:41:45.325 --> 00:41:47.945
do we just put a pause on this, evaluate

950
00:41:47.945 --> 00:41:49.025
what we already have,

951
00:41:49.485 --> 00:41:50.665
and then report back

952
00:41:50.665 --> 00:41:53.505
to the public about what's working and what's not?

953
00:41:54.245 --> 00:41:56.505
And then the last thing here, um,

954
00:41:56.855 --> 00:41:57.905
because, you know,

955
00:41:57.905 --> 00:42:01.065
we've been having some real conversations about, you know,

956
00:42:01.685 --> 00:42:02.945
you know, student privacy

957
00:42:03.205 --> 00:42:05.105
and data privacy and what that means.

958
00:42:05.925 --> 00:42:09.785
Um, and, you know, there's, there's no

959
00:42:10.295 --> 00:42:12.945
real understanding here of how student data

960
00:42:13.445 --> 00:42:15.265
and family data is being used.

961
00:42:15.335 --> 00:42:16.625
What it's being used for.

962
00:42:17.405 --> 00:42:20.945
Um, you know, you know, is this information,

963
00:42:21.095 --> 00:42:23.185
like there was a teacher spoke, said

964
00:42:23.185 --> 00:42:27.545
that she doesn't even get like the information from these

965
00:42:27.545 --> 00:42:29.545
assessments for her own classroom.

966
00:42:30.095 --> 00:42:33.145
Like so at what, so you have to ask yourself, well,

967
00:42:33.485 --> 00:42:35.705
if the teacher that's sitting in front of these children,

968
00:42:36.605 --> 00:42:39.585
um, doesn't have access to the assessment data

969
00:42:40.325 --> 00:42:43.145
for their own students, then who has that data

970
00:42:43.165 --> 00:42:44.265
and what are they doing with it?

971
00:42:45.295 --> 00:42:47.755
And, you know, at the end of the day,

972
00:42:48.035 --> 00:42:52.275
I am not comfortable voting yes on contract items.

973
00:42:52.275 --> 00:42:55.155
Number two, I am not comfortable.

974
00:42:55.815 --> 00:42:59.955
Um, you know, I will probably abstain, um,

975
00:43:00.865 --> 00:43:04.075
from all of these, you know, stuff, contracts.

976
00:43:04.935 --> 00:43:09.155
Um, but I think, you know, at a time when we are,

977
00:43:10.015 --> 00:43:11.435
um, when schools are sitting

978
00:43:11.435 --> 00:43:14.795
around looking at their budget shrink, um, we need

979
00:43:14.795 --> 00:43:16.715
to take a hard look at these contracts

980
00:43:17.375 --> 00:43:20.795
and we have to have a different kind of conversation

981
00:43:21.545 --> 00:43:24.355
that says, you know, if if

982
00:43:24.875 --> 00:43:27.915
students in special education are a priority,

983
00:43:27.915 --> 00:43:29.315
then we need to invest in that.

984
00:43:29.815 --> 00:43:31.635
If students in schools

985
00:43:31.635 --> 00:43:33.875
that don't have enough teachers are a priority,

986
00:43:33.875 --> 00:43:35.235
then we need to invest in that.

987
00:43:35.495 --> 00:43:37.315
And we have to take a look at all these other things

988
00:43:37.855 --> 00:43:40.195
and tell ourselves, is this like,

989
00:43:40.705 --> 00:43:43.195
does this serve the best interest of our students?

990
00:43:43.265 --> 00:43:45.235
Does it serve the best interest of our teachers?

991
00:43:45.625 --> 00:43:47.835
Does it serve the best interest of our communities?

992
00:43:48.335 --> 00:43:51.035
And if there's any hesitation on any

993
00:43:51.035 --> 00:43:54.275
of those three questions, then we should not be, um,

994
00:43:54.755 --> 00:43:55.875
considering those contracts.

995
00:43:56.335 --> 00:43:59.915
Um, so with that said, um, I want to thank you.

996
00:44:00.455 --> 00:44:02.715
Uh, oh, there is one other thing I wanna speak to.

997
00:44:03.375 --> 00:44:05.555
And that is agenda item number six.

998
00:44:06.415 --> 00:44:09.915
Um, the, the heat and hot water for co-op city schools.

999
00:44:10.215 --> 00:44:14.275
The, the schools around, um, co-op City, um, for River Bay.

1000
00:44:15.485 --> 00:44:20.385
Now, you know, my kids went to school in in district 11.

1001
00:44:20.685 --> 00:44:24.025
My, um, youngest daughter went to 180 1,

1002
00:44:24.025 --> 00:44:25.345
which is one of the schools here.

1003
00:44:25.435 --> 00:44:27.105
She's in, she's in high school now.

1004
00:44:27.205 --> 00:44:30.545
But, you know, I understand that,

1005
00:44:32.135 --> 00:44:36.555
um, you know, it's important to make sure that we have heat

1006
00:44:36.655 --> 00:44:38.075
and hot water in our schools.

1007
00:44:38.895 --> 00:44:43.315
Um, but I also think that we should be looking at, um,

1008
00:44:43.925 --> 00:44:46.195
especially with a lot of these older school buildings,

1009
00:44:46.335 --> 00:44:51.035
how do we modernize these school buildings or retrofit them

1010
00:44:51.095 --> 00:44:53.835
or upgrade them in a way, um,

1011
00:44:54.405 --> 00:44:58.795
where we are not looking at, you know, millions of dollars,

1012
00:44:59.535 --> 00:45:03.515
you know, paid out to, um, a utility.

1013
00:45:03.935 --> 00:45:06.475
Uh, 'cause River Bay in co-op City is a utility.

1014
00:45:07.415 --> 00:45:09.925
Um, and you know,

1015
00:45:09.925 --> 00:45:12.445
this is a one year contract.

1016
00:45:12.565 --> 00:45:13.965
I believe it's an extension.

1017
00:45:14.705 --> 00:45:18.245
Um, I think we need to really take the time to go

1018
00:45:18.245 --> 00:45:20.205
through the schools in co-op City

1019
00:45:20.745 --> 00:45:25.005
and make sure that, um, anything

1020
00:45:25.005 --> 00:45:27.245
that we can do to upgrade those schools,

1021
00:45:27.615 --> 00:45:32.325
especially when the city has committed, um, to, you know,

1022
00:45:32.395 --> 00:45:37.365
renewable energy, to solar, to these kinds of, um, uh,

1023
00:45:38.205 --> 00:45:39.805
upgrades to our infrastructure

1024
00:45:40.545 --> 00:45:43.285
and really invest that kind

1025
00:45:43.285 --> 00:45:47.285
of money into upgrading the older schools in co-op City.

1026
00:45:47.905 --> 00:45:51.845
Um, and, you know, I will support a one year extension,

1027
00:45:51.985 --> 00:45:56.485
but, um, you know, it, you know, anything longer than that,

1028
00:45:56.985 --> 00:45:58.325
um, I do think that we need

1029
00:45:58.325 --> 00:45:59.885
to have a different kind of conversation.

1030
00:46:00.175 --> 00:46:02.165
Thank you Chair Faulkner and I yield best. Sure. Thank you.

1031
00:46:02.585 --> 00:46:04.045
Um, chancellor Pleasures,

1032
00:46:04.335 --> 00:46:05.335
Thank you. Panel Member

1033
00:46:05.335 --> 00:46:07.965
Shepherd. Um, we do have Chief Dr.

1034
00:46:08.285 --> 00:46:10.685
Mia Pay who can respond to some

1035
00:46:10.685 --> 00:46:13.045
of the assessment, uh, concerns.

1036
00:46:13.065 --> 00:46:16.525
And then we also have, I believe, uh, chief Moran,

1037
00:46:16.525 --> 00:46:19.245
Kevin Moran, if you are here, uh, if you're able to respond.

1038
00:46:19.865 --> 00:46:21.825
So thank you for all the comments.

1039
00:46:22.105 --> 00:46:25.225
I wanted to just hone in on one particular part about the

1040
00:46:25.545 --> 00:46:28.305
teachers and just really kind of demystify.

1041
00:46:28.365 --> 00:46:32.585
So the design of the assessments that students are taking.

1042
00:46:33.325 --> 00:46:34.345
Two things to note.

1043
00:46:34.475 --> 00:46:37.145
Every teacher has direct access

1044
00:46:37.645 --> 00:46:39.665
to their students results.

1045
00:46:40.445 --> 00:46:44.825
And also every assessment provides a teacher portal

1046
00:46:45.275 --> 00:46:48.585
where teachers have direct access to their results.

1047
00:46:48.845 --> 00:46:53.745
Now, if there is anyone who knows of a teacher,

1048
00:46:53.925 --> 00:46:58.385
or maybe they are a teacher who does not have direct access

1049
00:46:58.485 --> 00:47:02.665
to your students' assessment data, that is a problem.

1050
00:47:03.245 --> 00:47:05.985
So I want to just make sure my email is

1051
00:47:06.405 --> 00:47:10.105
mpa@schools.nyc.gov.

1052
00:47:10.525 --> 00:47:12.785
You can email me directly,

1053
00:47:13.085 --> 00:47:16.585
and I will ensure that we investigate exactly

1054
00:47:16.815 --> 00:47:20.545
what the challenges are for any teacher within the city

1055
00:47:20.925 --> 00:47:23.665
who is having problems assessing and

1056
00:47:23.805 --> 00:47:25.785
or receiving the data

1057
00:47:26.575 --> 00:47:29.345
from their students assessment information.

1058
00:47:29.625 --> 00:47:33.765
Now, clarity teachers do not have citywide access

1059
00:47:33.985 --> 00:47:35.525
to any student's data,

1060
00:47:35.905 --> 00:47:39.085
but they do have direct access to their students' data.

1061
00:47:39.305 --> 00:47:42.205
So I just want to make sure, um, that you know,

1062
00:47:42.205 --> 00:47:45.445
that we are adamantly committed to ensuring

1063
00:47:45.875 --> 00:47:48.365
that teachers have the access in real time

1064
00:47:48.865 --> 00:47:51.925
to make the decisions that they need connected

1065
00:47:51.945 --> 00:47:53.125
to instruction

1066
00:47:53.545 --> 00:47:57.565
and ensuring that they are clearly aware of the gaps

1067
00:47:58.035 --> 00:47:59.965
that students may have so

1068
00:47:59.965 --> 00:48:02.965
that effective intervention can be provided to students.

1069
00:48:03.105 --> 00:48:07.845
So again, that email is m as in Maria, P as in Peter,

1070
00:48:08.165 --> 00:48:10.885
a t e@schools.nyc.gov.

1071
00:48:12.945 --> 00:48:13.705
I just wanna thank you, Dr.

1072
00:48:13.715 --> 00:48:14.945
Thank you for that clarification.

1073
00:48:17.215 --> 00:48:20.275
Uh, hello, Kevin Moran, uh, chief of School Operations.

1074
00:48:20.295 --> 00:48:23.035
Uh, thank you chancellor and thank you Member Shepherd.

1075
00:48:23.335 --> 00:48:25.715
Uh, a couple things just as it relates to the,

1076
00:48:26.095 --> 00:48:27.195
uh, sidewalks.

1077
00:48:27.615 --> 00:48:29.635
Uh, we're very fortunate to have a collaboration

1078
00:48:29.635 --> 00:48:31.235
with the New York City Department of Transportation.

1079
00:48:31.625 --> 00:48:33.355
They handle sidewalk repairs.

1080
00:48:33.815 --> 00:48:36.515
Um, we're very enthused to bring together,

1081
00:48:36.935 --> 00:48:38.115
uh, a variety of vendors.

1082
00:48:38.175 --> 00:48:41.435
And in this instance for the asphalt vendor, an MWE vendor

1083
00:48:41.615 --> 00:48:43.515
to help us with asphalt repairs.

1084
00:48:43.935 --> 00:48:47.475
Uh, we have some, uh, square footage, uh, that is, uh,

1085
00:48:47.535 --> 00:48:49.555
in the tens of thousands around the boroughs

1086
00:48:49.555 --> 00:48:52.355
that is playground specific, uh, where kids play

1087
00:48:52.655 --> 00:48:54.915
and where cracks could surface over time.

1088
00:48:55.015 --> 00:48:57.635
Uneven where we need an asphalt asphalt vendor.

1089
00:48:57.635 --> 00:49:00.035
So this $500,000 each year will allow us to get

1090
00:49:00.035 --> 00:49:03.315
to our 1400 physical plants, fix any trip hazards

1091
00:49:03.495 --> 00:49:05.195
or issues around the school perimeter.

1092
00:49:05.255 --> 00:49:07.635
Uh, so we're really enthused about that, uh, contract.

1093
00:49:08.055 --> 00:49:10.155
Um, as it relates specifically to co-op City,

1094
00:49:11.295 --> 00:49:13.875
the way the co-op was established in the late sixties

1095
00:49:13.895 --> 00:49:15.675
and into early seventies was an

1096
00:49:15.835 --> 00:49:17.035
engineering marvel to itself.

1097
00:49:17.455 --> 00:49:20.555
Our schools weren't constructed with boilers themselves.

1098
00:49:21.175 --> 00:49:24.435
Uh, we pair off of, uh, like all the residents

1099
00:49:24.435 --> 00:49:26.755
and properties on, uh, the, the,

1100
00:49:26.775 --> 00:49:28.715
the River Bay Management co-op.

1101
00:49:28.895 --> 00:49:32.595
Uh, we rely on them for heat, um, and hot water.

1102
00:49:32.975 --> 00:49:36.235
Um, to build out boiler rooms in a traditional sense

1103
00:49:36.235 --> 00:49:37.835
or upgrade would take some doing.

1104
00:49:37.855 --> 00:49:41.115
So I agree with you, Tom, looking at it at this year, just

1105
00:49:41.115 --> 00:49:43.635
as an extension of terms, um,

1106
00:49:44.095 --> 00:49:45.715
to figure out what is the best approach.

1107
00:49:45.715 --> 00:49:47.715
There's competing interest around electrification.

1108
00:49:47.715 --> 00:49:49.235
What does that mean? And and again,

1109
00:49:49.235 --> 00:49:51.395
we don't have boiler rooms, so it's loss of space

1110
00:49:51.395 --> 00:49:52.675
and there's some trade offs here.

1111
00:49:53.135 --> 00:49:55.715
Um, and there's some real value add to the system.

1112
00:49:55.945 --> 00:49:58.235
There's not a full-time employee assigned

1113
00:49:58.575 --> 00:50:00.675
to run the systems in the physical plant

1114
00:50:00.755 --> 00:50:02.395
to bring up the heat, to bring up the hot water.

1115
00:50:02.395 --> 00:50:03.475
They're turning a valve.

1116
00:50:03.815 --> 00:50:05.475
Um, it comes straight into the building so we don't have

1117
00:50:05.475 --> 00:50:08.315
to sign full-time employees to, to run the physical boilers.

1118
00:50:08.615 --> 00:50:11.835
But all that to say, we're gonna look at the options, some

1119
00:50:11.835 --> 00:50:13.155
of the options that we didn't have, type

1120
00:50:13.155 --> 00:50:15.195
of this services like a temporary boiler.

1121
00:50:15.195 --> 00:50:18.195
You've seen them in the street when we seek to upgrade, um,

1122
00:50:18.295 --> 00:50:20.355
as we're required to do, they have the, the,

1123
00:50:20.425 --> 00:50:21.755
they look like tractor trailers

1124
00:50:21.755 --> 00:50:23.235
and they're, they're cordoned off with barriers

1125
00:50:23.335 --> 00:50:24.875
and they have a large stainless stack

1126
00:50:24.875 --> 00:50:25.995
that runs alongside the building.

1127
00:50:27.015 --> 00:50:28.755
And, uh, Jess, I know you said you had one

1128
00:50:28.755 --> 00:50:30.675
and you guys celebrated in the street when it was gone.

1129
00:50:31.175 --> 00:50:35.675
Um, uh, but that is a product of, of the upgrade itself.

1130
00:50:36.095 --> 00:50:37.315
So what do you do in the interim?

1131
00:50:37.315 --> 00:50:39.035
But these are all very interesting conversations.

1132
00:50:39.375 --> 00:50:41.995
Um, I had offered, and I I I, I extend the offer again

1133
00:50:41.995 --> 00:50:43.715
to anyone who wants to go up to Cobb City.

1134
00:50:44.215 --> 00:50:46.515
Uh, I think Ream already said, yes, Tom,

1135
00:50:46.555 --> 00:50:47.555
I know you're nearby.

1136
00:50:47.695 --> 00:50:49.915
Uh, to see the physical plants, to see the complexities

1137
00:50:49.915 --> 00:50:51.795
and to have open and honest conversations about

1138
00:50:51.945 --> 00:50:54.555
what is the service that we get here with this contract item

1139
00:50:54.935 --> 00:50:56.275
and what are the trade-offs.

1140
00:50:56.495 --> 00:50:58.235
Um, and just on top lines,

1141
00:50:58.515 --> 00:50:59.755
'cause it was raised it

1142
00:50:59.755 --> 00:51:01.875
to put a heat pump system in every classroom in,

1143
00:51:01.895 --> 00:51:06.835
in all the plants across that campus, $440 million

1144
00:51:06.975 --> 00:51:08.235
to upgrade that and

1145
00:51:08.235 --> 00:51:10.675
to assign $500,000 a year to run those systems.

1146
00:51:11.135 --> 00:51:12.675
Um, and to change out a boiler

1147
00:51:12.675 --> 00:51:13.915
to try to do an electric boiler.

1148
00:51:14.005 --> 00:51:16.755
Again, those spaces, but we, we had that somewhere, uh,

1149
00:51:16.775 --> 00:51:18.195
in excess of a hundred million dollars.

1150
00:51:18.535 --> 00:51:20.395
Um, and so we see this as a, as a,

1151
00:51:20.395 --> 00:51:21.555
as a pretty efficient system.

1152
00:51:22.055 --> 00:51:24.315
Um, but I encourage the conversation going forward about

1153
00:51:24.335 --> 00:51:27.795
how, uh, folks can opine look at these, the financials

1154
00:51:27.795 --> 00:51:29.555
and so we can make a better decision together

1155
00:51:29.765 --> 00:51:30.915
about a contract term.

1156
00:51:31.055 --> 00:51:33.315
And what are the trade-offs, uh, before we go forward.

1157
00:51:33.525 --> 00:51:35.395
Thank, thank you for that. I know we had a really great

1158
00:51:35.715 --> 00:51:38.435
briefing, uh, from your team discussing exactly all

1159
00:51:38.435 --> 00:51:40.595
of those, uh, all of those concerns and issues

1160
00:51:40.735 --> 00:51:42.435
and, uh, those things that are,

1161
00:51:42.465 --> 00:51:43.835
make it a little bit more complicated.

1162
00:51:43.855 --> 00:51:45.995
So I'm glad that that's gonna be an ongoing discussion.

1163
00:51:49.795 --> 00:51:53.935
Any other panel? Yes. Yes. Go ahead. Panel member Alvin.

1164
00:51:54.245 --> 00:51:56.535
Okay. So, um, first I'm gonna say

1165
00:51:56.535 --> 00:51:59.895
that these assessments are usually not really

1166
00:52:00.155 --> 00:52:02.055
for the school level, right?

1167
00:52:02.415 --> 00:52:05.095
I it is more for the district, the borrower, citywide level.

1168
00:52:05.715 --> 00:52:08.015
The teachers are the best way of assessing,

1169
00:52:08.475 --> 00:52:11.535
but I'm not hearing that they're not getting the data

1170
00:52:11.755 --> 00:52:13.335
or they're not getting the results.

1171
00:52:13.885 --> 00:52:15.935
They are the, the issue is

1172
00:52:16.875 --> 00:52:18.975
our scholars are, are beyond tests.

1173
00:52:19.435 --> 00:52:21.615
If we keep increasing assessments,

1174
00:52:22.225 --> 00:52:25.365
that's taking away from their learning and enjoying school.

1175
00:52:25.785 --> 00:52:28.685
Not every, all students aren't test takers, right?

1176
00:52:29.185 --> 00:52:31.325
And that's not the only way we should be assessing

1177
00:52:31.325 --> 00:52:32.445
our children, right?

1178
00:52:32.445 --> 00:52:33.805
There's too many assessments.

1179
00:52:33.805 --> 00:52:35.405
And this is what I'm hearing, right?

1180
00:52:35.425 --> 00:52:36.725
We have all these assessments.

1181
00:52:36.825 --> 00:52:39.045
We may need to restrategize

1182
00:52:39.705 --> 00:52:42.325
how we assess our students maybe is less

1183
00:52:42.325 --> 00:52:43.965
because real life, yeah.

1184
00:52:44.325 --> 00:52:46.285
Occasionally we take tests, but real life we are not

1185
00:52:46.285 --> 00:52:47.325
taking tests all the time.

1186
00:52:47.575 --> 00:52:49.565
40% of the time we're not taking tests.

1187
00:52:49.785 --> 00:52:53.405
So if we're trying to reimagine the school experience,

1188
00:52:53.575 --> 00:52:56.085
increasing assessments, that's not part of it.

1189
00:52:56.475 --> 00:52:58.685
Some of them going to clam up under pressure.

1190
00:52:59.145 --> 00:53:01.405
Why We gotta take a test every time we gotta take a test.

1191
00:53:01.525 --> 00:53:04.445
I gotta take a test that is not making education fun.

1192
00:53:04.915 --> 00:53:08.845
This is not, um, being, um, project based managing to see

1193
00:53:08.845 --> 00:53:10.525
how it relates to real life.

1194
00:53:10.905 --> 00:53:12.285
We are not always taking tests.

1195
00:53:12.625 --> 00:53:14.765
So I think that is what I'm hearing, right?

1196
00:53:14.905 --> 00:53:17.685
But the data, I have to say the data is being used

1197
00:53:18.185 --> 00:53:19.565
but not at the school level.

1198
00:53:19.865 --> 00:53:22.245
And we really don't want our teachers

1199
00:53:22.545 --> 00:53:25.885
and at the school level assessing students solely on tests

1200
00:53:25.885 --> 00:53:29.245
because that doesn't show the whole student, right?

1201
00:53:29.665 --> 00:53:31.605
So that, that is what's being said,

1202
00:53:31.865 --> 00:53:34.085
not about accessing the results

1203
00:53:34.185 --> 00:53:37.845
of the assess the assessments is what it's doing to a lot

1204
00:53:37.845 --> 00:53:40.565
of the children and the learn teaching, right?

1205
00:53:40.995 --> 00:53:43.845
It's taking away from the teaching time of the subject

1206
00:53:43.875 --> 00:53:45.605
because we have to do assessments,

1207
00:53:45.815 --> 00:53:47.805
which will help maybe the district

1208
00:53:47.805 --> 00:53:49.605
to give it an overall thing,

1209
00:53:49.625 --> 00:53:52.445
but it's not helping the teachers at the school level.

1210
00:53:52.545 --> 00:53:55.565
And we want to make sure our school levels, uh,

1211
00:53:55.705 --> 00:53:57.685
the students, our scholars, our children,

1212
00:53:58.185 --> 00:54:00.165
is getting the education they want.

1213
00:54:00.585 --> 00:54:02.445
And, and it's enjoyable, right?

1214
00:54:02.785 --> 00:54:05.085
You know, the students who like, okay, it's a test day.

1215
00:54:05.105 --> 00:54:07.245
I'm not gonna show up because I don't do well.

1216
00:54:07.305 --> 00:54:08.605
We don't want that to happen.

1217
00:54:08.945 --> 00:54:11.125
And we need to feel that the whole

1218
00:54:11.805 --> 00:54:14.005
academic career is based on a test, right?

1219
00:54:14.025 --> 00:54:15.325
Our children are beyond the test.

1220
00:54:15.385 --> 00:54:17.045
That's what is being said today.

1221
00:54:17.425 --> 00:54:19.365
Not about access to information.

1222
00:54:19.715 --> 00:54:21.285
That is what they're trying to protect.

1223
00:54:21.315 --> 00:54:23.405
This is what I'm getting. I'm just gonna say that's

1224
00:54:23.405 --> 00:54:25.605
what I'm getting from the public comments.

1225
00:54:25.985 --> 00:54:29.325
And I agree with the assessment, you know, you know, agree

1226
00:54:29.325 --> 00:54:31.565
what they're saying about too many assessments,

1227
00:54:31.785 --> 00:54:34.565
but the, it is unnecessary, uh, the case.

1228
00:54:35.225 --> 00:54:38.085
Now I don't plan to vote yes for number two

1229
00:54:38.585 --> 00:54:40.125
for other reasons, right?

1230
00:54:40.125 --> 00:54:42.205
Because we do got too many assessments.

1231
00:54:42.505 --> 00:54:45.805
But it is, is necessary to get a overall view

1232
00:54:46.065 --> 00:54:48.085
how New York City Public Schools is doing.

1233
00:54:48.435 --> 00:54:49.885
It's not gonna give a accurate picture,

1234
00:54:50.185 --> 00:54:52.685
but it will give us something right to go on.

1235
00:54:52.685 --> 00:54:55.725
Because again, the district, the city is not at the school.

1236
00:54:56.195 --> 00:54:58.725
They're not dealing with the children's directly.

1237
00:54:59.145 --> 00:55:02.365
So then we leave it to our teachers to assess them.

1238
00:55:02.905 --> 00:55:04.965
Um, so it's just for data

1239
00:55:04.985 --> 00:55:06.565
for the computers to give a measurement.

1240
00:55:06.785 --> 00:55:09.565
And in that case, so I just wanna clarify, this is

1241
00:55:09.565 --> 00:55:11.965
what the parents are saying, uh, in regards to,

1242
00:55:12.425 --> 00:55:14.125
uh, these assessments.

1243
00:55:14.225 --> 00:55:16.845
It shouldn't take up so many, so much of their time

1244
00:55:17.565 --> 00:55:18.925
teaching the students, right?

1245
00:55:18.945 --> 00:55:23.245
And we need to come up with better assessments, uh,

1246
00:55:23.625 --> 00:55:27.245
so we can assess them when needed, but not so much.

1247
00:55:27.565 --> 00:55:30.565
'cause we are going to technology, they're already doing

1248
00:55:31.135 --> 00:55:32.685
state exams gonna be online.

1249
00:55:32.985 --> 00:55:37.405
The SA is going online, the AP exams online.

1250
00:55:37.825 --> 00:55:40.605
We, you know, we're all beyond the technology.

1251
00:55:40.835 --> 00:55:44.245
It's too not personal, right? It's too personal.

1252
00:55:44.245 --> 00:55:45.965
If they have to take these tests online,

1253
00:55:46.175 --> 00:55:48.805
let's eliminate some, you know, reduce the amount.

1254
00:55:48.945 --> 00:55:51.805
We know it's necessary, but let's try to reduce

1255
00:55:51.825 --> 00:55:56.615
and be more, um, how say more effective

1256
00:55:56.615 --> 00:55:59.615
and impactful when we do do the assessments.

1257
00:55:59.955 --> 00:56:02.855
Let those assessments do what they should do.

1258
00:56:03.005 --> 00:56:04.855
Instead of doing multiple assessments,

1259
00:56:05.165 --> 00:56:08.135
like I think Tom said elegantly assess

1260
00:56:08.195 --> 00:56:09.255
the assess the assess.

1261
00:56:09.435 --> 00:56:11.335
You know, if all these things are working, we need

1262
00:56:11.335 --> 00:56:14.975
to be more effective and more use of our time.

1263
00:56:15.555 --> 00:56:17.695
Um, and so the teachers can actually do

1264
00:56:17.845 --> 00:56:20.095
what they're supposed to do in the classroom.

1265
00:56:20.395 --> 00:56:23.285
And kids don't feel intimidated that all I go

1266
00:56:23.285 --> 00:56:24.685
to school is just to do a test.

1267
00:56:24.975 --> 00:56:28.285
Right? So that, I think that is what's being clarified here.

1268
00:56:28.825 --> 00:56:30.925
Um, for, so it could be clear,

1269
00:56:30.955 --> 00:56:33.805
it's not about getting information about the test scores.

1270
00:56:33.905 --> 00:56:35.285
We know what the test scores are.

1271
00:56:35.465 --> 00:56:37.125
We might not know specific assessments,

1272
00:56:37.125 --> 00:56:38.725
but of course we get the state exam.

1273
00:56:38.725 --> 00:56:40.205
That is not what they're talking about.

1274
00:56:40.555 --> 00:56:42.645
They don't know how the data is being used.

1275
00:56:43.025 --> 00:56:45.245
But I'm saying it is being used at the

1276
00:56:45.405 --> 00:56:46.485
district level, right?

1277
00:56:46.825 --> 00:56:49.325
It should be talked about at the district leadership team.

1278
00:56:50.035 --> 00:56:52.045
What, how they using these assessments,

1279
00:56:52.275 --> 00:56:53.685
what are those results are,

1280
00:56:53.685 --> 00:56:56.445
because the district comprehension education plan is

1281
00:56:56.765 --> 00:56:58.485
supposed to be based on those assessments.

1282
00:56:58.715 --> 00:57:01.645
This is what I'm trying to, trying to clarify here.

1283
00:57:01.865 --> 00:57:05.205
So if your DLT or your SLT

1284
00:57:05.625 --> 00:57:09.605
or whatever is not doing, get those information, you can get

1285
00:57:09.605 --> 00:57:14.085
that information right for your school or for your district.

1286
00:57:14.335 --> 00:57:15.645
There. They, you know, there is

1287
00:57:15.645 --> 00:57:16.925
the structure in place for that.

1288
00:57:17.705 --> 00:57:19.445
Um, I was gonna say something else,

1289
00:57:19.545 --> 00:57:20.805
but I think I took enough time,

1290
00:57:21.065 --> 00:57:24.245
but I just wanna re I want us to, the goal is,

1291
00:57:24.305 --> 00:57:25.405
and it's everybody's goal

1292
00:57:25.605 --> 00:57:28.485
'cause we're not gonna agree is the children, what is best

1293
00:57:28.485 --> 00:57:30.685
for the children and all these assessments.

1294
00:57:30.985 --> 00:57:33.445
It, it's not, it's, it's, it is just too much.

1295
00:57:34.275 --> 00:57:35.885
Okay. Thank you. pem Alban,

1296
00:57:35.885 --> 00:57:38.285
I think I saw Pem AIA with, or was it?

1297
00:57:38.345 --> 00:57:39.645
Yes. Yeah. Panel member.

1298
00:57:43.365 --> 00:57:48.145
Hello everyone. Adriana, she, her, um, I have a couple

1299
00:57:48.165 --> 00:57:49.425
of of things to know.

1300
00:57:49.425 --> 00:57:52.025
There's been a lot said about contract item number two

1301
00:57:52.025 --> 00:57:53.705
already, so I won't say anything else there.

1302
00:57:54.045 --> 00:57:55.905
But I do have a couple of concerns.

1303
00:57:56.125 --> 00:58:00.095
Um, I am inclined to believe the teachers when they say

1304
00:58:00.095 --> 00:58:02.895
that they do not have access to their students'

1305
00:58:03.415 --> 00:58:06.305
testing data assessment, data assessment records,

1306
00:58:06.305 --> 00:58:10.785
because these people are people I trust with my son, right?

1307
00:58:10.805 --> 00:58:13.265
So I don't think that they would lie to me or lie to us.

1308
00:58:13.685 --> 00:58:17.265
Um, in that, in that though, uh, who's,

1309
00:58:17.365 --> 00:58:19.905
who sees the data in that case, the,

1310
00:58:19.905 --> 00:58:21.825
the testing folks see it and they keep it.

1311
00:58:21.885 --> 00:58:23.825
Why are they keeping it? Um,

1312
00:58:23.825 --> 00:58:26.065
because we know that testing data is sold

1313
00:58:26.125 --> 00:58:27.745
and it's also tracked to see

1314
00:58:27.995 --> 00:58:29.785
where your kid is likely to go to high school.

1315
00:58:29.785 --> 00:58:30.785
And then based on that,

1316
00:58:31.045 --> 00:58:32.505
how they're likely to do on their SAT.

1317
00:58:32.505 --> 00:58:34.465
And based on that, they can advertise to them

1318
00:58:34.465 --> 00:58:36.265
for colleges, et cetera, et cetera.

1319
00:58:36.325 --> 00:58:40.045
So if our teachers aren't seeing the results,

1320
00:58:40.425 --> 00:58:44.525
but the testing company is seeing it, are they keeping it?

1321
00:58:45.065 --> 00:58:47.285
How often are they reviewing it?

1322
00:58:47.345 --> 00:58:48.925
And then are they deleting it?

1323
00:58:49.105 --> 00:58:52.405
Are they scrubbing our students', PII from their systems?

1324
00:58:55.495 --> 00:58:59.515
Uh, my second question is, um, regarding

1325
00:59:00.935 --> 00:59:03.315
the lack of computer science education that we have,

1326
00:59:03.385 --> 00:59:06.395
there's been a lot of conversation so far about

1327
00:59:07.725 --> 00:59:09.625
our students taking assessments online

1328
00:59:09.765 --> 00:59:11.745
and taking their state exams online now.

1329
00:59:11.765 --> 00:59:13.905
And the shiza is going to be moving online as well,

1330
00:59:14.005 --> 00:59:15.825
as has already been mentioned this evening.

1331
00:59:16.045 --> 00:59:18.345
But we're not teaching our children how

1332
00:59:18.345 --> 00:59:19.505
to do simple things like type.

1333
00:59:19.965 --> 00:59:24.045
And I know from principals in my neck of the woods in Queens

1334
00:59:24.075 --> 00:59:29.005
that there is no time in the school day currently to add a,

1335
00:59:29.085 --> 00:59:31.485
a, a period where the tea, the children are taught how

1336
00:59:31.485 --> 00:59:33.805
to type, or the children are taught computer science,

1337
00:59:34.065 --> 00:59:36.365
or the children are taught how to navigate an interface,

1338
00:59:36.825 --> 00:59:38.045
or the children are taught how

1339
00:59:38.045 --> 00:59:39.405
to build a computer from scratch.

1340
00:59:39.405 --> 00:59:40.725
These are all things I learned

1341
00:59:40.725 --> 00:59:41.965
as a New York City public school

1342
00:59:41.965 --> 00:59:43.645
student in the two thousands.

1343
00:59:43.995 --> 00:59:45.205
It's a long time ago, but

1344
00:59:45.205 --> 00:59:46.645
technology's gotten better since then.

1345
00:59:47.335 --> 00:59:48.835
So I would hope that our teaching

1346
00:59:48.835 --> 00:59:49.995
of it had gotten better too, but

1347
00:59:49.995 --> 00:59:51.355
that is not the case, unfortunately.

1348
00:59:51.975 --> 00:59:54.685
Um, and the last item that I would like

1349
00:59:54.685 --> 00:59:56.965
to address is an agenda item number 16.

1350
00:59:57.275 --> 01:00:00.845
This is yet another consultant for DIIT.

1351
01:00:00.845 --> 01:00:03.125
Can we please just get them a full-time person? Please?

1352
01:00:03.385 --> 01:00:04.965
Please. Thank you.

1353
01:00:05.965 --> 01:00:07.455
Okay. Thank you. Thank you. Panel member.

1354
01:00:07.635 --> 01:00:11.175
Um, any other panel members? Wish panel member Lee?

1355
01:00:13.275 --> 01:00:16.345
Thank you. Um, so I,

1356
01:00:16.425 --> 01:00:18.785
I know I brought this up about contract item number eight,

1357
01:00:19.205 --> 01:00:20.345
uh, in our briefing.

1358
01:00:20.765 --> 01:00:24.345
Um, but I guess I'm still wondering, uh,

1359
01:00:24.345 --> 01:00:26.505
because I don't think I got a really sufficient answer,

1360
01:00:26.965 --> 01:00:30.625
but these $85 million, um, in desktops

1361
01:00:30.625 --> 01:00:32.555
and laptop computers, I know

1362
01:00:32.555 --> 01:00:33.755
that some of them are going to central offices.

1363
01:00:33.755 --> 01:00:35.075
Those are not the ones I'm concerned about.

1364
01:00:35.495 --> 01:00:37.795
But for the ones that, um,

1365
01:00:39.115 --> 01:00:43.355
are theoretically headed towards our schools, I would like

1366
01:00:43.355 --> 01:00:46.155
to know more about what mechanisms are in place

1367
01:00:46.375 --> 01:00:50.035
to ensure there's an equitable distribution of these devices

1368
01:00:50.415 --> 01:00:54.395
to ensure that all schools, regardless of enrollment, um,

1369
01:00:55.135 --> 01:00:59.555
get to have the same kind of ratios of laptops

1370
01:00:59.555 --> 01:01:00.755
or tablets to students.

1371
01:01:01.375 --> 01:01:04.955
Um, because we know that our lower enrolled schools

1372
01:01:05.665 --> 01:01:06.835
have smaller budgets

1373
01:01:06.835 --> 01:01:08.875
because we fund students and not schools.

1374
01:01:09.695 --> 01:01:14.635
Um, and, you know, as all of our assessments

1375
01:01:15.665 --> 01:01:20.315
move to digital versions, when we under resource

1376
01:01:21.215 --> 01:01:24.955
low, lower lowly enrolled schools in this particular manner,

1377
01:01:25.265 --> 01:01:28.915
what we are doing is under equipping students to perform

1378
01:01:29.615 --> 01:01:31.795
and students to be assessed accurately.

1379
01:01:31.855 --> 01:01:34.875
We are exacerbating the digital divide if we don't have a

1380
01:01:34.875 --> 01:01:38.075
mechanism in place to ensure equitable distribution.

1381
01:01:38.655 --> 01:01:41.515
Um, and so I'm really puzzled by this.

1382
01:01:42.195 --> 01:01:45.395
I would love it if somebody could explain how this works.

1383
01:01:46.175 --> 01:01:50.065
Um, because, you know, as Adriana mentioned, we don't want,

1384
01:01:50.555 --> 01:01:53.265
we're in the business here of increasing educational

1385
01:01:53.265 --> 01:01:54.945
opportunities and economic opportunities,

1386
01:01:56.045 --> 01:01:57.345
but if we're not providing kids

1387
01:01:57.345 --> 01:02:01.305
with the actual digital infrastructure to do so, then we are

1388
01:02:01.985 --> 01:02:04.105
exacerbating the preschool to prison pipeline.

1389
01:02:04.365 --> 01:02:05.945
We are exacerbating the digital divide,

1390
01:02:05.945 --> 01:02:07.825
and we are exacerbating socioeconomic divide,

1391
01:02:08.245 --> 01:02:10.395
you know, here.

1392
01:02:10.575 --> 01:02:13.075
So if somebody could help me with this.

1393
01:02:13.515 --> 01:02:15.455
Thank you. Thank you, chancellor.

1394
01:02:15.945 --> 01:02:18.535
Thank you so much. Um, both panel member Ali

1395
01:02:19.065 --> 01:02:21.245
and um, Hannah, member, uh, Lee.

1396
01:02:21.345 --> 01:02:23.485
So we have some, uh, responses.

1397
01:02:23.905 --> 01:02:27.245
If somebody from, uh, OPE, Ette, I believe you're here,

1398
01:02:27.265 --> 01:02:29.125
or Dan can speak to the assessment piece.

1399
01:02:29.125 --> 01:02:31.965
And then Shaquille, if you chief, um, Shaquille,

1400
01:02:31.965 --> 01:02:33.645
if you can also speak to the devices comment.

1401
01:02:33.645 --> 01:02:36.195
Thank you. And specifically I'd just like

1402
01:02:36.195 --> 01:02:38.155
to know about the distribution, um,

1403
01:02:39.565 --> 01:02:40.905
and equitable distributions.

1404
01:02:42.595 --> 01:02:44.095
Yes. Hi. Uh, good afternoon.

1405
01:02:45.195 --> 01:02:48.615
Uh, chief Information Officer, uh, in terms of the contract

1406
01:02:48.615 --> 01:02:50.895
that you're referring to, this is a requirement contract,

1407
01:02:50.895 --> 01:02:53.415
which allows school to use this contract

1408
01:02:53.415 --> 01:02:54.775
however they want to.

1409
01:02:55.275 --> 01:03:00.055
Uh, it's, uh, it's not limiting any school based on, um,

1410
01:03:00.715 --> 01:03:03.335
uh, uh, uh, DI City or anything like that.

1411
01:03:03.565 --> 01:03:06.215
This is just a requirement contract. So a school has budget.

1412
01:03:06.285 --> 01:03:07.575
They can use this contract

1413
01:03:07.595 --> 01:03:09.335
to buy any devices that they want.

1414
01:03:09.835 --> 01:03:11.855
So, uh, there's no limitation, uh,

1415
01:03:11.855 --> 01:03:14.135
based on this contract at this point time. But we

1416
01:03:14.135 --> 01:03:16.295
Don't, we don't do anything sort of

1417
01:03:17.125 --> 01:03:18.655
help under-resourced schools.

1418
01:03:19.265 --> 01:03:22.255
Lowly enrolled schools had their budgets to access

1419
01:03:22.795 --> 01:03:25.055
new technology or replace broken technology.

1420
01:03:26.335 --> 01:03:29.455
I, I think, uh, our, uh, chief Operating Officer, Emma,

1421
01:03:29.875 --> 01:03:32.455
she addressed that the budget has increased,

1422
01:03:32.455 --> 01:03:34.495
but I would ask Emma to respond on.

1423
01:03:39.685 --> 01:03:43.305
So, um, thanks for the question and thank you, Shaquille.

1424
01:03:43.765 --> 01:03:47.625
Um, so we do leave, we do give our school some options about

1425
01:03:47.625 --> 01:03:49.505
what types of devices they want for their students.

1426
01:03:49.645 --> 01:03:52.225
And so these devices, this Lenovo contract

1427
01:03:52.225 --> 01:03:55.505
and some of the others are devices that make it possible

1428
01:03:55.565 --> 01:03:57.265
for schools to purchase contracts.

1429
01:03:57.325 --> 01:03:59.985
And Central, they don't require any particular spend.

1430
01:04:00.365 --> 01:04:02.145
No, you know, that, but just so we're clear about the

1431
01:04:02.145 --> 01:04:04.665
amounts, um, I mean, as I said

1432
01:04:04.665 --> 01:04:06.905
before, we, we have continued where we can

1433
01:04:07.005 --> 01:04:10.345
to pour money directly into school budgets, both for staff,

1434
01:04:10.365 --> 01:04:11.945
but also for other costs like this.

1435
01:04:11.965 --> 01:04:14.145
We have increased those dollars over time.

1436
01:04:14.685 --> 01:04:16.145
We have held schools harmless

1437
01:04:16.145 --> 01:04:18.465
that have lost enrollment at the beginning of this year.

1438
01:04:19.085 --> 01:04:20.985
Um, we, we do actually have a lot

1439
01:04:20.985 --> 01:04:23.545
of devices in our schools at this moment in time.

1440
01:04:23.645 --> 01:04:24.665
Is the, is the truth.

1441
01:04:25.015 --> 01:04:27.025
That doesn't mean there might not be some places

1442
01:04:27.075 --> 01:04:28.105
where that's not true.

1443
01:04:28.485 --> 01:04:29.785
And I'd say two things about that.

1444
01:04:30.445 --> 01:04:34.065
One is going into the winter as a test of the system,

1445
01:04:34.605 --> 01:04:36.185
we are having all of our schools

1446
01:04:36.205 --> 01:04:39.265
and all of our superintendents at the actual school level

1447
01:04:39.885 --> 01:04:42.995
do a, um, remote learning test.

1448
01:04:43.095 --> 01:04:44.435
But a piece of that is going

1449
01:04:44.435 --> 01:04:46.315
to be do you have devices for your students?

1450
01:04:46.375 --> 01:04:48.155
Do they have devices? Do you have devices you

1451
01:04:48.155 --> 01:04:49.235
can send home for your students?

1452
01:04:49.735 --> 01:04:53.115
And the case of an actual remote learning need, we think

1453
01:04:53.115 --> 01:04:55.355
that's going to give us good data at the school

1454
01:04:55.535 --> 01:04:58.955
and superintendent level in terms of where there are needs

1455
01:04:59.015 --> 01:05:00.675
and where we really hold schools to it.

1456
01:05:00.675 --> 01:05:02.475
They still think they need additional devices.

1457
01:05:03.015 --> 01:05:04.835
We do then think there, there is funding

1458
01:05:04.855 --> 01:05:06.795
and budgets for that where there is not,

1459
01:05:07.095 --> 01:05:09.555
our schools will come to our division of school leadership

1460
01:05:09.695 --> 01:05:11.715
and note where they think they have a real need

1461
01:05:11.715 --> 01:05:13.235
that there can't be space for in their budget.

1462
01:05:13.295 --> 01:05:15.475
And we, we will take a look at that as well.

1463
01:05:15.815 --> 01:05:17.885
And this test we're doing is gonna happen next week,

1464
01:05:17.945 --> 01:05:19.245
and we should have a better sense of that.

1465
01:05:19.395 --> 01:05:20.805
Okay. Thank you. That's really helpful information.

1466
01:05:20.805 --> 01:05:23.085
And within that test renewing, is there, um,

1467
01:05:23.305 --> 01:05:26.405
are you also assessing the, like, the status

1468
01:05:26.465 --> 01:05:27.805
of the devices in terms of whether

1469
01:05:27.805 --> 01:05:29.885
or not they're functioning, like to ensure

1470
01:05:29.885 --> 01:05:32.125
that schools are not distributing devices that don't work?

1471
01:05:33.065 --> 01:05:34.725
Yes. So part of good question.

1472
01:05:35.565 --> 01:05:38.085
Um, part of the, the part, part

1473
01:05:38.085 --> 01:05:40.245
of the evaluation we're doing next week.

1474
01:05:41.975 --> 01:05:43.265
Yeah, next week, part

1475
01:05:43.265 --> 01:05:44.265
of the evaluation we're doing next

1476
01:05:44.265 --> 01:05:45.305
week, weeks are going very quickly.

1477
01:05:45.535 --> 01:05:47.785
Part of the evaluation we're doing next week is all students

1478
01:05:47.805 --> 01:05:49.025
are going to need to log on.

1479
01:05:49.025 --> 01:05:50.665
So it's going to be a test of does the device

1480
01:05:50.665 --> 01:05:51.785
work, whatever device they're using.

1481
01:05:51.785 --> 01:05:54.025
It might not be our device, but does the device work?

1482
01:05:54.125 --> 01:05:55.225
Do they know how to log on?

1483
01:05:55.225 --> 01:05:56.585
Do the teachers know how to post an assignment?

1484
01:05:56.605 --> 01:05:57.865
Do the students know how to do one?

1485
01:05:58.165 --> 01:06:01.505
So it should test each of those pieces of the system,

1486
01:06:02.165 --> 01:06:03.625
uh, for usage.

1487
01:06:03.965 --> 01:06:08.705
And how granular is like, I guess I, I, is is the data

1488
01:06:08.705 --> 01:06:12.545
that's collected through that attached to IDs specifically?

1489
01:06:15.695 --> 01:06:19.635
Yes. We will be looking down to the school level.

1490
01:06:19.975 --> 01:06:22.195
So principals can know what's happening in their school by,

1491
01:06:22.195 --> 01:06:23.875
by whether or not they're working student

1492
01:06:23.975 --> 01:06:26.445
by student, student by student. Okay.

1493
01:06:26.785 --> 01:06:28.045
We, we, we'll, I think some

1494
01:06:28.045 --> 01:06:29.365
of this could be held to a, at a briefing.

1495
01:06:29.365 --> 01:06:32.685
Okay. So, um, I, I want it to be give some latitude to,

1496
01:06:32.685 --> 01:06:35.405
you know, have some questions, but, um, I think some

1497
01:06:35.405 --> 01:06:37.005
of this is more appropriate for a, a a,

1498
01:06:37.085 --> 01:06:38.605
a specific briefing on some of these topics.

1499
01:06:39.025 --> 01:06:41.655
Is there anyone other panel members?

1500
01:06:41.655 --> 01:06:43.215
Panel members, well, let me go around

1501
01:06:43.215 --> 01:06:44.935
and make sure there's no other panel member who wishes

1502
01:06:45.075 --> 01:06:47.455
to speak first and then come back.

1503
01:06:48.075 --> 01:06:49.695
Uh, yes. Panel member. Um,

1504
01:06:51.445 --> 01:06:53.705
Ca Ca i, I don't know, ca

1505
01:06:54.575 --> 01:06:57.545
Well actually, Laura had her hands up even before,

1506
01:06:59.015 --> 01:07:01.395
So you wanna yield the floor to Yeah, go ahead.

1507
01:07:01.935 --> 01:07:04.835
You sure? Yeah. Okay. I move this forward. Sure.

1508
01:07:08.555 --> 01:07:10.785
Thank you. Uh, panel member Cass. Ready.

1509
01:07:11.845 --> 01:07:16.265
Um, I would like to, uh, reiterate some comments about

1510
01:07:17.425 --> 01:07:19.945
a couple of, um, agenda items

1511
01:07:20.125 --> 01:07:24.545
and also, um, asks questions on a couple of others,

1512
01:07:26.115 --> 01:07:29.955
um, on agenda item number two.

1513
01:07:30.375 --> 01:07:32.755
Um, really appreciate the chancellor's comments

1514
01:07:33.655 --> 01:07:36.355
and, uh, not trying in any way to pile on.

1515
01:07:36.735 --> 01:07:40.475
Um, but our office would really like

1516
01:07:40.475 --> 01:07:42.635
to uplift the public comments tonight on

1517
01:07:42.635 --> 01:07:43.755
agenda item number two.

1518
01:07:44.775 --> 01:07:46.115
And reiterate something

1519
01:07:46.115 --> 01:07:48.955
that I did mention in a recent meeting with the chancellor,

1520
01:07:49.415 --> 01:07:54.235
um, that our office has heard, um, from multiple teachers

1521
01:07:54.235 --> 01:07:57.525
and principals, um, on MAP testing.

1522
01:07:58.595 --> 01:08:01.815
And they have almost all told us, um,

1523
01:08:02.125 --> 01:08:05.255
that while measuring student progress is important

1524
01:08:05.475 --> 01:08:08.855
and essential, that these particular assessments,

1525
01:08:08.955 --> 01:08:13.895
map assessments, which are mandated three times a year, take

1526
01:08:14.495 --> 01:08:16.205
valuable time, resources

1527
01:08:16.345 --> 01:08:20.045
and staff capacity away from instruction

1528
01:08:21.275 --> 01:08:24.885
with no obvious benefit over less intrusive

1529
01:08:24.885 --> 01:08:26.045
assessment options.

1530
01:08:27.985 --> 01:08:31.245
And without any New York City specific data

1531
01:08:31.865 --> 01:08:34.885
on the impact these assessments have had on student

1532
01:08:35.325 --> 01:08:39.495
outcomes, I wanna reiterate what others have said

1533
01:08:39.835 --> 01:08:43.855
and uplift the idea that it is time to pause

1534
01:08:44.675 --> 01:08:49.175
and reassess whether investing another $15 million into

1535
01:08:49.175 --> 01:08:50.935
these assessments make sense.

1536
01:08:50.955 --> 01:08:55.305
At this point, these assessments were introduced to capture

1537
01:08:55.825 --> 01:08:57.665
pandemic learning, loss and recovery.

1538
01:08:59.005 --> 01:09:01.065
And what data do we have on the benefits

1539
01:09:01.065 --> 01:09:04.625
of these assessments before we enter into another five

1540
01:09:04.625 --> 01:09:05.665
year contract?

1541
01:09:07.375 --> 01:09:11.795
Um, I'd like to ask about agenda item number four.

1542
01:09:13.515 --> 01:09:17.335
Um, it was a little over two years ago that

1543
01:09:18.075 --> 01:09:19.575
former deputy chancellor,

1544
01:09:19.605 --> 01:09:22.855
Kara Med dismissed instructional coordinators from their

1545
01:09:22.855 --> 01:09:24.895
roles in providing three K

1546
01:09:24.895 --> 01:09:26.015
and pre-K programs

1547
01:09:26.015 --> 01:09:27.855
with professional development and support.

1548
01:09:29.405 --> 01:09:32.345
Um, this mtac has been around for a while.

1549
01:09:32.345 --> 01:09:33.625
It's definitely not new,

1550
01:09:34.985 --> 01:09:37.285
but I guess, um, it would be good to know,

1551
01:09:37.385 --> 01:09:41.445
is this the only remaining source of staff development, um,

1552
01:09:41.675 --> 01:09:44.205
that these three K and pre-K providers have?

1553
01:09:44.265 --> 01:09:47.925
Is it just these vendors, um, that are providing WIM

1554
01:09:47.955 --> 01:09:49.325
with the, um, the professional

1555
01:09:49.325 --> 01:09:50.685
development they need at this point?

1556
01:09:51.555 --> 01:09:55.685
What, if any, other supports do our essential CBO early

1557
01:09:55.685 --> 01:09:58.765
childhood education providers have in terms

1558
01:09:58.865 --> 01:10:02.245
of instructional support other than these contracts?

1559
01:10:03.785 --> 01:10:08.665
Um, on agenda item number five, um, super glad to see this.

1560
01:10:09.405 --> 01:10:13.705
Um, and glad to hear recently from, um,

1561
01:10:13.785 --> 01:10:18.105
deputy Chancellor Fody that the $25 million investment in,

1562
01:10:18.105 --> 01:10:21.985
in-house special education and skis classes is happening.

1563
01:10:23.145 --> 01:10:25.265
Um, it would be great, um,

1564
01:10:25.445 --> 01:10:27.905
if the panel could get an update on the current number

1565
01:10:28.445 --> 01:10:32.425
of preschool age children with disabilities, still waiting

1566
01:10:32.605 --> 01:10:36.025
for a special education preschool seat nearly two months

1567
01:10:36.075 --> 01:10:37.945
after the start of the current school year.

1568
01:10:39.095 --> 01:10:42.555
And finally, um, I would like to, um,

1569
01:10:42.745 --> 01:10:45.195
provide a last comment on agenda item number six.

1570
01:10:46.555 --> 01:10:48.895
Um, I want to uplift, um,

1571
01:10:48.925 --> 01:10:51.815
what the panel member from the Bronx, um, said earlier.

1572
01:10:52.965 --> 01:10:55.725
I want to thank Chief Moran for his work on this

1573
01:10:56.305 --> 01:10:57.925
and would just like to mention, um,

1574
01:10:58.085 --> 01:10:59.645
a few things about this contract.

1575
01:11:00.635 --> 01:11:04.335
Um, the contract with River Bay dates to 1971

1576
01:11:04.965 --> 01:11:09.335
when natural gas fueled co-generation plants were reviewed

1577
01:11:09.595 --> 01:11:13.015
as a green alternative to energy sources such

1578
01:11:13.085 --> 01:11:14.325
as coal and oil.

1579
01:11:15.025 --> 01:11:16.365
But that was a long time ago.

1580
01:11:17.645 --> 01:11:20.185
And as our office mentioned previously in the recent

1581
01:11:20.585 --> 01:11:24.505
contracts briefing, the vendor has a wage theft violation

1582
01:11:24.615 --> 01:11:27.305
that has landed them on our employer wall of shame.

1583
01:11:27.755 --> 01:11:31.005
There is a pending wage theft lawsuit noted in

1584
01:11:31.005 --> 01:11:32.285
the RA as well.

1585
01:11:33.945 --> 01:11:35.995
Therefore, we are super glad to see

1586
01:11:36.105 --> 01:11:38.835
that DOE has followed up on our recommendation at the

1587
01:11:39.035 --> 01:11:40.315
briefing to take this opportunity

1588
01:11:40.815 --> 01:11:43.915
to evaluate whether electrification might be an alternative

1589
01:11:43.915 --> 01:11:46.675
for these schools with a new feasibility study.

1590
01:11:47.335 --> 01:11:48.955
And by reducing the contract term

1591
01:11:49.855 --> 01:11:52.805
to one year from five years to allow the Department

1592
01:11:52.805 --> 01:11:54.485
of Education to evaluate that study

1593
01:11:54.505 --> 01:11:57.725
before entering into a long-term contract.

1594
01:11:59.035 --> 01:12:01.925
This is especially relevant given the mayor's leading the

1595
01:12:01.925 --> 01:12:05.525
charge commitment of $4 billion two years ago

1596
01:12:05.985 --> 01:12:07.085
to electrify schools.

1597
01:12:08.545 --> 01:12:12.085
New York's electrical grid is in transition right now

1598
01:12:12.825 --> 01:12:15.805
as we move toward greener energy sources such

1599
01:12:15.805 --> 01:12:16.885
as offshore wind.

1600
01:12:17.935 --> 01:12:20.515
If our goal is truly to rid our schools

1601
01:12:20.535 --> 01:12:22.355
of dependence on fossil fuels,

1602
01:12:23.025 --> 01:12:26.085
an investment like this would be a good one as we work

1603
01:12:26.085 --> 01:12:27.765
to meet our city's climate targets

1604
01:12:28.145 --> 01:12:31.065
and decarbonize our grid. Thank

1605
01:12:31.065 --> 01:12:32.065
You. Thank you.

1606
01:12:32.065 --> 01:12:36.335
iia.

1607
01:12:36.335 --> 01:12:39.055
There's some responses from the, the, uh, department

1608
01:12:47.505 --> 01:12:49.005
To all the Panel to all the panel.

1609
01:12:49.005 --> 01:12:50.005
Okay. I thought,

1610
01:12:51.405 --> 01:12:52.405
I Think that well wait minute. Well

1611
01:12:52.405 --> 01:12:53.885
hold it. Are there any other panel members

1612
01:12:53.885 --> 01:12:54.965
before you start, any other panel

1613
01:12:54.965 --> 01:12:57.855
members who wish to comment? Oh, I'm sorry. Come here.

1614
01:12:57.985 --> 01:12:59.735
Sorry. Can I just jump in really quickly?

1615
01:12:59.825 --> 01:13:01.535
We're gonna ask the team if we could just hold

1616
01:13:01.535 --> 01:13:03.095
until the panel members make their comments

1617
01:13:03.235 --> 01:13:04.415
and then we will all respond

1618
01:13:04.415 --> 01:13:05.615
appropriately. Thank you so much.

1619
01:13:06.465 --> 01:13:07.535
Thank you so much.

1620
01:13:07.955 --> 01:13:12.235
Um, so I wanted

1621
01:13:12.335 --> 01:13:14.555
to let everybody know that when

1622
01:13:15.275 --> 01:13:19.995
I am reviewing these contracts, I try to keep our vision

1623
01:13:20.135 --> 01:13:22.285
and mission at heart.

1624
01:13:22.545 --> 01:13:25.045
And so I'd like to read to you all quickly

1625
01:13:25.235 --> 01:13:28.725
what is on the panel for education policy website.

1626
01:13:29.405 --> 01:13:30.425
The panel believes

1627
01:13:30.425 --> 01:13:32.705
that education is a fundamental human right.

1628
01:13:33.405 --> 01:13:36.865
It is our duty to ensure that all students have equal access

1629
01:13:37.005 --> 01:13:38.025
to the opportunity

1630
01:13:38.165 --> 01:13:41.145
and resources needed to reach their full potential.

1631
01:13:41.925 --> 01:13:45.665
The P'S commitment to New York City families is

1632
01:13:45.665 --> 01:13:48.025
to forge the key to a brighter future

1633
01:13:48.125 --> 01:13:49.985
for all families of New York City.

1634
01:13:51.315 --> 01:13:52.535
The panel is committed

1635
01:13:52.655 --> 01:13:54.895
to ensuring every student has an education

1636
01:13:54.895 --> 01:13:58.415
of the highest quality, fortified by a curriculum

1637
01:13:58.475 --> 01:13:59.855
of inclusion and pride,

1638
01:14:00.735 --> 01:14:04.035
and that children will be prepared for success in college

1639
01:14:04.175 --> 01:14:06.715
and career imbued with a sense of action

1640
01:14:06.775 --> 01:14:09.715
and engagement as a responsible member of society.

1641
01:14:11.925 --> 01:14:16.245
I have looked at this language at least six times in the

1642
01:14:16.245 --> 01:14:18.605
last few days, and I try to really keep

1643
01:14:18.605 --> 01:14:20.205
that at the heart of what I do.

1644
01:14:21.435 --> 01:14:25.815
So when I see contracts like the one that was refu removed,

1645
01:14:26.165 --> 01:14:29.375
item number one for $17 million of testing,

1646
01:14:30.325 --> 01:14:33.975
item number two, $15 million of testing.

1647
01:14:35.155 --> 01:14:40.035
And item number 14, which may have just sort of been

1648
01:14:40.035 --> 01:14:44.035
outside of anybody's radar for 210,000 for delivery

1649
01:14:44.555 --> 01:14:47.875
services, of testing materials,

1650
01:14:49.265 --> 01:14:52.905
I add that up to $32,210,000.

1651
01:14:53.125 --> 01:14:56.995
And I wonder to myself, where could that money go?

1652
01:14:57.575 --> 01:15:02.455
And then I look at, and

1653
01:15:02.455 --> 01:15:04.415
then I look at the rest of these contracts,

1654
01:15:04.915 --> 01:15:06.375
things like family

1655
01:15:06.515 --> 01:15:08.535
and community engagement services

1656
01:15:08.595 --> 01:15:13.535
for early childhood education, $150,000

1657
01:15:16.095 --> 01:15:20.105
special education enhancement, 1.7 million

1658
01:15:22.345 --> 01:15:26.195
extension for early learn services, 8 million

1659
01:15:28.175 --> 01:15:32.535
UPK, half day and UPK extensions, 1.3 million.

1660
01:15:33.655 --> 01:15:35.395
And then education programs

1661
01:15:35.415 --> 01:15:38.435
for students initiatives 112,000.

1662
01:15:39.455 --> 01:15:43.665
That comes to barely one third of

1663
01:15:43.665 --> 01:15:45.105
what we're spending on testing.

1664
01:15:51.495 --> 01:15:53.975
I think we really need to think about our values

1665
01:15:54.235 --> 01:15:57.615
and mission when we're looking at these contracts.

1666
01:15:57.755 --> 01:16:01.175
And so I'll just stop there. Thank you. Okay.

1667
01:16:02.605 --> 01:16:04.545
Any other, any other panel members wish to comment?

1668
01:16:06.605 --> 01:16:07.675
Panel member Sheard.

1669
01:16:09.225 --> 01:16:10.295
Thank you, chair Faulkner.

1670
01:16:10.295 --> 01:16:11.615
I'll make this one quick 'cause I

1671
01:16:11.615 --> 01:16:12.935
forgot to add it the first time.

1672
01:16:13.475 --> 01:16:16.495
Um, but I've mentioned over the years, um,

1673
01:16:16.565 --> 01:16:19.535
that we really do, and this is agenda item number seven,

1674
01:16:20.475 --> 01:16:24.775
we really do need to take a look at, um, you know,

1675
01:16:25.155 --> 01:16:29.145
how we, um, fund, um,

1676
01:16:29.335 --> 01:16:32.665
Bard High School early college in a way where we don't have

1677
01:16:32.665 --> 01:16:35.145
to keep coming back here every year

1678
01:16:35.205 --> 01:16:39.425
or every other year, um, you know, to, to fund,

1679
01:16:40.285 --> 01:16:43.825
um, you know, this particular program that, um,

1680
01:16:44.405 --> 01:16:47.225
is wildly popular throughout the city, right?

1681
01:16:47.525 --> 01:16:50.225
We, we've opened, uh, Bard High School,

1682
01:16:50.225 --> 01:16:51.225
early college in Bronx,

1683
01:16:51.285 --> 01:16:54.105
and we've recently opened, uh, Bard High School,

1684
01:16:54.355 --> 01:16:55.625
early college in Brooklyn.

1685
01:16:56.325 --> 01:17:00.145
And I am sure that the majority of the lion's share

1686
01:17:00.145 --> 01:17:04.265
of this 1.8 million, um, is really going into making sure

1687
01:17:04.295 --> 01:17:08.545
that the college part of Bard High School early college, uh,

1688
01:17:08.685 --> 01:17:11.485
is, is fully funded, um, for the Bronx

1689
01:17:11.505 --> 01:17:12.845
and Brooklyn, which is cool.

1690
01:17:13.585 --> 01:17:18.365
Um, but it, you know, we, we are guaranteeing,

1691
01:17:19.225 --> 01:17:20.685
uh, that our students

1692
01:17:20.875 --> 01:17:24.965
that graduate New York City public high schools, uh, will,

1693
01:17:25.185 --> 01:17:30.165
you know, can automatically go to a cuny um, school.

1694
01:17:30.985 --> 01:17:34.445
And, you know, there's, there's no question about what

1695
01:17:34.445 --> 01:17:35.925
that costs or anything.

1696
01:17:35.985 --> 01:17:39.005
We, we made that commitment and we said we're gonna do it.

1697
01:17:39.825 --> 01:17:43.925
And I am just asking a chancellor if perhaps, um,

1698
01:17:44.825 --> 01:17:49.125
you can have the types of conversations with, um,

1699
01:17:49.755 --> 01:17:52.565
CUNY with state, um, and with Bard,

1700
01:17:52.565 --> 01:17:57.005
and let's figure out how we can, uh, sustainably fund,

1701
01:17:57.745 --> 01:18:00.685
um, the Bard High School early college programs across the

1702
01:18:00.685 --> 01:18:05.325
city in a way, um, where funding for both sides of

1703
01:18:05.325 --> 01:18:07.165
that program, the, the high school side

1704
01:18:07.265 --> 01:18:10.925
and the early college side, um, are just fully funded,

1705
01:18:11.585 --> 01:18:13.285
um, and sustainably.

1706
01:18:13.345 --> 01:18:14.345
So. Thank you.

1707
01:18:16.985 --> 01:18:20.485
Any other panel members? Yes, panel members.

1708
01:18:22.765 --> 01:18:24.615
Good. Um, good evening.

1709
01:18:25.715 --> 01:18:29.815
So what I heard when I was listening to the, the

1710
01:18:30.575 --> 01:18:34.215
comments about assessments and receiving the results

1711
01:18:34.515 --> 01:18:37.695
and the mechanisms within New York City Public Schools

1712
01:18:37.755 --> 01:18:40.135
to address, which is, um, school leadership team

1713
01:18:40.135 --> 01:18:42.535
and district leadership team, what I hear is

1714
01:18:42.535 --> 01:18:46.015
that there's a breakdown in the functionality

1715
01:18:46.355 --> 01:18:49.655
and the integrity of the way these groups function,

1716
01:18:49.955 --> 01:18:52.655
and that these teams are not actually doing the job

1717
01:18:52.655 --> 01:18:55.455
that they're supposed to, which is mandated in New York

1718
01:18:55.455 --> 01:18:57.095
State Education law 25 90.

1719
01:18:58.035 --> 01:19:01.615
And so when we hear teachers telling us that are supposed

1720
01:19:01.615 --> 01:19:04.055
to be on these teams, and we hear parents telling us

1721
01:19:04.055 --> 01:19:05.455
that they're supposed to be on these teams

1722
01:19:05.635 --> 01:19:07.415
and we hear CEC members telling us,

1723
01:19:07.415 --> 01:19:09.375
and they're supposed to be on these teams, then

1724
01:19:09.375 --> 01:19:11.175
that's a breakdown in the,

1725
01:19:11.355 --> 01:19:13.695
the engagement structure developed

1726
01:19:13.995 --> 01:19:16.095
to meet the mandate of the state law.

1727
01:19:16.475 --> 01:19:18.415
So I think the better conversation is

1728
01:19:18.595 --> 01:19:21.175
how do we revisit S SLT than DOT

1729
01:19:21.475 --> 01:19:23.815
and ensure that they're functioning with integrity,

1730
01:19:24.315 --> 01:19:26.815
and that they are actually getting the information

1731
01:19:26.995 --> 01:19:29.095
and having the conversations that they're supposed to

1732
01:19:29.275 --> 01:19:31.215
and not being given a document to sign

1733
01:19:31.215 --> 01:19:32.535
that they have no idea what it means.

1734
01:19:33.415 --> 01:19:37.455
Second, um, the assessments, the assessments are not

1735
01:19:37.475 --> 01:19:39.895
for everybody, and we spend a whole lot of money on it.

1736
01:19:40.275 --> 01:19:42.575
Um, I don't really see a whole lot being done

1737
01:19:42.675 --> 01:19:45.295
to differentiate the assessments for students

1738
01:19:45.295 --> 01:19:48.695
that learn differently, to differentiate the assessments

1739
01:19:48.835 --> 01:19:50.775
for students that may be alternately assessed

1740
01:19:50.995 --> 01:19:52.415
to differentiate for students

1741
01:19:52.415 --> 01:19:53.855
that may speak a different language.

1742
01:19:54.235 --> 01:19:57.325
And that work falls on the teachers with

1743
01:19:57.325 --> 01:19:58.645
what time do they have left.

1744
01:19:59.875 --> 01:20:01.135
So I really wanna, like,

1745
01:20:01.275 --> 01:20:04.375
and again, this is an SLT conversation about assessment

1746
01:20:04.755 --> 01:20:07.015
and time and doing school-based option

1747
01:20:07.135 --> 01:20:09.925
where you're giving teachers the time to then have

1748
01:20:10.075 --> 01:20:12.645
that training in the beginning or whatever part of the day,

1749
01:20:12.905 --> 01:20:14.365
and to alter your school schedule.

1750
01:20:14.425 --> 01:20:16.485
And that's a very individualized conversation

1751
01:20:16.945 --> 01:20:18.085
that's not happening

1752
01:20:18.085 --> 01:20:20.125
because we've been hearing this at

1753
01:20:20.125 --> 01:20:21.165
least for the last four years.

1754
01:20:22.625 --> 01:20:24.965
Um, and then the last thing, co-Op City,

1755
01:20:26.935 --> 01:20:29.265
everybody knows co-Op City is my heart, right?

1756
01:20:29.735 --> 01:20:31.185
I've been here every single year

1757
01:20:31.205 --> 01:20:33.465
for the last six years talking about co-op city.

1758
01:20:34.485 --> 01:20:36.675
Happy to vote yes for one year extension,

1759
01:20:37.375 --> 01:20:38.835
but like the other contracts,

1760
01:20:38.835 --> 01:20:40.035
like when we talk about our budget

1761
01:20:40.255 --> 01:20:43.275
and how we're given something that already has to happen,

1762
01:20:43.275 --> 01:20:45.715
whether we vote yes or no, and please vote yes

1763
01:20:45.715 --> 01:20:47.035
because we have to keep moving.

1764
01:20:47.825 --> 01:20:51.275
When do we stop the system to account for the students

1765
01:20:51.305 --> 01:20:54.475
that we serve versus keeping it functioning to say

1766
01:20:54.475 --> 01:20:56.715
that it's functioning and doing a job that it's supposed

1767
01:20:56.715 --> 01:20:57.835
to do, but not doing it well.

1768
01:20:58.455 --> 01:21:00.715
So I would love for us to yes to this

1769
01:21:00.715 --> 01:21:03.355
so we can have hot heat right in the winter,

1770
01:21:04.055 --> 01:21:07.675
but to have the conversation about what would it entail

1771
01:21:07.815 --> 01:21:11.995
to upgrade to something modern that will function

1772
01:21:12.215 --> 01:21:13.595
for all the schools on the campus.

1773
01:21:13.975 --> 01:21:16.635
And I understand that there's a lot of concerns faced this,

1774
01:21:16.635 --> 01:21:18.755
and these are great SLT conversations.

1775
01:21:18.755 --> 01:21:19.755
Thank you.

1776
01:21:20.235 --> 01:21:24.075
Thank you. Any other, okay, uh, chance?

1777
01:21:25.085 --> 01:21:27.545
Uh, so I wanna thank everybody for their comments.

1778
01:21:27.765 --> 01:21:31.025
Um, you know, this is the type of conversation

1779
01:21:31.135 --> 01:21:34.505
that we enjoy having and really hearing your, your insight.

1780
01:21:34.525 --> 01:21:36.905
And these are the things that we then take back to the table

1781
01:21:37.005 --> 01:21:39.385
and we, we really give thought to as a team.

1782
01:21:39.765 --> 01:21:42.625
And we have some of, we have our folks here who are ready

1783
01:21:42.625 --> 01:21:43.945
to respond to some of these things.

1784
01:21:43.965 --> 01:21:46.025
And so I'm going to ask, I know that we've,

1785
01:21:46.245 --> 01:21:47.425
uh, communicated already.

1786
01:21:47.425 --> 01:21:49.425
We have a number of people who are ready to respond.

1787
01:21:49.485 --> 01:21:53.305
So if our team can respond, we have Deputy Chancellor Fody,

1788
01:21:53.305 --> 01:21:54.945
we have Deputy Chancellor Hawkins.

1789
01:21:55.445 --> 01:21:57.145
Um, if, if you two can come up

1790
01:21:57.145 --> 01:21:59.865
and give some responses to some of what was raised here,

1791
01:22:03.755 --> 01:22:05.095
one, um, I just wanted

1792
01:22:05.095 --> 01:22:07.815
to quickly address Laura's question about preschool special

1793
01:22:07.815 --> 01:22:09.135
education play placements.

1794
01:22:09.345 --> 01:22:10.935
Laura, I did not look at the numbers today,

1795
01:22:10.935 --> 01:22:12.855
but what I can tell you is that we're tracking them closely.

1796
01:22:13.355 --> 01:22:16.455
We are up to date in terms of, uh, rolling giving.

1797
01:22:16.715 --> 01:22:19.215
Um, we are both doing rolling openings

1798
01:22:19.355 --> 01:22:21.815
and rolling, um, offers of seats.

1799
01:22:22.075 --> 01:22:23.375
So, so far so good.

1800
01:22:23.395 --> 01:22:26.495
We are preparing for another heavy lift in January of,

1801
01:22:26.555 --> 01:22:29.895
of opening up, up the remaining bulk of the classrooms.

1802
01:22:29.995 --> 01:22:33.135
But right now, kids are, we're are getting the seats

1803
01:22:33.135 --> 01:22:35.775
that they need and, um, we're able to accommodate every,

1804
01:22:35.775 --> 01:22:36.855
every child who needs one.

1805
01:22:38.025 --> 01:22:39.445
Not, not a wait list, no,

1806
01:22:40.105 --> 01:22:42.325
but every day another kid needs a placement, right?

1807
01:22:42.425 --> 01:22:44.205
So it's, it's a moving target,

1808
01:22:44.305 --> 01:22:46.205
but we're positioned to keep up with the movement.

1809
01:22:46.655 --> 01:22:47.125
Thank you.

1810
01:22:52.355 --> 01:22:54.005
Good evening. This is my first

1811
01:22:54.035 --> 01:22:55.725
meeting, so happy to meet you.

1812
01:22:55.725 --> 01:22:59.845
All right. Thank you. Um, d DC Hawkins.

1813
01:22:59.845 --> 01:23:02.165
So wanting to respond your, your, your point as well

1814
01:23:02.165 --> 01:23:05.805
around supports we're providing to our DEC support team,

1815
01:23:06.125 --> 01:23:07.125
specifically our instructional

1816
01:23:07.125 --> 01:23:08.485
coordinators and social workers.

1817
01:23:09.365 --> 01:23:12.775
This one contract is just a one of many supports

1818
01:23:12.775 --> 01:23:14.695
that we are providing to really build their muscles

1819
01:23:14.695 --> 01:23:16.495
around family engagement strategies.

1820
01:23:16.645 --> 01:23:20.055
However, there is a structure within the team where each

1821
01:23:20.075 --> 01:23:21.175
of the social work

1822
01:23:21.175 --> 01:23:23.575
and instructional quarters are actually on a team.

1823
01:23:23.725 --> 01:23:26.135
It's called a pod under a leadership coach.

1824
01:23:26.725 --> 01:23:29.775
They work in concert with them to provide direct coaching

1825
01:23:29.875 --> 01:23:31.815
to leadership at the program level,

1826
01:23:31.875 --> 01:23:34.295
but also coaching for the IC and social worker as well.

1827
01:23:34.755 --> 01:23:37.255
We have asynchronous synchronous training that we provide,

1828
01:23:37.315 --> 01:23:40.775
not just around clearly our curriculum literacy,

1829
01:23:40.775 --> 01:23:42.455
family engagement strategies,

1830
01:23:42.475 --> 01:23:44.175
but also those soft skills that they need

1831
01:23:44.175 --> 01:23:45.255
to do the work long term.

1832
01:23:46.075 --> 01:23:47.695
And we offer coursework

1833
01:23:47.795 --> 01:23:50.335
and trainings that, that provide them CTLE

1834
01:23:50.335 --> 01:23:51.375
and EU credits

1835
01:23:51.635 --> 01:23:53.535
so they can continue their professional

1836
01:23:53.535 --> 01:23:55.015
expertise, um, and their journey.

1837
01:23:55.155 --> 01:23:59.095
So there is a host of, uh, supports training

1838
01:23:59.275 --> 01:24:02.535
and coaching that we provide our staff in turn

1839
01:24:02.535 --> 01:24:05.375
that they also provide our providers at CBOs

1840
01:24:05.975 --> 01:24:07.095
district schools, pre-K centers,

1841
01:24:07.115 --> 01:24:08.895
and all the settings that we provide early

1842
01:24:08.895 --> 01:24:10.095
childhood programming in.

1843
01:24:10.825 --> 01:24:13.315
Just to clarify, those ics are DOE staff,

1844
01:24:13.315 --> 01:24:14.515
or those are contracted workers?

1845
01:24:14.515 --> 01:24:17.225
They're DOE staff. You're welcome.

1846
01:24:26.445 --> 01:24:29.625
Um, in terms of the questions raised about, or the comments

1847
01:24:29.805 --> 01:24:31.585
and questions raised about DLT

1848
01:24:31.845 --> 01:24:36.105
and Bard, um, again, uh, panel member e you

1849
01:24:36.105 --> 01:24:37.665
and I have a long history

1850
01:24:37.665 --> 01:24:39.385
and we've talked about this, um, in,

1851
01:24:39.485 --> 01:24:41.185
in my previous roles as well.

1852
01:24:41.205 --> 01:24:44.025
And so I look forward to working with Deputy Chancellor Rux,

1853
01:24:44.435 --> 01:24:48.025
along with our, uh, executive, um, the director, uh,

1854
01:24:48.045 --> 01:24:51.465
Dr. Melendez on how we can actually strengthen that work.

1855
01:24:51.485 --> 01:24:52.785
And I know that that has started.

1856
01:24:52.925 --> 01:24:54.585
We know that Sharon Reer and Dr.

1857
01:24:54.945 --> 01:24:59.025
ux, um, had a, a really great, um, day of training,

1858
01:24:59.445 --> 01:25:01.905
and I think we need to continue that kind of work.

1859
01:25:01.965 --> 01:25:03.225
So I look forward to speaking with you

1860
01:25:03.225 --> 01:25:05.145
and other panel members and others families

1861
01:25:05.385 --> 01:25:07.225
and community members to seek their input.

1862
01:25:07.605 --> 01:25:09.585
And Panel member Shepherd, I will be honest with you

1863
01:25:09.585 --> 01:25:10.945
and say that we need to go back to the team

1864
01:25:10.945 --> 01:25:12.345
and really look at what you're speaking of.

1865
01:25:12.465 --> 01:25:14.145
I do not wanna speak from a place of ignorance,

1866
01:25:14.165 --> 01:25:15.225
but thank you for raising that

1867
01:25:15.645 --> 01:25:16.705
and, and we'll get back to you.

1868
01:25:17.995 --> 01:25:19.925
Okay, great. Are there any

1869
01:25:19.925 --> 01:25:20.965
other comments from panel members?

1870
01:25:22.225 --> 01:25:24.285
Are we ready to proceed to question?

1871
01:25:25.475 --> 01:25:26.725
Okay, let's, uh, proceed.

1872
01:25:32.635 --> 01:25:36.615
Um, I just wanna respond to, I think member Ali's comment

1873
01:25:37.005 --> 01:25:40.655
that, um, perhaps the vendor would be selling data.

1874
01:25:41.335 --> 01:25:44.825
I just wanna clarify, um, uh,

1875
01:25:45.445 --> 01:25:47.185
and that they release the data.

1876
01:25:47.885 --> 01:25:51.705
So just to clarify, um, educational law 2D prohibits,

1877
01:25:52.685 --> 01:25:54.345
um, let me just finish the statement

1878
01:25:54.345 --> 01:25:55.625
and then you can respond.

1879
01:25:56.125 --> 01:25:59.945
Um, that prohibits third party contracts from selling PII

1880
01:25:59.945 --> 01:26:01.345
or disclosing it for commercial

1881
01:26:01.405 --> 01:26:04.000
or marketing purposes, both, both the state law

1882
01:26:04.305 --> 01:26:06.805
and the right state regulations that implement that.

1883
01:26:07.345 --> 01:26:10.445
Um, we do make our vendors go through a data privacy review,

1884
01:26:10.545 --> 01:26:11.645
but they cannot use it

1885
01:26:11.665 --> 01:26:14.165
for marketing purposes under state law, right?

1886
01:26:14.945 --> 01:26:19.365
Except it happened. Okay. Time. Yeah, go ahead. Okay.

1887
01:26:20.625 --> 01:26:21.895
Thank you. I have a nuts

1888
01:26:21.895 --> 01:26:24.015
and bolts question about what we're about to do here.

1889
01:26:24.435 --> 01:26:25.935
Um, you know,

1890
01:26:26.075 --> 01:26:27.695
and this really springs from

1891
01:26:28.655 --> 01:26:31.535
actually an email you sent earlier this week, chair Buchner,

1892
01:26:31.635 --> 01:26:34.655
uh, requesting the specific verbiage of a contract.

1893
01:26:35.235 --> 01:26:37.095
Um, and I was alarmed to learn that

1894
01:26:37.725 --> 01:26:40.415
what we're voting on are not contracts that exist.

1895
01:26:40.985 --> 01:26:44.175
We're voting on pre contract pre contracts here.

1896
01:26:44.885 --> 01:26:47.965
Could somebody please like, clarify this?

1897
01:26:47.965 --> 01:26:51.455
Because yeah, we were unable to, you, y'all were unable

1898
01:26:51.455 --> 01:26:53.575
to supply us with the actual language.

1899
01:26:53.755 --> 01:26:56.095
We wanted the full specific contract of the full contract,

1900
01:26:56.875 --> 01:26:59.935
not because of privacy or discretionary issues

1901
01:26:59.935 --> 01:27:02.855
because it doesn't exist, um, yet.

1902
01:27:03.435 --> 01:27:06.525
So I guess I've been under the perception

1903
01:27:06.525 --> 01:27:08.405
that we've been voting on actual contracts,

1904
01:27:08.465 --> 01:27:11.165
but it seems like we're voting on concepts of contracts.

1905
01:27:11.505 --> 01:27:13.245
If somebody please, could, could correct me

1906
01:27:13.305 --> 01:27:17.605
or clarify what exactly it is we're voting on here.

1907
01:27:17.775 --> 01:27:20.255
Thank you. Mm-Hmm. Yep.

1908
01:27:21.545 --> 01:27:23.675
Good evening. All right.

1909
01:27:23.675 --> 01:27:26.115
I'll, uh, leave it to our chief procurement officer,

1910
01:27:26.455 --> 01:27:28.595
Alicia Oui, if I get this right,

1911
01:27:28.755 --> 01:27:31.035
'cause I'm always not positioned well to be heard.

1912
01:27:31.415 --> 01:27:33.835
Alicia Oui, chief Procurement Officer here at the DOE.

1913
01:27:34.215 --> 01:27:38.755
Um, so the, the vote that, that you are going

1914
01:27:38.755 --> 01:27:43.075
to render tonight is for us to move forward with a contract.

1915
01:27:43.415 --> 01:27:46.555
So we're not allowed to move forward with the development

1916
01:27:46.555 --> 01:27:49.835
of contracts without the panel's permission to move forward.

1917
01:27:50.215 --> 01:27:54.875
So this is why the contract is not developed at the moment.

1918
01:27:55.445 --> 01:27:59.555
There are steps in the process prior to us bringing items

1919
01:27:59.735 --> 01:28:04.035
to the panel, uh, data privacy clearances on both the, uh,

1920
01:28:04.055 --> 01:28:07.195
the technology side and on the legal side that has to occur,

1921
01:28:07.695 --> 01:28:10.795
but nothing is finalized until after the panel votes on it.

1922
01:28:11.425 --> 01:28:13.625
Does that answer your question?

1923
01:28:15.895 --> 01:28:19.065
This is where the gist of what we're voting on here

1924
01:28:19.845 --> 01:28:22.425
varies differently or, you know, from

1925
01:28:22.425 --> 01:28:24.105
what isn't actually in the contracts.

1926
01:28:24.405 --> 01:28:27.225
No. That, that would not occur.

1927
01:28:27.415 --> 01:28:28.505
What we communicate

1928
01:28:28.605 --> 01:28:31.745
and in terms of what's summarized in the, uh, request

1929
01:28:31.745 --> 01:28:33.745
for authorization does not vary.

1930
01:28:33.925 --> 01:28:37.265
We, we, we establish what those terms are prior

1931
01:28:37.645 --> 01:28:38.745
to bringing it to panel,

1932
01:28:38.805 --> 01:28:40.785
and we're not allowed to change it after the fact

1933
01:28:41.805 --> 01:28:43.575
Clarification. I appreciate it. Okay.

1934
01:28:44.285 --> 01:28:45.465
Any other questions? Yeah,

1935
01:28:45.465 --> 01:28:46.465
Panel andia.

1936
01:28:48.135 --> 01:28:49.355
So I have a question.

1937
01:28:49.675 --> 01:28:52.195
A, a few weeks ago, maybe it was a month ago, so ago now,

1938
01:28:52.495 --> 01:28:55.435
uh, we were discussing a contract that had to do

1939
01:28:55.435 --> 01:28:58.595
with reading materials being available in other languages.

1940
01:28:59.135 --> 01:29:04.005
And I'm wondering if there was so much pushback during

1941
01:29:04.005 --> 01:29:07.965
that conversation, because there is not actually a way

1942
01:29:07.985 --> 01:29:11.685
to negotiate that because the contract is written

1943
01:29:11.685 --> 01:29:14.645
after the money has already been voted on.

1944
01:29:15.315 --> 01:29:18.845
Okay, Sue, I I just wanna make a clarifying statement.

1945
01:29:19.145 --> 01:29:20.845
Um, a majority of the contracts

1946
01:29:20.845 --> 01:29:22.165
requirements contracts, right?

1947
01:29:22.505 --> 01:29:25.285
So the contract value is not a guaranteed value, not

1948
01:29:26.145 --> 01:29:27.885
in the case of requirements contracts.

1949
01:29:28.345 --> 01:29:32.285
So we have a contract, I, I believe it was for assessments,

1950
01:29:32.385 --> 01:29:34.045
and someone mentioned that we're,

1951
01:29:34.055 --> 01:29:36.085
we're giving away $15 million.

1952
01:29:36.305 --> 01:29:37.485
That's not the case.

1953
01:29:38.465 --> 01:29:42.085
The vendors are being paid for services that are rendered.

1954
01:29:42.865 --> 01:29:46.685
So there's no guarantee we have to establish estimates

1955
01:29:46.685 --> 01:29:49.205
for contract value in order to enter into the contract.

1956
01:29:49.265 --> 01:29:51.125
And, but it does not guarantee

1957
01:29:51.125 --> 01:29:54.205
that these vendors are actually going to be rendered,

1958
01:29:54.465 --> 01:29:56.005
uh, that amount of money.

1959
01:29:56.275 --> 01:30:00.565
It's usually based on past spend, right? It's an estimate.

1960
01:30:00.585 --> 01:30:02.205
And I know, Tom, you're gonna have your counter,

1961
01:30:02.205 --> 01:30:04.845
because you always say, well, if it's based on, um, past,

1962
01:30:05.075 --> 01:30:07.445
past spend and or historical spend, then

1963
01:30:07.445 --> 01:30:08.485
that means we're going to pay.

1964
01:30:08.485 --> 01:30:12.365
There's no guarantee of that, right? So just

1965
01:30:12.425 --> 01:30:14.085
So, so what's, the contract is developed,

1966
01:30:14.085 --> 01:30:15.285
how soon is it available

1967
01:30:17.715 --> 01:30:19.455
to be seen the full contract?

1968
01:30:20.235 --> 01:30:23.375
So, um, after panel there, there are a number

1969
01:30:23.375 --> 01:30:25.575
of steps in the process that have to occur.

1970
01:30:25.995 --> 01:30:28.975
It could take somewhere between two to three months

1971
01:30:29.035 --> 01:30:30.495
for the contract to be finalized

1972
01:30:30.515 --> 01:30:32.015
and registered with the controller.

1973
01:30:32.475 --> 01:30:35.815
If, if the, if anyone from the public is looking

1974
01:30:36.675 --> 01:30:39.815
or wants to see a, uh, a record of the contract,

1975
01:30:40.165 --> 01:30:43.015
they would have to request it, um, through our legal team.

1976
01:30:43.175 --> 01:30:44.335
I believe you would have to foil

1977
01:30:44.335 --> 01:30:49.335
it. Any additional questions?

1978
01:30:49.855 --> 01:30:53.655
I assume there might be. So any other que none? Oh, yes.

1979
01:30:57.155 --> 01:31:00.895
Go back to, back to the data and privacy part of it.

1980
01:31:00.895 --> 01:31:04.095
Because if we are contracted, you're not getting really,

1981
01:31:04.215 --> 01:31:06.295
I think it's legal for you to Yeah.

1982
01:31:06.295 --> 01:31:08.855
Yeah. I'm just gonna make a comment, um,

1983
01:31:09.385 --> 01:31:10.695
about the privacy, right?

1984
01:31:11.985 --> 01:31:14.655
There was one meeting that we had contracts about,

1985
01:31:14.825 --> 01:31:17.055
we're doing, uh, business with a parent

1986
01:31:17.165 --> 01:31:18.455
with the child, right?

1987
01:31:18.795 --> 01:31:21.175
Not the parent. So this goes back to data

1988
01:31:21.355 --> 01:31:23.455
and, uh, sharing data and information.

1989
01:31:23.795 --> 01:31:26.535
So if we are not doing business with the parent company,

1990
01:31:27.115 --> 01:31:28.495
but we are doing it with a child,

1991
01:31:28.875 --> 01:31:30.575
I'm just gonna call it a child by one

1992
01:31:30.575 --> 01:31:34.535
of the sub companies under the umbrella, our contract,

1993
01:31:34.795 --> 01:31:37.575
we can tell them you can't share the data, blah, blah, blah.

1994
01:31:37.875 --> 01:31:40.575
And we had this conversation that the parent company,

1995
01:31:40.755 --> 01:31:43.255
we cannot tell what the parent company to do.

1996
01:31:43.755 --> 01:31:48.495
So they still are sub going surround the law

1997
01:31:48.875 --> 01:31:51.335
and sharing and sharing that data privacy.

1998
01:31:51.835 --> 01:31:55.255
And as this agency, this is where people have issues

1999
01:31:55.255 --> 01:31:57.015
with the data privacy law.

2000
01:31:57.475 --> 01:31:58.695
Why don't we strengthen it?

2001
01:31:58.695 --> 01:32:01.525
They're, you, you know who the parent company is.

2002
01:32:02.185 --> 01:32:04.525
If you, if you wanna do business, you have

2003
01:32:04.525 --> 01:32:08.285
to ensure you don't sell or share, uh, privacy.

2004
01:32:08.985 --> 01:32:11.445
Or we go to someone else who will uphold it.

2005
01:32:11.645 --> 01:32:13.645
I don't know why we always dealing with, oh,

2006
01:32:13.645 --> 01:32:14.765
we are not dealing with the parent.

2007
01:32:15.145 --> 01:32:17.925
We are dealing with this. So they only obligated

2008
01:32:17.995 --> 01:32:19.245
that should not be.

2009
01:32:19.705 --> 01:32:21.605
And I think that is a lot of the issues here.

2010
01:32:21.605 --> 01:32:23.765
And that was what, um, parent member

2011
01:32:24.325 --> 01:32:25.725
Ali say was saying, right?

2012
01:32:25.885 --> 01:32:27.125
I could not, not say nothing,

2013
01:32:27.385 --> 01:32:29.205
but that is what she going with, right?

2014
01:32:29.205 --> 01:32:32.205
Because we may the child company not, may not be sharing it,

2015
01:32:32.705 --> 01:32:34.125
and I'm sorry, I keep saying child,

2016
01:32:34.465 --> 01:32:36.845
but the parent company is doing it.

2017
01:32:37.865 --> 01:32:38.885
It should be liable.

2018
01:32:38.885 --> 01:32:40.285
They should be held liable,

2019
01:32:40.285 --> 01:32:42.085
even though they're not under contract.

2020
01:32:42.085 --> 01:32:44.445
They're little, a company, the sub company is

2021
01:32:45.185 --> 01:32:47.805
so they are sub they sub surround.

2022
01:32:47.965 --> 01:32:50.925
I can't think of my, my vocabulary off today along

2023
01:32:50.925 --> 01:32:55.685
with my voice, but, uh, they, they circumventing the system,

2024
01:32:56.345 --> 01:32:58.765
you know, so that, that we need to strengthen.

2025
01:32:59.105 --> 01:33:01.925
And I'm glad that we suspended the, that,

2026
01:33:01.925 --> 01:33:03.285
that chancellor's regulations

2027
01:33:03.285 --> 01:33:04.765
because it's not strong enough.

2028
01:33:04.985 --> 01:33:07.565
We gotta make sure that the, the data and the privacy

2029
01:33:08.025 --> 01:33:10.605
and the, and the meaning of the true contracts

2030
01:33:10.605 --> 01:33:12.765
that we want is secure right?

2031
01:33:13.025 --> 01:33:15.805
In, in all aspects. That's, I have to say that

2032
01:33:16.035 --> 01:33:19.285
Legally the sub, the prime contractor will have

2033
01:33:19.285 --> 01:33:21.685
to make sure that the subcontractor is compliant.

2034
01:33:21.685 --> 01:33:23.845
The subcontractor must also comply.

2035
01:33:24.265 --> 01:33:26.365
Um, you know, educational law 2D as well

2036
01:33:26.365 --> 01:33:29.925
as the implementing regulations would not permit a vendor

2037
01:33:29.925 --> 01:33:32.045
to circumvent the requirements

2038
01:33:32.185 --> 01:33:34.165
by letting another party use the data

2039
01:33:34.345 --> 01:33:36.845
and distribute the data. Okay.

2040
01:33:37.525 --> 01:33:41.445
I remember ke are you waving information? Okay.

2041
01:33:41.545 --> 01:33:44.525
Let, I think we're ready for the, for the vote on this.

2042
01:33:45.225 --> 01:33:49.725
Um, yes. So Secretary, please call the roll.

2043
01:33:50.305 --> 01:33:51.325
Uh, yes, I wanna note

2044
01:33:51.605 --> 01:33:54.765
that there are no recusals on the proposed resolution.

2045
01:33:55.305 --> 01:33:57.365
Uh, I will call the role if you want

2046
01:33:57.365 --> 01:34:00.845
to vote differently on any particular items, please, uh,

2047
01:34:00.905 --> 01:34:02.405
let me know when I call your name.

2048
01:34:03.105 --> 01:34:06.565
Um, member Ali, please come back to me.

2049
01:34:08.185 --> 01:34:12.765
Okay. Member Ali, say no on to yes on everything else.

2050
01:34:14.225 --> 01:34:16.085
Um, member bin,

2051
01:34:17.675 --> 01:34:19.375
No one to and yes to everything else.

2052
01:34:21.495 --> 01:34:23.115
Um, member Katti

2053
01:34:25.415 --> 01:34:28.355
No on, no on to, no on 14.

2054
01:34:28.735 --> 01:34:32.715
And I would like to be recused from item 11.

2055
01:34:33.095 --> 01:34:33.315
Oh,

2056
01:34:39.095 --> 01:34:40.715
um, member Dean Stag.

2057
01:34:42.035 --> 01:34:45.805
Yes. On all member fair.

2058
01:34:46.945 --> 01:34:50.705
All member Garcia? Yes.

2059
01:34:52.385 --> 01:34:55.285
Member Giordano. Yes. Across the board?

2060
01:34:56.455 --> 01:35:01.265
Uh, vice Chair Green? Yes. Member Hassan?

2061
01:35:02.415 --> 01:35:06.215
Yes. Member ho. Yes.

2062
01:35:06.235 --> 01:35:10.495
To all member Es no. On two.

2063
01:35:10.955 --> 01:35:14.705
Yes. To the rest Member. Lee?

2064
01:35:16.985 --> 01:35:21.205
No. On two, abstain on eight. No. To 11 and 12.

2065
01:35:22.375 --> 01:35:25.585
Hold on. No. To 11 and 12.

2066
01:35:26.685 --> 01:35:29.305
Um, member Wyn? Yes. To all

2067
01:35:30.525 --> 01:35:31.905
Member Ong? Yes.

2068
01:35:31.925 --> 01:35:34.105
To all Member sap?

2069
01:35:34.525 --> 01:35:36.655
Yes. To all Member Shepherd?

2070
01:35:39.275 --> 01:35:42.315
No. To two, no to 14

2071
01:35:44.025 --> 01:35:45.675
abstain from 11 and 12.

2072
01:35:47.605 --> 01:35:48.745
And yes. To the rest.

2073
01:35:51.035 --> 01:35:55.995
Uh, member seat Sang Yes to all member Tora?

2074
01:35:56.775 --> 01:35:59.755
Yes. To all, Uh, chair Faulkner?

2075
01:36:00.495 --> 01:36:04.355
Uh, yes to all. And returning to Member Ali?

2076
01:36:05.815 --> 01:36:10.575
Yes. To all Secretary Nathan?

2077
01:36:11.805 --> 01:36:14.155
Yes. Um, I'm sorry.

2078
01:36:14.375 --> 01:36:17.515
It was also abstained from number eight.

2079
01:36:18.045 --> 01:36:21.955
Sorry. That's okay. So I have you no, on two and 14.

2080
01:36:22.425 --> 01:36:24.675
Abstain on eight 11 and 12.

2081
01:36:25.255 --> 01:36:28.785
Yes. Okay. Let me do the tallying.

2082
01:36:29.185 --> 01:36:31.305
I do believe that they'll pass, but let me tally.

2083
01:36:31.305 --> 01:36:31.625
Mm-Hmm.

2084
01:36:36.185 --> 01:36:37.185
Right.

2085
01:37:44.355 --> 01:37:46.055
Um, the resolution passes.

2086
01:37:46.955 --> 01:37:50.215
Um, on item two there were 14 yeses

2087
01:37:50.395 --> 01:37:52.055
and six nos.

2088
01:37:53.075 --> 01:37:57.205
On item eight, there were 19 yeses

2089
01:37:57.465 --> 01:37:58.565
and one abstention.

2090
01:37:59.985 --> 01:38:03.525
On item 11, there were 17 yeses.

2091
01:38:04.315 --> 01:38:06.415
Uh, two abstentions and a recusal.

2092
01:38:07.225 --> 01:38:10.715
Item 12 had 19 yeses and one abstention.

2093
01:38:12.025 --> 01:38:16.925
And item 14 had two nos and 18 yeses. Great.

2094
01:38:18.415 --> 01:38:20.305
Okay. Thank you very much. First, I wanna just say

2095
01:38:20.305 --> 01:38:22.305
that this was a, a great discussion.

2096
01:38:22.885 --> 01:38:24.105
Um, and I think this is really

2097
01:38:24.105 --> 01:38:25.745
what we wanna see here at the panel.

2098
01:38:26.205 --> 01:38:27.545
Um, I want to thank the chancellor

2099
01:38:27.545 --> 01:38:30.945
and I wanna thank the staff for, um, coming up

2100
01:38:30.945 --> 01:38:33.825
and participating and really enriching that conversation.

2101
01:38:34.525 --> 01:38:37.185
Um, I'd also like to speak to the folks around,

2102
01:38:37.385 --> 01:38:39.145
I listen carefully around the issue of assessment.

2103
01:38:39.885 --> 01:38:41.985
And I'm wondering whether the panel,

2104
01:38:42.045 --> 01:38:44.705
and I'm looking at you, Tom Shepherd, um,

2105
01:38:44.855 --> 01:38:46.945
whether this is something that the panel might want

2106
01:38:46.945 --> 01:38:48.945
to be proactive and get involved in,

2107
01:38:49.485 --> 01:38:51.905
and maybe we can create some kind of follow up.

2108
01:38:51.905 --> 01:38:54.625
And I would also like to invite, um, some of the folks

2109
01:38:54.625 --> 01:38:57.905
that are here in the audience that had specific concerns,

2110
01:38:58.085 --> 01:38:59.545
you know, specific concerns.

2111
01:39:00.125 --> 01:39:02.745
If we can find some way of engaging and,

2112
01:39:02.805 --> 01:39:03.945
and see if we can create

2113
01:39:03.945 --> 01:39:05.145
something that works a little bit better.

2114
01:39:05.305 --> 01:39:07.785
'cause what I'm hearing is there's a real feeling

2115
01:39:07.785 --> 01:39:10.305
that it's not working in the way

2116
01:39:10.385 --> 01:39:11.625
that it was intended to work.

2117
01:39:12.165 --> 01:39:13.745
And if that's the case, then let's,

2118
01:39:13.755 --> 01:39:14.865
let's put our heads together

2119
01:39:15.485 --> 01:39:17.705
and see if we can come up with something that would, uh,

2120
01:39:17.735 --> 01:39:19.825
work some, some pen of shepherd.

2121
01:39:23.605 --> 01:39:27.825
Thank you Chair Harner. Um, I will say yes to that, right?

2122
01:39:27.885 --> 01:39:30.785
And you, you're appointed. So, uh, now let's, let's,

2123
01:39:31.445 --> 01:39:32.445
No, I'm sorry. I'm sorry.

2124
01:39:32.445 --> 01:39:34.065
Yeah, yeah, yeah. I'll say yes to that.

2125
01:39:34.465 --> 01:39:38.505
I will also say that it was raised in this conversation

2126
01:39:39.255 --> 01:39:43.795
that the point behind this is that

2127
01:39:44.655 --> 01:39:48.275
the people who make the decisions seem

2128
01:39:48.275 --> 01:39:50.355
to be disconnected from the people

2129
01:39:50.585 --> 01:39:51.875
that have to implement them.

2130
01:39:52.775 --> 01:39:55.955
And No, no, I, I, the point here is the people

2131
01:39:55.985 --> 01:40:00.875
that are tasked with implementing these things ought to be

2132
01:40:01.795 --> 01:40:04.195
a part of, like a committee

2133
01:40:04.295 --> 01:40:05.835
or anything that we put together

2134
01:40:05.935 --> 01:40:09.875
to examine these assessments, how they work or don't work,

2135
01:40:10.295 --> 01:40:12.035
and what appropriate solutions look

2136
01:40:12.035 --> 01:40:13.035
Like. No, I, I, I

2137
01:40:13.035 --> 01:40:13.755
absolutely agree with you.

2138
01:40:13.775 --> 01:40:15.915
And I think we should start with some members of the public

2139
01:40:15.975 --> 01:40:19.435
who were here, um, that offered some great commentary.

2140
01:40:20.175 --> 01:40:22.755
And, um, and let's really see if there's a way

2141
01:40:22.755 --> 01:40:24.595
that we can put our heads together.

2142
01:40:24.675 --> 01:40:27.435
I think we have, you know, commitment from DOE

2143
01:40:27.545 --> 01:40:30.715
that they've heard this and, uh, let's not leave here

2144
01:40:30.715 --> 01:40:32.875
and then come back a year and then say, you know, here we,

2145
01:40:33.175 --> 01:40:34.475
we, we missed an opportunity.

2146
01:40:35.055 --> 01:40:36.875
Um, so I think there's an opportunity for us

2147
01:40:36.895 --> 01:40:38.595
to put our heads together and collaborate.

2148
01:41:01.735 --> 01:41:05.675
Um, just keeping in mind, uh,

2149
01:41:06.975 --> 01:41:11.615
you know, as a panel member, being able to listen to

2150
01:41:11.615 --> 01:41:14.595
what other parents and,

2151
01:41:14.615 --> 01:41:15.835
and the decisions that need

2152
01:41:15.835 --> 01:41:17.875
to be made across the five boroughs.

2153
01:41:18.535 --> 01:41:21.835
Um, and it's a very particular situation to be able

2154
01:41:21.835 --> 01:41:26.375
to sit back and here the, the opposition.

2155
01:41:26.395 --> 01:41:31.215
So I think that will be a really great conversation to have

2156
01:41:31.725 --> 01:41:35.375
because, um, this is one of the, you know,

2157
01:41:35.375 --> 01:41:37.455
the contracts I'm not in agreement with.

2158
01:41:37.915 --> 01:41:42.405
And it actually brings back pretty awful memories, um,

2159
01:41:43.875 --> 01:41:44.935
of getting left back

2160
01:41:45.045 --> 01:41:48.735
because I, I knew I wasn't a great tech test taker

2161
01:41:49.475 --> 01:41:50.725
with the Regents exam,

2162
01:41:51.535 --> 01:41:54.675
but I also knew that I was, um, you know, in

2163
01:41:54.675 --> 01:41:56.195
what they called resource room.

2164
01:41:56.575 --> 01:42:00.875
And I was so afraid to be stigmatized in the fifth grade

2165
01:42:00.875 --> 01:42:03.155
that I actually just filled in the circles

2166
01:42:03.805 --> 01:42:05.985
on a test I wanted to finish with everybody else.

2167
01:42:06.525 --> 01:42:09.145
So I wouldn't, you know, you know, um,

2168
01:42:09.395 --> 01:42:10.425
stand out in that way.

2169
01:42:10.425 --> 01:42:13.265
And unfortunately, you know, I, that was the year

2170
01:42:13.265 --> 01:42:15.505
that I was left back in the fifth grade.

2171
01:42:15.925 --> 01:42:18.225
And then having to listen to parents

2172
01:42:19.325 --> 01:42:21.905
who benefit from this assessment.

2173
01:42:22.205 --> 01:42:26.265
So I think just if we can, if we can have this conversation

2174
01:42:27.065 --> 01:42:29.115
with people that are really impacted

2175
01:42:29.215 --> 01:42:31.235
by this contract, that'll be lovely.

2176
01:42:32.255 --> 01:42:33.785
Some, something has to happen in the middle.

2177
01:42:34.245 --> 01:42:37.675
Yep. We're gonna try to, uh, to see if we can have some,

2178
01:42:37.935 --> 01:42:40.115
um, some, some impact in this area.

2179
01:42:40.535 --> 01:42:42.555
So, um, yes,

2180
01:42:43.965 --> 01:42:45.465
I'd, I'd like to recommend, um,

2181
01:42:45.465 --> 01:42:48.345
potentially doing it focus group style so

2182
01:42:48.345 --> 01:42:50.265
that we have different stakeholders present

2183
01:42:50.265 --> 01:42:53.785
because there are at least 10%,

2184
01:42:53.845 --> 01:42:55.865
and it could be more of students that most

2185
01:42:55.865 --> 01:42:58.265
of this never works for and never will work for.

2186
01:42:58.845 --> 01:43:02.585
And the stakeholders that are putting in the extra work,

2187
01:43:02.725 --> 01:43:05.225
not only to prep for the exam, deliver the exam,

2188
01:43:05.225 --> 01:43:06.865
proctor the exam score exams,

2189
01:43:06.865 --> 01:43:09.465
but now they're differentiating, translating, interpreting.

2190
01:43:10.175 --> 01:43:13.265
None of that is really like their job, right?

2191
01:43:13.295 --> 01:43:15.825
Like they're supposed to be teaching kids not assessing.

2192
01:43:15.845 --> 01:43:19.225
So focus group with different stakeholders to get a Sure.

2193
01:43:19.445 --> 01:43:21.185
An a varied view of, of

2194
01:43:21.185 --> 01:43:23.225
what our city really looks like and not few

2195
01:43:23.225 --> 01:43:24.225
People. That's a great

2196
01:43:24.225 --> 01:43:24.865
suggestion.

2197
01:43:24.925 --> 01:43:26.985
I'm gonna leave it to the group to kind of figure out

2198
01:43:26.985 --> 01:43:29.225
what the best way to facilitate so that,

2199
01:43:29.465 --> 01:43:31.545
although it, it might be in terms of the contract

2200
01:43:31.545 --> 01:43:32.745
that we just passed might be late.

2201
01:43:32.745 --> 01:43:34.905
There may be other times and other contracts

2202
01:43:34.905 --> 01:43:36.625
and other opportunities where this will come up

2203
01:43:37.005 --> 01:43:39.665
and we'll have an opportunity to maybe have some, um,

2204
01:43:40.215 --> 01:43:42.785
some sense of where we would like to see this, uh, move.

2205
01:43:43.215 --> 01:43:47.765
Yeah. Yes. Panel member. I'll see it. I can't

2206
01:43:49.045 --> 01:43:50.045
Contract isn't written yet.

2207
01:43:50.095 --> 01:43:52.405
Since the contract isn't actually written yet.

2208
01:43:52.745 --> 01:43:55.005
Can that focus group, especially with the teachers

2209
01:43:55.005 --> 01:43:56.285
who are here tonight, take place

2210
01:43:56.285 --> 01:43:59.045
before the contract is written and or finalized?

2211
01:44:00.235 --> 01:44:03.325
Because it is, they're right. You just, we all right.

2212
01:44:03.365 --> 01:44:05.405
I voted no, but we all just signed away five years. So

2213
01:44:05.405 --> 01:44:07.725
I'm gonna suggest that you all, maybe just when this ends,

2214
01:44:07.725 --> 01:44:09.725
we all kind of move some of the folks here

2215
01:44:09.725 --> 01:44:11.205
and we get together and figure out what we

2216
01:44:11.235 --> 01:44:12.235
Next steps. It's more of a

2217
01:44:12.235 --> 01:44:13.205
question of is that possible?

2218
01:44:13.265 --> 01:44:15.685
That's like a contract poss Like can they do that

2219
01:44:16.165 --> 01:44:17.165
Logistically? I just, I

2220
01:44:17.165 --> 01:44:18.365
don't wanna, I I would think,

2221
01:44:18.405 --> 01:44:19.805
I mean, the chance's right there think it's possible.

2222
01:44:19.805 --> 01:44:20.885
Yeah. Want you?

2223
01:44:21.385 --> 01:44:25.005
No, yeah, I don't, uh, Judy, can you answer that question?

2224
01:44:25.065 --> 01:44:27.885
Do you know if that's, or walking out? Oh, perfect.

2225
01:44:28.105 --> 01:44:29.165
We have our general counsel

2226
01:44:29.165 --> 01:44:33.905
here once this panel.

2227
01:44:35.835 --> 01:44:39.265
Hello? Oh. Once the panel has voted

2228
01:44:39.325 --> 01:44:41.905
to approve the substantive terms of the contract,

2229
01:44:41.965 --> 01:44:44.825
what's left is negotiating standard provisions

2230
01:44:44.825 --> 01:44:48.385
that really don't impact on the substance of the, um,

2231
01:44:48.645 --> 01:44:50.345
matter itself, right?

2232
01:44:50.465 --> 01:44:53.585
There's indemnification issues, there's our data agreements,

2233
01:44:53.615 --> 01:44:56.305
there's stuff that really, if you read it in isolation,

2234
01:44:57.085 --> 01:44:59.105
you would have no idea what it's connected to

2235
01:44:59.105 --> 01:45:03.505
because it's, it's the part, it's a part of formalizing, um,

2236
01:45:03.685 --> 01:45:07.185
the deal that your vote has just entered us

2237
01:45:07.255 --> 01:45:08.305
into with the vendor.

2238
01:45:09.815 --> 01:45:12.915
So no, we can't really stop the process.

2239
01:45:13.495 --> 01:45:17.355
Two, um, I don't believe that the work that has

2240
01:45:17.355 --> 01:45:20.875
to be done now to finalize a contract really speaks

2241
01:45:20.895 --> 01:45:22.755
to the issues that members are raising.

2242
01:45:27.775 --> 01:45:32.575
Yes. And this focus group,

2243
01:45:32.625 --> 01:45:35.135
maybe, you know, assessments are important.

2244
01:45:35.355 --> 01:45:36.975
We need a benchmark, right?

2245
01:45:38.405 --> 01:45:43.245
Can we come up with different kinds of assessments

2246
01:45:43.635 --> 01:45:45.445
that will reach different children?

2247
01:45:46.395 --> 01:45:50.945
See the state, acknowledge the regions as a exit exam.

2248
01:45:51.755 --> 01:45:53.005
Exam is not good for everyone.

2249
01:45:53.675 --> 01:45:56.495
So they have multiple pathways now.

2250
01:45:56.495 --> 01:45:59.415
They, they, they're working on creating multiple pathways

2251
01:45:59.795 --> 01:46:01.175
to graduate, right?

2252
01:46:01.245 --> 01:46:02.855
High school measurements, right?

2253
01:46:03.155 --> 01:46:06.335
And one of them is to get rid of, one of the suggestions is

2254
01:46:06.335 --> 01:46:09.055
to get rid of the three diplomas that only have one.

2255
01:46:09.475 --> 01:46:10.775
And then you can have seals,

2256
01:46:10.915 --> 01:46:13.335
but then multiple, if you don't want to take the regents,

2257
01:46:13.445 --> 01:46:16.415
they're creating other pathways for students

2258
01:46:16.515 --> 01:46:17.895
to graduate again.

2259
01:46:18.135 --> 01:46:20.975
'cause we know that all students are not the greatest test.

2260
01:46:21.165 --> 01:46:24.815
They may, they may know the, the subject brilliantly,

2261
01:46:25.035 --> 01:46:28.055
but then for when it comes to a test, they freeze up

2262
01:46:28.395 --> 01:46:31.055
or they can't, it doesn't translate on paper,

2263
01:46:31.595 --> 01:46:32.935
let alone on a computer.

2264
01:46:33.425 --> 01:46:37.975
Right? So maybe we should come up with sta you know,

2265
01:46:37.975 --> 01:46:40.535
different assessments for different students.

2266
01:46:41.035 --> 01:46:44.055
So to help to give a better understanding of that.

2267
01:46:44.195 --> 01:46:46.535
And again, we should like kind of minimize.

2268
01:46:47.315 --> 01:46:50.245
And then also, so all stakeholders understand

2269
01:46:50.715 --> 01:46:51.725
what is the reasoning

2270
01:46:51.725 --> 01:46:54.965
and purposes of these assessments could create an assessment

2271
01:46:55.945 --> 01:46:58.565
is to look for every single thing that you want,

2272
01:46:58.945 --> 01:47:00.245
and then also make sure

2273
01:47:00.515 --> 01:47:02.765
that the teachers can see this is their

2274
01:47:02.965 --> 01:47:04.245
strengths, this is their weakness.

2275
01:47:04.245 --> 01:47:08.085
But I know they create tests to show that, okay,

2276
01:47:08.085 --> 01:47:10.725
in math you are, you're weak in word problems.

2277
01:47:11.025 --> 01:47:12.685
It might be a lit literacy

2278
01:47:12.845 --> 01:47:14.605
'cause you're not understanding what the question,

2279
01:47:14.705 --> 01:47:16.325
the question is asking, right?

2280
01:47:16.425 --> 01:47:20.685
You are strong in, in, um, using the formulas.

2281
01:47:20.785 --> 01:47:22.605
But do you know when to use the formulas?

2282
01:47:23.025 --> 01:47:24.605
If we're gonna create assessments

2283
01:47:24.785 --> 01:47:27.565
and teachers feel that, you know, it is worth their time,

2284
01:47:27.955 --> 01:47:30.045
they gotta be make sure they know how,

2285
01:47:30.585 --> 01:47:33.365
how they would further as help them assess their child

2286
01:47:33.535 --> 01:47:34.685
right at the school level.

2287
01:47:34.685 --> 01:47:36.805
Because not a lot of that issue is there.

2288
01:47:36.865 --> 01:47:40.005
We know that assessments is needed to get overall sense

2289
01:47:40.005 --> 01:47:41.965
of the city, the district, et cetera.

2290
01:47:42.425 --> 01:47:46.125
But if we're gonna give these assessments list, um,

2291
01:47:46.185 --> 01:47:49.365
the teachers minimize the amount, first of all,

2292
01:47:49.425 --> 01:47:53.205
and then show them how they can use that data.

2293
01:47:53.505 --> 01:47:55.445
And some of them, I'm pretty sure know they can

2294
01:47:55.445 --> 01:47:56.525
use the data, right?

2295
01:47:56.625 --> 01:47:59.165
If they see the breakdown of what their child is,

2296
01:47:59.385 --> 01:48:01.845
but the, their ch your, their students are doing,

2297
01:48:02.075 --> 01:48:05.205
because I'm I, the tests that I believe

2298
01:48:05.835 --> 01:48:08.245
that they give their, their children help them

2299
01:48:08.305 --> 01:48:11.325
to know which contact area they're weak or strong,

2300
01:48:11.865 --> 01:48:15.375
but maybe I don't know how the assessments are showing

2301
01:48:15.405 --> 01:48:17.255
that at the school level for their child.

2302
01:48:17.295 --> 01:48:18.975
I don't know if they actually even showing that,

2303
01:48:19.045 --> 01:48:21.055
because at least they will see that, oh,

2304
01:48:21.535 --> 01:48:23.575
I can use help, use help assess.

2305
01:48:23.915 --> 01:48:26.815
But if they're just assessing so somewhere else,

2306
01:48:26.995 --> 01:48:29.925
use the data that is not conducive

2307
01:48:30.305 --> 01:48:31.765
to the learning environment.

2308
01:48:32.135 --> 01:48:35.445
Chancellor. So I wanna thank everybody for this

2309
01:48:36.275 --> 01:48:39.805
very intense and informative conversation around assessment.

2310
01:48:40.145 --> 01:48:44.205
And we're not trying to avoid the topic, obviously.

2311
01:48:44.205 --> 01:48:46.925
We're here listening and we're taking notes as a team.

2312
01:48:47.395 --> 01:48:50.885
What I do wanna offer is an opportunity for our team

2313
01:48:50.945 --> 01:48:51.965
to brief the panel.

2314
01:48:52.525 --> 01:48:55.325
I understand, um, that the focus group suggestion,

2315
01:48:55.325 --> 01:48:56.605
I think it's an excellent idea.

2316
01:48:56.705 --> 01:48:59.645
Our team is also holding our own focus groups

2317
01:49:00.145 --> 01:49:02.405
and doing our own listening sessions around the city.

2318
01:49:02.505 --> 01:49:04.485
And those are kicking off very shortly.

2319
01:49:05.025 --> 01:49:09.685
But what I will say is we welcome any opportunity for topics

2320
01:49:09.795 --> 01:49:12.685
that are taking this amount of time, not

2321
01:49:12.685 --> 01:49:14.645
because we don't wanna listen here, but

2322
01:49:14.645 --> 01:49:17.725
because we would love to spend time with you

2323
01:49:18.645 --> 01:49:20.605
briefing you on just this topic.

2324
01:49:21.305 --> 01:49:22.805
So I'm asking the panel

2325
01:49:22.905 --> 01:49:24.965
to consider accepting that invitation.

2326
01:49:25.265 --> 01:49:28.765
So our team can give you a robust briefing on

2327
01:49:28.865 --> 01:49:31.485
how assessments can be selected at the school level,

2328
01:49:32.025 --> 01:49:35.485
the role that school leaders have in assessments, the role

2329
01:49:35.485 --> 01:49:38.285
that superintendents and the role that Central has.

2330
01:49:38.585 --> 01:49:40.605
And of course, hearing our teachers on

2331
01:49:40.625 --> 01:49:43.125
how we can strengthen our systems of assessments

2332
01:49:43.425 --> 01:49:45.245
and what can be done at the teacher level.

2333
01:49:46.725 --> 01:49:48.925
That sounds great. I think, I think we're in agreement.

2334
01:49:49.065 --> 01:49:50.065
Yes. Panel member,

2335
01:49:52.425 --> 01:49:56.345
I, I have a concern about like the, the trend

2336
01:49:56.485 --> 01:49:58.385
of the five year contracts in general.

2337
01:49:59.175 --> 01:50:02.065
Because if, if we're always only presented

2338
01:50:02.065 --> 01:50:05.145
with this five year option, if we want something different,

2339
01:50:05.165 --> 01:50:06.505
we have to ask for that.

2340
01:50:07.045 --> 01:50:11.825
We, the landscape changes too quickly for us to commit

2341
01:50:11.825 --> 01:50:15.025
to five years to anybody for anything, you know?

2342
01:50:15.085 --> 01:50:18.185
And so like, kids don't even spend five years in a school

2343
01:50:18.185 --> 01:50:20.025
unless it's elementary and that's six years,

2344
01:50:20.025 --> 01:50:21.505
and then it's three years and four years

2345
01:50:21.965 --> 01:50:23.465
unless you're in district 75

2346
01:50:23.645 --> 01:50:25.265
and none of this works for those students.

2347
01:50:25.325 --> 01:50:27.185
So like, we're not gonna do that, right? Mm-Hmm.

2348
01:50:27.445 --> 01:50:31.785
So how, how do we, I would like to ask

2349
01:50:32.045 --> 01:50:35.585
to see one in two year contracts going forward so

2350
01:50:35.585 --> 01:50:37.825
that when people make a comment, and

2351
01:50:37.825 --> 01:50:39.785
because right, sometimes comment comes

2352
01:50:39.785 --> 01:50:42.385
after certain things where the conversation then leads

2353
01:50:42.405 --> 01:50:45.265
to a point where there's like a different understanding

2354
01:50:45.765 --> 01:50:49.225
and there is, as you said, no mechanism to go back.

2355
01:50:49.605 --> 01:50:51.265
But if the contract was only one

2356
01:50:51.265 --> 01:50:54.145
or two years, we wouldn't be committed to a decision

2357
01:50:54.175 --> 01:50:55.745
that nobody really liked.

2358
01:50:56.685 --> 01:50:57.555
There are people that voted

2359
01:50:57.555 --> 01:50:58.555
yes that said they didn't like it.

2360
01:50:59.095 --> 01:51:00.355
And, and that's problematic.

2361
01:51:01.335 --> 01:51:04.915
So how do we then make this like for the kids,

2362
01:51:05.185 --> 01:51:07.435
because that's a, a company thing.

2363
01:51:07.435 --> 01:51:08.875
That's a business thing. That's a,

2364
01:51:09.135 --> 01:51:11.195
we don't wanna revisit this for another five years.

2365
01:51:11.615 --> 01:51:13.675
We as a company don't wanna redo a contract.

2366
01:51:13.675 --> 01:51:15.235
We don't wanna negotiate again,

2367
01:51:15.235 --> 01:51:16.835
because all that takes time and payroll.

2368
01:51:17.145 --> 01:51:19.475
That doesn't matter because that doesn't serve our students.

2369
01:51:20.215 --> 01:51:23.595
So that topic, I'm gonna refer to the contract committee

2370
01:51:24.375 --> 01:51:25.755
to address that.

2371
01:51:25.825 --> 01:51:27.755
What, what the practicality of that is.

2372
01:51:28.215 --> 01:51:30.075
Uh, that actually is a misnomer.

2373
01:51:30.075 --> 01:51:31.555
We do have a contract committee.

2374
01:51:32.135 --> 01:51:35.195
Um, the information that was put that we got rid the, we,

2375
01:51:35.195 --> 01:51:37.675
what we did is we changed the requirement that it had

2376
01:51:37.675 --> 01:51:38.915
to be meet in person

2377
01:51:39.585 --> 01:51:41.795
because it was only, there were only three people

2378
01:51:41.795 --> 01:51:43.515
that regularly attended and there was a call.

2379
01:51:43.575 --> 01:51:45.995
So we still have a contract committee.

2380
01:51:46.055 --> 01:51:49.595
We have a very able contract committee chair. Thank you.

2381
01:51:50.215 --> 01:51:54.385
Um, yes. Panel member lie and then panel member Casre.

2382
01:51:54.385 --> 01:51:56.225
And then we're gonna move on to the public comment.

2383
01:51:56.485 --> 01:51:57.625
Oh, I'm so sorry, chief.

2384
01:51:58.385 --> 01:52:01.145
I just clarify. Yeah. What are we talking about?

2385
01:52:04.175 --> 01:52:06.145
Okay. Are we talking about the same meeting? No,

2386
01:52:06.585 --> 01:52:08.225
I think we were talking about the length of contracts.

2387
01:52:08.225 --> 01:52:09.665
That's the portion I was directing.

2388
01:52:10.285 --> 01:52:13.065
It wasn't, it was a general comment about contracts,

2389
01:52:13.245 --> 01:52:15.585
but specifically talking about the assessment contract,

2390
01:52:15.585 --> 01:52:19.145
that was the five year proposal and asking if we can see one

2391
01:52:19.145 --> 01:52:20.705
or two year proposals in the future.

2392
01:52:20.705 --> 01:52:22.985
Yeah. Right. Because the landscape changes in five years.

2393
01:52:23.205 --> 01:52:24.585
If we don't like it now in two

2394
01:52:24.585 --> 01:52:26.265
years, we're probably gonna hate it. Right.

2395
01:52:26.285 --> 01:52:28.105
So I heard what you said. Is this a part of

2396
01:52:28.105 --> 01:52:29.745
The, it's a bigger con it's a bigger issue

2397
01:52:29.745 --> 01:52:31.825
around contracting and, and length of contracts.

2398
01:52:32.045 --> 01:52:33.185
So I've expanded it in that.

2399
01:52:33.255 --> 01:52:35.985
Okay. I'm, I'm talking specifically about, um,

2400
01:52:36.135 --> 01:52:40.065
getting together and talking about, um, uh,

2401
01:52:40.125 --> 01:52:41.585
the assessments and stuff like that.

2402
01:52:41.805 --> 01:52:43.345
Is that a part of this conversation?

2403
01:52:43.485 --> 01:52:47.525
No. Separate things. I Used it as an

2404
01:52:47.525 --> 01:52:48.325
Example. As an example.

2405
01:52:48.435 --> 01:52:49.925
Yeah. So like as an example,

2406
01:52:50.105 --> 01:52:52.205
we have this five year assessment contract.

2407
01:52:52.315 --> 01:52:55.445
Yeah. Could we, we already voted on it, so there's no way,

2408
01:52:55.505 --> 01:52:58.605
as he said to like the general counsel said, there's no way

2409
01:52:58.605 --> 01:52:59.845
of like amending or reversing that.

2410
01:53:00.185 --> 01:53:02.005
But going forward we shouldn't see five

2411
01:53:02.005 --> 01:53:03.045
year contract. Right? Yeah.

2412
01:53:03.475 --> 01:53:05.085
Okay. The bigger issue, I

2413
01:53:05.085 --> 01:53:06.285
Don't necessarily agree to, she didn't

2414
01:53:06.285 --> 01:53:07.285
Have five year contracts. Folks.

2415
01:53:07.285 --> 01:53:09.365
Both please wait to be recognized. Okay.

2416
01:53:09.585 --> 01:53:12.125
The next person. Yeah. Then we're gonna public comment.

2417
01:53:12.585 --> 01:53:14.405
Um, Pamela Maretti and then Pamela.

2418
01:53:14.765 --> 01:53:17.085
And then we're going to thank you Pam.

2419
01:53:17.305 --> 01:53:18.205
Oh, we'll let you speak and then

2420
01:53:18.205 --> 01:53:19.445
we'll move into public comment. Oh,

2421
01:53:19.615 --> 01:53:20.725
Chancellor Ramos.

2422
01:53:21.285 --> 01:53:25.285
I, I am just curious regarding the screeners, um,

2423
01:53:26.585 --> 01:53:30.165
uh, the, the way that they're rolled out where Central

2424
01:53:30.705 --> 01:53:32.205
is sort of like holding them

2425
01:53:32.265 --> 01:53:35.925
and then the schools can, uh, have them distributed.

2426
01:53:36.905 --> 01:53:40.445
Is, is there like a chance that, that, that pathway

2427
01:53:41.175 --> 01:53:44.325
would change similar to the way the computers went,

2428
01:53:44.375 --> 01:53:45.885
where the schools would then

2429
01:53:46.395 --> 01:53:48.485
just Central would negotiate the contract

2430
01:53:48.545 --> 01:53:50.685
and the schools would decide whether they want

2431
01:53:50.705 --> 01:53:52.405
to do the screeners or not?

2432
01:53:53.075 --> 01:53:55.965
Like, is that sort of where we're go going ultimately?

2433
01:53:56.315 --> 01:53:57.925
Like right now, the schools are mandated

2434
01:53:57.925 --> 01:53:59.245
to do the screeners,

2435
01:53:59.825 --> 01:54:01.565
but is there, is there a chance

2436
01:54:01.565 --> 01:54:04.125
that it'll turn into something where the schools get

2437
01:54:04.125 --> 01:54:06.685
to just choose whether they wanna use those screeners?

2438
01:54:07.805 --> 01:54:10.475
Panel member? I, I really thank you for the question,

2439
01:54:10.615 --> 01:54:13.195
but I'm going to respectfully ask if I can regroup

2440
01:54:13.195 --> 01:54:14.715
with my team and if we can make that part

2441
01:54:14.715 --> 01:54:17.115
of the follow up in the briefing. Thank you.

2442
01:54:17.425 --> 01:54:20.565
Okay. Lie, Uh, thank you Chair.

2443
01:54:20.725 --> 01:54:24.405
I just wanted to address the idea, uh, two ideas.

2444
01:54:24.665 --> 01:54:26.765
One that there's no going back once you,

2445
01:54:27.105 --> 01:54:28.645
the contract has been voted on

2446
01:54:29.225 --> 01:54:30.805
and you can't do anything for five years.

2447
01:54:31.185 --> 01:54:33.285
And the idea that we're having the focus group

2448
01:54:33.335 --> 01:54:35.325
after the panel voted on the contract.

2449
01:54:35.945 --> 01:54:38.605
Um, I, but I but the clar no.

2450
01:54:38.605 --> 01:54:41.445
The clarification I wanna provide though is something

2451
01:54:41.445 --> 01:54:45.045
that was recently mentioned to the panel, um,

2452
01:54:45.225 --> 01:54:49.685
and that in baked into every DOE contract is the ability

2453
01:54:49.785 --> 01:54:52.325
for DOE to cancel the contract for any reason.

2454
01:54:52.625 --> 01:54:55.085
Is that right? I just wanna confirm that. That's right.

2455
01:54:55.785 --> 01:54:58.405
And so if there is a change in policy

2456
01:54:58.825 --> 01:55:03.365
or if there is a change based on input, um,

2457
01:55:03.795 --> 01:55:06.605
from folks, there is the ability of DOE

2458
01:55:06.605 --> 01:55:08.325
to pivot on a contract even

2459
01:55:08.325 --> 01:55:10.605
after the contract has been passed by pep, even

2460
01:55:10.605 --> 01:55:13.445
after it's been registered from by the comptroller's office.

2461
01:55:13.505 --> 01:55:14.725
So I just wanna clarify that,

2462
01:55:15.625 --> 01:55:16.965
and I'm hoping I'm correct about that.

2463
01:55:17.245 --> 01:55:18.605
I see Alicia, yeah,

2464
01:55:20.085 --> 01:55:23.495
I, I I think the issue, Yeah.

2465
01:55:24.155 --> 01:55:26.295
Are there any additional comments?

2466
01:55:26.945 --> 01:55:28.815
We're gonna move on now to public comment.

2467
01:55:29.195 --> 01:55:30.415
Um, section of the meeting.

2468
01:55:31.115 --> 01:55:34.855
Um, let me just sort of re remind everyone of the rules of,

2469
01:55:34.955 --> 01:55:38.495
um, public comment, um, during tonight's public comment,

2470
01:55:38.545 --> 01:55:40.295
we'll again, be calling speakers up in groups.

2471
01:55:40.575 --> 01:55:43.485
Secretary Nathan will call people up, uh, to speak.

2472
01:55:44.145 --> 01:55:46.445
Um, we're gonna begin first with students.

2473
01:55:46.945 --> 01:55:48.605
And I know there was a student here, Earl,

2474
01:55:48.605 --> 01:55:49.685
that wanted to speak earlier.

2475
01:55:49.735 --> 01:55:52.725
We'll begin with students education council members

2476
01:55:52.745 --> 01:55:54.885
and elected officials, followed by members

2477
01:55:54.885 --> 01:55:57.165
of the general public during open comment.

2478
01:55:57.195 --> 01:55:59.325
Each individual that is signed up to speak,

2479
01:55:59.775 --> 01:56:01.485
we'll be allot up to two minutes.

2480
01:56:02.145 --> 01:56:05.085
Um, I would like to remind speakers to refrain from,

2481
01:56:05.625 --> 01:56:06.885
um, use of harsh language.

2482
01:56:07.005 --> 01:56:09.805
I know sometimes these discussions become pretty, um,

2483
01:56:09.875 --> 01:56:12.805
emotional so that, um, we just need to refrain from that.

2484
01:56:13.185 --> 01:56:15.205
So at this point, I'd like to ask, uh, secretary Nathan,

2485
01:56:15.205 --> 01:56:17.925
if you could please call the names up for public comment.

2486
01:56:18.995 --> 01:56:20.775
And can I ask everybody? Please come to order.

2487
01:56:21.195 --> 01:56:22.695
Do we have the room? Please come to order.

2488
01:56:24.035 --> 01:56:26.735
So, uh, there was a student who had signed up, um,

2489
01:56:27.085 --> 01:56:29.295
Lila Torres, if you're here,

2490
01:56:34.615 --> 01:56:35.755
um, the green.

2491
01:56:35.775 --> 01:56:39.825
So I don't know, I will call, um, people

2492
01:56:39.825 --> 01:56:42.945
who signed up under the education council name.

2493
01:56:43.205 --> 01:56:44.465
Uh, is there Lila? Is that student?

2494
01:56:44.745 --> 01:56:47.825
I think that is maybe, oh, no, no, no, no. Okay.

2495
01:56:48.405 --> 01:56:48.625
Um,

2496
01:56:53.585 --> 01:56:54.075
wait a minute.

2497
01:56:54.615 --> 01:56:58.225
That's, that's, these are,

2498
01:57:02.665 --> 01:57:05.005
um, I'll call up while we're waiting, I think

2499
01:57:05.005 --> 01:57:06.565
for our student speaker, Dr.

2500
01:57:06.745 --> 01:57:11.525
Miriam, Ben Ellis, Craig Slutkin,

2501
01:57:11.775 --> 01:57:13.765
Gavin Healy, and Dr.

2502
01:57:13.915 --> 01:57:15.205
Darling Meme.

2503
01:57:18.385 --> 01:57:20.365
And please state your name before you begin speaking.

2504
01:57:20.455 --> 01:57:22.285
Thank you. I was told I was number two.

2505
01:57:22.955 --> 01:57:24.805
Good evening, everyone. My name is Dr.

2506
01:57:25.105 --> 01:57:29.385
Mim Ben Shake Ellis, um, CC 13 Brooklyn.

2507
01:57:33.175 --> 01:57:37.415
So I'm here to share with everyone, uh,

2508
01:57:37.715 --> 01:57:42.255
an issue about PSL, public School Athletic league,

2509
01:57:44.935 --> 01:57:45.995
So PSL

2510
01:57:46.055 --> 01:57:47.915
and the opportunities for sports

2511
01:57:48.055 --> 01:57:51.835
for all our students in NYC public schools.

2512
01:57:53.885 --> 01:57:57.165
I have many points, and I really wish not to be interrupted.

2513
01:57:58.195 --> 01:58:00.925
Parents and families do not know about sports

2514
01:58:00.925 --> 01:58:02.605
opportunities in their kids.

2515
01:58:02.605 --> 01:58:05.615
Incoming high school parents

2516
01:58:05.715 --> 01:58:08.375
and families are not aware of the multiple deadlines

2517
01:58:08.835 --> 01:58:12.175
for applying to the three season sports fall, winter

2518
01:58:12.435 --> 01:58:15.495
and spring that PSL offers to our

2519
01:58:16.415 --> 01:58:17.735
1800 NYC schools.

2520
01:58:18.395 --> 01:58:20.655
And of course, I'm talking only about the high schools

2521
01:58:20.675 --> 01:58:22.175
and the middle schools, but the most

2522
01:58:22.175 --> 01:58:23.335
important thing is the high schools.

2523
01:58:24.325 --> 01:58:27.855
When parents realized that PSL missed, uh,

2524
01:58:28.395 --> 01:58:30.055
the PSL missed deadline

2525
01:58:30.235 --> 01:58:33.055
and opportunities, they direct their request

2526
01:58:33.115 --> 01:58:34.655
to their superintendent's office.

2527
01:58:35.775 --> 01:58:39.355
The superintendent's office replies to these families

2528
01:58:39.375 --> 01:58:43.365
and parents that they cannot overrule any PSL

2529
01:58:43.725 --> 01:58:46.455
decision or decisions.

2530
01:58:47.575 --> 01:58:49.615
PSL executives respond to parents

2531
01:58:49.615 --> 01:58:51.615
because the parents are persistent

2532
01:58:52.275 --> 01:58:54.415
and they find the numbers of PSL.

2533
01:58:54.605 --> 01:58:56.455
It's public knowledge on the website.

2534
01:58:56.915 --> 01:59:00.015
So, PSL executive respond to the parents and families

2535
01:59:00.235 --> 01:59:03.375
and guardians that no communication with their office

2536
01:59:03.635 --> 01:59:05.335
or staff should happen,

2537
01:59:05.475 --> 01:59:08.415
and PSL direct families to their principal

2538
01:59:08.755 --> 01:59:10.175
and athletic directors.

2539
01:59:10.755 --> 01:59:13.655
If the latter ad athletic director

2540
01:59:14.165 --> 01:59:15.575
does exist in their school,

2541
01:59:17.035 --> 01:59:20.395
PSL does not accept any help in students' assignment

2542
01:59:21.175 --> 01:59:24.915
to other neighboring schools if there are no teams

2543
01:59:25.095 --> 01:59:29.195
or less than six teams in the freshman high school or,

2544
01:59:29.375 --> 01:59:30.955
or the high school of the student.

2545
01:59:32.945 --> 01:59:35.025
I hope you're following with me right now. Thank

2546
01:59:35.025 --> 01:59:36.025
You. Your time is

2547
01:59:36.025 --> 01:59:36.585
elapsed.

2548
01:59:36.885 --> 01:59:41.275
Can I just finish this? PSL assert

2549
01:59:41.275 --> 01:59:44.155
that other DOE offices are only their partner

2550
01:59:44.775 --> 01:59:48.715
and cannot help correct or adjust any PSL assignment.

2551
01:59:50.055 --> 01:59:51.175
I just wanna speak about the

2552
01:59:51.175 --> 01:59:52.175
Student. Okay. No, I'm sorry. Your

2553
01:59:52.175 --> 01:59:52.895
time has expired.

2554
01:59:53.555 --> 01:59:55.895
If you could give us, you could provide us a

2555
01:59:55.895 --> 01:59:57.495
statement afterwards

2556
02:00:15.185 --> 02:00:15.405
And

2557
02:00:25.965 --> 02:00:28.005
I understand, but your time has expired and I,

2558
02:00:28.325 --> 02:00:29.325
And we have, we do. Yeah.

2559
02:00:29.325 --> 02:00:32.965
Yes, we do have a response. And, and I thank you.

2560
02:00:33.125 --> 02:00:35.485
I thank you for your comment. We do have our chief

2561
02:00:35.705 --> 02:00:39.285
who oversees PSAL here, mark Rampant.

2562
02:00:39.315 --> 02:00:42.445
We'd like an opportunity to respond. Thank you so much.

2563
02:00:53.205 --> 02:00:55.705
I'm gonna talk to this parent individually about the

2564
02:00:55.705 --> 02:00:58.305
respect, um, the confusion as it relates

2565
02:00:58.405 --> 02:01:00.265
to deadlines and so forth.

2566
02:01:00.335 --> 02:01:04.425
Many people believe that the PSAL directly oversees

2567
02:01:04.695 --> 02:01:07.305
what happens at the schools young people.

2568
02:01:07.565 --> 02:01:09.705
So just, I'm gonna paint a picture for you.

2569
02:01:10.285 --> 02:01:13.105
The PSAL provides the funding to the schools.

2570
02:01:13.775 --> 02:01:17.865
Each one of our schools hires an athletic director, um,

2571
02:01:18.165 --> 02:01:22.465
AP phys, a AP who is in charge of the coaches per sec.

2572
02:01:23.285 --> 02:01:26.745
We pay the procession for those, um,

2573
02:01:27.105 --> 02:01:28.625
athletic directors, right?

2574
02:01:29.045 --> 02:01:30.225
And they hire the coaches.

2575
02:01:30.735 --> 02:01:32.625
Each one of the coaches has a tryout.

2576
02:01:32.715 --> 02:01:35.585
There is a start and an end to the tryout process.

2577
02:01:36.205 --> 02:01:39.885
I'm gonna talk to this parent to get, get clarity

2578
02:01:40.265 --> 02:01:44.005
as it relates to the PSA's responsibility versus the

2579
02:01:44.005 --> 02:01:45.165
school's responsibility.

2580
02:01:45.725 --> 02:01:48.045
PSAL doesn't oversee exactly

2581
02:01:48.115 --> 02:01:49.685
what is happening at the school level.

2582
02:01:50.025 --> 02:01:53.245
We provide procession opportunities who, for those

2583
02:01:53.265 --> 02:01:56.245
who are chosen by the principals, in order to ensure

2584
02:01:56.595 --> 02:01:58.205
that they are in full compliance,

2585
02:01:58.455 --> 02:01:59.885
while they are in fact rules

2586
02:01:59.885 --> 02:02:04.525
and regulations, the, the selection of teams, the selection

2587
02:02:04.525 --> 02:02:08.045
of team members of that, of the individual schools, all of

2588
02:02:08.045 --> 02:02:09.525
that information is publicized.

2589
02:02:09.785 --> 02:02:11.685
It is open book. One of the things

2590
02:02:11.685 --> 02:02:14.965
that we are doing in the PSAL is creating greater

2591
02:02:15.085 --> 02:02:18.285
transparency so that folks have a greater understanding

2592
02:02:18.345 --> 02:02:21.085
of this entire mammoth of a process

2593
02:02:21.305 --> 02:02:23.205
for our public schools athletically.

2594
02:02:23.465 --> 02:02:25.605
I'm gonna talk to this parent and get specifics

2595
02:02:25.745 --> 02:02:28.285
and put her in touch with the executive director

2596
02:02:28.285 --> 02:02:31.565
for the PSAL so that we gain full, um, overall clarity.

2597
02:02:31.665 --> 02:02:35.085
And if there are areas where parents are not understanding,

2598
02:02:35.325 --> 02:02:37.285
I can assure you that we will make that clear

2599
02:02:37.285 --> 02:02:38.325
for parents going forward.

2600
02:02:39.435 --> 02:02:43.325
Right? Thank you. We have the next speaker,

2601
02:02:44.465 --> 02:02:49.325
um, I, it, Craig Slutkin, Gavin Healy or Dr.

2602
02:02:49.325 --> 02:02:53.895
Darling Remy. Okay. Yeah.

2603
02:02:53.975 --> 02:02:56.815
I was told I was number two on list when I signed.

2604
02:02:56.975 --> 02:02:58.855
I started with, we went from student

2605
02:02:58.955 --> 02:03:00.615
to education council members.

2606
02:03:00.815 --> 02:03:02.735
I will now go back to the top of the list

2607
02:03:02.915 --> 02:03:05.415
and call, um, other speakers.

2608
02:03:06.305 --> 02:03:09.485
Uh, I'm Dr. D. Member of CC three.

2609
02:03:10.485 --> 02:03:12.725
I don't know if it's my right, my time right now

2610
02:03:14.375 --> 02:03:15.375
That Dr. Meme.

2611
02:03:15.375 --> 02:03:16.145
Yes. Yes.

2612
02:03:16.615 --> 02:03:18.985
Alright. Thank you so much. Good evening everyone.

2613
02:03:19.485 --> 02:03:20.985
Um, and happy to be here.

2614
02:03:21.125 --> 02:03:23.945
And, uh, I would like to remind that we have the polish,

2615
02:03:24.125 --> 02:03:25.305
uh, heritage month.

2616
02:03:26.005 --> 02:03:29.025
And this time I'm coming here again on behalf

2617
02:03:29.025 --> 02:03:30.145
of Polish community.

2618
02:03:31.195 --> 02:03:35.415
Uh, we request, uh, many times in, uh,

2619
02:03:35.735 --> 02:03:38.495
district three, district 24 CCLL pass resolution

2620
02:03:38.835 --> 02:03:41.975
to support change of regulation, council regulation

2621
02:03:41.995 --> 02:03:46.135
as six three to enlarge number of communications

2622
02:03:46.655 --> 02:03:48.375
languages, permanent communication,

2623
02:03:48.375 --> 02:03:51.415
but DOE to the, uh, community.

2624
02:03:52.035 --> 02:03:56.895
Uh, as you know, New York State speak 12 languages, DOE,

2625
02:03:57.125 --> 02:03:58.815
only nine permanent languages.

2626
02:03:59.115 --> 02:04:00.735
And it's, again, Polish is missing.

2627
02:04:00.965 --> 02:04:03.135
Italian is missing, it is missing.

2628
02:04:03.935 --> 02:04:06.815
I mean, uh, I don't know how other communities

2629
02:04:06.815 --> 02:04:08.815
but the Polish community really need to support

2630
02:04:09.565 --> 02:04:12.695
because what's happened today, what hit me today

2631
02:04:13.285 --> 02:04:16.535
that the principal of only one Brooklyn, uh,

2632
02:04:16.765 --> 02:04:21.205
bilingual school tell the parents that the closing

2633
02:04:21.835 --> 02:04:23.725
program, how it's possible,

2634
02:04:24.185 --> 02:04:25.925
it was hard to build this program.

2635
02:04:26.345 --> 02:04:30.485
And he's easy to say, oh, me and superintendent

2636
02:04:31.145 --> 02:04:35.005
and director of, uh, a multilingual, uh, department,

2637
02:04:35.105 --> 02:04:36.165
we decide to close it.

2638
02:04:37.585 --> 02:04:40.165
Not talking to parents, not talking to SLT even.

2639
02:04:40.625 --> 02:04:43.755
So how it's possible, it's possible

2640
02:04:43.755 --> 02:04:45.435
because parents don't know even

2641
02:04:46.555 --> 02:04:49.485
because DOE not communicate in Polish language

2642
02:04:49.485 --> 02:04:52.805
to polish parents, that they have chance to put the students

2643
02:04:52.805 --> 02:04:55.285
through great bilingual program.

2644
02:04:56.915 --> 02:04:59.775
And again, same situation is in different

2645
02:05:00.015 --> 02:05:01.215
languages in different companies.

2646
02:05:01.755 --> 02:05:05.215
I'm really support if you want to provide you

2647
02:05:05.215 --> 02:05:07.095
with materials, but we need support from

2648
02:05:07.105 --> 02:05:09.515
phase to talk to parents.

2649
02:05:09.745 --> 02:05:11.955
Alright, so thank you so much.

2650
02:05:12.105 --> 02:05:13.675
Have a great evening and please,

2651
02:05:13.675 --> 02:05:15.275
let's continue this conversation.

2652
02:05:16.405 --> 02:05:19.555
Thank you. Thank, I'll call the next group of speakers.

2653
02:05:19.655 --> 02:05:21.195
Um, some people, I'm going to have

2654
02:05:21.195 --> 02:05:24.075
to just use the first part of their email address,

2655
02:05:24.455 --> 02:05:25.755
um, to call them up.

2656
02:05:26.375 --> 02:05:30.475
So the first speaker is mishmash Kella.

2657
02:05:33.275 --> 02:05:37.915
Oh, is, um, Lala Torres here. Okay, please. Sorry.

2658
02:05:38.775 --> 02:05:39.775
Of course.

2659
02:05:47.655 --> 02:05:49.805
Hello everyone. Hope you're having a great day.

2660
02:05:50.145 --> 02:05:53.845
I'm here on behalf of students who don't have a bus

2661
02:05:53.945 --> 02:05:55.045
and don't like school lunch.

2662
02:06:02.755 --> 02:06:06.605
Okay. Um, first, not a lot of kids like school lunch,

2663
02:06:07.025 --> 02:06:08.125
and there's a reason why.

2664
02:06:08.825 --> 02:06:12.165
So the fruits are typically frozen, pretty much unedible.

2665
02:06:12.585 --> 02:06:15.285
Um, I've had an experience where I've had moldy food.

2666
02:06:15.485 --> 02:06:16.685
I bet other kids have two.

2667
02:06:18.065 --> 02:06:20.885
Um, one time I went to go talk to a teacher about it

2668
02:06:21.285 --> 02:06:23.005
and he said, okay, then just don't eat it.

2669
02:06:23.555 --> 02:06:25.445
Some kids don't get sent with lunches.

2670
02:06:25.455 --> 02:06:27.165
Maybe their parents can't afford it

2671
02:06:27.385 --> 02:06:29.645
or they just don't have it.

2672
02:06:30.345 --> 02:06:33.085
The kids should be able to eat the school's lunch

2673
02:06:33.195 --> 02:06:35.205
that the parents tax dollars pay for.

2674
02:06:36.695 --> 02:06:39.195
And I propose there should be another food taste

2675
02:06:39.195 --> 02:06:40.435
testing for the kids.

2676
02:06:41.255 --> 02:06:43.155
And I think maybe the parents should be able

2677
02:06:43.155 --> 02:06:45.115
to taste the food or the kitchen staff, the food

2678
02:06:45.115 --> 02:06:46.675
that they're making, that the kids don't like.

2679
02:06:48.415 --> 02:06:52.635
And yeah. Um, so school buses.

2680
02:06:53.795 --> 02:06:55.755
I don't have a school bus. I don't have an IEP

2681
02:06:55.755 --> 02:06:57.275
and I'm two blocks outta the district.

2682
02:06:57.875 --> 02:06:59.435
I live about two miles away from

2683
02:06:59.435 --> 02:07:00.795
the school, 20 minutes away.

2684
02:07:01.495 --> 02:07:02.595
And I don't have a bus.

2685
02:07:03.575 --> 02:07:06.475
Um, I used to have a bus because my brother had an IEP.

2686
02:07:07.035 --> 02:07:08.715
I don't anymore because he graduated

2687
02:07:08.715 --> 02:07:09.915
and he's two years older than me.

2688
02:07:11.095 --> 02:07:13.635
Um, I might go into middle school without a bus

2689
02:07:14.135 --> 02:07:17.435
and my parents spend maybe a hundred dollars a month on just

2690
02:07:17.525 --> 02:07:20.235
maybe four or five cats because they're like $20.

2691
02:07:21.435 --> 02:07:24.095
Um, it's unfair how I had a bus

2692
02:07:24.155 --> 02:07:26.335
and then when my brother graduated, I didn't have one.

2693
02:07:26.955 --> 02:07:31.715
So I propose kids who already had a bus or some,

2694
02:07:31.935 --> 02:07:34.955
or like even had a bus at one point for whatever reason,

2695
02:07:35.465 --> 02:07:37.925
should be able to keep their bus until they graduate.

2696
02:07:38.865 --> 02:07:42.525
And they should be able to

2697
02:07:43.105 --> 02:07:46.325
extend the distance that kids can have a bus at,

2698
02:07:46.755 --> 02:07:49.605
because two blocks outta the district is not that much.

2699
02:07:50.105 --> 02:07:54.525
Um, I Thank you. Hope y'all have a great night.

2700
02:07:54.525 --> 02:07:56.045
Happy birthday memory schedule.

2701
02:08:03.685 --> 02:08:06.645
We have other speakers. Any other

2702
02:08:06.645 --> 02:08:07.645
Speakers? We do have other

2703
02:08:07.645 --> 02:08:08.485
speakers. Yes.

2704
02:08:09.065 --> 02:08:12.685
So the first speaker, again, the email part, the

2705
02:08:12.685 --> 02:08:14.445
before the email was mishmosh.

2706
02:08:14.765 --> 02:08:18.695
K. Um, then we have Leoni Hamson,

2707
02:08:19.625 --> 02:08:24.485
then ea Gelman, um, David

2708
02:08:25.835 --> 02:08:29.545
dama and ga,

2709
02:08:30.955 --> 02:08:32.865
sorry, excuse me on the pronunciation.

2710
02:08:33.915 --> 02:08:36.115
G-A-L-I-N-A-U-A-U.

2711
02:08:36.985 --> 02:08:40.855
Um, you ready? Yes.

2712
02:08:40.915 --> 02:08:42.855
Please say your name so we know who's speaking.

2713
02:08:43.235 --> 02:08:44.255
My name is Dright

2714
02:08:44.955 --> 02:08:47.015
and I'm gonna be introducing several parents

2715
02:08:47.155 --> 02:08:50.175
who will share their children's experiences at Beacon High

2716
02:08:50.175 --> 02:08:53.775
School and discuss the profound failure in leadership

2717
02:08:54.435 --> 02:08:55.935
by principal Johnny Ventura

2718
02:08:56.595 --> 02:08:59.375
and the assistant principal of Special Ed Naisha Bailey.

2719
02:09:00.165 --> 02:09:01.555
Their shocking inability

2720
02:09:01.855 --> 02:09:04.155
to achieve even the most basic standards

2721
02:09:04.175 --> 02:09:07.715
of compliance program coherence and communication,

2722
02:09:08.535 --> 02:09:11.235
and how these issues are impacting the broader school

2723
02:09:11.235 --> 02:09:12.475
community at Beacon High School

2724
02:09:12.775 --> 02:09:15.915
and the students, particularly IEP students.

2725
02:09:15.915 --> 02:09:18.875
Overall wellbeing. At this time, I yield my time

2726
02:09:18.895 --> 02:09:20.795
to the next speaker from Beacon.

2727
02:09:24.405 --> 02:09:27.305
No, well still two minutes. Okay.

2728
02:09:33.285 --> 02:09:34.735
Good evening. Sign Up.

2729
02:09:35.005 --> 02:09:36.135
Yeah, I know. I'm here tonight

2730
02:09:36.135 --> 02:09:38.415
to read the following statement On behalf

2731
02:09:38.515 --> 02:09:42.095
of another Beacon parent, dear members of the panel

2732
02:09:42.275 --> 02:09:45.465
and senior leadership, I am a beacon parent

2733
02:09:45.605 --> 02:09:49.025
and a career educator with deep knowledge of what it takes

2734
02:09:49.085 --> 02:09:52.025
to make and sustain high quality schools.

2735
02:09:52.025 --> 02:09:54.545
Within the DOEI have been listening to

2736
02:09:54.685 --> 02:09:57.825
and supporting students, staff, and families.

2737
02:09:57.965 --> 02:10:02.745
As we attempt to save Beacon Under Principal Ventura,

2738
02:10:03.045 --> 02:10:06.465
we have experienced incompetent leadership

2739
02:10:07.015 --> 02:10:08.985
that is unwilling to do what it takes

2740
02:10:09.085 --> 02:10:12.295
to make a great school, school administration

2741
02:10:12.405 --> 02:10:16.135
that dismisses the concerns of all constituents

2742
02:10:16.915 --> 02:10:19.215
and speaks in vague generalities

2743
02:10:19.435 --> 02:10:23.165
or blatantly ignores them the dangers

2744
02:10:23.265 --> 02:10:27.205
of toxic fumes, student bomb and shooting threats

2745
02:10:27.865 --> 02:10:30.725
and threats made pointedly against blacks

2746
02:10:30.785 --> 02:10:34.795
and Jews, Serious violations

2747
02:10:34.935 --> 02:10:37.075
of students' rights to a free

2748
02:10:37.295 --> 02:10:41.675
and appropriate public education that cause students to fail

2749
02:10:42.175 --> 02:10:45.705
for classes, actions that violate

2750
02:10:46.305 --> 02:10:49.495
numerous chancellor's regulations, New York State

2751
02:10:49.595 --> 02:10:52.855
and federal laws, including the individuals

2752
02:10:52.885 --> 02:10:57.575
with Disabilities Education Act, et cetera, racism,

2753
02:10:58.455 --> 02:11:00.775
antisemitism, Islamophobia,

2754
02:11:01.195 --> 02:11:04.775
and a lack of safety for LGBTQ plus students.

2755
02:11:05.485 --> 02:11:09.055
Significantly declining staff morale

2756
02:11:10.055 --> 02:11:13.875
and arts and special programs being cut or eliminated.

2757
02:11:14.085 --> 02:11:15.275
Thank you for your comments.

2758
02:11:19.675 --> 02:11:24.455
Um, the next speaker, whose name I read? Yes.

2759
02:11:25.665 --> 02:11:27.165
Hi. Thank you. I'm Amaya Gelman.

2760
02:11:27.185 --> 02:11:28.885
I'm reading for Beacon parents who are anonymous

2761
02:11:29.025 --> 02:11:30.285
for fear of retribution.

2762
02:11:31.615 --> 02:11:35.755
In four years as AP for special ed, Naisha Beatty hasn't

2763
02:11:35.955 --> 02:11:38.795
provided a basic safety net for vulnerable students.

2764
02:11:39.395 --> 02:11:43.235
Beacon's IEP satisfaction is at 48% the lowest

2765
02:11:43.375 --> 02:11:46.275
of all DOE high schools by almost 12%.

2766
02:11:47.005 --> 02:11:49.415
Meanwhile, interim principal of interim background,

2767
02:11:49.555 --> 02:11:50.975
it does a guidance counselor

2768
02:11:51.195 --> 02:11:53.775
and AP for special ed at Brooklyn Tech,

2769
02:11:53.775 --> 02:11:56.015
where he was named in an OCR complaint

2770
02:11:56.035 --> 02:11:57.255
by special ed families.

2771
02:11:58.395 --> 02:11:59.405
Last third quarter,

2772
02:11:59.825 --> 02:12:03.725
beacon special ed students had about a 54% failure rate

2773
02:12:03.785 --> 02:12:06.525
for 10th grade geometry, ninth grade algebra.

2774
02:12:06.525 --> 02:12:09.525
It was 46% ninth grade bio 42%

2775
02:12:10.645 --> 02:12:12.485
11th grade math 54%.

2776
02:12:12.665 --> 02:12:15.005
We got this data through Superintendent Chang's office

2777
02:12:15.005 --> 02:12:17.285
because the administration refused to provide it.

2778
02:12:17.905 --> 02:12:21.555
Ventura is unwilling or unable to engage teachers, students,

2779
02:12:21.655 --> 02:12:23.995
and parents, or look at actual data

2780
02:12:24.135 --> 02:12:26.915
to understand school needs and make meaningful change.

2781
02:12:27.815 --> 02:12:30.075
In June, deputy Chancellor Rux was made aware

2782
02:12:30.195 --> 02:12:34.235
of special ed issues and given 208 pages of FAPE violations,

2783
02:12:34.735 --> 02:12:36.515
she decided more coaching was the answer.

2784
02:12:36.645 --> 02:12:39.115
There are now at least six advisors on site.

2785
02:12:39.135 --> 02:12:40.915
In addition to the five from last year,

2786
02:12:41.175 --> 02:12:42.755
our children get no such support.

2787
02:12:43.715 --> 02:12:46.205
This fall, Mr. Ventura grossly misrepresented

2788
02:12:46.205 --> 02:12:49.405
well-researched parent grading policy recommendations

2789
02:12:49.935 --> 02:12:52.085
suggesting that parents want a grade inflation.

2790
02:12:52.385 --> 02:12:55.645
He pitted us against teachers resulting in UFT complaints.

2791
02:12:56.185 --> 02:12:59.805
Course contracts are still waiting. The CEP is overdue.

2792
02:12:59.805 --> 02:13:02.765
Parents have stepped in to develop a CEP grounded in data

2793
02:13:02.835 --> 02:13:04.205
that responds to actual needs.

2794
02:13:05.545 --> 02:13:06.945
Students gave personal attention

2795
02:13:07.005 --> 02:13:09.345
and support a rating of 56%.

2796
02:13:09.535 --> 02:13:12.345
Even so, special ed teachers were just stripped

2797
02:13:12.345 --> 02:13:13.705
of their advisories and tutoring

2798
02:13:14.625 --> 02:13:16.385
teaching teams completely reshuffled so

2799
02:13:16.385 --> 02:13:19.625
that ICT practices were lost Special ed teachers

2800
02:13:19.905 --> 02:13:21.105
assigned to new subjects.

2801
02:13:21.255 --> 02:13:23.545
Many students say that now their special ed teachers aren't

2802
02:13:23.865 --> 02:13:25.865
familiar enough with their subjects to help them.

2803
02:13:28.405 --> 02:13:31.445
I'll say one more thing. Uh, Ventura has no classroom

2804
02:13:31.445 --> 02:13:32.525
or curriculum experience.

2805
02:13:32.525 --> 02:13:35.005
He came in completely unfamiliar with the consortium model.

2806
02:13:35.115 --> 02:13:36.365
He's never held an invo session

2807
02:13:36.365 --> 02:13:39.725
with parents describing our school's PE pedagogy, presumably

2808
02:13:39.725 --> 02:13:42.205
because he can't DOE is prioritizing

2809
02:13:42.665 --> 02:13:43.325
and experienced

2810
02:13:43.325 --> 02:13:45.005
administrators over the welfare of our children.

2811
02:13:45.015 --> 02:13:45.805
Thank you. Thank you.

2812
02:13:55.775 --> 02:14:00.185
Are you one of the speakers who signed up? I signed up.

2813
02:14:00.185 --> 02:14:04.505
Yeah. I can't hear you. Okay, then please speak.

2814
02:14:08.805 --> 02:14:10.345
My name is Lenny Hamson

2815
02:14:10.345 --> 02:14:13.345
and I co-chair the Parent Coalition for Student Privacy.

2816
02:14:13.645 --> 02:14:16.905
We let the fight for stronger student privacy law

2817
02:14:17.605 --> 02:14:19.345
and the legislature listened

2818
02:14:19.405 --> 02:14:23.105
and passed a new law called Education 2D in 2014.

2819
02:14:24.145 --> 02:14:27.025
Updating the chancellor's regulations on student privacy was

2820
02:14:27.025 --> 02:14:31.105
long overdue and hadn't been done for 16 years, especially

2821
02:14:31.105 --> 02:14:34.305
as there's been an explosion of data sharing by DOE,

2822
02:14:34.415 --> 02:14:37.505
including with more than 500 ed tech companies.

2823
02:14:38.125 --> 02:14:41.385
The need for stronger privacy protections was also shown

2824
02:14:41.405 --> 02:14:42.705
by the recent Illuminate

2825
02:14:42.885 --> 02:14:45.665
and MoveIt breaches, which exposed the personal data

2826
02:14:45.665 --> 02:14:49.385
of over 1 million current and former New York City students.

2827
02:14:49.885 --> 02:14:52.345
Yet instead of strengthening privacy protections,

2828
02:14:52.605 --> 02:14:55.545
the proposed chancellors regulations would significantly

2829
02:14:55.825 --> 02:14:58.145
weakened them by saying that a huge

2830
02:14:58.285 --> 02:15:01.065
and unlimited range of personal student data,

2831
02:15:01.295 --> 02:15:03.625
including their names, phone numbers, emails,

2832
02:15:03.815 --> 02:15:05.945
home addresses, birth dates, photos

2833
02:15:06.045 --> 02:15:07.225
and more could be shared

2834
02:15:07.225 --> 02:15:10.385
with anyone DOE likes without parental consent

2835
02:15:10.385 --> 02:15:13.825
and without any of the privacy protections required

2836
02:15:13.965 --> 02:15:16.865
by the state law to the chancellor.

2837
02:15:17.325 --> 02:15:18.905
We urge you to listen to parents

2838
02:15:18.965 --> 02:15:23.065
and privacy advocates who sent over 3000 emails to you

2839
02:15:23.085 --> 02:15:27.065
and PEP members urging you to require parental consent

2840
02:15:27.285 --> 02:15:30.385
and a written agreement to protect any personal student data

2841
02:15:30.615 --> 02:15:34.065
that is shared with any third parties not contracted

2842
02:15:34.065 --> 02:15:36.185
to provide specific services to schools.

2843
02:15:36.645 --> 02:15:39.185
And that you require that all school medical

2844
02:15:39.405 --> 02:15:42.545
and mental health records be afforded at least

2845
02:15:42.685 --> 02:15:45.865
as strong privacy protections as other student records.

2846
02:15:46.245 --> 02:15:49.305
And that the most rigorous security must be mandated

2847
02:15:49.485 --> 02:15:51.185
to protect against breaches

2848
02:15:51.185 --> 02:15:53.865
and the misuse of student data In general.

2849
02:15:54.005 --> 02:15:56.745
We need the DOE to show far more concern

2850
02:15:56.745 --> 02:15:58.985
and commitment towards protecting the privacy

2851
02:15:59.165 --> 02:16:00.825
and safety of New York City students.

2852
02:16:01.445 --> 02:16:03.025
We also ask that you

2853
02:16:03.245 --> 02:16:06.425
or your staff meet with us along with other advocates

2854
02:16:06.425 --> 02:16:10.065
and parents as soon as possible to ensure the privacy

2855
02:16:10.285 --> 02:16:12.065
and safety of New York City students.

2856
02:16:12.605 --> 02:16:15.865
I'm also concerned what I heard from pe PEP members tonight,

2857
02:16:16.175 --> 02:16:18.265
that they did not receive the 3000

2858
02:16:18.265 --> 02:16:19.665
emails that were sent to them.

2859
02:16:20.085 --> 02:16:22.505
Um, many of them said they received none at all,

2860
02:16:22.515 --> 02:16:24.305
which is extremely concerning

2861
02:16:24.685 --> 02:16:28.625
and makes me worry that DOE is somehow blocking those

2862
02:16:28.765 --> 02:16:30.285
Messages from the public.

2863
02:16:30.575 --> 02:16:32.685
Thank you very much. Thank you. Thank you.

2864
02:16:34.035 --> 02:16:38.885
Um, there's a speaker, David dama

2865
02:16:41.705 --> 02:16:43.325
or Gala now.

2866
02:16:45.925 --> 02:16:47.185
Uh, good afternoon.

2867
02:16:48.065 --> 02:16:49.905
I would like to say that Mass Department

2868
02:16:49.965 --> 02:16:52.225
of Beacon High School is not complying

2869
02:16:52.305 --> 02:16:55.025
with our school's grad policy and philosophy

2870
02:16:55.165 --> 02:16:56.385
and current administration

2871
02:16:56.405 --> 02:16:58.345
of the school is not able to fix the problem.

2872
02:16:58.885 --> 02:17:02.185
I'm the parent of the 10th grader, uh, who has an ip.

2873
02:17:02.325 --> 02:17:03.785
And my child has struggled at

2874
02:17:03.785 --> 02:17:04.985
this school since the beginning.

2875
02:17:05.485 --> 02:17:08.905
We came to begin as a consortium school that should be able

2876
02:17:08.905 --> 02:17:12.865
to, uh, evaluate the different ways in which a child learns

2877
02:17:13.245 --> 02:17:15.985
and beacon, particularly math classes, uh,

2878
02:17:16.055 --> 02:17:19.105
very heavily weighted on, uh, by test in order

2879
02:17:19.165 --> 02:17:21.305
to assess chi uh, students.

2880
02:17:21.605 --> 02:17:23.385
My child is not a good test taker

2881
02:17:23.565 --> 02:17:26.825
and that's why we chose a consortium school in first place

2882
02:17:27.085 --> 02:17:30.745
in Nans Gray, she was assigned to a math ICT class

2883
02:17:30.775 --> 02:17:35.065
with a general ed teacher unsympathetic to special learners.

2884
02:17:35.365 --> 02:17:37.465
The teacher didn't understand my child

2885
02:17:37.565 --> 02:17:39.065
or what her challenges were.

2886
02:17:39.405 --> 02:17:42.105
She didn't believe she struggled with tests in,

2887
02:17:42.325 --> 02:17:44.105
um, in the teacher's class.

2888
02:17:44.245 --> 02:17:48.665
The grade was based 70% on tests, uh, with no opportunity

2889
02:17:48.805 --> 02:17:51.065
for retakes or any grade improvement in

2890
02:17:51.065 --> 02:17:52.225
student fails to test.

2891
02:17:52.565 --> 02:17:56.145
We would work so hard and a lot to prepare her

2892
02:17:56.145 --> 02:17:58.225
or my child for tests and she would fail

2893
02:17:58.885 --> 02:18:02.065
and the teacher would never let her retake, of course.

2894
02:18:02.245 --> 02:18:04.225
And the general education teacher started

2895
02:18:04.245 --> 02:18:08.505
to ignore my emails, eventually send a generic, uh,

2896
02:18:08.875 --> 02:18:10.945
email informing my child was failing.

2897
02:18:11.765 --> 02:18:14.585
Now, uh, instead of mastering the material,

2898
02:18:14.805 --> 02:18:17.345
the priority became attempting to pass the test

2899
02:18:18.045 --> 02:18:19.465
via any means available.

2900
02:18:20.085 --> 02:18:23.225
And my child's IEP lists anxiety over the test

2901
02:18:23.445 --> 02:18:24.665
and their refusal

2902
02:18:24.665 --> 02:18:27.345
to provide recommendation recommendations at Beacon has

2903
02:18:27.545 --> 02:18:31.105
severely impacted my child's mental state self confidence.

2904
02:18:31.105 --> 02:18:33.345
And her, uh, anxiety was worsened.

2905
02:18:33.805 --> 02:18:36.825
Uh, her middle school was a consortium school,

2906
02:18:36.995 --> 02:18:39.985
which allowed retakes and it was never a problem before.

2907
02:18:40.405 --> 02:18:43.145
But then my child came to Beacon and everything changed.

2908
02:18:43.685 --> 02:18:46.345
Uh, and this year the story repeats itself.

2909
02:18:46.375 --> 02:18:49.345
Test 70% of the grade, no retakes.

2910
02:18:49.865 --> 02:18:52.705
I don't mind if you test as one of many other ways

2911
02:18:52.725 --> 02:18:55.945
to assess my child, maybe 20, 25% of the grade,

2912
02:18:56.085 --> 02:18:59.345
but to have the bulk of the grade based on test

2913
02:18:59.415 --> 02:19:01.985
with no opportunity for retakes.

2914
02:19:02.445 --> 02:19:03.865
Uh, with such policies,

2915
02:19:03.865 --> 02:19:06.265
these teachers are sentencing my child to fail

2916
02:19:06.445 --> 02:19:09.785
and no one is able to, uh, fix the problem.

2917
02:19:10.435 --> 02:19:14.385
Thank you. The next group of speakers is

2918
02:19:15.015 --> 02:19:19.915
Jean Ween, um, Eve Smith, Paul Joseph,

2919
02:19:20.535 --> 02:19:22.715
and Mattis Berger.

2920
02:19:23.255 --> 02:19:25.315
If you could make your way to the microphone,

2921
02:19:28.965 --> 02:19:30.345
Um, over there.

2922
02:19:30.445 --> 02:19:33.065
And I'm one of the Beacon parents who also signed up

2923
02:19:33.065 --> 02:19:34.665
to speak, but I don't hear my name being

2924
02:19:34.665 --> 02:19:35.665
Called. Um, I'm

2925
02:19:35.665 --> 02:19:37.745
going down the list All right. As I see it.

2926
02:19:38.205 --> 02:19:42.745
So, alright. There are still some other names to call,

2927
02:19:46.955 --> 02:19:48.615
uh, Gman.

2928
02:19:48.615 --> 02:19:52.495
Yes. Thank you. Thank you. Um, hello, my name is Gwen.

2929
02:19:52.615 --> 02:19:55.055
I am the program director of CAN International.

2930
02:19:55.475 --> 02:19:56.815
We hope to connect with schools

2931
02:19:56.835 --> 02:19:59.615
and organizations that could benefit from our support.

2932
02:20:00.435 --> 02:20:03.055
Canada International is a nonprofit dedicated

2933
02:20:03.155 --> 02:20:05.655
to helping first generation college bound students

2934
02:20:06.575 --> 02:20:09.615
navigate a school application process, preparing them

2935
02:20:09.615 --> 02:20:11.735
with my mentors for college students

2936
02:20:11.875 --> 02:20:14.655
and professionals across various fields.

2937
02:20:15.235 --> 02:20:17.215
We have our 100 active mentors

2938
02:20:17.475 --> 02:20:19.135
and most of them are graduates

2939
02:20:19.135 --> 02:20:20.415
of New York City public schools.

2940
02:20:21.415 --> 02:20:23.015
I am a proud CUNY graduate

2941
02:20:23.015 --> 02:20:25.255
and a New York City public school system

2942
02:20:25.635 --> 02:20:28.775
and a parent who raised white children in the same system.

2943
02:20:29.735 --> 02:20:31.455
I am deeply committed to the mission

2944
02:20:31.795 --> 02:20:34.695
and my experience on the advisory board of high schools.

2945
02:20:34.795 --> 02:20:37.735
And CUNY fuels my passion for empowering these students.

2946
02:20:38.835 --> 02:20:41.095
For the past three years, we've worked with schools,

2947
02:20:41.725 --> 02:20:43.455
schools in Brooklyn, Manhattan,

2948
02:20:43.915 --> 02:20:46.055
and we are currently in our fourth cohort.

2949
02:20:46.755 --> 02:20:48.135
Any guidance from the board

2950
02:20:48.675 --> 02:20:51.775
and panel on how we can better connect

2951
02:20:51.775 --> 02:20:54.655
with schools in the system to provide mentorship

2952
02:20:54.675 --> 02:20:57.335
and support for first generation college students

2953
02:20:57.465 --> 02:20:58.695
would be greatly appreciated.

2954
02:20:58.905 --> 02:21:01.405
Thank you for your time. Thank you.

2955
02:21:02.705 --> 02:21:05.525
Um, is Eve Smith, Paul Joseph,

2956
02:21:05.945 --> 02:21:09.635
or Mattis Berger as the next speakers?

2957
02:21:15.535 --> 02:21:16.575
I have a quick question

2958
02:21:16.895 --> 02:21:18.935
'cause I was allotted a minute 20,

2959
02:21:19.435 --> 02:21:22.435
so if I could just have 40 seconds to finish.

2960
02:21:22.575 --> 02:21:24.955
Are you, did you sign up to be a speaker? I'm Eve Smith.

2961
02:21:25.695 --> 02:21:26.995
You're Eve Smith? Yes.

2962
02:21:27.535 --> 02:21:30.825
Oh, oh, so she someone else referred

2963
02:21:30.825 --> 02:21:32.265
to her so she can speak.

2964
02:21:32.975 --> 02:21:37.435
Yeah. Yeah. Okay. Okay. Okay. Okay. Thank you.

2965
02:21:38.975 --> 02:21:41.675
So, just continuing this statement, on behalf of the

2966
02:21:42.205 --> 02:21:45.525
other person from the other parent from Beacon, many

2967
02:21:45.525 --> 02:21:48.365
of us are losing faith in this system

2968
02:21:48.785 --> 02:21:50.805
and wonder why we are at Beacon.

2969
02:21:51.735 --> 02:21:55.025
Even with the support of Superintendent Chang's staff

2970
02:21:55.285 --> 02:21:57.225
for over a year, Mr.

2971
02:21:57.415 --> 02:22:01.225
Ventura has failed to address fundamental challenges

2972
02:22:01.845 --> 02:22:05.105
and has been unable to inspire key stakeholders

2973
02:22:05.695 --> 02:22:07.985
that the school is moving in the right direction.

2974
02:22:09.745 --> 02:22:13.925
The recent 2324 New York City School survey dashboard shows

2975
02:22:13.925 --> 02:22:15.365
that Beacon is dying.

2976
02:22:16.105 --> 02:22:19.245
Nearly every category is red.

2977
02:22:20.155 --> 02:22:23.295
You know, this means that interim acting Principal Ventura,

2978
02:22:23.365 --> 02:22:27.045
it's failing the students, students and staff in his care.

2979
02:22:28.245 --> 02:22:31.785
We are watching Beacon's demise and we feel trapped.

2980
02:22:32.395 --> 02:22:34.865
There is so much special about this school.

2981
02:22:35.365 --> 02:22:38.385
It has good bones and can still be healed.

2982
02:22:39.105 --> 02:22:42.765
Expert teachers on staff have a deep understanding of

2983
02:22:43.265 --> 02:22:46.525
and commitment to consortium equity

2984
02:22:46.785 --> 02:22:49.605
and culturally responsive pedagogy.

2985
02:22:50.395 --> 02:22:51.885
They will not stay forever.

2986
02:22:52.385 --> 02:22:56.125
If this continues, we cannot all speak directly

2987
02:22:56.225 --> 02:23:00.865
to those in power for fear of retaliation, we have lot

2988
02:23:00.885 --> 02:23:04.465
to lose and we have already lost too much.

2989
02:23:05.085 --> 02:23:07.665
But we are here, we are watching

2990
02:23:08.045 --> 02:23:10.785
and we are begging you to step in.

2991
02:23:11.075 --> 02:23:12.875
Thank you. Thank

2992
02:23:20.885 --> 02:23:22.975
Paul Joseph or Matts Berger.

2993
02:23:25.715 --> 02:23:28.015
Uh, good evening Panel for educational policy

2994
02:23:28.195 --> 02:23:30.295
and a Chancellor of Vz Ramos.

2995
02:23:30.515 --> 02:23:32.815
Uh, thank you for giving me the time tonight to speak.

2996
02:23:33.435 --> 02:23:34.535
Uh, my name is Paul Joseph,

2997
02:23:34.675 --> 02:23:38.295
and I'm an ELA teacher at a transfer school at Brooklyn High

2998
02:23:38.295 --> 02:23:40.015
School for Leadership and Community Service.

2999
02:23:40.795 --> 02:23:43.415
One of about 50 transfer schools, uh, throughout New York.

3000
02:23:43.875 --> 02:23:47.215
Um, on October 7th, um, superintendent, um,

3001
02:23:47.535 --> 02:23:50.575
Jonathan Sullivan announced that he was submitting our name,

3002
02:23:51.315 --> 02:23:54.735
um, to be closed, uh, at the end of this term.

3003
02:23:55.435 --> 02:23:58.095
And, um, so that catapulted me

3004
02:23:58.095 --> 02:23:59.815
to be here this evening, speaking to you.

3005
02:24:00.115 --> 02:24:01.935
And, um, in, in, in the minute

3006
02:24:01.995 --> 02:24:04.095
and 25 seconds I have left, there's really two things

3007
02:24:04.095 --> 02:24:05.135
that I wanna accomplish.

3008
02:24:05.195 --> 02:24:06.975
And, and the first one is, is

3009
02:24:07.175 --> 02:24:09.295
to just point out the complete, I guess,

3010
02:24:09.525 --> 02:24:13.455
cognitive dissonance and complete, uh, kind of confusion

3011
02:24:13.455 --> 02:24:15.495
and puzzlement that exists when you have

3012
02:24:16.195 --> 02:24:20.215
two narratives about the same place that are so divergent.

3013
02:24:20.675 --> 02:24:22.775
And on one hand, we're failing school, and,

3014
02:24:22.795 --> 02:24:26.135
and even though there were 62 schools on the state

3015
02:24:26.415 --> 02:24:29.375
receivership list and the 60 were removed

3016
02:24:29.475 --> 02:24:31.015
and all remaining, only us

3017
02:24:31.015 --> 02:24:32.735
and one other student, um,

3018
02:24:33.965 --> 02:24:35.385
it would look like a failing school.

3019
02:24:35.405 --> 02:24:38.225
But on the other hand, we have this really vital, really,

3020
02:24:38.225 --> 02:24:41.985
really experienced, uh, school that is responding relevantly

3021
02:24:41.985 --> 02:24:43.545
to our families and students.

3022
02:24:43.965 --> 02:24:46.025
And we have so many good things happening.

3023
02:24:46.565 --> 02:24:49.905
So, um, I just, it it puzzles me

3024
02:24:50.785 --> 02:24:52.165
to live with that dissonance.

3025
02:24:52.625 --> 02:24:55.485
Um, the last thing that I would like to do is I would, I, I,

3026
02:24:55.645 --> 02:24:58.005
I really would love to have some of you come out

3027
02:24:58.005 --> 02:25:01.845
to see our school on 300 Willoughby Avenue in Bedstuy.

3028
02:25:02.125 --> 02:25:04.045
I I know that you're very, very, very busy,

3029
02:25:04.505 --> 02:25:07.205
but if some of you can make some time to come see

3030
02:25:07.205 --> 02:25:09.565
what we do, I think you will come to the same conclusion

3031
02:25:09.955 --> 02:25:12.925
that it is worth saving this school.

3032
02:25:13.425 --> 02:25:15.405
Um, and so I please invite you,

3033
02:25:15.405 --> 02:25:16.445
and again, I thank you

3034
02:25:16.445 --> 02:25:17.765
for your time this evening. Thank you.

3035
02:25:17.935 --> 02:25:18.365
Thank you.

3036
02:25:26.905 --> 02:25:29.025
Good evening. Uh, my name is Mattai Lindberger.

3037
02:25:29.045 --> 02:25:31.305
I'm the school social worker at the Brooklyn High School

3038
02:25:31.305 --> 02:25:32.705
of Leadership and Community Service.

3039
02:25:33.405 --> 02:25:36.705
Um, I have been there since 2012.

3040
02:25:37.345 --> 02:25:40.425
I started out as a special education teacher, um,

3041
02:25:40.525 --> 02:25:43.425
and then transitioned into the role of school social Worker,

3042
02:25:43.925 --> 02:25:45.345
um, for years ago.

3043
02:25:45.925 --> 02:25:50.305
Um, as my, uh, colleague, um, Mr. Joseph explained, we, uh,

3044
02:25:50.305 --> 02:25:55.185
were recently told that our school is, um, scheduled

3045
02:25:55.205 --> 02:25:56.865
or, or proposed to be closed.

3046
02:25:57.445 --> 02:26:00.265
Uh, and the reason, uh, for that was, um,

3047
02:26:00.775 --> 02:26:05.305
basically bad attendance, um, data,

3048
02:26:05.805 --> 02:26:08.785
uh, on, uh, on regents passing, um,

3049
02:26:09.845 --> 02:26:11.185
and, uh, and graduation rates.

3050
02:26:11.725 --> 02:26:13.825
So, um, I believe

3051
02:26:13.825 --> 02:26:16.185
that we've made tremendous progress in

3052
02:26:16.185 --> 02:26:17.465
those, uh, those respects.

3053
02:26:17.965 --> 02:26:20.545
Our, our, um, graduation rate

3054
02:26:21.465 --> 02:26:23.945
actually is significantly higher than

3055
02:26:24.525 --> 02:26:28.025
the transfer school average, uh, at 60, uh, 7%.

3056
02:26:28.645 --> 02:26:33.465
Um, we graduated 60 students just last year between January

3057
02:26:34.205 --> 02:26:35.705
and, uh, and August of this year.

3058
02:26:36.085 --> 02:26:38.425
Uh, we graduated 60 students. We're a small school.

3059
02:26:38.845 --> 02:26:41.745
Uh, so that's about 30% of our, our student population

3060
02:26:41.745 --> 02:26:43.185
that was able to graduate last year

3061
02:26:43.185 --> 02:26:45.265
with a high school diploma, uh, which is not nothing.

3062
02:26:45.885 --> 02:26:48.795
Um, I also believe that, you know,

3063
02:26:48.795 --> 02:26:50.355
the numbers don't tell the whole story.

3064
02:26:50.535 --> 02:26:53.875
Um, we, we, um, we provide much more

3065
02:26:53.875 --> 02:26:55.635
to our students than just classroom instruction.

3066
02:26:55.915 --> 02:26:58.475
A lot of our students, um, come in with, you know,

3067
02:26:58.825 --> 02:27:00.715
just being our, their, their third

3068
02:27:00.715 --> 02:27:04.795
or fourth school, um, having, uh, uh,

3069
02:27:04.825 --> 02:27:07.555
significant barriers to coming to school at home.

3070
02:27:07.815 --> 02:27:10.995
Um, a lot of our students struggle with, uh,

3071
02:27:10.995 --> 02:27:14.995
mental health issues, depression, anxiety, uh, uh,

3072
02:27:14.995 --> 02:27:16.755
housing insecurity, food insecurity,

3073
02:27:17.175 --> 02:27:19.955
and all these become barriers to attendance.

3074
02:27:20.535 --> 02:27:22.355
And we work around that.

3075
02:27:22.415 --> 02:27:24.915
We engage with all of our students, uh, even those

3076
02:27:24.915 --> 02:27:27.435
that don't show up every day, uh, through ELT,

3077
02:27:27.585 --> 02:27:28.635
through outreach.

3078
02:27:29.095 --> 02:27:30.115
Um, and, and,

3079
02:27:30.175 --> 02:27:32.875
and many more, um, ways that we connect with our students.

3080
02:27:33.455 --> 02:27:36.715
Uh, like my co uh, co uh, coworkers said we'd love

3081
02:27:36.715 --> 02:27:40.035
to invite you guys and see what we're doing at leadership.

3082
02:27:40.695 --> 02:27:41.995
And I know my time is up. Thank

3083
02:27:41.995 --> 02:27:42.995
You. Thank you.

3084
02:27:42.995 --> 02:27:44.605
And the next,

3085
02:27:46.555 --> 02:27:51.405
the next group of speakers, Dan Bright, Michelle Baptist,

3086
02:27:53.165 --> 02:27:56.675
Alexandra Opolis, Ellen Chu,

3087
02:27:56.895 --> 02:27:58.635
and Christina Collins.

3088
02:28:01.925 --> 02:28:04.015
Okay. So, um, my name is Dan Bright.

3089
02:28:04.195 --> 02:28:06.295
I'm, uh, very dissatisfied

3090
02:28:06.515 --> 02:28:11.135
and soon to be former, uh, customer at Beacon High School.

3091
02:28:11.475 --> 02:28:14.695
Um, I'm asked to come here by other parents

3092
02:28:14.795 --> 02:28:16.215
who don't wanna speak publicly

3093
02:28:16.335 --> 02:28:19.455
'cause they're scared of retaliation by the schools, uh,

3094
02:28:19.455 --> 02:28:21.165
administration and by teachers.

3095
02:28:21.545 --> 02:28:23.005
So my son is a freshman.

3096
02:28:23.375 --> 02:28:24.885
We've been there just under two months,

3097
02:28:24.945 --> 02:28:29.685
and thank God I just got a, a guidance transfer, uh, request

3098
02:28:30.485 --> 02:28:32.005
approved to get him out of that school

3099
02:28:32.425 --> 02:28:34.045
and into another school beginning Monday.

3100
02:28:34.945 --> 02:28:37.405
I'm gonna just read to you an email, uh, that I sent

3101
02:28:37.405 --> 02:28:39.045
to Crystal Davis two days ago.

3102
02:28:39.905 --> 02:28:42.525
Uh, she's the Director of Special Education in the office

3103
02:28:42.585 --> 02:28:44.685
of superintendent Alan Chang.

3104
02:28:45.045 --> 02:28:46.365
I just wrote to her because I had dealt

3105
02:28:46.365 --> 02:28:47.725
with her once before about something.

3106
02:28:47.745 --> 02:28:49.245
She was the only person I could think of

3107
02:28:49.465 --> 02:28:50.725
to try to help us with this.

3108
02:28:51.345 --> 02:28:54.605
So dear Ms. Davis, our son's treatment at Beacon High School

3109
02:28:54.625 --> 02:28:58.245
has deteriorated rapidly since we last communicated.

3110
02:28:58.675 --> 02:29:00.125
He's being bullied by teachers.

3111
02:29:00.385 --> 02:29:02.525
His IEP requirements are being violated

3112
02:29:02.665 --> 02:29:04.165
by teachers on a daily basis.

3113
02:29:04.555 --> 02:29:06.925
Despite our repeated requests to teachers

3114
02:29:06.985 --> 02:29:09.805
and administrators to comply with the IEP mandates.

3115
02:29:09.985 --> 02:29:13.045
And he's now experiencing anxiety that we believe is going

3116
02:29:13.045 --> 02:29:15.085
to lead to a very serious mental health crisis.

3117
02:29:15.545 --> 02:29:18.245
We do not get him to another school immediately.

3118
02:29:18.795 --> 02:29:20.925
Last week, I went to the Family Welcome Center

3119
02:29:21.465 --> 02:29:23.005
at 3 33 seventh Avenue

3120
02:29:23.065 --> 02:29:25.405
and requested an immediate transfer to the Academy

3121
02:29:25.545 --> 02:29:27.365
for Careers in television and film.

3122
02:29:27.665 --> 02:29:29.845
We urgently request that you do whatever you can

3123
02:29:29.845 --> 02:29:31.485
to get this transfer approved right away.

3124
02:29:31.705 --> 02:29:33.125
The IEP violations

3125
02:29:33.125 --> 02:29:34.925
that have been ongoing since the beginning

3126
02:29:34.925 --> 02:29:37.885
of the school year include one requiring my son

3127
02:29:37.885 --> 02:29:41.445
to write answers to test questions by hand, despite the fact

3128
02:29:41.445 --> 02:29:43.765
that his IEP mandates, he'd be permitted

3129
02:29:43.765 --> 02:29:47.845
to use assistive technology, EG typed answers on his laptop

3130
02:29:47.865 --> 02:29:50.845
or dictate answers orally using voice to text software.

3131
02:29:51.105 --> 02:29:54.245
Two, refusing to reduce the quantity of homework he is given

3132
02:29:55.115 --> 02:29:57.905
three, refusing to let him hand in homework late without a

3133
02:29:57.905 --> 02:30:00.905
penalty with some teachers giving him a zero if he tries

3134
02:30:00.905 --> 02:30:02.665
to hand in homework a day late.

3135
02:30:02.685 --> 02:30:05.985
And his IEP says he shouldn't be penalized for handing in

3136
02:30:06.585 --> 02:30:08.505
homework late, not reducing the number

3137
02:30:08.505 --> 02:30:10.705
of questions on quizzes, and then failing him

3138
02:30:10.705 --> 02:30:13.025
because he can't complete the number they've given him,

3139
02:30:13.115 --> 02:30:16.625
which are well beyond his neurological capacities,

3140
02:30:16.925 --> 02:30:18.185
and it's in his IEP.

3141
02:30:18.205 --> 02:30:20.105
And they refuse to modify

3142
02:30:20.365 --> 02:30:21.945
or do anything they're required to.

3143
02:30:22.155 --> 02:30:25.025
We've talked to the principal, we've talked to the AP

3144
02:30:25.045 --> 02:30:27.105
for special ed, we've talked to the teachers.

3145
02:30:27.105 --> 02:30:28.625
They just ignore us. They do nothing.

3146
02:30:28.735 --> 02:30:30.785
They're the most incompetent people we've

3147
02:30:30.785 --> 02:30:31.905
ever seen in our lives.

3148
02:30:32.285 --> 02:30:34.905
My wife works at another high school for nearly 20 years

3149
02:30:34.965 --> 02:30:38.585
as an SLP, and she's absolutely shocked at the low

3150
02:30:38.585 --> 02:30:40.025
quality of the teaching.

3151
02:30:40.285 --> 02:30:42.985
The, the rudeness and lack of respect from a lot

3152
02:30:42.985 --> 02:30:44.825
of the teachers, from the administrators.

3153
02:30:44.935 --> 02:30:48.145
None of these people would last a few months at her school.

3154
02:30:48.205 --> 02:30:50.545
And I've been hearing about her school for almost 20 years.

3155
02:30:50.765 --> 02:30:52.945
And what happens there when a new, when, when,

3156
02:30:52.945 --> 02:30:54.625
when a teacher is causing trouble

3157
02:30:54.805 --> 02:30:56.465
or when an AP isn't performing.

3158
02:30:56.465 --> 02:30:58.025
Thank you. They get it. They get rid of them.

3159
02:30:58.285 --> 02:31:00.185
You need to clean that place up. Thank you.

3160
02:31:07.595 --> 02:31:09.455
Uh, beacons, families

3161
02:31:09.875 --> 02:31:14.495
and staff, thank you for your comments and your input

3162
02:31:14.795 --> 02:31:16.975
and to, uh, Brooklyn Leadership.

3163
02:31:16.985 --> 02:31:20.525
Thank you so much. I just wanna clarify something that, uh,

3164
02:31:20.825 --> 02:31:22.765
we are in early stages of engagement.

3165
02:31:22.965 --> 02:31:25.125
A decision has not been made about closure.

3166
02:31:25.425 --> 02:31:27.245
So I just wanna, I wanna make that point.

3167
02:31:27.665 --> 02:31:29.085
Uh, and thank you for the invitation.

3168
02:31:32.865 --> 02:31:37.235
High school early. Um, the next Michelle Baptist,

3169
02:31:38.625 --> 02:31:42.495
Alexandra Opolis, Ellen McCue,

3170
02:31:43.735 --> 02:31:45.035
or Christina Collins.

3171
02:31:46.885 --> 02:31:49.665
Hi, uh, thank you to the panel for your time this evening.

3172
02:31:49.925 --> 02:31:53.345
Um, we wanna say first, welcome to the new Chancellor Ramos.

3173
02:31:53.345 --> 02:31:54.385
We're very happy to have you.

3174
02:31:55.045 --> 02:31:56.945
Um, I'm a teacher at a consortium high

3175
02:31:56.945 --> 02:31:58.225
school and Chancellor Ramos.

3176
02:31:58.265 --> 02:32:00.985
I really hope that we can begin to ease the relationship

3177
02:32:00.985 --> 02:32:03.265
between the consortium and the DOE.

3178
02:32:03.655 --> 02:32:06.585
It's been a rough ride so far with the Adams administration,

3179
02:32:06.805 --> 02:32:10.185
and we really look forward to your, um, encouragement

3180
02:32:10.205 --> 02:32:12.745
of the type of learning and assessment that we do.

3181
02:32:12.775 --> 02:32:15.265
Project-based learning, culturally responsive learning,

3182
02:32:15.805 --> 02:32:17.225
um, curriculum rather.

3183
02:32:18.165 --> 02:32:22.065
Um, you've heard tonight about how, uh, ill-equipped these,

3184
02:32:22.205 --> 02:32:25.145
um, sort of pre-programmed assessments are

3185
02:32:25.205 --> 02:32:26.745
to truly get to know our students.

3186
02:32:26.845 --> 02:32:29.065
And that's the type of, that's the opposite of the type

3187
02:32:29.065 --> 02:32:31.905
of learning that we try to do in the consortium model.

3188
02:32:32.085 --> 02:32:34.745
Um, teachers are best equipped to assess their students,

3189
02:32:35.325 --> 02:32:38.585
not computers, um, in regards to these contracts.

3190
02:32:38.645 --> 02:32:39.865
I'd also like to pose a question.

3191
02:32:39.965 --> 02:32:41.345
Why are we signing contracts

3192
02:32:41.345 --> 02:32:43.145
for longer than the mayor's term limits?

3193
02:32:43.815 --> 02:32:46.545
Mayoral control leads to a very chaotic

3194
02:32:47.245 --> 02:32:50.505
system on the ground floor in the DOE, um,

3195
02:32:50.565 --> 02:32:51.985
and extending these contracts

3196
02:32:51.985 --> 02:32:54.145
for such long times, do nothing to help it.

3197
02:32:54.525 --> 02:32:57.425
Um, I'd also like to say that I hope one

3198
02:32:57.425 --> 02:32:59.585
of the first things this new administration does is

3199
02:32:59.905 --> 02:33:03.025
reinstate Taj Sutton as CEC 14 president,

3200
02:33:04.315 --> 02:33:08.575
as you did with the racist homophobic CET two President,

3201
02:33:08.575 --> 02:33:11.375
whose groups have recently been founded to be funded

3202
02:33:11.435 --> 02:33:13.895
by Na Nazi enthusiast, Harlan Crow,

3203
02:33:14.535 --> 02:33:17.095
Republican hedge fund billionaire, such as Joseph Derman,

3204
02:33:17.115 --> 02:33:19.975
Dan Loeb, Paul Singer, and the list goes on.

3205
02:33:19.975 --> 02:33:23.375
These hyper conservatives have no place putting their money

3206
02:33:23.395 --> 02:33:27.255
in the DOE and shame on the DOE for reinstating this type

3207
02:33:27.255 --> 02:33:29.055
of depravity or depravity,

3208
02:33:29.055 --> 02:33:31.735
and continuing to sign light, the much needed leadership

3209
02:33:31.955 --> 02:33:34.655
of Taj Sutton in d and CEC 14.

3210
02:33:35.035 --> 02:33:36.495
Now I yield the rest of my time. Thank you.

3211
02:33:39.435 --> 02:33:40.445
Next speaker, please.

3212
02:33:46.345 --> 02:33:47.845
Oh, I'll take a shot. Yeah.

3213
02:33:49.895 --> 02:33:51.035
My name is Ellen McQue

3214
02:33:51.055 --> 02:33:53.515
and I am along with Shirley Bin,

3215
02:33:54.195 --> 02:33:56.355
a recovering Mets fan, but

3216
02:33:56.355 --> 02:34:01.255
I'm also, I am also

3217
02:34:01.255 --> 02:34:05.055
the parent of a deaf, uh, deaf person, an adult who went

3218
02:34:05.055 --> 02:34:07.895
through the New York City public school system successfully.

3219
02:34:10.725 --> 02:34:15.565
I am also hearing an oral, so I have my feet in both worlds

3220
02:34:16.605 --> 02:34:17.795
over, over the summer.

3221
02:34:18.145 --> 02:34:19.475
It's come to my attention

3222
02:34:19.535 --> 02:34:22.315
and it's a small world, even though I have big feet.

3223
02:34:22.655 --> 02:34:26.795
But the, over the summer, it's come to our attention

3224
02:34:27.865 --> 02:34:31.835
that three students at a non-public school had their hearing

3225
02:34:31.945 --> 02:34:35.115
education services aborted, um,

3226
02:34:35.735 --> 02:34:37.115
by the Department of Ed.

3227
02:34:37.255 --> 02:34:40.595
The people were given a short amount of time

3228
02:34:40.815 --> 02:34:43.275
to get what's called a related service provider.

3229
02:34:43.575 --> 02:34:47.235
The related service provider was not available.

3230
02:34:48.025 --> 02:34:50.395
This is not the first and only example.

3231
02:34:50.905 --> 02:34:53.515
Some of you ha may have seen the, um,

3232
02:34:54.765 --> 02:34:56.675
press conference in Staten Island.

3233
02:34:57.265 --> 02:35:00.795
There's also been an ins a few incidences in the Bronx,

3234
02:35:01.575 --> 02:35:05.275
and collectively at 3 47, which is the

3235
02:35:05.985 --> 02:35:07.005
junior high school

3236
02:35:07.145 --> 02:35:09.805
and elementary school for the deaf, there are a number

3237
02:35:09.805 --> 02:35:12.255
of children who've had their busing

3238
02:35:12.855 --> 02:35:14.615
services taken away from them.

3239
02:35:14.845 --> 02:35:17.215
They are there at that school for both cultural

3240
02:35:17.275 --> 02:35:18.655
and linguistic reasons.

3241
02:35:20.055 --> 02:35:22.075
The unfortunate part about this is

3242
02:35:22.075 --> 02:35:26.355
that the DOE has the legal department of the DOE has chosen

3243
02:35:26.495 --> 02:35:30.035
to enforce a ruling about

3244
02:35:30.625 --> 02:35:34.915
providing information to the DOE by June one

3245
02:35:35.185 --> 02:35:37.955
that was created in 2007.

3246
02:35:38.415 --> 02:35:43.085
It has never been implemented like this,

3247
02:35:44.115 --> 02:35:45.855
and families are unaware.

3248
02:35:46.525 --> 02:35:47.935
When questioned, I was told

3249
02:35:47.935 --> 02:35:50.255
that families get a due process Notice

3250
02:35:50.915 --> 02:35:54.895
the due process notice is 42 pages.

3251
02:35:56.515 --> 02:35:58.205
It's difficult enough for a person

3252
02:35:58.385 --> 02:36:01.285
who is English speaking to understand it.

3253
02:36:01.635 --> 02:36:04.285
It's almost impossible for someone who is not

3254
02:36:06.395 --> 02:36:09.085
well educated in our

3255
02:36:10.235 --> 02:36:12.065
legal system to understand it.

3256
02:36:13.535 --> 02:36:16.075
I'd also like to bring two things to your attention.

3257
02:36:16.825 --> 02:36:21.185
When I walked in here today, there was steps to come up

3258
02:36:21.185 --> 02:36:22.265
to this auditorium.

3259
02:36:23.105 --> 02:36:27.645
The individuals at the door, while kind did not know

3260
02:36:28.015 --> 02:36:31.205
where the accessible site is,

3261
02:36:31.625 --> 02:36:33.325
the accessible access is.

3262
02:36:34.445 --> 02:36:36.285
Additionally, if I'm at home

3263
02:36:36.705 --> 02:36:38.085
and watching this online,

3264
02:36:38.445 --> 02:36:40.325
I can turn on my closed captioning.

3265
02:36:40.735 --> 02:36:41.885
While I understand

3266
02:36:41.915 --> 02:36:45.725
that requesting an A SL interpreter take some time

3267
02:36:46.225 --> 02:36:47.285
and should be done well

3268
02:36:47.285 --> 02:36:50.205
before this meeting, I am dumbfounded

3269
02:36:50.205 --> 02:36:53.165
that you don't have real time captioning.

3270
02:36:53.975 --> 02:36:58.675
This is silly outside of the fact that for most

3271
02:36:58.675 --> 02:37:01.995
of us, we mumble when we get up to a microphone.

3272
02:37:02.335 --> 02:37:04.915
And it was very hard to hear some of the people

3273
02:37:04.975 --> 02:37:08.045
who spoke tonight with real time captioning.

3274
02:37:08.105 --> 02:37:11.365
Not only a deaf person, but a hearing person could hear

3275
02:37:11.385 --> 02:37:14.725
and understand what was being said, whether it was

3276
02:37:14.725 --> 02:37:15.725
Eloquent or not. Was

3277
02:37:15.725 --> 02:37:19.685
it material? It was being said. Shirley next year.

3278
02:37:19.685 --> 02:37:21.325
Thank you. Thank you.

3279
02:37:29.515 --> 02:37:31.015
Hi, I'm Christina Collins.

3280
02:37:31.275 --> 02:37:33.815
I'm Director of Education Policy for the UFT.

3281
02:37:34.155 --> 02:37:38.975
Um, I'm here tonight, uh, both to, uh, bring, uh,

3282
02:37:39.125 --> 02:37:43.375
back the issue of our, uh, occupational physical therapist

3283
02:37:43.555 --> 02:37:45.495
who spoke at last month's meeting.

3284
02:37:46.075 --> 02:37:49.615
Um, they did share, they did share

3285
02:37:49.715 --> 02:37:51.575
as requested an overview

3286
02:37:51.675 --> 02:37:54.055
of their concerns about the outsourcing of their work,

3287
02:37:54.055 --> 02:37:56.335
particularly in District 75 as of right now.

3288
02:37:56.995 --> 02:37:59.935
Um, as of the last time I spoke to 'em a couple days ago,

3289
02:37:59.935 --> 02:38:02.575
they had not yet received a response from

3290
02:38:02.575 --> 02:38:03.815
what they had sent to the pep.

3291
02:38:03.915 --> 02:38:05.575
So if you could just confirm that

3292
02:38:05.575 --> 02:38:07.415
that message was received from them

3293
02:38:07.515 --> 02:38:09.535
and let them know if you have any

3294
02:38:09.535 --> 02:38:11.015
additional questions, that would be great.

3295
02:38:11.395 --> 02:38:13.815
The primary reason I'm here tonight, though, is to speak

3296
02:38:13.835 --> 02:38:17.255
to the student privacy regulation, which was, uh,

3297
02:38:17.255 --> 02:38:18.815
removed from tonight's agenda,

3298
02:38:18.875 --> 02:38:22.375
but, which I understand is likely to appear on, uh,

3299
02:38:22.435 --> 02:38:23.535
an upcoming agenda.

3300
02:38:24.235 --> 02:38:27.895
And, uh, to that, I just wanna read a very brief, uh,

3301
02:38:28.245 --> 02:38:31.655
statement, um, that the ts uh,

3302
02:38:31.785 --> 02:38:33.855
about the t's concerns around this issue.

3303
02:38:34.145 --> 02:38:36.775
We're particularly concerned that the proposed changes

3304
02:38:37.345 --> 02:38:40.255
would, rather than strengthening student privacy,

3305
02:38:40.445 --> 02:38:43.175
protect protections, uh, would weaken them.

3306
02:38:43.755 --> 02:38:47.775
Um, the state law passed in 2014, we think is a good model

3307
02:38:48.395 --> 02:38:51.255
and, uh, includes, uh, safeguards

3308
02:38:51.255 --> 02:38:55.095
for student data protections that address the issues

3309
02:38:55.325 --> 02:38:58.095
that are intensifying with the increased access

3310
02:38:58.115 --> 02:39:01.295
to student data by private vendors and by private companies.

3311
02:39:01.875 --> 02:39:05.855
Um, however, upon review of the regulations

3312
02:39:05.875 --> 02:39:09.375
as they were proposed, we believe they do not align with

3313
02:39:09.375 --> 02:39:12.575
that 2014 law with other state regulations

3314
02:39:12.835 --> 02:39:15.815
or with state, uh, department of Education guidance.

3315
02:39:16.515 --> 02:39:17.615
Um, and we stand

3316
02:39:17.645 --> 02:39:19.695
with the Parent Coalition per Student privacy.

3317
02:39:19.835 --> 02:39:23.615
And the more than 3000, uh, advocates and students

3318
02:39:23.755 --> 02:39:25.935
and teachers and parents who have already reached out

3319
02:39:25.935 --> 02:39:27.295
to you on this, we are concerned

3320
02:39:27.365 --> 02:39:30.215
that you may not have received, uh, those messages

3321
02:39:30.235 --> 02:39:32.735
of concern about this issue.

3322
02:39:33.195 --> 02:39:37.295
Uh, we believe in particular, that any student data be

3323
02:39:37.515 --> 02:39:40.175
to be shared would require parental consent

3324
02:39:40.235 --> 02:39:42.815
and should comply with HIPAA and state standards,

3325
02:39:43.235 --> 02:39:46.575
and that any security measures implement, uh, require

3326
02:39:46.575 --> 02:39:50.055
by state law should be clearly reflected in any contract

3327
02:39:50.155 --> 02:39:53.455
and aggressively required by the DOE

3328
02:39:53.455 --> 02:39:54.655
of all vendors. Thank you.

3329
02:39:54.745 --> 02:39:59.635
Thank you. I have called all the speakers

3330
02:39:59.635 --> 02:40:00.875
who have signed up for public comment.

3331
02:40:07.425 --> 02:40:07.705
I mean,

3332
02:40:14.305 --> 02:40:15.395
yeah, we're gonna check.

3333
02:40:16.775 --> 02:40:19.905
You can sign. Yeah,

3334
02:40:20.285 --> 02:40:21.745
but they would've had to sign up for the, uh,

3335
02:40:21.745 --> 02:40:22.745
they should have signed up for, um, second.

3336
02:40:22.745 --> 02:40:26.505
They should signed up for, for both. Yeah. I don't know.

3337
02:40:28.185 --> 02:40:31.665
I, um, okay. Same thing happened last month.

3338
02:40:41.415 --> 02:40:43.305
Hold on one sec. Hold on one minute.

3339
02:40:49.715 --> 02:40:52.695
My apologies. Technology, um, I'm,

3340
02:40:53.295 --> 02:40:55.575
I will call the names people who signed up for both.

3341
02:40:56.865 --> 02:41:01.835
Okay. So I will go back to Emily Haynes Elona,

3342
02:41:02.505 --> 02:41:05.525
Nene, Kamala Carmen,

3343
02:41:08.945 --> 02:41:12.805
um, clear Salas and Martina Meyer.

3344
02:41:16.805 --> 02:41:19.525
I want to speak to not just the assessments,

3345
02:41:19.625 --> 02:41:21.205
but what we're talking about in terms

3346
02:41:21.205 --> 02:41:24.325
of teacher expertise in designing

3347
02:41:24.425 --> 02:41:26.605
and implementing our own curriculum.

3348
02:41:27.145 --> 02:41:30.285
My school is under a mandate from our superintendent

3349
02:41:30.315 --> 02:41:33.365
that we have to teach a specific ELA curriculum

3350
02:41:33.385 --> 02:41:36.965
and a specific math curriculum on a specific pacing

3351
02:41:37.275 --> 02:41:39.205
that does not allow us to differentiate

3352
02:41:39.345 --> 02:41:41.125
or meet the needs of our students.

3353
02:41:41.705 --> 02:41:44.245
As it was pointed out earlier by one of the panel members,

3354
02:41:44.255 --> 02:41:46.845
we're in a time when our amazing New York City office

3355
02:41:46.865 --> 02:41:48.445
of Student Pathways recognizes

3356
02:41:48.595 --> 02:41:50.245
that not all students are on the same

3357
02:41:50.245 --> 02:41:51.325
post-secondary pathway.

3358
02:41:52.165 --> 02:41:54.125
Nysed recognizes the need for alternatives

3359
02:41:54.125 --> 02:41:55.165
to regents assessments,

3360
02:41:55.425 --> 02:41:58.645
but somehow our city education leaders, or our mayor,

3361
02:41:58.705 --> 02:42:00.645
or whoever it is that is in charge of this,

3362
02:42:00.915 --> 02:42:04.205
does not acknowledge that curriculum cannot be uniform.

3363
02:42:04.655 --> 02:42:08.645
Uniformity is not equity and uniformity is not excellence.

3364
02:42:09.505 --> 02:42:13.745
I am also confused as to why there seems to be a conflation

3365
02:42:14.015 --> 02:42:17.425
between teaching children to read using phonics

3366
02:42:17.525 --> 02:42:19.225
and an ELA curriculum.

3367
02:42:19.645 --> 02:42:20.705
People think that

3368
02:42:20.705 --> 02:42:22.785
because of the science of reading, we need

3369
02:42:22.785 --> 02:42:25.425
to tell teachers exactly which books to teach

3370
02:42:25.445 --> 02:42:27.305
and when, which is an ELA curriculum.

3371
02:42:27.525 --> 02:42:29.265
It is not phonics at my school,

3372
02:42:29.265 --> 02:42:30.745
which is a sixth to 12 school.

3373
02:42:31.125 --> 02:42:32.465
We graduated in June

3374
02:42:32.485 --> 02:42:36.785
of 20 24, 17, 17 12th graders

3375
02:42:37.005 --> 02:42:41.025
who started with us in sixth grade in phonics interventions

3376
02:42:41.055 --> 02:42:42.585
because we understand

3377
02:42:42.775 --> 02:42:45.985
that we can teach them a top quality teacher created

3378
02:42:45.985 --> 02:42:48.985
curriculum during their ELA period

3379
02:42:49.485 --> 02:42:51.825
and give them a phonics intervention such

3380
02:42:51.825 --> 02:42:54.145
that when they graduated from us this past June,

3381
02:42:54.145 --> 02:42:57.025
after seven years of being with us, they got accepted to

3382
02:42:57.785 --> 02:43:00.785
multiple post-secondary pathways colleges and universities.

3383
02:43:00.785 --> 02:43:04.985
Because we know how to do this well. Now our hands are tied.

3384
02:43:05.365 --> 02:43:07.905
We have this scripted curriculum that we have to teach.

3385
02:43:08.165 --> 02:43:09.785
We are not meeting the needs of our students.

3386
02:43:09.845 --> 02:43:11.605
It is not culturally responsive.

3387
02:43:11.625 --> 02:43:14.605
It does not respect our expertise as teachers.

3388
02:43:14.785 --> 02:43:16.925
It takes the power away from the teachers.

3389
02:43:16.925 --> 02:43:20.205
It takes the joy out of the teaching and the learning.

3390
02:43:20.345 --> 02:43:23.325
Our te our students are reading and writing less.

3391
02:43:23.915 --> 02:43:25.525
That does not make any sense.

3392
02:43:25.525 --> 02:43:28.365
They're not even finishing the books, the curriculum,

3393
02:43:28.385 --> 02:43:30.925
the ELA curriculum, the EL ELA curriculum

3394
02:43:30.925 --> 02:43:33.005
that we're using does not require students

3395
02:43:33.105 --> 02:43:35.205
to ever finish a book.

3396
02:43:35.375 --> 02:43:35.805
Thank you.

3397
02:43:40.905 --> 02:43:45.035
Next speaker, please. Good evening.

3398
02:43:45.145 --> 02:43:48.155
Once again, two minutes with so much to say.

3399
02:43:48.315 --> 02:43:49.995
'cause Manhattan is on fire right now.

3400
02:43:50.735 --> 02:43:54.475
Um, I do wanna echo the sentiments of the parents at Beacon

3401
02:43:54.975 --> 02:43:58.515
as a, as a current consortium parent, um,

3402
02:43:58.535 --> 02:44:00.715
and somebody that supported, uh,

3403
02:44:00.715 --> 02:44:03.075
the principal when they came in, I've seen

3404
02:44:04.175 --> 02:44:05.995
and lived those concerns.

3405
02:44:06.415 --> 02:44:09.355
Um, superintendent Alan Chang has provided the supports.

3406
02:44:09.455 --> 02:44:12.635
The consortium has also provided supports for the principal.

3407
02:44:13.175 --> 02:44:14.675
And there's a lot to be said

3408
02:44:14.675 --> 02:44:16.755
to having conversations when principals

3409
02:44:16.755 --> 02:44:17.875
are just not a good fit.

3410
02:44:18.495 --> 02:44:22.675
Um, I respect, um, principal Ventura in trying

3411
02:44:22.675 --> 02:44:25.235
to take this on, but again, I,

3412
02:44:25.495 --> 02:44:28.635
as the former borough president Appointee received a lot

3413
02:44:28.635 --> 02:44:30.115
of concerns from these parents,

3414
02:44:30.255 --> 02:44:31.675
and I really hope that we're

3415
02:44:31.915 --> 02:44:33.235
actively engaging the community.

3416
02:44:33.975 --> 02:44:35.995
Uh, the other thing that I wanna elevate was something

3417
02:44:35.995 --> 02:44:39.115
that was just mentioned, which is, uh, the fact

3418
02:44:39.115 --> 02:44:41.955
that we're currently revising chancellor's Regulation

3419
02:44:42.555 --> 02:44:47.355
D two 10, um, which I, as a former parent leader, actively

3420
02:44:48.015 --> 02:44:51.475
helped, uh, engage in the conversation of the existence

3421
02:44:51.475 --> 02:44:53.835
because of the targeting of parents

3422
02:44:54.145 --> 02:44:57.195
that were focused on equity, uh, policies.

3423
02:44:57.615 --> 02:44:59.515
Um, it's been consistent, this attack

3424
02:44:59.515 --> 02:45:01.515
that has been happening to black

3425
02:45:01.615 --> 02:45:04.555
and Latino parent leaders, the silencing of black

3426
02:45:04.555 --> 02:45:05.835
and latino parent leaders.

3427
02:45:06.095 --> 02:45:09.235
And it's being done by a group of people that have hundreds

3428
02:45:09.235 --> 02:45:11.315
and thousands of dollars donated to them.

3429
02:45:12.135 --> 02:45:15.235
And some of those people that have donated to them

3430
02:45:15.295 --> 02:45:18.675
and have supported their platform also have donated

3431
02:45:19.015 --> 02:45:22.795
to Mayor Eric Bank, Eric, Adam, sorry, um, campaign.

3432
02:45:23.215 --> 02:45:24.675
And so we beg, begged

3433
02:45:24.675 --> 02:45:28.115
to question why these particular parents have actually

3434
02:45:28.115 --> 02:45:32.475
gotten a platform in our spaces in order to push, uh,

3435
02:45:32.665 --> 02:45:35.195
push out a lot of the equity policies

3436
02:45:35.255 --> 02:45:37.395
as we have seen in this administration.

3437
02:45:38.055 --> 02:45:41.115
Um, the lack of integration in our schools.

3438
02:45:41.455 --> 02:45:43.795
And it's very unfortunate that first, uh,

3439
02:45:43.795 --> 02:45:46.035
deputy Chancellor Dan Weissberg has been one

3440
02:45:46.035 --> 02:45:47.515
that has given them this platform.

3441
02:45:47.895 --> 02:45:49.955
Uh, because it's been two minutes, I'll yield my time.

3442
02:45:50.165 --> 02:45:50.595
Thank you.

3443
02:45:54.635 --> 02:45:55.565
Next speaker, please.

3444
02:45:56.105 --> 02:45:58.665
Um, I signed up to speak again

3445
02:45:58.665 --> 02:46:00.185
during the general comments section

3446
02:46:00.185 --> 02:46:03.385
because as a public school teacher, I'm very afraid of

3447
02:46:03.385 --> 02:46:05.625
what feels like the death of public education

3448
02:46:05.625 --> 02:46:08.265
with the ongoing onslaught of privatization.

3449
02:46:09.305 --> 02:46:11.605
Uh, now this certainly feels like one of the goals

3450
02:46:11.605 --> 02:46:12.605
of mayoral control,

3451
02:46:12.665 --> 02:46:15.805
but considering that a majority of the pep uh,

3452
02:46:15.805 --> 02:46:20.325
members are mayoral appointees, uh, it feels, um, useless

3453
02:46:20.345 --> 02:46:22.765
to highlight the destructiveness of mayoral control.

3454
02:46:23.035 --> 02:46:24.365
Instead, I'm gonna ask you all

3455
02:46:24.365 --> 02:46:27.525
to really think deeply about whether what we are asking

3456
02:46:27.625 --> 02:46:30.005
and mandating NYC public school students,

3457
02:46:30.505 --> 02:46:32.605
if you would feel okay having your own

3458
02:46:32.655 --> 02:46:34.045
child be in that position.

3459
02:46:34.935 --> 02:46:38.085
Would you feel okay having your child locked in a room,

3460
02:46:38.225 --> 02:46:42.045
taking an assessment that serves zero purpose hours

3461
02:46:42.065 --> 02:46:43.165
or days on end?

3462
02:46:43.855 --> 02:46:45.245
Would you feel okay?

3463
02:46:45.305 --> 02:46:48.645
Having your child sit through canned curricula

3464
02:46:48.915 --> 02:46:50.605
that is culturally destructive?

3465
02:46:50.905 --> 02:46:53.485
And having worked as part of the literacy collaborative

3466
02:46:53.485 --> 02:46:56.365
that was disbanded, we vetted those curricula

3467
02:46:56.385 --> 02:46:57.805
and our recommendation was

3468
02:46:57.805 --> 02:47:00.485
that these are not based in any science of reading,

3469
02:47:00.905 --> 02:47:03.965
and we were told that they were gonna go through anyways.

3470
02:47:05.275 --> 02:47:08.755
So things like HMH, just to give you a little taste,

3471
02:47:08.815 --> 02:47:10.755
and it goes beyond just one curriculum

3472
02:47:10.755 --> 02:47:14.355
because there is no standard curriculum that can respond

3473
02:47:14.375 --> 02:47:17.195
and fit the needs of 1.1 million students.

3474
02:47:18.615 --> 02:47:22.025
But just so that we know, I want folks

3475
02:47:22.025 --> 02:47:24.345
to really think about the 12th grade.

3476
02:47:24.585 --> 02:47:27.345
HMH curricula only features white authors.

3477
02:47:27.795 --> 02:47:31.005
There's not a single author of color in the 12th grade.

3478
02:47:31.995 --> 02:47:36.505
Similarly in the 11th grade, you also have very few,

3479
02:47:37.005 --> 02:47:39.625
uh, authors of color when you, uh,

3480
02:47:39.625 --> 02:47:42.265
when they speak about enslaved persons in the curricula,

3481
02:47:42.425 --> 02:47:43.905
they refer to them as servants,

3482
02:47:43.935 --> 02:47:46.585
essentially whitewashing our history of slavery.

3483
02:47:47.725 --> 02:47:51.385
Um, and so I really, when I hear the consortium schools,

3484
02:47:51.525 --> 02:47:52.985
I'm like, why is it that some schools

3485
02:47:53.045 --> 02:47:55.665
and communities get exemptions from the curricula,

3486
02:47:55.925 --> 02:47:58.825
get responsive curricula and not all of our students?

3487
02:47:59.045 --> 02:48:01.785
If you would not be okay with your child having

3488
02:48:01.785 --> 02:48:04.345
that curricula, how are we forcing this on all kids?

3489
02:48:04.725 --> 02:48:07.065
And finally, please reinstate Chancellor,

3490
02:48:07.065 --> 02:48:08.865
please reinstate Taj Sutton.

3491
02:48:09.085 --> 02:48:11.825
We have reinstated Maude Marin, who has said transphobic

3492
02:48:11.925 --> 02:48:13.705
and racist things to CC two.

3493
02:48:14.085 --> 02:48:16.905
It is only right that re reinstate ta su Sutton

3494
02:48:17.285 --> 02:48:20.345
and incredible parent leader who has fought for equity,

3495
02:48:20.575 --> 02:48:22.665
anti-racism, and culturally responsive

3496
02:48:22.665 --> 02:48:24.105
curricula in Brooklyn.

3497
02:48:24.165 --> 02:48:27.225
And for all students across the city, it is only right

3498
02:48:27.225 --> 02:48:28.745
that we actually reinstate someone

3499
02:48:28.765 --> 02:48:30.185
who is democratically elected.

3500
02:48:30.275 --> 02:48:30.745
Thank you.

3501
02:48:31.865 --> 02:48:36.655
Um, me.

3502
02:48:38.195 --> 02:48:41.985
Oh, okay. Um, hi. First, I wanna welcome our new chancellor.

3503
02:48:42.485 --> 02:48:44.865
Um, in your remarks earlier tonight, uh,

3504
02:48:44.865 --> 02:48:45.985
you echoed the statements

3505
02:48:45.985 --> 02:48:47.865
that appeared in a recent Chalkbeat article.

3506
02:48:48.325 --> 02:48:49.745
In those remarks you said you wanted

3507
02:48:49.745 --> 02:48:52.025
to continue Chancellor Bank's signature initiatives,

3508
02:48:52.065 --> 02:48:53.665
NYC reads and NYC solves.

3509
02:48:53.805 --> 02:48:56.225
You also said you'd be listening to parents and educators.

3510
02:48:56.225 --> 02:48:58.945
Unfortunately, these things are inherently contradictory.

3511
02:48:59.245 --> 02:49:00.505
Ah, NYC reads.

3512
02:49:00.505 --> 02:49:02.705
And now, NYC solves work, to my knowledge,

3513
02:49:02.705 --> 02:49:03.785
rolled out without regard

3514
02:49:03.785 --> 02:49:05.505
to general parent educator feedback.

3515
02:49:05.845 --> 02:49:08.885
The imposition of specific mandated curriculum in New York

3516
02:49:08.885 --> 02:49:12.485
City public school system-wide in a system, um,

3517
02:49:12.795 --> 02:49:14.165
that it has a great number

3518
02:49:14.185 --> 02:49:17.165
and wide variety of students is Ill-advised,

3519
02:49:17.745 --> 02:49:19.635
um, curriculum.

3520
02:49:19.635 --> 02:49:21.835
These curriculum are accompanied by strict pacing guides

3521
02:49:21.835 --> 02:49:22.755
that are supposed to be followed,

3522
02:49:22.755 --> 02:49:23.915
quote unquote, with fidelity.

3523
02:49:24.225 --> 02:49:26.395
This is a new thing in this system.

3524
02:49:26.775 --> 02:49:28.915
My own children were lucky enough to attend the handful

3525
02:49:28.975 --> 02:49:30.595
of progressive public schools in the city.

3526
02:49:30.775 --> 02:49:33.675
I'm so relieved that they learned to read and calculate

3527
02:49:33.675 --> 02:49:35.955
before the adoption of these one size fits all private

3528
02:49:35.975 --> 02:49:37.195
equity owned curriculum.

3529
02:49:37.445 --> 02:49:39.595
These would've precluded the wonderful child centered

3530
02:49:39.615 --> 02:49:41.595
and culturally responsive experiences they had.

3531
02:49:41.825 --> 02:49:43.515
They would've tied the hands of their wonderful

3532
02:49:44.315 --> 02:49:45.635
creative education professionals

3533
02:49:45.635 --> 02:49:47.235
that use NYC as their classroom.

3534
02:49:47.235 --> 02:49:48.315
Something that will be harder

3535
02:49:48.335 --> 02:49:51.075
to make happen using a national curriculum designed

3536
02:49:51.075 --> 02:49:53.315
to please the denizens of Texas and Florida.

3537
02:49:53.775 --> 02:49:56.195
Before finishing, I wanna say that the complaints of parents

3538
02:49:56.195 --> 02:49:57.275
of children with dyslexia

3539
02:49:57.275 --> 02:50:00.155
and other language-based learning issues, um, uh, um,

3540
02:50:00.975 --> 02:50:03.475
are legitimate about teaching reading legitimate.

3541
02:50:03.695 --> 02:50:06.315
But the response of mandated curriculum

3542
02:50:06.415 --> 02:50:10.355
by NYC reads is not the way, it is not the way it's

3543
02:50:10.375 --> 02:50:11.675
for every student in the system.

3544
02:50:11.745 --> 02:50:14.195
It's questionable. What's even helpful for dyslexic students

3545
02:50:14.375 --> 02:50:16.635
as these particular curriculum are not phonics-based.

3546
02:50:16.745 --> 02:50:18.835
When we look at private schools, which specialize in working

3547
02:50:18.835 --> 02:50:21.115
with children on reading, they work one-on-one

3548
02:50:21.135 --> 02:50:22.235
or in very small groups.

3549
02:50:22.535 --> 02:50:23.675
So maybe this DOE,

3550
02:50:23.675 --> 02:50:26.715
we should be more focused on reducing class size rather than

3551
02:50:26.715 --> 02:50:28.635
enriching private equity corporations.

3552
02:50:29.015 --> 02:50:33.275
Yes, thank you. Martina Meyer.

3553
02:50:35.255 --> 02:50:38.085
Again, I'm speaking, um, my personal behalf, not

3554
02:50:38.145 --> 02:50:41.325
as an employee, but as a concern to citizen and taxpayers.

3555
02:50:41.745 --> 02:50:43.605
Dr. Pete did ask the teachers

3556
02:50:43.605 --> 02:50:46.165
to identify the challenges exactly that we face.

3557
02:50:46.265 --> 02:50:50.085
So I'm telling you the i-Ready assessment that we are forced

3558
02:50:50.185 --> 02:50:51.925
to implement does not tell us

3559
02:50:51.925 --> 02:50:54.205
what standards were assessed for our students.

3560
02:50:54.705 --> 02:50:56.045
We don't see any information

3561
02:50:56.045 --> 02:50:57.965
beyond the i-Ready abbreviated report.

3562
02:50:58.265 --> 02:50:59.605
We never see what series

3563
02:50:59.605 --> 02:51:02.165
of questions the students were asked, the nature

3564
02:51:02.265 --> 02:51:03.285
of their errors

3565
02:51:03.585 --> 02:51:06.005
or what questions specifically, um,

3566
02:51:06.035 --> 02:51:07.365
they were they were going through.

3567
02:51:07.795 --> 02:51:10.285
It's concerning that we are being told something different

3568
02:51:10.315 --> 02:51:12.325
from what we are actually experiencing.

3569
02:51:12.785 --> 02:51:16.245
Please listen. We are telling you that all across the city,

3570
02:51:16.585 --> 02:51:19.485
all teachers using i-Ready do not have any way

3571
02:51:19.725 --> 02:51:21.005
of doing error analysis.

3572
02:51:21.585 --> 02:51:23.205
We don't see what standards were assessed.

3573
02:51:23.425 --> 02:51:24.805
We don't see what questions were asked.

3574
02:51:24.905 --> 02:51:27.205
We watch our students click through and guess

3575
02:51:27.315 --> 02:51:29.085
because they quickly figure out

3576
02:51:29.235 --> 02:51:30.885
that the questions keep getting harder.

3577
02:51:31.265 --> 02:51:33.445
And so they want to get it done as fast as possible.

3578
02:51:33.835 --> 02:51:34.925
It's the design of the program

3579
02:51:34.925 --> 02:51:37.725
that this body has put millions of dollars into.

3580
02:51:37.945 --> 02:51:40.405
And the fact that DOE officers don't seem to know

3581
02:51:40.405 --> 02:51:43.205
how this works or are acting like this is an individual

3582
02:51:43.205 --> 02:51:46.085
problem or a school level problem is alarming.

3583
02:51:46.265 --> 02:51:47.965
But unfortunately not surprising.

3584
02:51:48.395 --> 02:51:51.165
This is a central de design feature of i-Ready.

3585
02:51:51.265 --> 02:51:53.005
And it means that the assessment is not at all

3586
02:51:53.005 --> 02:51:54.045
helpful to teachers.

3587
02:51:54.545 --> 02:51:57.365
Beyond that, we need you to hear us that there are too many

3588
02:51:57.385 --> 02:51:59.125
of these assessments, regardless of whether

3589
02:51:59.125 --> 02:52:00.605
or not we have access to the data.

3590
02:52:01.225 --> 02:52:03.045
And we need every moment that we have

3591
02:52:03.065 --> 02:52:05.125
to take our work seriously in our instructional time.

3592
02:52:05.505 --> 02:52:06.805
It feels like the central offices

3593
02:52:07.055 --> 02:52:08.405
don't take our work seriously.

3594
02:52:08.675 --> 02:52:10.725
What we do see in central offices is a lot

3595
02:52:10.725 --> 02:52:11.725
of bloated salaries.

3596
02:52:11.905 --> 02:52:14.805
And I would be remiss to omit that this is outrageous,

3597
02:52:14.805 --> 02:52:17.005
that the mayor's partner has had a no-show job

3598
02:52:17.275 --> 02:52:18.845
with a big old six figure salary.

3599
02:52:19.185 --> 02:52:20.965
The corruption is eroding our trust.

3600
02:52:21.265 --> 02:52:23.965
And I'm calling for the mayoral appointees on the pep

3601
02:52:24.225 --> 02:52:27.205
to step down in light of the scandal surrounding the mayor,

3602
02:52:27.815 --> 02:52:30.205
every contract should be called into question

3603
02:52:30.465 --> 02:52:32.845
and there should be an audit from the comptroller's office.

3604
02:52:34.105 --> 02:52:35.545
I have so much more to say thank you in

3605
02:52:35.545 --> 02:52:36.625
five seconds is not enough.

3606
02:52:41.545 --> 02:52:44.445
Uh, Johanna Bjork and Lupe Hernandez.

3607
02:52:49.585 --> 02:52:52.215
Hello there, pep. Um, my name is Johanna Bjork.

3608
02:52:52.395 --> 02:52:56.255
I'm here as the parent as again, as you heard before,

3609
02:52:56.475 --> 02:53:00.175
but I also was a member of the class size working group.

3610
02:53:00.315 --> 02:53:03.655
And I am very happy to see so many people who I worked

3611
02:53:03.755 --> 02:53:05.895
so hard for with on that work.

3612
02:53:06.635 --> 02:53:10.735
Um, I'm speaking tonight only as in my capacity as a parent.

3613
02:53:11.525 --> 02:53:13.825
Um, one of the things that's been buzzing

3614
02:53:13.825 --> 02:53:16.385
that we heard about here that's been in the press is the

3615
02:53:16.585 --> 02:53:18.665
upcoming mergers and consolidations

3616
02:53:18.965 --> 02:53:20.705
and closures that are coming.

3617
02:53:20.885 --> 02:53:23.065
And I think that it, you know, many of us have been seeing

3618
02:53:23.065 --> 02:53:26.785
that coming down, but those of us who are data inclined, uh,

3619
02:53:26.785 --> 02:53:28.665
have been seeing that coming for a while.

3620
02:53:28.835 --> 02:53:31.105
We've been hearing about schools that are too small,

3621
02:53:31.175 --> 02:53:33.105
unsustainable unviable,

3622
02:53:33.605 --> 02:53:36.105
and yet we don't hear any strategy around it.

3623
02:53:36.605 --> 02:53:39.625
Um, I went to the Office of District planning meetings

3624
02:53:39.625 --> 02:53:40.625
because I'm like that.

3625
02:53:41.245 --> 02:53:45.385
And, uh, um, was really surprised to hear

3626
02:53:45.385 --> 02:53:47.625
that there is a merger considered

3627
02:53:47.625 --> 02:53:49.705
for being in considered for my building.

3628
02:53:50.095 --> 02:53:52.905
When I brought that to my principal, it was new news to her.

3629
02:53:53.405 --> 02:53:55.185
I'm on the SLT, I brought the SLT

3630
02:53:55.185 --> 02:53:56.505
and it was news to the SLT.

3631
02:53:57.125 --> 02:54:00.665
And I really hope that as this becomes something

3632
02:54:00.935 --> 02:54:02.545
that we look at, that it's, it's something

3633
02:54:02.545 --> 02:54:04.425
that is done very thoughtfully.

3634
02:54:04.695 --> 02:54:07.105
I've sat in so many pep meetings where it's been so,

3635
02:54:07.105 --> 02:54:10.385
there's been so much trauma happening to kids,

3636
02:54:10.525 --> 02:54:11.865
our most vulnerable kids,

3637
02:54:11.975 --> 02:54:14.545
because it's our kids who are the most vulnerable,

3638
02:54:14.545 --> 02:54:15.825
who are in those small schools.

3639
02:54:16.525 --> 02:54:18.145
And as we look at those mergers

3640
02:54:18.145 --> 02:54:19.665
and consolidations, I really hope

3641
02:54:19.665 --> 02:54:21.945
that you center the new class size law in

3642
02:54:21.945 --> 02:54:25.585
that I was shocked, I was appalled that the Office

3643
02:54:25.585 --> 02:54:28.065
of District Planning did not have, was not taking

3644
02:54:28.065 --> 02:54:29.825
that into consideration whatsoever.

3645
02:54:30.285 --> 02:54:31.385
In their presentations

3646
02:54:31.485 --> 02:54:33.705
or their planning, they deferred those questions.

3647
02:54:33.705 --> 02:54:34.825
They were like, oh, well that's something

3648
02:54:34.825 --> 02:54:36.185
that somebody else is dealing with.

3649
02:54:36.605 --> 02:54:40.105
How is that possible? How is that possible?

3650
02:54:40.565 --> 02:54:43.385
We have to reach 60% compliance next year.

3651
02:54:43.525 --> 02:54:46.705
We need a strategy, not just every superintendent needs

3652
02:54:46.705 --> 02:54:49.305
to increase by 3%, which by the way,

3653
02:54:49.325 --> 02:54:51.705
are we gonna get any accountability reports on that?

3654
02:54:51.995 --> 02:54:55.025
There were, um, uh, how that's going.

3655
02:54:55.385 --> 02:54:58.225
I can't find out from my superintendent, partly

3656
02:54:58.225 --> 02:55:00.465
because my superintendent is super citywide.

3657
02:55:00.525 --> 02:55:04.925
So there's no vehicle for hearing from him other than a body

3658
02:55:04.935 --> 02:55:07.645
where I personally was attacked

3659
02:55:07.705 --> 02:55:09.845
and insulted for being a concerned parent.

3660
02:55:10.145 --> 02:55:12.045
And I'm speaking of the CCHS,

3661
02:55:12.505 --> 02:55:15.965
and I sent you all an email about this, um, where

3662
02:55:15.965 --> 02:55:18.685
after I had expressed my concern about

3663
02:55:19.305 --> 02:55:21.725
the agenda about not dealing with these issues,

3664
02:55:21.825 --> 02:55:23.565
the president personally attacked me

3665
02:55:23.565 --> 02:55:25.565
and invoked the D two 10 process,

3666
02:55:25.995 --> 02:55:28.125
clearly emboldened by its suspension.

3667
02:55:28.905 --> 02:55:33.005
Um, so much more. Um, thank you. Thank you.

3668
02:55:39.795 --> 02:55:42.725
Good evening. Um, my name is Lupe Hernandez

3669
02:55:42.725 --> 02:55:44.645
and I'm speaking in my own personal capacity.

3670
02:55:45.765 --> 02:55:47.805
I wanna welcome Chancellor Avila.

3671
02:55:47.805 --> 02:55:51.685
Thank you for, um, listening to parents and listening to us

3672
02:55:51.825 --> 02:55:54.445
and our suggestion and bringing yourself back on the panel.

3673
02:55:54.705 --> 02:55:56.205
Um, and actually listening

3674
02:55:56.345 --> 02:55:58.645
and engaging with parents throughout this evening.

3675
02:55:58.675 --> 02:56:01.445
It's actually been very refreshing.

3676
02:56:04.035 --> 02:56:06.215
It gives us purpose to why we come here,

3677
02:56:06.355 --> 02:56:09.735
why we do this work when we feel heard, when we feel seen.

3678
02:56:10.635 --> 02:56:13.615
Um, I, I had originally had planned

3679
02:56:13.615 --> 02:56:14.775
to speak on the student data

3680
02:56:14.955 --> 02:56:17.935
and I'm very grateful to see that that was pulled along

3681
02:56:17.935 --> 02:56:19.455
with some of the other agenda items.

3682
02:56:19.555 --> 02:56:23.015
But I will say that this, um, is very

3683
02:56:23.015 --> 02:56:27.135
concerning in regards to weakening our already state

3684
02:56:27.135 --> 02:56:30.535
and federal laws that are barely being, um, upholded.

3685
02:56:30.795 --> 02:56:33.895
Um, and I say that because we have seen many breaches,

3686
02:56:34.675 --> 02:56:38.695
and I will tie that even to the box curriculum

3687
02:56:38.695 --> 02:56:41.255
that we heard a lot about because I do agree I'm very lucky

3688
02:56:41.275 --> 02:56:43.095
to be a consortium school parent.

3689
02:56:43.675 --> 02:56:46.455
And I'm looking forward to the recommendations, um,

3690
02:56:46.645 --> 02:56:48.655
that will come out of that Blue Ribbon Commission

3691
02:56:48.755 --> 02:56:51.455
and being able to provide other pathways for our students

3692
02:56:52.075 --> 02:56:54.455
to, um, excel beyond high school

3693
02:56:54.475 --> 02:56:56.375
and especially for our students with disabilities.

3694
02:56:56.675 --> 02:57:00.815
But the box curriculum that my younger ones in pre-K

3695
02:57:01.495 --> 02:57:03.095
creative curriculum, some

3696
02:57:03.095 --> 02:57:06.015
of the biggest concerns I heard from teachers was the data

3697
02:57:06.045 --> 02:57:09.415
that is being, um, having to put, be put in.

3698
02:57:09.915 --> 02:57:13.215
Um, I was shocked when I saw the amount of paperwork

3699
02:57:13.215 --> 02:57:14.295
that the teachers have to do

3700
02:57:14.295 --> 02:57:16.975
and it's taking away time from real learning

3701
02:57:17.315 --> 02:57:18.455
inside the classroom.

3702
02:57:19.395 --> 02:57:23.575
And I think that we need to really invest the money

3703
02:57:23.575 --> 02:57:26.415
because none of our kids are learning at the same level.

3704
02:57:26.515 --> 02:57:28.055
We need to differentiate. We need

3705
02:57:28.055 --> 02:57:29.175
to meet them where they're at.

3706
02:57:29.555 --> 02:57:32.415
And these box curriculums do not allow for that to happen.

3707
02:57:32.675 --> 02:57:35.095
But we've been saying that month after month

3708
02:57:35.095 --> 02:57:37.975
after month, I will say my last thing is we need

3709
02:57:37.975 --> 02:57:40.375
to reinstate Taj Sutton, D two 10.

3710
02:57:41.075 --> 02:57:42.895
Uh, you need to reevaluate

3711
02:57:42.995 --> 02:57:46.255
and also reconsider, we still have Chancellor 8 8 30

3712
02:57:46.285 --> 02:57:49.175
that also, uh, you know, um,

3713
02:57:50.125 --> 02:57:51.935
addresses dis anti-discrimination

3714
02:57:51.935 --> 02:57:53.895
that folks are experiencing here.

3715
02:57:54.385 --> 02:57:55.175
Thank you. Thank you.

3716
02:58:00.565 --> 02:58:03.515
I believe that now I have gotten through all of the speakers

3717
02:58:03.515 --> 02:58:04.795
and the general public comment.

3718
02:58:05.765 --> 02:58:07.275
Great to you, Chair fa

3719
02:58:07.685 --> 02:58:08.875
Thank, thank you very much.

3720
02:58:09.055 --> 02:58:12.395
Yes. Panel member chair. Thank, thank you.

3721
02:58:12.655 --> 02:58:14.675
Um, do you mind if I just make a quick comment?

3722
02:58:14.775 --> 02:58:16.475
My son done fell asleep underneath the clock

3723
02:58:16.695 --> 02:58:20.195
and he gotta be up at 5:00 AM to get on the five,

3724
02:58:20.305 --> 02:58:21.515
like 30 ferry.

3725
02:58:21.655 --> 02:58:23.475
So do you mind if I just make a quick comment

3726
02:58:23.815 --> 02:58:25.635
and, you know, get 'em home?

3727
02:58:26.725 --> 02:58:28.085
Absolutely. Go ahead. Thank you.

3728
02:58:29.165 --> 02:58:31.025
Um, I wouldn't make it outta here if I didn't.

3729
02:58:31.025 --> 02:58:32.505
Uh, yeah, go ahead.

3730
02:58:32.965 --> 02:58:37.835
Um, I just wanna say, first of all, chancellor,

3731
02:58:37.835 --> 02:58:40.555
thank you for joining us on the stage.

3732
02:58:40.655 --> 02:58:45.035
It is very important as the community has stated, um,

3733
02:58:45.935 --> 02:58:48.555
for you to be present with us so

3734
02:58:48.555 --> 02:58:51.395
that we all feel like we are in this together.

3735
02:58:51.575 --> 02:58:53.075
So thank you and welcome.

3736
02:58:53.935 --> 02:58:58.715
Um, I also want to say to my, uh, colleague from Bronx,

3737
02:58:59.215 --> 02:59:00.395
uh, happy birthday.

3738
02:59:02.565 --> 02:59:03.875
Happy birthday Rema.

3739
02:59:07.655 --> 02:59:10.675
And I'm gonna make my, my comments brief tonight.

3740
02:59:10.915 --> 02:59:12.235
'cause again, I gotta get my son home.

3741
02:59:12.775 --> 02:59:16.235
And, um, so I want everybody

3742
02:59:16.785 --> 02:59:20.275
sitting here at this table to really understand

3743
02:59:20.905 --> 02:59:23.995
that the decisions we make impact real people

3744
02:59:24.495 --> 02:59:27.115
and the decisions that we make here have

3745
02:59:27.145 --> 02:59:28.435
real life consequences.

3746
02:59:29.855 --> 02:59:32.875
And we hear those consequences every month

3747
02:59:33.385 --> 02:59:37.475
when really the experts in our communities,

3748
02:59:37.855 --> 02:59:39.515
the experts with our children

3749
02:59:40.215 --> 02:59:42.395
are sitting in this room, right?

3750
02:59:43.075 --> 02:59:44.955
Teachers might be experts in pedagogy,

3751
02:59:44.975 --> 02:59:46.675
but parents are experts in their children

3752
02:59:47.645 --> 02:59:50.785
and they bring their concerns into these spaces every month.

3753
02:59:51.165 --> 02:59:53.385
And they tell us what works

3754
02:59:53.605 --> 02:59:55.385
and they share with us what doesn't.

3755
02:59:56.285 --> 02:59:59.625
And I think that we have an obligation to

3756
03:00:00.165 --> 03:00:01.265
not just hear them,

3757
03:00:01.805 --> 03:00:05.225
but we have an obligation to work with them as partners

3758
03:00:05.725 --> 03:00:09.425
to make sure that this system does right by them, does right

3759
03:00:09.445 --> 03:00:10.465
by their families,

3760
03:00:10.645 --> 03:00:12.385
and does right by the communities

3761
03:00:12.385 --> 03:00:14.025
that they all exist as part of.

3762
03:00:15.595 --> 03:00:20.275
And one of the ways that we do that outside

3763
03:00:20.535 --> 03:00:23.915
of this school board is by voting.

3764
03:00:25.415 --> 03:00:27.835
And I say that because,

3765
03:00:28.255 --> 03:00:32.825
and this is kind of like the off, like off topic part,

3766
03:00:33.045 --> 03:00:35.365
but it's connected in this way.

3767
03:00:36.505 --> 03:00:40.365
The change we want to see as a community exists

3768
03:00:41.305 --> 03:00:43.725
in our votes, right?

3769
03:00:44.185 --> 03:00:47.165
So today is still, it's still early voting.

3770
03:00:47.585 --> 03:00:49.285
Go vote, right?

3771
03:00:49.705 --> 03:00:52.925
You don't like mayoral control, go vote, right?

3772
03:00:53.345 --> 03:00:56.685
You got state elected officials up for election

3773
03:00:57.305 --> 03:01:00.405
and if they are supporting something that you have a problem

3774
03:01:00.435 --> 03:01:01.645
with, go vote.

3775
03:01:02.525 --> 03:01:06.285
Right? And, you know, election day is

3776
03:01:06.875 --> 03:01:09.045
next Tuesday, right?

3777
03:01:09.585 --> 03:01:11.405
We even got the, like our kids got the

3778
03:01:11.405 --> 03:01:12.605
day off from school, right?

3779
03:01:12.635 --> 03:01:15.645
Like, take them with you to the polls, let them see

3780
03:01:15.645 --> 03:01:16.805
how this process works.

3781
03:01:17.225 --> 03:01:19.525
That's why my son is sitting in the back

3782
03:01:19.525 --> 03:01:21.445
where I started bringing him with me every month.

3783
03:01:21.905 --> 03:01:24.045
He tired and he can't hang. And that's all right.

3784
03:01:24.705 --> 03:01:28.005
But he's no, he's no, keep in mind, he's a,

3785
03:01:28.115 --> 03:01:29.125
he's, he's young.

3786
03:01:29.505 --> 03:01:33.965
He wakes up at 5:00 AM every day to be on a ferry at five 30

3787
03:01:34.065 --> 03:01:35.685
to be to school by eight o'clock.

3788
03:01:36.145 --> 03:01:37.885
And then he does it all over again

3789
03:01:37.885 --> 03:01:40.545
to come home every evening, right?

3790
03:01:41.165 --> 03:01:43.605
And, you know, one of the things

3791
03:01:43.605 --> 03:01:45.645
that was mentioned tonight is

3792
03:01:46.065 --> 03:01:49.165
as we consider the decisions we make, you know,

3793
03:01:49.545 --> 03:01:52.365
are you comfortable with your own child's dealing

3794
03:01:52.365 --> 03:01:54.165
with the issues that we're dealing with?

3795
03:01:54.705 --> 03:01:58.755
And I could tell you for a fact that I'm not, and I'm not

3796
03:01:58.755 --> 03:02:00.995
because my votes have reflected the fact

3797
03:02:00.995 --> 03:02:03.515
that I am not comfortable with a lot of the decisions

3798
03:02:03.775 --> 03:02:06.435
and a lot of the policies that come off

3799
03:02:06.435 --> 03:02:08.635
of this board, right?

3800
03:02:08.815 --> 03:02:13.395
So if we are serious about changing this system in a way

3801
03:02:13.395 --> 03:02:14.675
that works for parents

3802
03:02:15.135 --> 03:02:17.275
and works for our students especially,

3803
03:02:17.655 --> 03:02:19.315
and works for our educators

3804
03:02:19.535 --> 03:02:21.835
and works for our administrators,

3805
03:02:21.855 --> 03:02:24.675
and works for our staff, then we have to,

3806
03:02:25.575 --> 03:02:28.795
and like we have to not just engage with them,

3807
03:02:28.815 --> 03:02:31.235
but we have to start with the premise

3808
03:02:31.545 --> 03:02:35.635
that we are all partners and our children are the center.

3809
03:02:36.665 --> 03:02:40.005
And we have, like, the whole point in this is to make sure

3810
03:02:40.035 --> 03:02:44.925
that we as a community give them the best educational

3811
03:02:45.015 --> 03:02:48.165
experience that we can possibly give them, right?

3812
03:02:48.165 --> 03:02:51.365
Whether that means reevaluate, co reevaluating contracts,

3813
03:02:52.005 --> 03:02:54.605
reevaluating policies, reevaluating

3814
03:02:54.705 --> 03:02:56.565
how we interact and deal with each other.

3815
03:02:57.225 --> 03:02:58.885
The point is, is that we have

3816
03:02:58.885 --> 03:03:01.645
to really take a long hard look at how we do things

3817
03:03:01.985 --> 03:03:04.525
and we have to make the types of changes necessary

3818
03:03:04.905 --> 03:03:06.565
to make sure that at the end of the day,

3819
03:03:06.905 --> 03:03:08.485
our children get what they need.

3820
03:03:08.945 --> 03:03:10.845
So with that, I just wanna say thank y'all

3821
03:03:10.845 --> 03:03:13.645
for your understanding and I'm gonna get my son home. Okay?

3822
03:03:13.695 --> 03:03:15.645
Thank you. And I yield back thank you Perry.

3823
03:03:15.845 --> 03:03:16.925
Although you went way beyond the two

3824
03:03:16.925 --> 03:03:19.685
and a half minutes that we normally, uh, uh, do that.

3825
03:03:19.825 --> 03:03:22.245
But, um, so for the next three meetings,

3826
03:03:22.905 --> 03:03:24.325
you owe me some, uh, time there.

3827
03:03:24.425 --> 03:03:26.645
So, uh, but I appreciate your comments

3828
03:03:27.185 --> 03:03:28.805
and you did allude to a birthday

3829
03:03:29.045 --> 03:03:30.725
and I also extend happy birthday,

3830
03:03:30.825 --> 03:03:33.485
but this must be a great month for panel members.

3831
03:03:33.685 --> 03:03:34.925
'cause we have three panel birthdays.

3832
03:03:35.305 --> 03:03:36.925
Um, and I wanna recognize him as well.

3833
03:03:37.255 --> 03:03:40.085
Panel member, uh, nave Hasan, happy birthday.

3834
03:03:40.675 --> 03:03:41.805
It's his birthday as well.

3835
03:03:42.545 --> 03:03:45.245
Um, Marjorie, Seb, happy birthday.

3836
03:03:45.435 --> 03:03:46.605
It's her birthday as well.

3837
03:03:47.785 --> 03:03:49.245
And I bet you didn't think we knew,

3838
03:03:49.275 --> 03:03:51.645
knew this Dr. Green, our vice chair.

3839
03:03:52.505 --> 03:03:56.125
It is our birthday as well. So happy birthday to all.

3840
03:03:56.665 --> 03:03:59.325
We for panel members, if you come back into the next room,

3841
03:03:59.325 --> 03:04:01.125
we do have some, uh, uh,

3842
03:04:01.245 --> 03:04:03.205
I was gonna say light refreshment, that implies something else.

3843
03:04:04.275 --> 03:04:08.005
Yeah, we will, uh, have a little cake in, uh, if you,

3844
03:04:08.025 --> 03:04:09.165
if you have the availability.

3845
03:04:09.185 --> 03:04:10.605
But yeah, happy birthday to all.

3846
03:04:11.105 --> 03:04:15.645
Um, at this point we're gonna now turn into, uh,

3847
03:04:15.695 --> 03:04:19.165
panel member comments, um, uh, as we close the meeting.

3848
03:04:19.265 --> 03:04:21.415
So panel members, what I didn't do

3849
03:04:21.415 --> 03:04:22.535
before, lemme remind you now,

3850
03:04:22.535 --> 03:04:24.735
those pa those comments should be limited

3851
03:04:24.835 --> 03:04:26.095
to two and a half minutes.

3852
03:04:26.715 --> 03:04:29.135
So, um, who wants to begin? Yes, panel member, Lee.

3853
03:04:30.155 --> 03:04:32.465
Thank you. Can I ask the audience please to, uh,

3854
03:04:32.465 --> 03:04:35.085
before we start, Iris, opposed to leaving?

3855
03:04:35.185 --> 03:04:38.405
Can, can you, um, come to attention come to order?

3856
03:04:39.765 --> 03:04:43.195
Thank you. I'll be brief. Um, I have two things to say.

3857
03:04:43.215 --> 03:04:46.315
One is a request, um, could I formally request

3858
03:04:46.315 --> 03:04:50.715
that whomever controls these things at DIIT set the panel at

3859
03:04:51.495 --> 03:04:54.475
NYC schools dot, you know, our panel email

3860
03:04:54.775 --> 03:04:58.195
to automatically forward all emails that were received in

3861
03:04:58.195 --> 03:04:59.515
that inbox to each one

3862
03:04:59.515 --> 03:05:01.875
of our individual DOE issued inbox emails

3863
03:05:02.025 --> 03:05:03.515
because we do not receive them.

3864
03:05:03.835 --> 03:05:06.395
I don't know who sees them or where they land,

3865
03:05:06.495 --> 03:05:08.995
but they do not get distributed to us individually.

3866
03:05:09.495 --> 03:05:13.595
Um, so I would like to formally request that DIIT do that

3867
03:05:13.615 --> 03:05:15.875
for us please, and thank you. Um,

3868
03:05:16.335 --> 03:05:19.115
By the way, I, let me interrupt you must have been,

3869
03:05:19.135 --> 03:05:20.235
uh, that's gonna happen.

3870
03:05:20.285 --> 03:05:21.475
We've already made that request

3871
03:05:21.535 --> 03:05:24.315
and, um, email will go directly to panel members.

3872
03:05:24.625 --> 03:05:26.155
Good, because, and also, yeah, yeah.

3873
03:05:26.415 --> 03:05:28.795
So we, we heard you on that. That's, that's gonna happen.

3874
03:05:29.475 --> 03:05:31.875
Terrific. Um, the second thing, you know, uh,

3875
03:05:32.145 --> 03:05:34.195
that I wanted to bring up this evening, um,

3876
03:05:35.285 --> 03:05:38.905
and it's unfortunate, you know, I I I'm distressed

3877
03:05:38.905 --> 03:05:41.265
by the unfortunate stories I'm hearing out of Beacon.

3878
03:05:42.365 --> 03:05:45.045
I am a parent of an eighth grader who is a student

3879
03:05:45.045 --> 03:05:46.805
with a disability, multiple disabilities,

3880
03:05:46.805 --> 03:05:48.165
and I'm applying to high school right now,

3881
03:05:48.385 --> 03:05:50.485
and I've been on a million open houses,

3882
03:05:50.915 --> 03:05:52.645
virtual and in person.

3883
03:05:52.905 --> 03:05:55.565
And I feel the need to elevate, um,

3884
03:05:57.265 --> 03:06:00.525
the reality that we need to do a real check-in

3885
03:06:00.525 --> 03:06:03.605
with our high school administrators on services

3886
03:06:04.265 --> 03:06:06.245
for students, for special education students

3887
03:06:06.395 --> 03:06:10.285
because I am hearing some absolutely insane

3888
03:06:10.385 --> 03:06:13.365
and not legal things happening, um, in our schools.

3889
03:06:13.735 --> 03:06:18.525
Everything from we phase out IEP services year over year,

3890
03:06:19.655 --> 03:06:23.865
um, to, we don't offer ICT,

3891
03:06:24.965 --> 03:06:28.545
um, and really bizarre gatekeeping, um,

3892
03:06:28.875 --> 03:06:31.705
which principals are not allowed to tell us that.

3893
03:06:31.705 --> 03:06:35.705
And it perpetuates, it perpetuates this type

3894
03:06:35.765 --> 03:06:40.255
of segregation and this type of, um, discrimination again,

3895
03:06:40.255 --> 03:06:41.855
against our students with disabilities

3896
03:06:42.195 --> 03:06:46.975
and essentially funnels them into lesser sought, um,

3897
03:06:47.075 --> 03:06:48.655
lesser resourced high schools.

3898
03:06:49.315 --> 03:06:51.575
Um, and it's really unfortunate,

3899
03:06:52.355 --> 03:06:55.405
and, you know, my criteria has really shifted honestly,

3900
03:06:55.505 --> 03:06:58.725
as a parent who's going through this, this second time to,

3901
03:06:59.835 --> 03:07:02.555
I wanna go, I wanna send my kid to anywhere that rep

3902
03:07:02.645 --> 03:07:05.875
where principals talk about robustly, enthusiastically,

3903
03:07:05.875 --> 03:07:08.795
and proudly implementing special education services rather

3904
03:07:08.795 --> 03:07:09.915
than doing it with reluctance.

3905
03:07:10.255 --> 03:07:13.235
But I, that needs to be the case at every high school.

3906
03:07:13.895 --> 03:07:16.075
Um, and principals need to be reminded

3907
03:07:16.075 --> 03:07:17.515
of their legal responsibility

3908
03:07:17.515 --> 03:07:20.155
because there is really a lot of discriminatory

3909
03:07:20.735 --> 03:07:25.505
and, um, biased policies

3910
03:07:25.685 --> 03:07:28.785
and informal practices in place across our city. Thank you.

3911
03:07:29.155 --> 03:07:31.065
Thank you, Adam. I, uh,

3912
03:07:31.405 --> 03:07:32.705
why don't we just go down the line.

3913
03:07:32.845 --> 03:07:33.845
Uh, so next,

3914
03:07:35.565 --> 03:07:36.565
Thank you. Um,

3915
03:07:36.565 --> 03:07:39.355
so everything we heard about Beacon, further

3916
03:07:40.815 --> 03:07:44.235
it is evidence of broken SLT and DLT systems

3917
03:07:44.425 --> 03:07:47.035
because if there was a functioning school leadership in

3918
03:07:47.035 --> 03:07:49.355
that team, this situation wouldn't be happening.

3919
03:07:49.615 --> 03:07:51.635
And it's, and if they had that equitable voice

3920
03:07:51.635 --> 03:07:52.915
where they're talking about data

3921
03:07:52.935 --> 03:07:55.315
and they're talking about their school and what works

3922
03:07:55.335 --> 03:07:57.755
and what doesn't work with the teachers included

3923
03:07:57.935 --> 03:08:00.715
and the parents and all of the mandatory members,

3924
03:08:01.135 --> 03:08:03.075
it doesn't sound like that's happening in that school.

3925
03:08:03.535 --> 03:08:06.435
I'd actually love a briefing about SLTs, DLTs

3926
03:08:06.435 --> 03:08:09.355
and Title One pacs because these are all mandated,

3927
03:08:09.355 --> 03:08:12.115
whether federally, because we received titled funding

3928
03:08:12.575 --> 03:08:17.395
or through state law 25 90 or through city codes, et cetera.

3929
03:08:17.735 --> 03:08:20.075
And these are broken systems that,

3930
03:08:20.865 --> 03:08:23.515
that then you get retaliated against when you force the

3931
03:08:23.515 --> 03:08:25.035
systems to make them functional.

3932
03:08:25.215 --> 03:08:27.355
So this is a bigger conversation that I don't,

3933
03:08:27.475 --> 03:08:28.995
I can't do it in two and a half minutes.

3934
03:08:29.585 --> 03:08:31.165
Um, and, and I hope that you know

3935
03:08:31.165 --> 03:08:33.165
that I appreciate Superintendent Chang

3936
03:08:33.165 --> 03:08:36.765
and I hope that he is celebrated for providing this data

3937
03:08:36.765 --> 03:08:39.045
that they are required by law to provide

3938
03:08:39.505 --> 03:08:42.565
and not having a conversation that's more in the negative.

3939
03:08:42.645 --> 03:08:43.925
I just wanna say that now.

3940
03:08:44.235 --> 03:08:47.205
SLTs and dots with regards to the curriculum

3941
03:08:47.205 --> 03:08:48.405
and what the teachers are saying

3942
03:08:48.785 --> 03:08:50.325
and what the parents are saying, right?

3943
03:08:51.505 --> 03:08:53.075
Some of the SLT conversations

3944
03:08:53.075 --> 03:08:54.475
and DLT are being absorbed

3945
03:08:54.495 --> 03:08:56.275
by the instructional leadership team

3946
03:08:56.535 --> 03:09:00.275
and only being had with the UFT members and the CSA members

3947
03:09:00.335 --> 03:09:01.435
or the superintendent

3948
03:09:01.535 --> 03:09:03.995
and the teachers in their consultation.

3949
03:09:04.295 --> 03:09:05.675
And the parents are completely

3950
03:09:06.035 --> 03:09:07.275
excluded from those conversations.

3951
03:09:07.775 --> 03:09:10.395
So then having a conversation about data may not even make

3952
03:09:10.395 --> 03:09:12.795
sense when you don't understand the data.

3953
03:09:12.855 --> 03:09:14.355
You weren't part of the conversation

3954
03:09:14.495 --> 03:09:16.635
and now we're backtracking to explain things.

3955
03:09:17.015 --> 03:09:18.915
So I just wanna contextualize that

3956
03:09:19.495 --> 03:09:21.875
the IDEA complaints are outrageous.

3957
03:09:22.455 --> 03:09:26.155
Um, ocip, uh, office of Special Education Programs,

3958
03:09:26.285 --> 03:09:27.755
which is the U-S-D-O-E,

3959
03:09:27.755 --> 03:09:30.195
just released a report which talks about

3960
03:09:30.195 --> 03:09:33.035
how poorly New York City has done in the last 12 years

3961
03:09:33.345 --> 03:09:35.195
with regards to special education.

3962
03:09:35.775 --> 03:09:38.395
Um, beacon parents file a state complaint

3963
03:09:38.745 --> 03:09:40.595
because your, your students,

3964
03:09:40.695 --> 03:09:42.515
by the time it gets rectified here, are going

3965
03:09:42.515 --> 03:09:43.555
to have graduated.

3966
03:09:43.735 --> 03:09:45.155
Please file a state complaint.

3967
03:09:45.505 --> 03:09:48.955
Also, the UFT complaints have been helpful for some of us,

3968
03:09:49.055 --> 03:09:51.675
and through that UFT actually mandated

3969
03:09:51.675 --> 03:09:54.845
that each school create a special education committee,

3970
03:09:55.395 --> 03:09:57.445
that they have to have these discussions.

3971
03:09:57.585 --> 03:09:59.205
But there are no parents in this committee.

3972
03:09:59.465 --> 03:10:01.045
No parents were notified of this,

3973
03:10:01.225 --> 03:10:02.925
but the students belong to us.

3974
03:10:04.025 --> 03:10:07.045
So just please, when we are creating committees

3975
03:10:07.045 --> 03:10:09.205
and task force and, and structures

3976
03:10:09.205 --> 03:10:11.685
to fix issues include the people

3977
03:10:11.805 --> 03:10:14.205
that the issues are affecting in high school,

3978
03:10:14.265 --> 03:10:16.245
we can include students in those conversations.

3979
03:10:16.865 --> 03:10:18.085
Um, and the assistive tech.

3980
03:10:18.105 --> 03:10:20.325
To that point, I would like a briefing about assistive

3981
03:10:20.325 --> 03:10:23.485
technology and, and how we are doing as a city.

3982
03:10:23.515 --> 03:10:25.885
Because as a parent of three students

3983
03:10:25.885 --> 03:10:28.365
that had assisted technology, I can tell you

3984
03:10:28.555 --> 03:10:30.645
that I can get private school for all my kids

3985
03:10:30.645 --> 03:10:32.605
because not one of their assisted technology

3986
03:10:32.765 --> 03:10:33.885
mandates is being met.

3987
03:10:34.265 --> 03:10:38.045
Not one of them. And I have to, every year ask for training

3988
03:10:38.425 --> 03:10:39.965
for whoever the staff is,

3989
03:10:39.975 --> 03:10:42.325
which should be a consideration when you're creating classes

3990
03:10:43.265 --> 03:10:45.165
to make sure that they know how to use it.

3991
03:10:45.345 --> 03:10:47.125
And to the point of the teacher and the time.

3992
03:10:47.805 --> 03:10:50.845
Assisted technology is a great tool that reduces the amount

3993
03:10:50.845 --> 03:10:52.445
of time that staff have

3994
03:10:52.445 --> 03:10:55.085
to spend on prep, creating materials.

3995
03:10:55.135 --> 03:10:57.445
There are program that have materials

3996
03:10:57.445 --> 03:10:59.205
that are already created and vetted

3997
03:10:59.205 --> 03:11:01.565
and differentiated that they don't have access to.

3998
03:11:01.925 --> 03:11:03.125
I wanna see those contracts.

3999
03:11:03.605 --> 03:11:07.245
I wanna see contracts for technology that supports staff

4000
03:11:07.625 --> 03:11:09.765
to be able to spend more time in classrooms.

4001
03:11:11.525 --> 03:11:14.865
And a SL interpretation, why don't we have it?

4002
03:11:16.255 --> 03:11:19.435
Nobody in New York City can participate.

4003
03:11:19.845 --> 03:11:23.395
There was a town hall held for, uh, busing

4004
03:11:23.775 --> 03:11:26.475
and the amount of families that showed up

4005
03:11:26.615 --> 03:11:28.515
for a SL interpretation.

4006
03:11:29.255 --> 03:11:30.435
And, and, and you know what?

4007
03:11:30.775 --> 03:11:33.115
We were like, go use the chatter, fill out the form.

4008
03:11:33.115 --> 03:11:34.555
And do you know what these people said?

4009
03:11:36.305 --> 03:11:37.485
That's not our language.

4010
03:11:37.705 --> 03:11:41.575
We speak a SL They are not literate sometimes.

4011
03:11:41.835 --> 03:11:44.855
So to tell someone to go to a website, read a form,

4012
03:11:45.205 --> 03:11:47.895
look at passions is not reasonable.

4013
03:11:48.205 --> 03:11:52.655
When they have learned A, B, CD, E, they do not know

4014
03:11:53.175 --> 03:11:54.535
A, B, C, D, E.

4015
03:11:55.235 --> 03:11:57.455
So we are completely inaccessible

4016
03:11:57.795 --> 03:12:01.855
to a hugely underserved population that is screaming

4017
03:12:01.855 --> 03:12:03.335
for help, but don't have a voice.

4018
03:12:03.365 --> 03:12:04.895
Literally, literally don't.

4019
03:12:05.595 --> 03:12:09.375
So if we can just at minimum provide a SL interpretation

4020
03:12:09.385 --> 03:12:12.455
every month, because when we show it on the Zoom platform,

4021
03:12:12.715 --> 03:12:15.215
it can be galleried where they're pinned to the screen

4022
03:12:15.555 --> 03:12:18.135
and they can watch the recording and be included.

4023
03:12:18.565 --> 03:12:21.455
They can't file busting complaints. They can't call OPT.

4024
03:12:21.725 --> 03:12:22.735
Explain to me

4025
03:12:22.915 --> 03:12:24.575
how we are servicing these families

4026
03:12:24.715 --> 03:12:25.815
in a briefing. Thank you.

4027
03:12:25.925 --> 03:12:30.445
Sure. Thank you panel member.

4028
03:12:30.545 --> 03:12:33.845
Um, Alicia, did you have any comment? Any other,

4029
03:12:37.235 --> 03:12:40.975
Um, I'm gonna switch,

4030
03:12:41.915 --> 03:12:43.175
switch topics a little bit.

4031
03:12:43.305 --> 03:12:47.205
Hello everyone. Um, so we know

4032
03:12:47.205 --> 03:12:50.245
that class sizes are much the same as they were last year,

4033
03:12:50.245 --> 03:12:51.525
which is super concerning.

4034
03:12:51.945 --> 03:12:55.165
In August, I was promised a briefing on class size by Mr.

4035
03:12:55.165 --> 03:12:56.365
Weisberg. Hi, Deanna.

4036
03:12:58.005 --> 03:13:00.665
Um, since then, though, one of the Queen

4037
03:13:01.175 --> 03:13:03.545
CECs has not only formed a public

4038
03:13:04.075 --> 03:13:07.735
class size committee within their district,

4039
03:13:07.735 --> 03:13:09.815
they've had two meetings, both

4040
03:13:09.835 --> 03:13:12.175
of which were healthfully attended by the public

4041
03:13:12.675 --> 03:13:16.135
and were attended by members of the superintendent's office

4042
03:13:16.475 --> 03:13:18.895
who came with data, came with answers,

4043
03:13:19.115 --> 03:13:22.135
and came with a very open attitude

4044
03:13:22.195 --> 03:13:25.455
to answering questions not only from the committee members

4045
03:13:25.595 --> 03:13:26.935
who are made up by moms of the public,

4046
03:13:27.075 --> 03:13:29.495
but also from CEC members who they have to see every month.

4047
03:13:31.475 --> 03:13:34.495
So I would really love an answer on when we can

4048
03:13:34.495 --> 03:13:35.815
get that briefing.

4049
03:13:36.955 --> 03:13:38.635
'cause it's October now.

4050
03:13:38.965 --> 03:13:41.075
Sorry, could you repeat the topic briefing?

4051
03:13:42.735 --> 03:13:43.595
We will, we will definitely

4052
03:13:43.595 --> 03:13:44.595
make sure that we'll schedule one.

4053
03:13:45.565 --> 03:13:50.135
Thank you. Yeah, we'll go back.

4054
03:13:50.135 --> 03:13:51.215
Panama Valley. Yep.

4055
03:13:51.435 --> 03:13:55.595
If that's okay. Thank you.

4056
03:13:56.195 --> 03:13:58.435
I just wanted to say thank you to the parents

4057
03:13:58.615 --> 03:14:00.395
and the, uh, teachers

4058
03:14:00.395 --> 03:14:02.315
that have come from Beacon High School.

4059
03:14:02.815 --> 03:14:05.515
Uh, thank you. I've received your information

4060
03:14:05.775 --> 03:14:06.955
and we'll be following up.

4061
03:14:06.965 --> 03:14:07.965
Thank you.

4062
03:14:10.375 --> 03:14:12.035
Thanks. Yes.

4063
03:14:12.315 --> 03:14:13.555
I wanna thank everyone who came

4064
03:14:13.615 --> 03:14:15.875
and spoke, uh, taking copious notes

4065
03:14:15.895 --> 03:14:18.755
and we'll be following up with both, uh, DOE staff

4066
03:14:18.855 --> 03:14:22.075
and with your, um, with yourselves as soon as possible.

4067
03:14:22.395 --> 03:14:24.515
I wanna welcome, uh, the Chancellor.

4068
03:14:24.775 --> 03:14:25.955
Uh, thank you for sitting with us.

4069
03:14:25.975 --> 03:14:27.475
Uh, it's really important to see you here,

4070
03:14:27.895 --> 03:14:29.475
uh, involved in the work together.

4071
03:14:30.055 --> 03:14:33.235
Uh, a couple of things. I had a really productive discussion

4072
03:14:33.235 --> 03:14:36.935
with, uh, um, with, uh,

4073
03:14:37.265 --> 03:14:39.935
chair Shaquille is chair, I forget his title,

4074
03:14:40.315 --> 03:14:41.775
but, uh, love him.

4075
03:14:41.795 --> 03:14:44.935
And, and we, he wants to involve the panel in a visit

4076
03:14:45.115 --> 03:14:48.415
to their, um, office in Brooklyn to show us what they do

4077
03:14:49.035 --> 03:14:51.735
and, and, and sort of to get us a better idea of

4078
03:14:51.795 --> 03:14:55.335
how we can support a lot of this stuff that needs

4079
03:14:55.335 --> 03:14:57.975
to be done in-house, in, in my opinion, as a technologist.

4080
03:14:58.275 --> 03:15:00.655
Uh, and, and, and have better contracts

4081
03:15:00.655 --> 03:15:04.095
and less, less outsourcing, more insourcing, have expertise

4082
03:15:04.115 --> 03:15:06.415
of the things that really should be done by the system.

4083
03:15:06.835 --> 03:15:10.215
Uh, and hopefully, uh, we'll send an email and follow up.

4084
03:15:10.355 --> 03:15:12.735
Uh, I have already a lot of interest from some members here.

4085
03:15:13.195 --> 03:15:16.495
Um, we have, uh, continued to have lots

4086
03:15:16.495 --> 03:15:18.615
of families living in temporary housing.

4087
03:15:19.115 --> 03:15:20.735
Uh, that's something that I'm working

4088
03:15:20.735 --> 03:15:21.935
on essentially on a daily basis.

4089
03:15:22.325 --> 03:15:23.495
It's, uh, heartening to see

4090
03:15:23.495 --> 03:15:26.495
that they're not doing the DHS evictions yet.

4091
03:15:26.875 --> 03:15:28.455
Uh, I hope they never do them.

4092
03:15:28.755 --> 03:15:31.855
Uh, so that the kids that are in school, uh,

4093
03:15:32.155 --> 03:15:35.015
and have no documented status can remain both in their

4094
03:15:35.015 --> 03:15:36.335
schools and easily commute.

4095
03:15:36.715 --> 03:15:39.775
Uh, and, uh, nothing happens to their housing

4096
03:15:40.415 --> 03:15:42.575
situation except for finding permanent housing

4097
03:15:42.715 --> 03:15:43.735
during the school year.

4098
03:15:44.195 --> 03:15:47.695
Um, and I think that's it. My time. Thank you. Thank you

4099
03:15:50.155 --> 03:15:51.535
Ano virus.

4100
03:15:58.295 --> 03:16:00.775
Good evening. Evening everyone. And thank you again,

4101
03:16:00.775 --> 03:16:01.935
chancellor for joining us today.

4102
03:16:01.935 --> 03:16:03.215
And thank you for visiting Renaissance.

4103
03:16:05.035 --> 03:16:08.245
Um, I just was curious, just in general,

4104
03:16:08.245 --> 03:16:09.765
just thinking about Rema, what she was saying.

4105
03:16:09.905 --> 03:16:13.085
Is there videos that goes out, typically the parents

4106
03:16:13.105 --> 03:16:14.245
to help them understand how

4107
03:16:14.245 --> 03:16:15.405
to navigate our

4108
03:16:15.405 --> 03:16:16.845
electronics at the beginning of the school year?

4109
03:16:16.845 --> 03:16:17.885
Have they ever been considered?

4110
03:16:21.375 --> 03:16:22.755
So I, I really love that idea.

4111
03:16:22.975 --> 03:16:26.275
And right now we are really thinking about the multiple ways

4112
03:16:26.275 --> 03:16:28.435
that we can engage and empower our families

4113
03:16:28.435 --> 03:16:31.875
through social media, through written communication,

4114
03:16:31.875 --> 03:16:32.955
verbal communication.

4115
03:16:33.135 --> 03:16:35.275
So thank you for the, the idea

4116
03:16:35.335 --> 03:16:36.955
and we'll definitely look to see

4117
03:16:36.955 --> 03:16:38.115
how we can operationalize that.

4118
03:16:38.685 --> 03:16:40.755
Thank you for that. And then regarding the assessment,

4119
03:16:40.935 --> 03:16:42.355
I'm just curious 'cause I know I'm a parent.

4120
03:16:42.475 --> 03:16:43.715
I was texting my daughter, like,

4121
03:16:44.065 --> 03:16:45.115
when you take your assessment,

4122
03:16:45.215 --> 03:16:46.395
did your teacher communicate with you?

4123
03:16:46.435 --> 03:16:47.835
I know a parent teacher did communicate

4124
03:16:47.835 --> 03:16:50.155
with me in my school, but for my colleagues

4125
03:16:50.175 --> 03:16:51.955
who do have children currently in school,

4126
03:16:52.495 --> 03:16:54.995
who has taken the assessment, have you not been communicated

4127
03:16:54.995 --> 03:16:55.995
to from your teachers?

4128
03:16:57.595 --> 03:16:58.165
Just curious.

4129
03:17:04.765 --> 03:17:06.425
And I only ask that question, chancellor,

4130
03:17:06.425 --> 03:17:10.155
because there, there is a concern in general that equity

4131
03:17:10.215 --> 03:17:12.235
of consistency across schools about

4132
03:17:13.405 --> 03:17:14.895
principal school leadership.

4133
03:17:15.035 --> 03:17:16.095
You know, Rema and I have talked

4134
03:17:16.095 --> 03:17:17.655
before, I've actually leaned on her a couple

4135
03:17:17.655 --> 03:17:20.175
of times when I became a parent leader at Renaissance.

4136
03:17:20.175 --> 03:17:21.935
Just making sure that I understood all

4137
03:17:21.935 --> 03:17:23.535
of the Chancellor regulations

4138
03:17:23.595 --> 03:17:27.215
and kind of use them at, you know, as necessary to be able

4139
03:17:27.215 --> 03:17:28.895
to remind the principal of their expectations.

4140
03:17:29.355 --> 03:17:33.015
So what can we do? Just curious as parents to be able to

4141
03:17:33.795 --> 03:17:35.215
not, not fight with leadership,

4142
03:17:35.395 --> 03:17:38.135
but better advocate to ensure that they're doing their job.

4143
03:17:38.725 --> 03:17:43.335
Yeah. Yes, sure. So, I I want to also

4144
03:17:44.165 --> 03:17:46.295
mention, I I am the mother

4145
03:17:46.355 --> 03:17:48.935
of a New York City public school student as well.

4146
03:17:49.395 --> 03:17:51.015
And one of the things

4147
03:17:51.015 --> 03:17:53.215
that I have been very transparent about is

4148
03:17:53.215 --> 03:17:55.135
that when I was a teacher, I was not a mother.

4149
03:17:55.685 --> 03:17:56.815
When I was a principal,

4150
03:17:56.935 --> 03:17:58.415
I was the mother of an infant toddler.

4151
03:17:58.715 --> 03:18:03.135
And when I got to the, uh, the district

4152
03:18:03.155 --> 03:18:05.255
as a deputy superintendent, acting superintendent,

4153
03:18:05.255 --> 03:18:08.335
and then eventually here at Tweed, um, I became the mother

4154
03:18:08.335 --> 03:18:09.535
of a school aged child.

4155
03:18:09.995 --> 03:18:12.055
And I will be extremely transparent

4156
03:18:12.155 --> 03:18:14.535
and say that my view

4157
03:18:15.475 --> 03:18:18.295
of our system definitely changed

4158
03:18:18.675 --> 03:18:21.455
and it sharpened my lens As a leader,

4159
03:18:22.315 --> 03:18:23.915
I think we do certain things very well,

4160
03:18:24.615 --> 03:18:27.435
and I think that there are things that need improvement.

4161
03:18:28.385 --> 03:18:31.925
Um, I will never sit here as a mother or as an educator

4162
03:18:31.945 --> 03:18:33.405
or as a school leader and tell you

4163
03:18:33.405 --> 03:18:34.685
that everything is perfect and

4164
03:18:34.685 --> 03:18:35.925
that we've done all the things.

4165
03:18:36.505 --> 03:18:40.635
And this is why PEP and our CECs

4166
03:18:40.895 --> 03:18:43.795
and all the additional things that we do to engage with all

4167
03:18:43.795 --> 03:18:46.475
of you and hear you out is so important

4168
03:18:47.075 --> 03:18:50.285
because everyone's experience as a parent

4169
03:18:50.985 --> 03:18:52.885
is very, very different.

4170
03:18:53.665 --> 03:18:56.565
Um, I am extremely privileged and resourced.

4171
03:18:57.025 --> 03:19:00.165
My daughter right now is at home with my sister, uh,

4172
03:19:00.725 --> 03:19:03.565
albeit she is going to be pretty upset with me

4173
03:19:03.565 --> 03:19:05.085
because tomorrow's Halloween.

4174
03:19:05.145 --> 03:19:06.885
And she's like, you better be up early

4175
03:19:06.905 --> 03:19:08.605
and make sure that my costume is ready.

4176
03:19:09.265 --> 03:19:12.285
Um, but I signed up for this, right?

4177
03:19:12.785 --> 03:19:15.805
And so I say all this to say that

4178
03:19:16.325 --> 03:19:19.085
I myself have had some interesting experiences

4179
03:19:19.635 --> 03:19:24.485
with assessment and inconsistency in how I get feedback.

4180
03:19:25.115 --> 03:19:29.125
Some teachers have been excellent, others have growth areas.

4181
03:19:30.025 --> 03:19:34.725
But this is why job embedded support is so important.

4182
03:19:35.195 --> 03:19:37.485
This is why leadership is so important.

4183
03:19:38.465 --> 03:19:42.365
Do we have the answer to all of this? A blanket answer?

4184
03:19:42.745 --> 03:19:44.725
No, because it's not one answer.

4185
03:19:44.725 --> 03:19:49.005
Because as you've all pointed out, different contexts,

4186
03:19:49.005 --> 03:19:52.125
different situations require different responses.

4187
03:19:52.785 --> 03:19:55.925
So the best that I can do is say that I hear you.

4188
03:19:56.355 --> 03:19:58.765
I've experienced some of this myself,

4189
03:19:59.505 --> 03:20:00.765
and we have a lot of work to do

4190
03:20:01.265 --> 03:20:02.405
and that's why we're here tonight

4191
03:20:02.425 --> 03:20:04.365
and that's why we're showing up in a different way

4192
03:20:04.365 --> 03:20:08.445
and making sure that we are listening to you.

4193
03:20:09.255 --> 03:20:10.325
Thank you. Thank

4194
03:20:10.325 --> 03:20:11.325
You.

4195
03:20:15.135 --> 03:20:17.065
Vice Chair Green. Any comment?

4196
03:20:17.915 --> 03:20:20.535
No, but I wanted just thank, uh, chancellor for being here

4197
03:20:20.795 --> 03:20:24.175
and I just wanna say yes, it is concerning that, uh,

4198
03:20:24.795 --> 03:20:27.895
the assessments have not been provided for parents.

4199
03:20:28.135 --> 03:20:31.215
I know as a principal, and I think my fellow principals can,

4200
03:20:31.315 --> 03:20:34.295
uh, attest to this, parents got letters in the mail

4201
03:20:34.445 --> 03:20:37.815
with their assessment results and online

4202
03:20:38.075 --> 03:20:39.215
and the children got them.

4203
03:20:39.275 --> 03:20:41.775
And we had data meetings and we had teacher data meetings.

4204
03:20:42.615 --> 03:20:45.495
So, uh, I'm very concerned about whatever school

4205
03:20:46.095 --> 03:20:48.495
teachers didn't get their student assessments.

4206
03:20:48.495 --> 03:20:49.495
Thank you.

4207
03:20:51.415 --> 03:20:52.815
Alban. We'll go

4208
03:20:52.815 --> 03:20:53.815
Around. Uh, good

4209
03:20:53.815 --> 03:20:55.135
evening. Good evening everyone.

4210
03:20:55.555 --> 03:20:57.575
I'm gonna make a comment with, I didn't plan to,

4211
03:20:57.795 --> 03:20:59.735
but due to comments that's happening now.

4212
03:21:00.355 --> 03:21:03.175
Um, I'm gonna add something to my closing remarks.

4213
03:21:03.715 --> 03:21:07.685
So the current citywide superintendents, I've worked

4214
03:21:07.685 --> 03:21:10.005
with them for the past couple of years, right?

4215
03:21:10.265 --> 03:21:12.645
And they've been very remarkable and resourceful.

4216
03:21:12.965 --> 03:21:16.285
I just wanna say that at this point in, in this particular,

4217
03:21:16.465 --> 03:21:20.765
the, um, Dr. Allen Chang, the superintendent, he is,

4218
03:21:21.425 --> 03:21:25.285
he is super, I know from experience, super pro parent

4219
03:21:25.425 --> 03:21:26.965
and family oriented.

4220
03:21:27.385 --> 03:21:30.405
And he also not only stop there, he want

4221
03:21:30.405 --> 03:21:31.925
to hear from the students, right?

4222
03:21:31.925 --> 03:21:35.565
He always encourages to self advocate, right?

4223
03:21:36.145 --> 03:21:37.245
To self promote.

4224
03:21:37.525 --> 03:21:39.605
'cause we don't know what they need if they

4225
03:21:39.605 --> 03:21:40.765
don't speak to us, right?

4226
03:21:40.955 --> 03:21:42.525
They, who better knows what they need.

4227
03:21:42.665 --> 03:21:44.245
So I just wanna put that out there.

4228
03:21:44.585 --> 03:21:47.205
And I'm gonna say for those parents who spoke about Beacon,

4229
03:21:47.835 --> 03:21:49.805
he's very well aware of what's happening

4230
03:21:49.985 --> 03:21:51.285
and he's been working on it.

4231
03:21:51.385 --> 03:21:53.565
And he's been working with, with leadership, right?

4232
03:21:53.565 --> 03:21:58.315
Especially with, um, DC Rucks, right? So he's aware.

4233
03:21:58.855 --> 03:22:00.275
And, and please reach out.

4234
03:22:00.495 --> 03:22:03.115
He will reach out back, his team will reach out back.

4235
03:22:03.295 --> 03:22:05.755
So when it comes to that, I just had to make sure

4236
03:22:05.945 --> 03:22:07.155
that it's clear there.

4237
03:22:07.535 --> 03:22:10.155
Um, I just wanna summarize what everybody's saying.

4238
03:22:10.455 --> 03:22:15.075
So if we continually or strive to do business

4239
03:22:15.335 --> 03:22:18.315
or do what we need to do for New York City public schools

4240
03:22:18.315 --> 03:22:19.515
through an equity lens,

4241
03:22:19.975 --> 03:22:22.235
and equity doesn't mean we take from

4242
03:22:22.235 --> 03:22:23.555
one and give to someone.

4243
03:22:24.015 --> 03:22:28.995
Equity means that we provide the support and resources.

4244
03:22:29.055 --> 03:22:30.475
Yes, everybody could take a test.

4245
03:22:30.615 --> 03:22:32.355
I'm gonna give the ssat for example,

4246
03:22:32.655 --> 03:22:33.795
all students are allowed.

4247
03:22:33.815 --> 03:22:36.115
That's equality. But is it equitable?

4248
03:22:36.255 --> 03:22:37.715
Do they have the same resources?

4249
03:22:38.015 --> 03:22:41.635
Are we getting them prepared to be able to do those tests?

4250
03:22:41.935 --> 03:22:43.795
That's what equity is, right?

4251
03:22:43.795 --> 03:22:45.715
And we want equity through all lenses.

4252
03:22:46.295 --> 03:22:51.155
So, um, I'm gonna take something from CPAC had created, um,

4253
03:22:51.155 --> 03:22:54.475
their own acronym of act, um, for this new,

4254
03:22:54.695 --> 03:22:55.995
the former administration.

4255
03:22:56.195 --> 03:22:57.235
'cause T Legal is different now

4256
03:22:57.515 --> 03:22:58.755
'cause we have a new chancellor.

4257
03:22:59.415 --> 03:23:04.355
But we had asked if we continued through ACT A

4258
03:23:04.495 --> 03:23:07.225
for accountability, communication,

4259
03:23:07.605 --> 03:23:10.145
and transparency, we'll be able to do better.

4260
03:23:10.245 --> 03:23:11.665
We could always strike perfection.

4261
03:23:11.765 --> 03:23:14.185
And if we keep these in the background, right?

4262
03:23:14.185 --> 03:23:16.945
We need to communicate with everybody, all stakeholders.

4263
03:23:17.325 --> 03:23:21.145
We need to be transparent, um, and say what we mean.

4264
03:23:21.245 --> 03:23:25.905
And if it's a no to say no, right? We we're, we're adults.

4265
03:23:26.325 --> 03:23:29.865
Um, it's not doable. And say why it's not doable, right?

4266
03:23:30.165 --> 03:23:34.145
It, you need to feel that partnership, that inclusion,

4267
03:23:34.415 --> 03:23:36.185
that our voice matters, right?

4268
03:23:36.365 --> 03:23:37.785
And our voice does matter.

4269
03:23:38.205 --> 03:23:39.665
So I'm just gonna leave it like that.

4270
03:23:39.795 --> 03:23:42.825
Let's work on act through equitable means.

4271
03:23:44.235 --> 03:23:48.675
Thank you. Next, uh, remember, do you wanna say this?

4272
03:23:50.925 --> 03:23:53.165
Although, although we've spoken about many things tonight,

4273
03:23:53.345 --> 03:23:54.805
one thing is resonating with me,

4274
03:23:55.025 --> 03:23:57.845
and that is the issue around assessment.

4275
03:23:58.545 --> 03:24:02.485
I'm appalled to to hear that teachers are not getting

4276
03:24:03.105 --> 03:24:05.005
the data from these assessments.

4277
03:24:05.635 --> 03:24:08.005
That is unheard of as a principal.

4278
03:24:08.005 --> 03:24:09.925
That never happened in my building.

4279
03:24:10.425 --> 03:24:12.765
And it's something that the panel surely needs to review.

4280
03:24:14.305 --> 03:24:17.115
Thank you Mama Garcia.

4281
03:24:21.465 --> 03:24:24.385
I wasn't going to say anything either, but just

4282
03:24:24.935 --> 03:24:27.225
because it was so long ago,

4283
03:24:27.865 --> 03:24:30.305
I just wanna tell parents you have no idea

4284
03:24:31.815 --> 03:24:35.275
how you are getting at least some information.

4285
03:24:35.335 --> 03:24:39.235
It may not be enough and it may not be what you need,

4286
03:24:39.295 --> 03:24:43.445
but I am telling you, when I was a teacher

4287
03:24:44.065 --> 03:24:47.085
in the top school in New York Public School

4288
03:24:48.415 --> 03:24:52.195
as an English teacher, my daughter attended the same school

4289
03:24:52.745 --> 03:24:57.125
when I was there, and we did not get information.

4290
03:24:57.345 --> 03:24:59.565
That's how we did not get assess.

4291
03:24:59.825 --> 03:25:04.565
So things are changing, I'm sure not fast enough,

4292
03:25:04.665 --> 03:25:09.135
but I am telling you parents did not get the information

4293
03:25:10.385 --> 03:25:12.585
that you get now.

4294
03:25:13.285 --> 03:25:17.465
And so hopefully it will keep getting better

4295
03:25:18.045 --> 03:25:22.745
and hopefully we can be a part of helping you get better.

4296
03:25:23.145 --> 03:25:28.035
I hope that is, um, at least some, some sauce.

4297
03:25:28.985 --> 03:25:29.985
Thank you.

4298
03:25:32.225 --> 03:25:32.975
Thank you, Anita.

4299
03:25:37.475 --> 03:25:41.555
I help you, Robert. I I appreciate that. Um, yes.

4300
03:25:42.215 --> 03:25:45.725
Um, thanks for, you know, hanging in there.

4301
03:25:46.895 --> 03:25:48.905
I appreciate detention

4302
03:25:49.815 --> 03:25:52.425
because it, it shows a part of humanity

4303
03:25:53.315 --> 03:25:56.525
when you can step in a room and not have to yes, man

4304
03:25:56.525 --> 03:25:59.285
and agree with what everybody is saying.

4305
03:25:59.585 --> 03:26:01.285
So I, there there is,

4306
03:26:03.115 --> 03:26:06.885
there's value in being able to speak your mind and,

4307
03:26:06.945 --> 03:26:10.765
and get what you have to say off your chest without, um,

4308
03:26:10.955 --> 03:26:14.045
failing as if that's something wrong.

4309
03:26:14.985 --> 03:26:17.125
And, and it keeps communication going.

4310
03:26:18.025 --> 03:26:22.555
Um, I have to say, it's challenging to hear.

4311
03:26:23.015 --> 03:26:26.275
Um, you know, people say they don't want may mayor rolls on

4312
03:26:26.275 --> 03:26:27.755
because it's time, you know,

4313
03:26:27.865 --> 03:26:29.275
they should leave or what have you.

4314
03:26:30.675 --> 03:26:32.975
At the end of the day, we're parents

4315
03:26:34.165 --> 03:26:36.985
and there's a lot of parent leadership.

4316
03:26:38.105 --> 03:26:41.745
And the reason why most

4317
03:26:41.745 --> 03:26:45.665
of us parents are on this panel is

4318
03:26:45.665 --> 03:26:47.745
because of the things we did not like.

4319
03:26:49.745 --> 03:26:52.715
It's not because we, we are kumbaya

4320
03:26:52.895 --> 03:26:55.875
and up here it is, what the heck is going on?

4321
03:26:56.615 --> 03:27:00.995
And what do I need to know? What do I need to learn?

4322
03:27:01.975 --> 03:27:04.715
And so once you, you get past being angry

4323
03:27:05.415 --> 03:27:08.745
and cursing under your breath, then you have to

4324
03:27:09.705 --> 03:27:12.905
position yourself or to ask the questions that will lead you

4325
03:27:12.925 --> 03:27:14.905
to not, and I'm not going

4326
03:27:14.905 --> 03:27:16.865
to look at this thing from the outside in.

4327
03:27:17.065 --> 03:27:21.665
I wanna find out from the inside what is actually happening.

4328
03:27:21.965 --> 03:27:25.345
And then how can we make changes? What is the language?

4329
03:27:25.485 --> 03:27:26.705
How does things move?

4330
03:27:28.845 --> 03:27:31.265
How long does a contract take? Okay?

4331
03:27:31.945 --> 03:27:34.105
I wanna be a, at the head of that

4332
03:27:34.325 --> 03:27:36.545
as a contract committee chair,

4333
03:27:37.375 --> 03:27:40.035
you get different perspective when you actually

4334
03:27:41.565 --> 03:27:44.915
don't complain or you limit your complaining and put your,

4335
03:27:44.935 --> 03:27:46.635
and stand in somebody's shoes.

4336
03:27:47.495 --> 03:27:51.435
So it's, it's not, it's not all, it's not fun at all,

4337
03:27:51.975 --> 03:27:53.395
but it's very informative.

4338
03:27:54.015 --> 03:27:57.195
And I know as a, which leads to my next thing.

4339
03:27:57.855 --> 03:28:01.235
As a black woman who was raised in Brooklyn, born

4340
03:28:01.235 --> 03:28:03.235
and raised in Brooklyn, I got a chance

4341
03:28:03.235 --> 03:28:05.395
to see quite a few paradigm shifts.

4342
03:28:06.405 --> 03:28:10.845
And to be uncomfortable would

4343
03:28:10.845 --> 03:28:11.885
be an understatement.

4344
03:28:13.155 --> 03:28:14.735
You learn how to deal with that type

4345
03:28:14.735 --> 03:28:16.335
of discourse and do it anyway.

4346
03:28:16.995 --> 03:28:21.515
Um, and I just wanted to share that because this is work.

4347
03:28:22.415 --> 03:28:23.865
This is, this is actual work,

4348
03:28:23.885 --> 03:28:26.425
and it takes time to figure things out.

4349
03:28:27.005 --> 03:28:30.545
It takes time to, to speak a language

4350
03:28:30.685 --> 03:28:32.905
and put it in several different languages.

4351
03:28:32.965 --> 03:28:35.225
And I'm still talking about English, right?

4352
03:28:35.565 --> 03:28:39.465
For people to understand how you communicate,

4353
03:28:39.855 --> 03:28:41.505
what are people's entry points?

4354
03:28:42.125 --> 03:28:44.585
How can they, how can I get my message across?

4355
03:28:45.085 --> 03:28:48.745
And so to not just learn what's going on as a parent,

4356
03:28:49.125 --> 03:28:52.705
but also learn what's going on in policy, in policy

4357
03:28:53.445 --> 03:28:54.985
and having to do the work there.

4358
03:28:55.805 --> 03:28:58.625
Um, and so, and, and that's the work.

4359
03:28:58.685 --> 03:29:00.305
And I, and I stand by the,

4360
03:29:00.405 --> 03:29:02.705
the second point is a little pet peeve of mine.

4361
03:29:03.145 --> 03:29:05.545
I do appreciate the conversation,

4362
03:29:06.085 --> 03:29:09.625
but I would prefer if parents did not refer to black people

4363
03:29:09.725 --> 03:29:12.185
as blacks, the blacks.

4364
03:29:13.425 --> 03:29:15.475
Okay? Gotta put some respect on that

4365
03:29:15.475 --> 03:29:20.035
because again, this has to deal with, with understanding

4366
03:29:20.655 --> 03:29:25.325
the racial harm that has been very pervasive

4367
03:29:26.315 --> 03:29:30.435
in these settings, black people, African Americans,

4368
03:29:31.515 --> 03:29:34.495
but the, the word blacks is, is very triggering

4369
03:29:34.495 --> 03:29:38.295
because that, that says that, you know, you, you,

4370
03:29:38.315 --> 03:29:40.015
you may not have recognized that.

4371
03:29:40.015 --> 03:29:42.535
That's just not what, what we say in public settings.

4372
03:29:42.585 --> 03:29:44.615
We're, and, and that's a part of the issue.

4373
03:29:44.865 --> 03:29:47.615
We're grouping people. We're not blacks.

4374
03:29:48.315 --> 03:29:50.575
So please take the S off and,

4375
03:29:50.635 --> 03:29:52.975
and, um, you know, come up with a better phrase and,

4376
03:29:52.975 --> 03:29:56.215
and so we can continue this conversation in a healthy way.

4377
03:29:57.285 --> 03:29:58.315
Thank you. Thank you

4378
03:30:02.105 --> 03:30:05.275
Quickly, hopefully, um, with respect,

4379
03:30:05.795 --> 03:30:08.635
I do appreciate everybody who contributed today.

4380
03:30:09.715 --> 03:30:13.345
And we probably all learned something today

4381
03:30:13.345 --> 03:30:16.025
because we really carried, I think this conversation

4382
03:30:16.185 --> 03:30:17.545
of assessment a lot farther.

4383
03:30:18.045 --> 03:30:20.465
Let me just give you my perspective, just

4384
03:30:20.465 --> 03:30:22.185
because culturally speaking,

4385
03:30:23.045 --> 03:30:26.305
my entire life has been an assessment from

4386
03:30:26.635 --> 03:30:27.865
where I came from.

4387
03:30:28.055 --> 03:30:32.105
Meaning my parents always told me, my father's 98 now,

4388
03:30:32.775 --> 03:30:37.345
that everything in his life was an assessment to get him to

4389
03:30:37.345 --> 03:30:38.385
where he is today.

4390
03:30:39.265 --> 03:30:43.245
So assessment is not a strange or foreign word to me.

4391
03:30:43.945 --> 03:30:47.965
So that when we have this conversation of, um, and,

4392
03:30:47.965 --> 03:30:50.125
and you might use a different word later in life

4393
03:30:50.125 --> 03:30:53.565
because we aren't going to be assessed the same way now.

4394
03:30:54.345 --> 03:30:57.925
Um, but I just want us to get used to that concept

4395
03:30:58.305 --> 03:31:02.085
of we may not be using the same metrics at the same time,

4396
03:31:03.105 --> 03:31:07.005
but the reality is our kids need to learn that

4397
03:31:07.805 --> 03:31:11.875
there are calls made by their behavior,

4398
03:31:12.375 --> 03:31:14.595
by their, uh, engagements,

4399
03:31:15.375 --> 03:31:18.315
by their testing, by their play.

4400
03:31:19.135 --> 03:31:23.635
And ask them to be true to themselves

4401
03:31:24.295 --> 03:31:26.875
and learn the words that they need to of

4402
03:31:27.545 --> 03:31:29.115
that doesn't feel right.

4403
03:31:30.055 --> 03:31:33.355
And overall, that's when you'll get to figure out

4404
03:31:33.385 --> 03:31:36.195
what assessment really means to them.

4405
03:31:36.975 --> 03:31:40.355
And hopefully you will find the schools that will match

4406
03:31:40.415 --> 03:31:43.855
to them to do the cor correct

4407
03:31:43.855 --> 03:31:45.575
or correct assessment for them.

4408
03:31:45.675 --> 03:31:49.135
And that's what I really took from the Beacon conversation

4409
03:31:49.565 --> 03:31:53.335
when we did not put Beacon back in the day from my child

4410
03:31:53.715 --> 03:31:55.335
who had more than a 5 0 4.

4411
03:31:55.795 --> 03:31:58.095
And when you look at the website now,

4412
03:31:58.835 --> 03:32:02.895
the leadership is listed as a 5 0 4 coordinator, which

4413
03:32:03.045 --> 03:32:04.895
that already would've put my kid out of the running

4414
03:32:04.895 --> 03:32:08.415
because their emphasis was a kid who had 5 0 4.

4415
03:32:08.955 --> 03:32:13.575
So I, I found it odd to be honest, when I looked at

4416
03:32:13.595 --> 03:32:16.835
and heard some of the mismatching

4417
03:32:17.305 --> 03:32:19.755
that was going on right, right now.

4418
03:32:20.415 --> 03:32:24.195
So I think that sometimes we're really not looking at really

4419
03:32:24.195 --> 03:32:27.195
what is there and asking the right questions if the website,

4420
03:32:27.255 --> 03:32:29.755
and that's the only thing we can really go by is

4421
03:32:29.865 --> 03:32:32.795
what comes out of what that school says that they represent,

4422
03:32:33.145 --> 03:32:34.195
even if, and,

4423
03:32:34.195 --> 03:32:36.875
and to ask those pertinent questions when given that time.

4424
03:32:37.375 --> 03:32:39.675
And, and I just looked at it as that was really difficult

4425
03:32:39.695 --> 03:32:42.195
to hear what I had heard four

4426
03:32:42.195 --> 03:32:44.795
or five years ago about the same school

4427
03:32:44.795 --> 03:32:46.435
that is being talked about now, where I'm like,

4428
03:32:46.855 --> 03:32:50.635
the assessment is no different from then that it is now,

4429
03:32:50.815 --> 03:32:53.075
but I'm hearing individuals who assume

4430
03:32:53.615 --> 03:32:55.555
the school should be acting in a certain way.

4431
03:32:56.375 --> 03:32:59.195
So I just really ask that people really think through,

4432
03:33:00.025 --> 03:33:01.915
like when they read of a school

4433
03:33:02.055 --> 03:33:05.785
and how it is today, really understand it

4434
03:33:05.805 --> 03:33:08.705
as does it really match up with my values.

4435
03:33:18.425 --> 03:33:20.885
Um, first I wanna welcome the Chancellor.

4436
03:33:21.145 --> 03:33:23.325
Um, look forward to working with you in the future.

4437
03:33:24.995 --> 03:33:29.745
Um, so tonight, um, I heard the

4438
03:33:30.545 --> 03:33:35.265
audience speaking about how they chose a consortium school,

4439
03:33:35.475 --> 03:33:37.965
sorry, I can't say that word, consortium school.

4440
03:33:38.425 --> 03:33:42.805
Um, and it made me think how proud I am

4441
03:33:42.905 --> 03:33:45.365
of the choices New York City Public Schools offer.

4442
03:33:46.105 --> 03:33:49.165
Um, personally I prefer a traditional school

4443
03:33:49.195 --> 03:33:50.565
because I like to see numbers

4444
03:33:50.865 --> 03:33:55.775
and, you know, um, decide how much I need to help my kid

4445
03:33:55.795 --> 03:33:57.855
to succeed while preserving their

4446
03:33:57.855 --> 03:33:59.215
happiness at the same time.

4447
03:34:00.915 --> 03:34:05.805
Um, I think it's important, um,

4448
03:34:05.985 --> 03:34:10.665
to keep it interesting for our students, um,

4449
03:34:10.815 --> 03:34:13.345
when they're learning in school and the safety.

4450
03:34:14.125 --> 03:34:18.785
So I hope that moving forward, um, these two items

4451
03:34:19.955 --> 03:34:21.845
come first before anything else.

4452
03:34:22.825 --> 03:34:26.605
Um, learning, being interesting and safety.

4453
03:34:27.705 --> 03:34:29.525
Um, so for the

4454
03:34:31.685 --> 03:34:36.325
contract item number two, um, my school, um,

4455
03:34:36.705 --> 03:34:39.125
the SLT was able to get the principal

4456
03:34:39.305 --> 03:34:42.685
to pilot a new geometry program in junior high school.

4457
03:34:43.935 --> 03:34:45.875
Um, the way they picked

4458
03:34:46.495 --> 03:34:49.595
and chose the kids to enter this program was

4459
03:34:49.655 --> 03:34:50.835
by i-Ready scores.

4460
03:34:51.245 --> 03:34:53.995
There were many students that were performing at eighth

4461
03:34:53.995 --> 03:34:57.915
grade and ninth grade level math, um, in the seventh grade.

4462
03:34:58.735 --> 03:35:00.235
And basically these kids

4463
03:35:00.495 --> 03:35:04.475
before this, um, program was implemented, um, piloted,

4464
03:35:05.105 --> 03:35:06.835
they were like spinning in chairs in

4465
03:35:06.835 --> 03:35:08.355
class and they were bored.

4466
03:35:09.015 --> 03:35:11.275
So it was nice to see that, you know, um,

4467
03:35:11.625 --> 03:35:16.235
like a small portion of classes was being, um,

4468
03:35:16.305 --> 03:35:19.635
piloted for a new program to see if it works instead

4469
03:35:19.635 --> 03:35:20.715
of the whole grade.

4470
03:35:21.865 --> 03:35:25.575
So I like this flexibility, um,

4471
03:35:26.165 --> 03:35:30.335
that was offered and I'm glad that, you know, um, we're able

4472
03:35:30.335 --> 03:35:31.895
to do that in New York City Public Schools.

4473
03:35:32.675 --> 03:35:36.365
Another thing I wanna talk about is the S-H-S-A-T.

4474
03:35:37.315 --> 03:35:42.075
Um, I hope that we get briefed

4475
03:35:42.385 --> 03:35:46.475
regarding the new contract item that it's thought out, um,

4476
03:35:47.575 --> 03:35:51.795
better, instead of just flipping to electronic,

4477
03:35:52.055 --> 03:35:54.075
we wanna know the cost savings

4478
03:35:55.015 --> 03:35:59.395
and, um, if, how it'll affect students that are not, um,

4479
03:36:00.095 --> 03:36:02.735
as virtually, um,

4480
03:36:05.525 --> 03:36:07.425
you know, uh, positioned.

4481
03:36:07.425 --> 03:36:11.265
Yeah. Um, and I also wanna like state something personal.

4482
03:36:11.485 --> 03:36:15.305
Um, so the S-H-S-A-T for many immigrant families,

4483
03:36:15.695 --> 03:36:19.625
they view this school, this opportunity as, um, the door

4484
03:36:19.625 --> 03:36:21.425
to the American, the American dream.

4485
03:36:22.165 --> 03:36:25.745
So it's very important for the immigrant community

4486
03:36:25.925 --> 03:36:27.385
to preserve these tests.

4487
03:36:27.885 --> 03:36:30.425
And we do want to see more different

4488
03:36:30.455 --> 03:36:31.865
populations in these schools.

4489
03:36:32.845 --> 03:36:35.765
So we hope that we could put more money into, you know,

4490
03:36:36.245 --> 03:36:38.925
tutoring students to reach these goals

4491
03:36:38.925 --> 03:36:42.485
because we'll, more people will be proud of, you know,

4492
03:36:42.775 --> 03:36:46.035
these goals being more, um, inclusive.

4493
03:36:46.735 --> 03:36:50.475
We do like that, and I hope that we can all like, um,

4494
03:36:50.475 --> 03:36:52.315
work together to make this happen.

4495
03:36:52.685 --> 03:36:53.755
Thank you. Sure.

4496
03:36:59.435 --> 03:37:01.805
When I hear the term assessment, my,

4497
03:37:02.385 --> 03:37:04.645
my whole world changes because assessment

4498
03:37:04.865 --> 03:37:08.725
for the men's men's school is not the same for the 75.

4499
03:37:09.065 --> 03:37:11.365
And I'm not talking about the top 20%.

4500
03:37:11.955 --> 03:37:14.805
I've been dealing with my son 15 years in the system.

4501
03:37:15.275 --> 03:37:18.325
They give him the same assessment and he refuses to do it.

4502
03:37:18.325 --> 03:37:21.125
Therefore, they have him now from a fourth grade reading

4503
03:37:21.135 --> 03:37:25.025
level to a kindergarten level now figure that one out

4504
03:37:25.295 --> 03:37:29.305
because they will not adjust to the way he's allowed.

4505
03:37:29.375 --> 03:37:31.265
He's able to give the answers.

4506
03:37:31.365 --> 03:37:32.705
If he's not interested, he's not.

4507
03:37:32.965 --> 03:37:34.385
So therefore he doesn't do it.

4508
03:37:34.925 --> 03:37:37.025
And they said it's okay because he can't do it.

4509
03:37:37.285 --> 03:37:38.945
No, he can't do it. This is a child

4510
03:37:39.245 --> 03:37:42.785
who can every day looks up every changes in the trans,

4511
03:37:43.565 --> 03:37:47.385
he can tell you where to change what delay and everything.

4512
03:37:47.565 --> 03:37:50.585
And now right now he's into doing, uh,

4513
03:37:50.615 --> 03:37:52.385
he's researching going abroad.

4514
03:37:52.575 --> 03:37:55.025
He's finding hotels in Brazil tomorrow.

4515
03:37:55.045 --> 03:37:57.785
He is going, I don't know where I take DR for the day,

4516
03:37:58.205 --> 03:37:59.985
but he's able to do all that.

4517
03:38:00.365 --> 03:38:01.385
And you wanna tell me

4518
03:38:01.385 --> 03:38:03.385
that he's reading at a kindergarten level.

4519
03:38:03.785 --> 03:38:06.385
Hmm. So what do you really call assessment

4520
03:38:06.685 --> 03:38:08.825
and to which group does he apply to?

4521
03:38:09.405 --> 03:38:11.905
And I think since we brought the subject up today,

4522
03:38:12.445 --> 03:38:15.385
we should really take a look at it, at the population

4523
03:38:15.385 --> 03:38:16.425
that we are teaching.

4524
03:38:16.925 --> 03:38:19.625
It is not about all the children who are going to college,

4525
03:38:20.055 --> 03:38:22.385
it's also those who can have a future.

4526
03:38:23.195 --> 03:38:24.195
Thank you.

4527
03:38:26.285 --> 03:38:28.915
Thank you. Um, I know it's getting late, so I'm gonna try

4528
03:38:28.915 --> 03:38:30.275
to be as quick as I can.

4529
03:38:30.975 --> 03:38:34.475
Um, I just wanted to let, um, our guests

4530
03:38:34.935 --> 03:38:36.755
and the people watching online

4531
03:38:37.385 --> 03:38:40.035
that we did have two briefings, uh,

4532
03:38:40.065 --> 03:38:42.235
regarding the OMNI cards.

4533
03:38:42.495 --> 03:38:46.435
And so we are still discussing how to ensure that

4534
03:38:47.475 --> 03:38:49.635
distribution can be made wider.

4535
03:38:50.275 --> 03:38:51.995
I just wanted to acknowledge that

4536
03:38:51.995 --> 03:38:55.395
because it didn't come up at all during our time tonight.

4537
03:38:56.135 --> 03:39:00.715
Um, and I wanted to thank Dr. Ellis for continuing her work

4538
03:39:00.785 --> 03:39:01.955
with PSAL

4539
03:39:02.015 --> 03:39:06.155
and trying to ensure that more students are having access

4540
03:39:06.495 --> 03:39:08.235
to sports.

4541
03:39:08.855 --> 03:39:13.765
Um, I, I think we would be remiss not to mention the,

4542
03:39:14.105 --> 03:39:18.405
um, ongoing deaths of students through gun violence

4543
03:39:18.585 --> 03:39:19.685
and subway surfing.

4544
03:39:20.085 --> 03:39:21.605
I think that we really need

4545
03:39:21.605 --> 03:39:23.045
to start addressing this in a much,

4546
03:39:23.045 --> 03:39:24.685
much bigger way than we've been doing.

4547
03:39:26.055 --> 03:39:30.445
Um, $17 million for S-H-S-A-T.

4548
03:39:30.765 --> 03:39:33.325
I would encourage all of you to try to come out

4549
03:39:33.325 --> 03:39:35.805
to Staten Island for our next meeting

4550
03:39:36.265 --> 03:39:38.765
and, um, voice your opinion.

4551
03:39:40.045 --> 03:39:41.985
If I could pay for a bus, I would.

4552
03:39:43.365 --> 03:39:47.505
Um, but just, you know, to throw out a second thought there,

4553
03:39:47.565 --> 03:39:52.305
we might wanna use that $17 million for tutoring instead.

4554
03:39:52.765 --> 03:39:54.865
But, um, I guess we'll talk

4555
03:39:54.865 --> 03:39:57.785
to our state elected officials about that.

4556
03:39:58.805 --> 03:40:01.385
Um, and then just kudos to the DOE.

4557
03:40:01.695 --> 03:40:04.625
I'll just try to end on a, like a positive note here.

4558
03:40:05.245 --> 03:40:09.385
Um, I don't know if any of you have heard or seen yet,

4559
03:40:09.565 --> 03:40:11.305
but the DOE has created

4560
03:40:11.825 --> 03:40:14.545
a school budgets at a glance document.

4561
03:40:15.095 --> 03:40:18.065
It's a very easy to read document.

4562
03:40:18.285 --> 03:40:21.105
All of our SLTs and DLTs

4563
03:40:21.205 --> 03:40:24.185
and parents are gonna benefit from this.

4564
03:40:24.285 --> 03:40:26.065
Our, our, uh, principals

4565
03:40:26.445 --> 03:40:30.785
and teachers, anyone who was trying to navigate

4566
03:40:31.085 --> 03:40:34.985
how on earth school funding works, it is all very,

4567
03:40:35.055 --> 03:40:36.945
very clear and easy to read.

4568
03:40:37.485 --> 03:40:41.465
So, um, please go to the DOE'S website,

4569
03:40:41.535 --> 03:40:44.745
look up your school, look under the reports tab

4570
03:40:45.445 --> 03:40:47.985
and look for school budgets at a glance.

4571
03:40:48.875 --> 03:40:52.735
Please do this ASAP so that you understand how the funding

4572
03:40:52.795 --> 03:40:54.295
for your school is operating.

4573
03:40:54.435 --> 03:40:59.055
But, um, I am so very, very grateful to the DOE

4574
03:40:59.075 --> 03:41:00.255
for putting this together

4575
03:41:00.255 --> 03:41:02.135
because this is something that, um,

4576
03:41:02.135 --> 03:41:04.455
parent leaders have been asking for for many years

4577
03:41:04.955 --> 03:41:09.255
and it is just brilliantly done and so easy to read.

4578
03:41:09.275 --> 03:41:11.615
And so thank you. Thank you. Thank you so much for that.

4579
03:41:11.705 --> 03:41:12.705
Thank you. Thank you.

4580
03:41:19.445 --> 03:41:22.825
Um, on behalf of the comptroller, um,

4581
03:41:23.185 --> 03:41:24.545
I just wanna mention a couple of things

4582
03:41:24.545 --> 03:41:26.505
that we actually haven't talked much about tonight,

4583
03:41:26.565 --> 03:41:29.865
but, um, would like to shed some light on.

4584
03:41:30.205 --> 03:41:32.585
Um, I would like to note

4585
03:41:32.585 --> 03:41:35.305
that mid-November is an important time

4586
03:41:35.605 --> 03:41:38.065
for class size rejection in New York City.

4587
03:41:38.815 --> 03:41:42.155
Um, as doe's annual report on their implementation

4588
03:41:42.155 --> 03:41:45.855
of their class size plan will be issued, um,

4589
03:41:45.915 --> 03:41:48.735
the comptroller certifies that annual report

4590
03:41:49.355 --> 03:41:50.455
and, um,

4591
03:41:50.555 --> 03:41:54.055
as noted in the comptroller's class size plan certification

4592
03:41:54.055 --> 03:41:59.015
letter from last June, um, doe's education expense

4593
03:41:59.035 --> 03:42:02.615
and capital funding plans do not provide sufficient funding

4594
03:42:02.635 --> 03:42:05.215
to reduce class size as required by state law.

4595
03:42:06.445 --> 03:42:10.305
Um, at that time, the office of the comptroller estimated

4596
03:42:10.855 --> 03:42:13.905
that the cost of the additional teachers required

4597
03:42:13.925 --> 03:42:17.325
to achieve class size targets grow from a range

4598
03:42:17.325 --> 03:42:19.565
of $374 million

4599
03:42:19.905 --> 03:42:24.005
and $422 million of fiscal year 2026 to

4600
03:42:24.005 --> 03:42:26.005
between 1.5 billion

4601
03:42:26.065 --> 03:42:29.845
and 1.65 billion at full implementation in fiscal

4602
03:42:29.955 --> 03:42:31.205
year 2028.

4603
03:42:33.085 --> 03:42:37.505
Um, we have seen no evidence of proactive planning

4604
03:42:37.885 --> 03:42:42.025
for implementation, especially in terms of funding schools.

4605
03:42:42.325 --> 03:42:45.225
And I mentioned this because we have visited schools

4606
03:42:45.235 --> 03:42:46.825
where principals have told us

4607
03:42:46.855 --> 03:42:51.065
that they actually have the space to reduce class size,

4608
03:42:51.645 --> 03:42:52.945
but they do not have the funding

4609
03:42:53.005 --> 03:42:55.305
to hire the teachers needed, um,

4610
03:42:55.445 --> 03:42:56.865
for the additional classrooms.

4611
03:42:57.795 --> 03:43:02.615
Um, and they don't know of any communication from DOE on

4612
03:43:02.675 --> 03:43:05.895
how compliance at the school level will actually work.

4613
03:43:06.675 --> 03:43:11.495
Um, we would like to suggest that DOE move more proactively

4614
03:43:11.675 --> 03:43:14.215
to adjust the way in which they fund schools

4615
03:43:14.395 --> 03:43:15.855
to reduce class size

4616
03:43:16.205 --> 03:43:19.015
because current funding is not going to work.

4617
03:43:19.805 --> 03:43:23.305
Um, and the state must consider class size as it gets set

4618
03:43:23.685 --> 03:43:26.625
to implement changes to the foundation aid formula.

4619
03:43:27.995 --> 03:43:32.635
Finally, I want to uplift, um, the,

4620
03:43:32.895 --> 03:43:35.235
um, the issue of school accessibility.

4621
03:43:36.375 --> 03:43:40.475
Um, the new school construction authority five-year capital

4622
03:43:40.665 --> 03:43:44.555
plan amendment comes out in two days on November 1st.

4623
03:43:45.495 --> 03:43:50.075
And there has been no more funding added to that plan

4624
03:43:50.175 --> 03:43:54.005
for school accessibility at $800 million.

4625
03:43:54.985 --> 03:43:56.325
Um, and given inflation

4626
03:43:56.505 --> 03:43:59.405
and other cost increases, the this amount

4627
03:43:59.925 --> 03:44:02.285
represents virtually no increase in the investment

4628
03:44:02.955 --> 03:44:04.485
over the last five year plan.

4629
03:44:05.995 --> 03:44:08.315
Children of this city cannot continue

4630
03:44:08.315 --> 03:44:12.035
to rely on inadequate bus transportation to get

4631
03:44:12.035 --> 03:44:13.515
to far away schools, just

4632
03:44:13.515 --> 03:44:15.995
because their own neighborhood school is inaccessible.

4633
03:44:17.215 --> 03:44:19.495
OMB and school construction authority

4634
03:44:20.395 --> 03:44:22.655
and DOE need to work together to come up

4635
03:44:22.655 --> 03:44:25.815
with the additional 450 million million

4636
03:44:25.815 --> 03:44:28.535
that advocates have been asking for for this school year,

4637
03:44:29.115 --> 03:44:31.615
for improving school accessibility.

4638
03:44:32.145 --> 03:44:33.145
Thank you.

4639
03:44:34.725 --> 03:44:37.045
Great. Well, thank you.

4640
03:44:37.165 --> 03:44:38.925
I want to thank all of you before I, um,

4641
03:44:39.495 --> 03:44:42.645
bring down the gavel on tonight's meeting and announce that.

4642
03:44:43.665 --> 03:44:46.845
And, um, Wednesday, November 20th, we'll meet again

4643
03:44:46.845 --> 03:44:48.805
and do this all over again at the Michael Petrie School.

4644
03:44:49.505 --> 03:44:53.365
Um, I did want to thank also, uh, make note of a few things.

4645
03:44:54.025 --> 03:44:56.605
One, and some of the things we referenced tonight really

4646
03:44:56.605 --> 03:44:58.685
involve policy and you, I think you referenced some things

4647
03:44:58.685 --> 03:45:01.245
that involve state policy and the need to lobby.

4648
03:45:01.385 --> 03:45:05.685
So, um, I will be, um, appointing a committee

4649
03:45:05.865 --> 03:45:10.005
to address some of these things to do with, um, legislation

4650
03:45:10.505 --> 03:45:14.645
and policy and to create a sort of an agenda of things that,

4651
03:45:14.645 --> 03:45:16.325
that the count that the, that we

4652
03:45:16.745 --> 03:45:18.245
as a panel field would be important.

4653
03:45:18.665 --> 03:45:21.045
So there are a number of issues that really we keep butting

4654
03:45:21.045 --> 03:45:23.725
our heads and we keep hearing this as a state mandate.

4655
03:45:23.835 --> 03:45:25.365
This is a state requirement

4656
03:45:25.825 --> 03:45:28.165
and, uh, yet our voice is not often heard in

4657
03:45:28.165 --> 03:45:29.285
these state conversations.

4658
03:45:29.945 --> 03:45:31.445
So we'll be, uh, working on,

4659
03:45:31.445 --> 03:45:33.085
I've drafted something, I'll send that out.

4660
03:45:33.425 --> 03:45:35.605
But Pam Imma, uh, offer a comment

4661
03:45:36.185 --> 03:45:37.885
and we'll be moving forward with a committee

4662
03:45:37.885 --> 03:45:40.485
that actually will do something around that, um,

4663
03:45:40.675 --> 03:45:42.445
legislative affairs and policy

4664
03:45:43.025 --> 03:45:44.285
and really do something so

4665
03:45:44.285 --> 03:45:46.765
that we're engaged in these conversations.

4666
03:45:46.825 --> 03:45:50.045
And so we we're not just constantly coming back and reacting

4667
03:45:50.045 --> 03:45:51.365
and saying, well, that's a state rule.

4668
03:45:51.385 --> 03:45:53.085
The state requires us to do these things,

4669
03:45:53.505 --> 03:45:55.085
but we're not in any way having our

4670
03:45:55.085 --> 03:45:56.205
voices heard in the state.

4671
03:45:56.785 --> 03:45:58.765
And, um, and so that's something that, um,

4672
03:45:59.145 --> 03:46:01.005
you'll be hearing more about very shortly.

4673
03:46:01.255 --> 03:46:03.485
Chancellor, I definitely wanna thank not only being here,

4674
03:46:03.485 --> 03:46:05.605
but staying for the entire meeting.

4675
03:46:06.345 --> 03:46:09.805
Um, you know, I feel that's like an inauguration, like,

4676
03:46:09.805 --> 03:46:11.245
you know, right there with us.

4677
03:46:11.305 --> 03:46:14.125
So I mean that, that means a lot sometimes

4678
03:46:17.235 --> 03:46:20.815
and leader and leadership and, um, you know, it means a lot.

4679
03:46:20.815 --> 03:46:22.815
And I want people to know that it,

4680
03:46:22.815 --> 03:46:25.335
that it doesn't go unnoticed when people go out,

4681
03:46:25.335 --> 03:46:26.775
when they do those types of things.

4682
03:46:27.355 --> 03:46:29.775
On a personal level, there were two items on the agenda

4683
03:46:29.885 --> 03:46:32.935
scheduled, um, uh, eight, um, eight 20,

4684
03:46:32.995 --> 03:46:34.935
and also the specialized high school exam.

4685
03:46:35.315 --> 03:46:38.615
And when I started hearing concerns, I approached the, uh,

4686
03:46:38.865 --> 03:46:41.255
chancellor and I said, look, can we postpone this?

4687
03:46:41.275 --> 03:46:44.455
Can we put some time to get to have more conversation?

4688
03:46:45.035 --> 03:46:47.415
And they were very receptive to that.

4689
03:46:47.675 --> 03:46:51.415
Um, you know, um, and, and so that also is appreciated.

4690
03:46:51.755 --> 03:46:54.015
So, so I think that we're, you know, there are a lot

4691
03:46:54.015 --> 03:46:55.535
of challenges that we have in front of us,

4692
03:46:55.875 --> 03:46:58.295
but I think we also should be mindful of the opportunities

4693
03:46:58.965 --> 03:46:59.975
that we have in front of us.

4694
03:47:00.035 --> 03:47:01.575
We have a lot of great opportunities.

4695
03:47:02.035 --> 03:47:05.135
We may not all view the same way as to how to get

4696
03:47:05.515 --> 03:47:06.575
to accomplish these things,

4697
03:47:06.955 --> 03:47:09.095
but I think we're all headed in the same direction.

4698
03:47:09.115 --> 03:47:11.855
We all wanna achieve some of the same kinds of things.

4699
03:47:12.395 --> 03:47:14.655
So with that, um, let's keep that,

4700
03:47:14.705 --> 03:47:15.935
let's leave with a positive focus.

4701
03:47:15.985 --> 03:47:18.015
We're, we're on the move, we're gonna do some great things.

4702
03:47:18.795 --> 03:47:19.795
Uh, yes.

4703
03:47:20.555 --> 03:47:23.375
Can we get an update on the Citywide Safety Committee?

4704
03:47:23.435 --> 03:47:24.655
We did ask last month.

4705
03:47:24.815 --> 03:47:27.015
I haven't heard anything since the last part meeting,

4706
03:47:27.155 --> 03:47:28.175
so I just wanna say that

4707
03:47:28.175 --> 03:47:29.935
Before I will make sure that we get an update.

4708
03:47:30.115 --> 03:47:31.655
Um, you know, gimme a few days

4709
03:47:31.655 --> 03:47:33.015
and I'll make sure we get an update on that.

4710
03:47:33.555 --> 03:47:35.855
Um, so again, thank you all

4711
03:47:35.855 --> 03:47:37.255
for coming out, thank members of the public.

4712
03:47:37.675 --> 03:47:38.895
And with that, we'll see everybody

4713
03:47:38.925 --> 03:47:40.215
next month in Staten Island.

4714
03:47:40.245 --> 03:47:41.815
With that, this meeting is adjourned.

4715
03:47:42.615 --> 03:47:43.055
I hollow.'''

format_subtitles(text)