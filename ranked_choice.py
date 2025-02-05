# It's election season!  And world series time!  Let's help a fictional town,
# Diamond City, elect their next mayor.  We have four candidates running for the
# honor of serving:
# - Derek Jeter
# - Shohei Ohtani
# - Barry Bonds
# - Ricky Henderson
#
# We're helping the city implement a system to count votes.  This city uses
# ranked choice voting.  You have the beginnings of an application for this from
# a team member, your first job is to finish counting the votes.
#
# There are no restrictions on tools - use anything you want, including LLMs.


candidates = ["Barry Bonds", "Shohei Ohtani", "Derek Jeter", "Ricky Henderson"]


def parse_votes(vote_data):
    votes = []
    vote_data_lines = vote_data.split()
    for line in vote_data_lines:
        vote = line.split(";")
        vote = [name for name in vote if name in candidates]
        votes.append(vote)
    return votes


def tabulate_results(votes):
    pass
    # set up hashmap with name and corresponding votes
    # to optimize use a second array where the index correlates to a canidate



def main():
   
    votes_data = """
        Ohtani,Jeter,Henderson,Bonds
        Bonds,Ohtani,Jeter,Henderson
        Jeter,Ohtani,Bonds,Henderson
        Henderson,Bonds,Ohtani,Jeter
        Ohtani,Jeter,Henderson,Bonds
        Jeter,Henderson,Bonds,Ohtani
        Jeter,Ohtani,Henderson,Bonds
        Ohtani,Jeter,Henderson,Bonds
        Jeter,Ohtani,Henderson,Bonds
        Ohtani,Jeter,Henderson,Bonds
        Ohtani,Jeter,Henderson,Ohtani
        Jeter,Ohtani,Henderson,Bonds
        Jeter,Henderson,Bonds,Ohtani
        Henderson,Bonds,Ohtani,Jeter
        Jeter,Henderson,Bonds,Ohtani
        Ohtani,Jeter,Henderson ,Bonds
        Jeter,Henderson,Bonds,Ohtani
        Jeter,Ohtani,Henderson,Bonds
        Jeter,Ohtani,Bonds,Henderson
        Jeter,Ohtani,Bonds,Henderson
        """
    votes = parse_votes(votes_data)
    print(votes)
    # Tabulate the results
    tabulate_results(votes)


if __name__ == "__main__":
    main()