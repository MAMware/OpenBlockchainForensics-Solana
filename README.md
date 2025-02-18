# Open Blockchain Forensics - The $LIBRA case on Solana

Welcome to **OpenBlockchainForensics-Solana**, an open-source, community-driven project dedicated to investigating blockchain activity on the Solana network through rigorous, data-driven forensics. Our initial focus is the $LIBRA token controversy, where insiders reportedly removed millions in liquidity, leading to allegations of fraud and a crash in the token’s value. This project aims to trace these funds, particularly to centralized exchanges (CEXs), to confirm on-chain evidence, quantify off-ramping, and assess the speed of cashouts, providing transparency and accountability.

We are committed to transparency, reproducibility, and collaboration, inviting contributions from affected users, X users, national universities, and the broader blockchain community. Join us in building a standard for blockchain forensics that empowers communities, supports regulatory action, and critically examines narratives to ensure objectivity.

## Table of Contents
1. [Overview](#overview)
2. [Goals](#goals)
3. [Scope](#scope)
4. [Methodology](#methodology)
5. [Setup Instructions](#setup-instructions)
6. [Usage Examples](#usage-examples)
7. [Contribution Guidelines](#contribution-guidelines)
8. [Collaboration with Universities](#collaboration-with-universities)
9. [Community Engagement](#community-engagement)
10. [License](#license)
11. [Disclaimer](#disclaimer)

## Overview

The $LIBRA token, launched on the Solana blockchain and promoted by Argentine President Javier Milei, gained significant attention in February 2025, with its market cap briefly reaching $4.5 billion before plummeting over 94%. Reports indicate that insiders removed millionz in liquidity, primarily in USDC and SOL, from liquidity pools on decentralized exchanges (DEXs) like Meteora and Raydium, fueling allegations of a rug pull or insider manipulation. Blockchain analysis has revealed high concentration, with 90% of the token supply held by just three wallets and 82% unlocked and sellable from the start, raising further concerns about potential fraud.

**OpenBlockchainForensics-Solana** was created to investigate these allegations through transparent, open-source blockchain forensics, focusing on tracing these millions to CEXs to confirm off-ramping and assess rapid cashouts. By open-sourcing our code, data, and findings, we aim to empower affected users, engage the X community, collaborate with national universities, and provide actionable evidence for accountability, while critically examining the narrative to ensure objectivity.

## Goals

Our goals are to:
- **Trace Funds**: Confirm on-chain traces of the millions withdrawn from $LIBRA liquidity pools, tracing USDC and SOL to CEX deposit addresses to quantify off-ramping and identify cashout methods.
- **Assess Rapid Cashouts**: Analyze transaction timestamps to determine the speed of insider cashouts, confirming whether they acted before significant action could be taken, addressing concerns about regulatory lag and market oversight.
- **Ensure Transparency**: Open-source all code, data, and findings, allowing independent verification and reproducibility, building trust with affected users, X users, and the broader community.
- **Foster Collaboration**: Engage national universities, particularly in Argentina, to leverage their compute power, expertise, and outreach, scaling the investigation efficiently and enhancing credibility.
- **Engage the Community**: Involve affected users, X users, and blockchain enthusiasts in the investigation, inviting contributions, feedback, and data submissions to amplify impact and support accountability.
- **Critically Examine Narratives**: Maintain objectivity by seeking concrete evidence of fraud or manipulation, while considering alternative explanations (e.g., market dynamics, legitimate liquidity management), ensuring a balanced view.

## Scope

The initial scope of **OpenBlockchainForensics-Solana** is focused on the $LIBRA token investigation, specifically tracing the millions to CEXs, as this is the most likely off-ramping method based on available reports and evidence of CEX activity. This focused strategy reduces resource demands while producing actionable results, with the option to expand to other strategies (e.g., tracing mixers, cross-chain bridges, P2P/OTC activity) if needed.

Future expansions may include additional Solana-based investigations, leveraging the methodologies and tools developed here to set a standard for blockchain forensics.

## Methodology

Our methodology for tracing the millions to CEXs is structured as follows:

1. **Identify Liquidity Pool Withdrawals**:
   - Locate the $LIBRA liquidity pool addresses on DEXs like Meteora and Raydium using Solscan or Dexscreener.
   - Retrieve withdrawal transactions from these pools within the relevant time frame (e.g., February 14–15, 2025) using the Solana JSON-RPC API or a local node, identifying insider wallets that received USDC and SOL.
   - Start with the eight insider wallets identified by Lookonchain and cross-reference with the three wallets holding 90% of $LIBRA’s supply.

2. **Trace Funds to CEX Deposit Addresses**:
   - Compile a database of known CEX deposit addresses for Solana-based assets (USDC, SOL) from blockchain analytics firms, community sources, or historical on-chain data.
   - Trace USDC and SOL from insider wallets to CEX deposit addresses, using clustering techniques to identify intermediate wallets and quantify off-ramped amounts.
   - Convert amounts to USD using historical price data to estimate the total off-ramped value.

3. **Assess Rapid Cashouts**:
   - Analyze transaction timestamps to determine the speed of withdrawals and CEX deposits, cross-referencing with $LIBRA’s price movements to confirm insiders acted during the peak.
   - Evaluate the lack of immediate oversight in cryptocurrency markets, confirming rapid cashouts before significant action could be taken.

4. **Open-Source Procedures**:
   - Develop and open-source Python scripts for data collection, tracing, and visualization, using tools like `solders`, `pandas`, `networkx`, and `matplotlib`.
   - Publish intermediate datasets and findings, ensuring they are anonymized to comply with privacy standards.

5. **Collaborate and Publish**:
   - Engage national universities to provide compute power, expertise, and outreach, scaling the investigation efficiently.
   - Publish a comprehensive report with visualizations (e.g., transaction graphs, timelines), sharing findings via open-access platforms, X, blockchain communities, and media outlets.

## Setup Instructions

Repository structure
```
OpenBlockchainForensics-Solana/
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
│   ├── data_collection/
│   │   └── collect_transactions.py
│   ├── tracing/
│   │   └── trace_to_cexs.py
│   └── visualization/
│       └── visualize_flows.py
├── docs/
│   └── ... (README.md, contributing guidelines, etc.)
├── tests/
│   └── ... (Tests will go here)
├── requirements.txt
├── LICENSE
└── README.md
```

To set up the environment and run the scripts, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MAMware/OpenBlockchainForensics-Solana.git
   cd OpenBlockchainForensics-Solana
   ```
2. **Install dependencies**:
  - Ensure Python 3.8+ is installed.
  - Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
  - The `requirements.txt` file includes dependencies like `solders`, `pandas`, `networkx`, and `matplotlib`.
3. Set up Solana data access:
  - Obtain access to a Solana RPC node (e.g., via QuickNode, Helius, or a local node) to query transaction data. Update the API endpoint in the scripts as needed.
  - lternatively, use publicly available data from Solscan for initial testing, but note that full-scale analysis requires direct blockchain access.
4. Run scripts, Testing and Expanding
  - See the Usage Examples (#usage-examples) section for instructions on running specific scripts.
  - These scripts are prototypes. You'll need to expand `collect_transactions.py` to actually use the Solana API once you have access. The `solders` library provides a Python interface for Solana's JSON-RPC API.
  - For `trace_to_cexs.py`, you'll need to read real CEX addresses from a CSV or another data source rather than using the mock function.
  - For `visualize_flows.py`, you might want to enhance the visualization further, perhaps by color-coding nodes based on transaction types or token types.
5. Commit and Push
   - Add these files to your repository
  ```bash
git add scripts/data_collection/collect_transactions.py
git add scripts/tracing/trace_to_cexs.py
git add scripts/visualization/visualize_flows.py
git commit -m "Added initial prototype scripts for data collection, tracing, and visualization"
git push origin main
```
Remember, these are placeholders, so once you have access to real Solana data, you'll need to replace the mock functions with actual API calls using the solders library or similar tools.

## Usage Examples
Below are examples of how to use the scripts in the repository. Note that these are placeholders, as the scripts are under development. Contributions are welcome to implement and expand these functionalities.

1. Collect transactional data:
  - Script: `scripts/data_collection/collect_transactions.py`
  - Purpose: Query Solana transaction data for $LIBRA liquidity pool withdrawals.
  - Example:
  ```bash
python scripts/data_collection/collect_transactions.py --pool-address [POOL_ADDRESS] --start-date 2025-02-14 --end-date 2025-02-15 --output data/raw/transactions.json
  ```   
  - Output: A JSON file in `data/raw/` containing raw transaction data.
2. Trace funds to CEXs:
  - Script: `scripts/tracing/trace_to_cexs.pyscripts/tracing/trace_to_cexs.py`
  - Purpose: Trace USDC and SOL from insider wallets to CEX deposit addresses.
  - Example:
   ```bash
python scripts/tracing/trace_to_cexs.py --input data/raw/transactions.json --cex-addresses data/cex_addresses.csv --output data/processed/cex_traces.csv
  ```
3. Visualize transaction flows
   - Script: `scripts/visualization/visualize_flows.py`
   - Purpose: Generate a transaction graph showing flows to CEXs.
   - Example_
   ```bash
   python scripts/visualization/visualize_flows.py --input data/processed/cex_traces.csv --output docs/transaction_graph.png
   ```
   - Output: A PNG file in `docs/` visualizing transaction flows.

## Contribution Guidelines
We welcome contributions from the community, including affected users, X users, developers, data scientists, and blockchain enthusiasts. To contribute, please follow these guidelines:
   
1. Fork and Clone:
   - Fork the repository to your GitHub account and clone it locally:
   ```bash
   git clone https://github.com/MAMware/OpenBlockchainForensics-Solana.git
   ```
2. Create a branch
   - Create a new branch for your changes:
   ```bash
   git checkout -b feature/[your-feature-name]
   ```
3. Make changes
   - Implement your changes, ensuring code quality, documentation, and adherence to the project’s scope.
   - Add unit tests in the `tests/` directory to validate your changes
4. Submit a Pull Request
   - Push your changes to your fork and submit a pull request to the main repository, describing your changes and their purpose.
   - Pull requests require at least one approval from a core contributor to be merged.
5. Follow the Code of Conduct:
   - Adhere to the project’s Code of Conduct (CODE_OF_CONDUCT.md) to ensure respectful, professional interactions.
For more details, see the CONTRIBUTING.md file.

   ## Collaboration with Universities
   We are actively seeking collaboration with national universities, particularly in Argentina, to leverage their resources and expertise in scaling the investigation. Universities can contribute in the following ways:
   - Compute Resources: Provide access to high-performance computing (HPC) clusters or cloud credits to process large volumes of Solana transaction data, especially for tracing and clustering wallets.
   - Expertise: Engage computer science, data science, or blockchain research departments to help develop, audit, and enhance the tracing scripts, ensuring robustness and accuracy.
   - Outreach: Use university networks to promote the project to affected users, the X community, and the broader public, emphasizing its transparency and open-source nature.

  To collaborate, plase submit an issue on GitHub with your proposal. See our project proposal (docs/project_proposal.md) for more details on how universities can get involved.
  ## Community Engagement    
  We invite the community, including affected users, X users, and blockchain enthusiasts, to engage with the project in the following ways:
  - Feedback: Share feedback, suggestions, or questions via GitHub issues or by tagging us on X with #OpenBlockchainForensics.
  - Data Submissions: Affected users are encouraged to submit their Solana wallet addresses (public keys) to help quantify losses and trace fund flows. Never share your private key or seed phrase with anyone, as this could result in the loss of your funds. See the data submission guide (docs/data_submission.md) for instructions.
  - Contributions: Contribute code, data, documentation, or visualizations by following the Contribution Guidelines (#contribution-guidelines).
  - Promotion: Share the project on X, blockchain forums, Reddit, and other platforms to increase visibility and impact, especially in Argentina, where the $LIBRA issue has significant social and political implications.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer
OpenBlockchainForensics-Solana is a community-driven effort to investigate blockchain activity through transparent, open-source forensics. It is not a formal legal or regulatory action, and its findings do not constitute legal advice or definitive proof of wrongdoing. All data published in this repository is anonymized to comply with privacy standards, and users are responsible for ensuring their own compliance with applicable laws and regulations.

The $LIBRA token’s crash may not solely be due to insider malfeasance. Market dynamics, such as speculative trading, panic selling, or external market conditions, could also play a role. This investigation seeks concrete evidence of fraud or manipulation, while remaining open to alternative explanations, ensuring a balanced and objective view.

## This project was co-created with the help of xAI.com Grok 2. 
