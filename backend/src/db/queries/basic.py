from neo4j import GraphDatabase

uri = "neo4j+s://2c828a38.databases.neo4j.io"
driver = GraphDatabase.driver(uri, auth=("neo4j", "17rbkP6xuQb_0t-kfJF_F4OH26a4iJ51Gren88t0aSU"))

def get_friends_of(tx, name):
    friends = []
    result = tx.run("""match p=(a:Person)-[]->(b:Person)
                        unwind nodes(p) as n unwind relationships(p) as r
                        with collect( distinct {id: ID( n),
                        label:labels(n), name: n.FirstNname,
                        gender:n.Gender, title:n.title,
                        url:n.img_url}) as nl,
                        collect( distinct {source: ID(startnode(r)), target: ID(endnode(r))}) as rl
                        RETURN {nodes: nl, links: rl}""")
    # result = tx.run(""" MATCH (tom {name: "Tom Hanks"}) RETURN tom""")
    print(result)
    for record in result:
        friends.append(record.data())
    return friends

def get_basic():
    with driver.session() as session:
        result = session.read_transaction(get_friends_of, "Alice")
        print(result)
    return result[0]['{nodes: nl, links: rl}']
