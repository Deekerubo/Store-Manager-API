-- create table to store users
create table if not exists users (
                id         serial    not null primary key,
                email      varchar   not null,
                password   varchar   not null
);

-- create table to handle products
create table if not exists products (
                id         serial    not null primary key,
                product_name      varchar   not null,
                product_description varchar not null,
                quantity       integer      not null,
                price       integer      not null,
                category     integer     default 0  references categories (id)
);

-- create table to handle categories
create table if not exists category (
                id         serial    not null primary key,
                name      varchar   not null,
);
-- create table to handle Sales
create table if not exists sales (
                id         serial    not null primary key,
                sales_items       integer      not null references products (id),	
		            price       integer      not null,
                quantity integer not null,
);
-- create table to handle revoked tokens
create table if not exists tokens (
  id         serial    not null primary key,
  token     varchar   

);