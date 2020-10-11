FROM python:3.8.3

LABEL maintainer "Masanari Kondo <m-kondo@se.is.kit.ac.jp>"

WORKDIR /home/work_dir

# install lscp
RUN apt-get update -y \
    && apt-get install -y git \
    && apt-get install -y software-properties-common \
    && apt-get install -y sudo \
    && apt-get install -y cpanminus \
    && cpanm File::Basename \
    && cpanm File::Find \
    && cpanm File::Slurp \
    && cpanm Lingua::Stem \
    && cpanm FindBin \
    && cpanm Log::Log4perl \
    && cpanm Test::Files \
    && cpanm Regexp::Common \
    && cpanm Exporter \
    && git clone --depth=1 https://github.com/doofuslarge/lscp.git \
    && cd lscp \
    && perl Makefile.PL \
    && make \
    && make test \
    && sudo make install



ENTRYPOINT ["/usr/bin/python3"]
CMD ["/home/work_dir/lscp_templates/exp_lscp.py"]

