var express = require("express");
var axios = require("axios");
var router = express.Router();
var UtilityClass = require("../utility");

// Perform a base request for token
router.get("/", async (req, res) => {
  res.write("Performing a base API Authentication Call\n\n");

  // Perform the request
  let token = await UtilityClass.RequestApiToken();

  res.write("Token call success\n");
  res.write(`API Bearer Token = ${token}`);

  res.end();
});

// Perform GetPolyId
router.get("/get-poly-id", async (req, res) => {
  res.write("Performing GetPolyId\n");

  // Perform the request to get the token
  let person = UtilityClass.GetSinglePerson();

  let token = await UtilityClass.RequestApiToken();

  let polyIdRequest = await axios.put(
    "https://api.piivault.com/api/profiles/GetPolyId",
    UtilityClass.GetSinglePerson(),
    { headers: { Authorization: `Bearer ${token}` } }
  );

  let polyIdResponse = polyIdRequest.data;

  if (polyIdResponse.Success) {
    res.write(
      `Get Poly Id For ${person.FirstName} ${person.LastName} is successful. ID = ${polyIdResponse.Data}\n`
    );
  } else {
    res.write("Get Poly Id error\n");
    res.write(`Error Status = ${polyIdResponse.Error.Status}\n`);
    res.write(`Error Message = ${polyIdResponse.Error.Message}\n`);
  }

  res.end();
});

// Perform GetPolyIdBulk
router.get("/get-poly-id-bulk", async (req, res) => {
  res.write("Performing GetPolyIdBulk\n");

  // Perform the request to get the token
  let token = await UtilityClass.RequestApiToken();

  let polyIdBulkRequest = await axios.put(
    "https://api.piivault.com/api/profiles/GetPolyIdBulk",
    { Profiles: UtilityClass.GetPeople() },
    { headers: { Authorization: `Bearer ${token}` } }
  );

  let polyIdBulkResponse = polyIdBulkRequest.data;

  if (polyIdBulkResponse.Success) {
    res.write("Get Poly Id Bulk For is successful\n\n");

    polyIdBulkResponse.Data.Responses.forEach((polyIdResponse) => {
      res.write(
        `Index ${polyIdResponse.Index} with System Source Key of '${polyIdResponse.SourceSystemKey}' Poly ID = ${polyIdResponse.PolyId}\n\n`
      );
    });
  } else {
    res.write("Get Poly Id error\n");
    res.write(`Error Status = ${polyIdBulkResponse.Error.Status}\n`);
    res.write(`Error Message = ${polyIdBulkResponse.Error.Message}\n`);
  }

  res.end();
});

module.exports = router;
