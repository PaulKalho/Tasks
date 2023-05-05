export class Model {
  constructor(model, listName, objectName, baseUrl, api) {
    this.model = model;
    this.listName = listName;
    this.objectName = objectName;
    this.url = baseUrl;
    this.api = api;
  }

  async getAll() {
    await this.api
      .get(this.url)
      .then((response) => {
        this.model[this.listName] = response;
      })
      .catch((err) => {
        return err;
      });
  }

  getBy() {
    //   this.api.post(url)
  }

  updateBy() {}
}
