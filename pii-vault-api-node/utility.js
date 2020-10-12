var axios = require("axios");

class UtilityClass {
  static RequestApiToken = async () => {
    let tokenRequest = await axios.post(
      "https://api.piivault.com/api/auth/login",
      {
        AccountId: process.env["ACCOUNT_ID"],
        ApiKey: process.env["API_KEY"],
      }
    );

    let tokenResponse = tokenRequest.data;

    if (tokenResponse.Success) {
      return tokenResponse.Data.Token;
    } else {
      console.log(`Error Status = ${tokenResponse.Error.Status}\n`);
      console.log(`Error Message = ${tokenResponse.Error.Message}\n`);
      return "";
    }
  };

  static GetSinglePerson = () => {
    return {
      Index: 0,
      SourceSystemKey: "12345",
      FirstName: "Rick",
      MiddleName: "",
      LastName: "Sanchez",
      DateOfBirth: "1980-10-10T01:00:00.000Z",
      Gender: "M",
      IsForgotten: 0,
      Emails: [{ EmailAddress: "rick.sanchez@all.com" }],
      Phones: [
        {
          PhoneType: "Mobile",
          PhoneOwner: "SSA",
          PhoneNumber: "123-456-7890",
        },
      ],
      Addresses: [
        {
          AddressType: "Home",
          StreetAddress1: "123 Anywhere Lane",
          StreetAddress2: "",
          City: "Anytown USA",
          State: "NY",
          Zip: "10001",
        },
      ],
      Keys: [
        {
          KeyType: "SSN",
          KeyOwner: "SSA",
          KeyValue: "123-45-6789",
        },
      ],
    };
  };

  static GetPeople = () => {
    var person_0 = {
      Index: 0,
      SourceSystemKey: "12345",
      FirstName: "Rick",
      MiddleName: "",
      LastName: "Sanchez",
      DateOfBirth: "1980-10-10T01:00:00.000Z",
      Gender: "M",
      IsForgotten: 0,
      Emails: [{ EmailAddress: "rick.sanchez@all.com" }],
      Phones: [
        {
          PhoneType: "Mobile",
          PhoneOwner: "SSA",
          PhoneNumber: "123-456-7890",
        },
      ],
      Addresses: [
        {
          AddressType: "Home",
          StreetAddress1: "123 Anywhere Lane",
          StreetAddress2: "",
          City: "Anytown USA",
          State: "NY",
          Zip: "10001",
        },
      ],
      Keys: [
        {
          KeyType: "SSN",
          KeyOwner: "SSA",
          KeyValue: "123-45-6789",
        },
      ],
    };

    var person_1 = {
      Index: 1,
      SourceSystemKey: "67890",
      FirstName: "Morty",
      MiddleName: "",
      LastName: "Smith",
      DateOfBirth: "1999-07-30T01:00:00.000Z",
      Gender: "M",
      IsForgotten: 0,
      Emails: [{ EmailAddress: "morty.smith@all.com" }],
      Phones: [
        {
          PhoneType: "Landline",
          PhoneOwner: "SSA",
          PhoneNumber: "987-605-4321",
        },
      ],
      Addresses: [
        {
          AddressType: "Home",
          StreetAddress1: "456 Everywhere Circle",
          StreetAddress2: "",
          City: "Anytown USA",
          State: "NY",
          Zip: "10001",
        },
      ],
      Keys: [
        {
          KeyType: "SSN",
          KeyOwner: "SSA",
          KeyValue: "987-65-4321",
        },
      ],
    };

    var person_2 = {
      Index: 2,
      SourceSystemKey: "84292",
      FirstName: "Lars",
      MiddleName: "",
      LastName: "Peters",
      DateOfBirth: "1985-11-15T01:00:00.000Z",
      Gender: "M",
      IsForgotten: 0,
      Emails: [{ EmailAddress: "lars.peters@all.com" }],
      Phones: [
        {
          PhoneType: "Jupiter",
          PhoneOwner: "SSA",
          PhoneNumber: "+31 902377345",
        },
      ],
      Addresses: [
        {
          AddressType: "HQ",
          StreetAddress1: "789 Nowhere Ave",
          StreetAddress2: "",
          City: "Anytown USA",
          State: "NY",
          Zip: "10001",
        },
      ],
      Keys: [
        {
          KeyType: "SSN",
          KeyOwner: "SSA",
          KeyValue: "826-01-1495",
        },
      ],
    };

    return [person_0, person_1, person_2];
  };
}

module.exports = UtilityClass;
