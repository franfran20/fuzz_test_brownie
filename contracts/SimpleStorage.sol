// SPDX-License-Identifier: MIT

pragma solidity 0.8.7;

contract SimpleStorage {
    mapping(address => uint256) public userToNumber;

    function storeYourNumber(uint256 _number) public {
        userToNumber[msg.sender] = _number;
    }

    function retrieveYourNumber(address _user) public view returns (uint256) {
        return userToNumber[_user];
    }
}
