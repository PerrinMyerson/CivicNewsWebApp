from openai import OpenAI
import time
api_key = "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"
client = OpenAI(api_key = api_key)

my_assistant = client.beta.assistants.retrieve("asst_H1nqDGtG39tEZ7OqIJthaB1g")
# print(my_assistant)
article ='''
Every year, more special education teachers quit than graduate from the nation’s teacher preparation programs, even as the number of students diagnosed with disabilities keeps rising.

Without enough qualified teachers and therapists, students don’t always get the help they need to be successful in school. Shortages also contribute to serious situations where kids are locked in small rooms, teachers physically hold down students, or children disrupt their classmates’ learning because they haven’t learned how to regulate their own behavior.

There was broad agreement that special education staffing shortages are a dire problem at a public briefing held by the U.S. Commission on Civil Rights on Friday. But there were widely divergent ideas about how to solve the issue and what role the federal government should play.

Some educators and experts said the solution is for the federal government to fulfill its decades-old pledge to cover more of the costs of special education. In their eyes, the Education Department should be flooding the special educator pipeline and offering training to all teachers to better support students with disabilities.

Others said it’s about incentivizing the job, and that special education teachers should be paid more than their colleagues and offered retention bonuses. Still others said that states should ease licensing rules and expand private school voucher programs to give desperate families more options.

The briefing, meant to inform the president and Congress, was held as President-elect Trump prepares to start his second term in office. Trump has vowed to expand school choice and dramatically scale back the federal role in education — a move panelists said could affect students with disabilities a lot or a little, depending on how the plan is executed.

The briefing did not include testimony from the U.S. Department of Education, which Trump has said he would abolish. Stephen Gilchrist, the Republican Trump-appointed commissioner who called for the briefing, said the department’s absence was “unconscionable.” An Education Department spokesperson said scheduling conflicts prevented the agency from being there in person, but it would send written responses.

The debate comes as the number of students with disabilities is growing. Some 7.5 million students required special education services as of the 2022-23 school year, the latest federal data shows, or around 15% of students. That was up from 7.1 million or 14% of students in the 2018-19 school year, just before the pandemic hit.

It’s unclear if the rise is due to schools getting better at identifying students with disabilities or if more children have needs now. Many young children missed early intervention and early special education services during the pandemic, and many educators say they are seeing higher behavioral needs and wider academic gaps in their classrooms.

Become a Chalkbeat sponsor

“Students are arriving in our classrooms with a high level of dysregulation, which is displayed through their fight, flight, or freeze responses,” Tiffany Anderson, the superintendent of Topeka, Kansas’ public schools, wrote in her statement. “Students are also displaying more physically aggressive behavior.”

All of that has trickle-down effects. When kids disengage or act out, schools often remove them from class, said Dan Stewart, the managing attorney for education and employment at the National Disability Rights Network. That could be a suspension or something more informal, like cutting a child’s day short. Then the burden of providing educational support falls on families, said Ariel Simms, the president of Disability Belongs, a nonprofit that advocates on behalf of people with disabilities.

“Parents and caregivers have had to step in to fill gaps in areas like tutoring, therapy, and learning accommodations, resulting in heightened stress and financial strain,” Simms told the commission in her statement.

Why special education teachers are in short supply
There are many reasons for the shortages. While the number of special education teachers has risen over the past two decades, the demand still outpaces the supply, writes Chad Aldeman, who researches teacher labor markets. Around 16,000 more special education teachers leave public schools each year than teacher prep programs train to replace them.

Special education teachers are more likely to change jobs or quit teaching than their general education colleagues. On top of that, many districts struggle to hire and keep paraprofessionals, whose crucial but low-paid work helps teachers meet the needs of students with disabilities. All of that increases workloads and contributes to burnout.

To get by, many schools increase class sizes or rely on substitutes and emergency credentialed teachers who often lack the proper training to work with students with disabilities.

“We had to hire virtual teachers and those on special visas, which complicated matters for our special needs students who were already facing academic and social challenges,” Karen Lockerman, a special education teacher in rural South Carolina, told the commission of how her district handled pandemic staffing shortages. “Language barriers and virtual instruction added further difficulties to their learning.”

Some say more funding; others want voucher expansion
To some advocates, the solution is obvious: The federal government needs to pay a bigger share of schools’ special education costs. Back in 1975, when federal lawmakers passed what would become the Individuals with Disabilities Education Act, they said the government would cover 40%.

But “actual federal funding for IDEA has never come close to that and is usually well below half of this ‘full funding’ amount,” Jessica Levin, the litigation director at the nonprofit Education Law Center, told the commission. Without adequate funding, Levin said, “it is impossible to meet the educational needs and legal rights of students with disabilities, including ensuring there are sufficient numbers of qualified teachers.”

Anderson said that underfunding means her district has to pull money from the general education budget to cover the costs of educating kids with disabilities. Kansas gave schools an extra $75 million to pay for special education this year, but there aren’t any plans to keep that up as of now. Federal pandemic aid that helped is about to expire.

Become a Chalkbeat sponsor

The federal government and states also could do more to knock down financial barriers to becoming a special education teacher, said Julian Vasquez Heilig, the director of the Network for Public Education, an advocacy group, by offering more scholarships, stipends, and loan forgiveness. Investing in the expansion of “grow your own” initiatives, which often produce too few teachers to change overall staffing levels, could also help.

Jonathan Butcher, a senior research fellow at the Heritage Foundation, a conservative think tank, said the federal government could elevate examples of states like Indiana, which created a program that pays for licensed teachers to go back to school to get their special education license and condenses their coursework. The pandemic aid-backed program has produced over 600 licensed special education teachers since 2021 and has become a go-to strategy for some districts to fill vacancies.

In Topeka, Anderson has tried recruiting paraprofessionals, career changers, and international teachers. Through a state program, parents who hadn’t gone to college or worked in a classroom before got on-the-job training from experienced teachers. Still, all of that effort hasn’t really made a dent.

“These programs have given us additional alternative pathways; however, the shortage is so significant, it has not eliminated the need and the crisis school districts like Topeka Public Schools continue to face,” Anderson told the commission.

Butcher, of the Heritage Foundation, also floated another idea: changing federal law so that families can take the portion of IDEA funding that would normally go to their child at a public school and use it however they see fit — an idea that’s similar to creating a national voucher program for students with disabilities.

“By making IDEA ‘portable,’ families could purchase services from education therapists, private school tuition, or other education products that fit their child’s needs,” Butcher told the commission in his statement. “This policy would help alleviate the pressure on public school officials to find special education personnel while also giving families private education choices when frustrating legal battles with school districts prevent students from receiving the services they require.”

Many advocates for students with disabilities worry such an idea would strip kids of their right to a free and appropriate education, as families typically have to waive that right to participate in a private school voucher program at the state level.

The idea would require action by Congress and buy-in from Trump. Still, some are taking Butcher’s proposal seriously, as the Heritage Foundation published Project 2025, a policy playbook written by several former Trump White House officials. That plan calls for turning most funding for special education into block grants that states would control.

'''
thread = client.beta.threads.create()
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content=article
)
run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id=my_assistant.id,
  instructions="Generate the neccesary SEO information for the provided article"
)
while run.status != 'completed':
    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        print(messages)
    
    else:
        print(run.status)
        print (run)
        time.sleep(1)


thread_messages = client.beta.threads.messages.list(thread.id)
print(thread_messages)