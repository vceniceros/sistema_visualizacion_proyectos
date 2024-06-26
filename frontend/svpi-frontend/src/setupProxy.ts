import { createProxyMiddleware } from 'http-proxy-middleware';

module.exports = function(app: any) {
  app.use(
    '/proyectos',
    createProxyMiddleware({
      target: 'http://127.0.0.1:5000',
      changeOrigin: true,
    })
  );
};
