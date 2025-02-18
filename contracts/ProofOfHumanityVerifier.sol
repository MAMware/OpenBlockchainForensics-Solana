// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IProofOfHumanity {
    function isRegistered(address _submissionID) external view returns (bool);
}

contract ProofOfHumanityVerifier {
    address public pohContract;

    constructor(address _pohContract) {
        pohContract = _pohContract;
    }

    function verifyHumanity(address user) external view returns (bool) {
        IProofOfHumanity poh = IProofOfHumanity(pohContract);
        return poh.isRegistered(user);
    }
}
