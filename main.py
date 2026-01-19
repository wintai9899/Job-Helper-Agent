from langchain_core.messages import HumanMessage
from agent.graph import react_graph

messages = [HumanMessage(content="""
                         
        Can you take a look at my CV ath the location 'data/WintaiChanResume_UK.pdf'  and these 3 job applications and tell me whichone is the most suitable for my expiriance: 
        
        'https://www.indeed.com/viewjob?jk=247e94f9a28c544f&tk=1isdf5na1h72t810&from=serp&vjs=3',
        'https://www.indeed.com/viewjob?jk=744686732444f370&tk=1isns1midj72r8b4&from=serp&vjs=3',
        'https://www.indeed.com/viewjob?jk=01e2f371f220e42a&tk=1isns1midj72r8b4&from=serp&vjs=3'
        
        """
        )]
result = react_graph.invoke({"message": messages})

for m in result['messages']:
    m.pretty_print()