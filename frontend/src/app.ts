import 'bootstrap';

declare global {
  function dashboard(url:string): void;
}

// テスト用dashboard
global.dashboard = (url: string) => {
  window.location.href = url;
};
