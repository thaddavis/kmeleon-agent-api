from sqlalchemy import Column, Integer, String, ForeignKey, UUID, JSON, DateTime, func, Double, Index
from sqlalchemy.orm import relationship
from .database import Base


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    reset_token = Column(String)

    def __repr__(self):
        return f'<Account {self.email}>'
    
class CheckpointMigrations(Base):
    """Table for tracking migration versions."""
    __tablename__ = "checkpoint_migrations"

    v = Column(Integer, primary_key=True)


class Checkpoints(Base):
    """Stores checkpoint data."""
    __tablename__ = "checkpoints"

    thread_id = Column(String, nullable=False)
    checkpoint_ns = Column(String, nullable=False)
    checkpoint_id = Column(UUID(as_uuid=True), primary_key=True)
    parent_checkpoint_id = Column(UUID(as_uuid=True), ForeignKey("checkpoints.checkpoint_id"), nullable=True)

    checkpoint_data = Column(JSON, nullable=False)  # Stores the checkpoint object as JSON
    checkpoint_metadata = Column(JSON, nullable=False, key="metadata")
    
    created_at = Column(DateTime, server_default=func.now())

    __table_args__ = (
        Index("idx_checkpoints_thread_ns", "thread_id", "checkpoint_ns"),
    )


class CheckpointBlobs(Base):
    """Stores checkpoint blobs separately."""
    __tablename__ = "checkpoint_blobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    thread_id = Column(String, nullable=False)
    checkpoint_ns = Column(String, nullable=False)
    checkpoint_id = Column(UUID(as_uuid=True), ForeignKey("checkpoints.checkpoint_id"), nullable=False)

    key = Column(String, nullable=False)
    value = Column(JSON, nullable=False)
    blob = Column(JSON, nullable=True) 

    __table_args__ = (
        Index("idx_checkpoint_blobs_thread_ns", "thread_id", "checkpoint_ns"),
    )


class CheckpointWrites(Base):
    """Stores intermediate writes linked to a checkpoint."""
    __tablename__ = "checkpoint_writes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    thread_id = Column(String, nullable=False)
    checkpoint_ns = Column(String, nullable=False)
    checkpoint_id = Column(UUID(as_uuid=True), ForeignKey("checkpoints.checkpoint_id"), nullable=False)

    task_id = Column(String, nullable=False)
    task_path = Column(String, nullable=True)
    writes = Column(JSON, nullable=False)  # Stores write operations as JSON

    __table_args__ = (
        Index("idx_checkpoint_writes_thread_ns", "thread_id", "checkpoint_ns"),
    )