// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract WalletCollector {
    address public owner;
    mapping(address => string) public solanaWallets;

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function submitWallet(string memory solanaWallet) external {
        solanaWallets[msg.sender] = solanaWallet;
    }

    function getWallet(address user) external view returns (string memory) {
        return solanaWallets
