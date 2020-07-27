import axios, { AxiosInstance } from 'axios';

export class Api {
  private axios: AxiosInstance;
  constructor() {
    this.axios = axios.create({
      headers: {
        common: {
          Accept: "application/json"
        }
      },
      baseURL: "http://localhost:4002"
    });
  }

  async postUserInfo(idToken: string) {
    const { data } = await this.axios.post("/", {
      idToken: idToken,
    });
    return data.message;
  }
}

export default new Api();
