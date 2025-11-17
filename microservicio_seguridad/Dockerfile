# Imagen base con Apache
FROM php:8.2-apache

# Instalar dependencias del sistema y extensiones necesarias
RUN apt-get update && apt-get install -y \
    git curl unzip libpng-dev libjpeg-dev libonig-dev libxml2-dev zip \
    nano \
    && docker-php-ext-install pdo_mysql mbstring exif pcntl bcmath gd

# Instalar Composer
RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer

# Habilitar mod_rewrite
RUN a2enmod rewrite

# Configurar Apache para permitir .htaccess
RUN echo '<Directory /var/www/html>\n\
    AllowOverride All\n\
</Directory>' > /etc/apache2/conf-available/laravel.conf \
    && a2enconf laravel

# Establecer directorio de trabajo
WORKDIR /var/www/html/microservicio_seguridad

# COPIAR tu proyecto local al contenedor
# COPY ./microservicio_seguridad /var/www/html/microservicio_seguridad
RUN chown -R www-data:www-data /var/www/html/microservicio_seguridad \
    && chmod -R 775 /var/www/html/microservicio_seguridad/storage \
    && chmod -R 775 /var/www/html/microservicio_seguridad/bootstrap/cache
# Instalar dependencias de Laravel
#RUN composer install --no-interaction --prefer-dist --no-scripts \
 #   && chown -R www-data:www-data /var/www/html \
 #   && chmod -R 775 storage bootstrap/cache

# Exponer puerto
EXPOSE 80

CMD ["apache2-foreground"]
