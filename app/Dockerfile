FROM rust:latest AS builder

RUN echo 'done cargo/rustup'
RUN cargo install trunk
RUN rustup target add wasm32-unknown-unknown

COPY . /usr/src/app

# RUN cargo build
# RUN rustc --target wasm32-unknown-unknown -O --crate-type=cdylib src/main.rs -o build/main.gid.wasm
# RUN wasm-gc build/main.big.wasm build/main.wasm

# CMD ["app/target/x86_64-unknown-linux-musl/release/app"]
CMD ["trunk", "serve"]


# FROM scratch

# WORKDIR /usr/src/app

# COPY --from=builder app/target/x86_64-unknown-linux-musl/release/app ./

# USER 1000:1000

# CMD ["./app"]

