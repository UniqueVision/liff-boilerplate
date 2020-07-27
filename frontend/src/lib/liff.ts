import liff from "@line/liff";

export class Liff {
  async init(liffId: string): Promise<boolean> {
    try {
      await liff.init({
        liffId: liffId
      })
      return true;
    } catch {
      return false;
    }
  }

  login() {
    liff.login();
  }

  isInClient() {
    return liff.isInClient();
  }

  isLoggedIn() {
    return liff.isLoggedIn();
  }

  idToken(): string {
    return liff.getIDToken() || '';
  }
}

export default new Liff();
