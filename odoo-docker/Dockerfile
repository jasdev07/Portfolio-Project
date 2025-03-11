FROM odoo:17.0

USER root

# Comprehensive Python dependencies for Odoo addons
RUN pip install --upgrade pip && \
    pip install pandas \
                countryinfo \
                httpx==0.27.2 \
                xlsxwriter \
                icecream==2.1.3 \
                httpagentparser==1.9.5 \
                user-agents==2.2.0 \
                pylightxl==1.61 \
                beautifulsoup4 \
                requests \
                openpyxl \
                numpy \
                python-dateutil \
                phonenumbers \
                psycopg2-binary \
                qrcode \
                urllib3 \
                passlib \
                pytz \
                lxml \
                xmltodict \
                decorator \
                cryptography

USER odoo