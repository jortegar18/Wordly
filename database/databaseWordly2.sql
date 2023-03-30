PGDMP         -                {            postgres    15.2    15.2 &    5           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            6           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            7           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            8           1262    5    postgres    DATABASE     ~   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Colombia.1252';
    DROP DATABASE postgres;
                postgres    false            9           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    3384                        3079    16384 	   adminpack 	   EXTENSION     A   CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;
    DROP EXTENSION adminpack;
                   false            :           0    0    EXTENSION adminpack    COMMENT     M   COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';
                        false    2            �            1259    16428    Aprendiz    TABLE     j   CREATE TABLE public."Aprendiz" (
    idiomas text[],
    id bigint NOT NULL,
    nivel text[] NOT NULL
);
    DROP TABLE public."Aprendiz";
       public         heap    postgres    false            �            1259    16459    EntradaForo    TABLE     �   CREATE TABLE public."EntradaForo" (
    id bigint NOT NULL,
    autor bigint NOT NULL,
    contenido text NOT NULL,
    padre bigint
);
 !   DROP TABLE public."EntradaForo";
       public         heap    postgres    false            �            1259    16471    Eventos    TABLE     �   CREATE TABLE public."Eventos" (
    id bigint NOT NULL,
    titulo character varying(50)[] NOT NULL,
    "Estado" "char" DEFAULT 'C'::"char" NOT NULL,
    "Mod" bigint,
    "Anfitrion" bigint NOT NULL
);
    DROP TABLE public."Eventos";
       public         heap    postgres    false            �            1259    16414 
   Instructor    TABLE     �   CREATE TABLE public."Instructor" (
    id bigint NOT NULL,
    descripcion text,
    video path,
    horario json,
    idioma text NOT NULL
);
     DROP TABLE public."Instructor";
       public         heap    postgres    false            �            1259    16495    MaterialDeEstudio    TABLE     �   CREATE TABLE public."MaterialDeEstudio" (
    id bigint NOT NULL,
    archivo text NOT NULL,
    publicador bigint NOT NULL,
    revisado boolean DEFAULT false
);
 '   DROP TABLE public."MaterialDeEstudio";
       public         heap    postgres    false            �            1259    16489 	   Moderador    TABLE     a   CREATE TABLE public."Moderador" (
    id bigint NOT NULL,
    "Ocupado" boolean DEFAULT false
);
    DROP TABLE public."Moderador";
       public         heap    postgres    false            �            1259    16443    Sesion    TABLE     �   CREATE TABLE public."Sesion" (
    "id_Aprendiz" bigint NOT NULL,
    "id_Tutor" bigint NOT NULL,
    "idSesion" bigint NOT NULL,
    fecha date NOT NULL,
    estado "char" DEFAULT 'B'::"char" NOT NULL
);
    DROP TABLE public."Sesion";
       public         heap    postgres    false            �            1259    16399    Usuario    TABLE     �   CREATE TABLE public."Usuario" (
    id bigint NOT NULL,
    nombre text NOT NULL,
    apellidos text NOT NULL,
    correo text NOT NULL,
    "fechaDeNacimiento" date,
    genero "char" DEFAULT 'O'::"char",
    "tarjetaDeCredito" bigint
);
    DROP TABLE public."Usuario";
       public         heap    postgres    false            -          0    16428    Aprendiz 
   TABLE DATA           8   COPY public."Aprendiz" (idiomas, id, nivel) FROM stdin;
    public          postgres    false    217   �*       /          0    16459    EntradaForo 
   TABLE DATA           D   COPY public."EntradaForo" (id, autor, contenido, padre) FROM stdin;
    public          postgres    false    219   �*       0          0    16471    Eventos 
   TABLE DATA           M   COPY public."Eventos" (id, titulo, "Estado", "Mod", "Anfitrion") FROM stdin;
    public          postgres    false    220   +       ,          0    16414 
   Instructor 
   TABLE DATA           O   COPY public."Instructor" (id, descripcion, video, horario, idioma) FROM stdin;
    public          postgres    false    216   8+       2          0    16495    MaterialDeEstudio 
   TABLE DATA           P   COPY public."MaterialDeEstudio" (id, archivo, publicador, revisado) FROM stdin;
    public          postgres    false    222   U+       1          0    16489 	   Moderador 
   TABLE DATA           4   COPY public."Moderador" (id, "Ocupado") FROM stdin;
    public          postgres    false    221   r+       .          0    16443    Sesion 
   TABLE DATA           X   COPY public."Sesion" ("id_Aprendiz", "id_Tutor", "idSesion", fecha, estado) FROM stdin;
    public          postgres    false    218   �+       +          0    16399    Usuario 
   TABLE DATA           s   COPY public."Usuario" (id, nombre, apellidos, correo, "fechaDeNacimiento", genero, "tarjetaDeCredito") FROM stdin;
    public          postgres    false    215   �+       �           2606    16434    Aprendiz Aprendiz_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public."Aprendiz"
    ADD CONSTRAINT "Aprendiz_pkey" PRIMARY KEY (id);
 D   ALTER TABLE ONLY public."Aprendiz" DROP CONSTRAINT "Aprendiz_pkey";
       public            postgres    false    217            �           2606    16465    EntradaForo EntradaForo_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public."EntradaForo"
    ADD CONSTRAINT "EntradaForo_pkey" PRIMARY KEY (id);
 J   ALTER TABLE ONLY public."EntradaForo" DROP CONSTRAINT "EntradaForo_pkey";
       public            postgres    false    219            �           2606    16478    Eventos Eventos_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public."Eventos"
    ADD CONSTRAINT "Eventos_pkey" PRIMARY KEY (id);
 B   ALTER TABLE ONLY public."Eventos" DROP CONSTRAINT "Eventos_pkey";
       public            postgres    false    220            �           2606    16422    Instructor InstructorPK 
   CONSTRAINT     Y   ALTER TABLE ONLY public."Instructor"
    ADD CONSTRAINT "InstructorPK" PRIMARY KEY (id);
 E   ALTER TABLE ONLY public."Instructor" DROP CONSTRAINT "InstructorPK";
       public            postgres    false    216            �           2606    16502 (   MaterialDeEstudio MaterialDeEstudio_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public."MaterialDeEstudio"
    ADD CONSTRAINT "MaterialDeEstudio_pkey" PRIMARY KEY (id);
 V   ALTER TABLE ONLY public."MaterialDeEstudio" DROP CONSTRAINT "MaterialDeEstudio_pkey";
       public            postgres    false    222            �           2606    16494    Moderador Moderador_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public."Moderador"
    ADD CONSTRAINT "Moderador_pkey" PRIMARY KEY (id);
 F   ALTER TABLE ONLY public."Moderador" DROP CONSTRAINT "Moderador_pkey";
       public            postgres    false    221            �           2606    16448    Sesion Sesion_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public."Sesion"
    ADD CONSTRAINT "Sesion_pkey" PRIMARY KEY ("idSesion");
 @   ALTER TABLE ONLY public."Sesion" DROP CONSTRAINT "Sesion_pkey";
       public            postgres    false    218            �           2606    16406    Usuario Usuario_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public."Usuario"
    ADD CONSTRAINT "Usuario_pkey" PRIMARY KEY (id);
 B   ALTER TABLE ONLY public."Usuario" DROP CONSTRAINT "Usuario_pkey";
       public            postgres    false    215            �           2606    16484    Eventos anfit    FK CONSTRAINT     v   ALTER TABLE ONLY public."Eventos"
    ADD CONSTRAINT anfit FOREIGN KEY ("Anfitrion") REFERENCES public."Usuario"(id);
 9   ALTER TABLE ONLY public."Eventos" DROP CONSTRAINT anfit;
       public          postgres    false    3207    220    215            �           2606    16466    EntradaForo father    FK CONSTRAINT     �   ALTER TABLE ONLY public."EntradaForo"
    ADD CONSTRAINT father FOREIGN KEY (padre) REFERENCES public."EntradaForo"(id) NOT VALID;
 >   ALTER TABLE ONLY public."EntradaForo" DROP CONSTRAINT father;
       public          postgres    false    3215    219    219            �           2606    16449    Sesion idAprend    FK CONSTRAINT     �   ALTER TABLE ONLY public."Sesion"
    ADD CONSTRAINT "idAprend" FOREIGN KEY ("id_Aprendiz") REFERENCES public."Aprendiz"(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 =   ALTER TABLE ONLY public."Sesion" DROP CONSTRAINT "idAprend";
       public          postgres    false    217    218    3211            �           2606    16454    Sesion idTutor    FK CONSTRAINT     �   ALTER TABLE ONLY public."Sesion"
    ADD CONSTRAINT "idTutor" FOREIGN KEY ("id_Tutor") REFERENCES public."Instructor"(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 <   ALTER TABLE ONLY public."Sesion" DROP CONSTRAINT "idTutor";
       public          postgres    false    3209    216    218            �           2606    16423    Instructor ids    FK CONSTRAINT     x   ALTER TABLE ONLY public."Instructor"
    ADD CONSTRAINT ids FOREIGN KEY (id) REFERENCES public."Usuario"(id) NOT VALID;
 :   ALTER TABLE ONLY public."Instructor" DROP CONSTRAINT ids;
       public          postgres    false    215    216    3207            �           2606    16435    Aprendiz ids    FK CONSTRAINT     �   ALTER TABLE ONLY public."Aprendiz"
    ADD CONSTRAINT ids FOREIGN KEY (id) REFERENCES public."Usuario"(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 8   ALTER TABLE ONLY public."Aprendiz" DROP CONSTRAINT ids;
       public          postgres    false    3207    215    217            �           2606    16479    Eventos user    FK CONSTRAINT     q   ALTER TABLE ONLY public."Eventos"
    ADD CONSTRAINT "user" FOREIGN KEY ("Mod") REFERENCES public."Usuario"(id);
 :   ALTER TABLE ONLY public."Eventos" DROP CONSTRAINT "user";
       public          postgres    false    3207    215    220            -      x������ � �      /      x������ � �      0      x������ � �      ,      x������ � �      2      x������ � �      1      x������ � �      .      x������ � �      +      x������ � �     