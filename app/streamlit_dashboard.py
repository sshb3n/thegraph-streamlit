import streamlit as st
import os
import requests

st.title("The Graph Dashboard")

# Function to use requests.post to make an API call to the subgraph url
def run_query(q):
    # endpoint where you are making the request
    request = requests.post(f"https://gateway-arbitrum.network.thegraph.com/api/{os.getenv('THE_GRAPH')}/subgraphs/id/HUZDsRpEVP2AvzDCyzDHtdc64dyDxx8FQjzsmqSg4H3B",
                            json={'query': q})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f'Query failed. Return code is {request.status_code}. {q}')

# The Graph query - Query for current ETH price
query = """
{
  bundles(first: 1) {
    ethPriceUSD
  }
}
"""
result = run_query(query)

# Display the current ETH price
st.success(f'Current ETH price is {result["data"]["bundles"][0]["ethPriceUSD"]}')